import math
import requests
requests.packages.urllib3.disable_warnings()
import redis
import json


def distance_on_unit_sphere(lat1, long1, lat2, long2):
    degrees_to_radians = math.pi/180.0
    phi1 = (90.0 - lat1)*degrees_to_radians
    phi2 = (90.0 - lat2)*degrees_to_radians
    theta1 = long1*degrees_to_radians
    theta2 = long2*degrees_to_radians
    cos = (math.sin(phi1)*math.sin(phi2)*math.cos(theta1 - theta2) +
           math.cos(phi1)*math.cos(phi2))
    arc = math.acos( cos )
    return 3960 * arc


def get_auth_header():
    url = "https://10.10.2.29:8443/oauth2/token"
    payload = {'grant_type': 'password', 'username': 'group4', 'password': 'Group4'}
    response = requests.post (url, data=payload, auth=('group4','Group4'), verify=False)
    json_data = json.loads(response.text)
    return {"Authorization":"{token_type} {access_token}".format(**json_data)}


def get_topology_info(authHeader=get_auth_header()):
    r = requests.get('https://10.10.2.29:8443/NorthStar/API/v1/tenant/1/topology/1', headers=authHeader, verify=False)
    return r.json()


def get_router_coordinates(topology_info=get_topology_info()):
    router_coordinates = {}
    for node in topology_info['nodes']:
        router_coordinates[node['name']] = node['topology']['coordinates']['coordinates']
    return router_coordinates


def get_link_latency(start, end):
    r = redis.StrictRedis(host='10.10.4.252', port=6379, db=0)
    query_string = ('{}:{}:latency'.format(start, end)
        .replace('NY', 'new york')
        .replace('SF', 'san francisco')
        .replace('LA', 'los angeles').lower())
    response = r.lrange(query_string, 0, -1)
    return json.loads(response[0])['rtt-average(ms)'] if len(response) > 0 else 1


def get_router_hostnames(topology_info=get_topology_info()):
    router_host_names = {}
    for node in topology_info["nodes"]:
        router_host_names[node['name']] = node['hostName']
    return router_host_names


def get_all_links(topology_info=get_topology_info(), router_host_names=get_router_hostnames(), router_coordinates=get_router_coordinates()):
    links = {}
    for link in topology_info["links"]:
        link_latency = get_link_latency(router_host_names[link['endA']['node']['name']], router_host_names[link['endZ']['node']['name']])
        link_distance = distance_on_unit_sphere(router_coordinates[link['endA']['node']['name']][0], router_coordinates[link['endA']['node']['name']][1], router_coordinates[link['endZ']['node']['name']][0], router_coordinates[link['endZ']['node']['name']][1])
        links[(link['endA']['node']['name'], link['endA']['ipv4Address']['address'])] = {
            'status' : True,
            'fails' : 0,
            'latency' : link_latency,
            'distance' : link_distance,
            'link_back' : (link['endZ']['node']['name'], link['endZ']['ipv4Address']['address'])
        }
        links[(link['endZ']['node']['name'], link['endZ']['ipv4Address']['address'])] = {
            'status' : True,
            'fails' : 0,
            'latency' : link_latency,
            'distance' : link_distance,
            'link_back' : (link['endA']['node']['name'], link['endA']['ipv4Address']['address'])
        }
    return links


def get_interfaces(topology_info=get_topology_info()):
    interfaces = {}
    for node in topology_info["nodes"]:
        interfaces[node["name"]] = {}
    for link in topology_info["links"]:
        interfaces[link["endA"]["node"]["name"]][link["endA"]["ipv4Address"]["address"]] = link["endZ"]["ipv4Address"]["address"]
        interfaces[link["endZ"]["node"]["name"]][link["endZ"]["ipv4Address"]["address"]] = link["endA"]["ipv4Address"]["address"]
    return interfaces


def link_weight(router, interface, links=get_all_links()):
    latencies = map(lambda x: x['latency'], links.values())
    latency_avg = sum(latencies) / len(latencies)
    latency_std_deviation = (sum(map(lambda x: (x - latency_avg)**2, latencies))/len(latencies))**0.5
    distances = map(lambda x: x['distance'], links.values())
    distance_avg = sum(distances) / len(distances)
    distance_std_deviation = (sum(map(lambda x: (x - distance_avg)**2, distances))/len(distances))**0.5
    fails = map(lambda x: x['fails'], links.values())
    fail_avg = sum(fails) / len(fails)
    fail_std_deviation = (sum(map(lambda x: (x - fail_avg)**2, fails))/len(fails))**0.5
    return ((links[(router, interface)]['latency'] - latency_avg) / latency_std_deviation) + ((links[(router, interface)]['distance'] - distance_avg) / distance_std_deviation) + ((links[(router, interface)]['fails'] - fail_avg) / (fail_std_deviation if fail_std_deviation != 0 else 1))


def get_topology_graph(topology_info=get_topology_info(), router_host_names=get_router_hostnames(), links=get_all_links()):
    G = {}
    for node in topology_info["nodes"]:
        G[node["name"]] = {}
    for link in topology_info["links"]:
        G[link["endA"]["node"]["name"]][link["endZ"]["node"]["name"]] = {
            "weight" : link_weight(link["endA"]["node"]["name"], link["endA"]["ipv4Address"]["address"], links),
            "interface" : link["endA"]["ipv4Address"]["address"],
            "target" : link["endZ"]["ipv4Address"]["address"]
        }
        G[link["endZ"]["node"]["name"]][link["endA"]["node"]["name"]] = {
            "weight" : link_weight(link["endZ"]["node"]["name"], link["endZ"]["ipv4Address"]["address"], links),
            "interface" : link["endZ"]["ipv4Address"]["address"],
            "target" : link["endA"]["ipv4Address"]["address"]
        }
    return G


def get_all_paths(start, end, path=[], G=get_topology_graph()):
    path = path + [start]
    if start == end:
        return [path]
    if not G.has_key(start):
        return []
    paths = []
    for node in G[start]:
        if node not in path:
            newpaths = get_all_paths(node, end, path, G)
            for newpath in newpaths:
                paths.append(newpath)
    return paths


def get_weighted_paths(G=get_topology_graph(), all_paths=get_all_paths('10.210.10.100', '10.210.10.118')):
    weighted_paths = []
    for path in all_paths:
        weight = 0
        for idx, element in enumerate(path):
            if idx == 0:
                continue
            weight += G[path[idx - 1]][element]["weight"]
        weighted_paths.append((path, weight))
        weighted_paths.sort(key=lambda x: x[1])
    return weighted_paths


def get_next_hop_paths(G=get_topology_graph(), weighted_paths=get_weighted_paths()):
    paths_with_next_hops = []
    for path in weighted_paths:
        new_path = []
        for idx, node in enumerate(path[0]):
            if idx != len(path[0]) - 1:
                new_path.append((node, G[path[0][idx]][path[0][idx+1]]['interface']))
        paths_with_next_hops.append((new_path, path[1]))
    return paths_with_next_hops


def get_best_path(links, paths_with_next_hops):
    best_path = None
    for path in paths_with_next_hops:
        if all(map(lambda x: links[x]['status'], path[0])):
            best_path = path
            break
    return best_path


def get_ero(links, paths_with_next_hops, interfaces):
    best_path = get_best_path(links, paths_with_next_hops)
    ero = []
    for element in best_path[0]:
        ero.append({ 'topoObjectType': 'ipv4', 'address': interfaces[element[0]][element[1]]})
    return ero, best_path


def set_ero(links, paths_with_next_hops, interfaces, authHeader=get_auth_header(), target_lsp="GROUP_FOUR_SF_NY_LSP{}"):
    r = requests.get('https://10.10.2.29:8443/NorthStar/API/v1/tenant/1/topology/1/te-lsps/', headers=authHeader, verify=False)

    p = json.dumps(r.json())
    lsp_list = json.loads(p)

    ero, best_path = get_ero(links, paths_with_next_hops, interfaces)
    print 'Setting Best ERO:'
    print ero

    for lsp_count in range(1, 5):
        for lsp in lsp_list:
            if lsp['name'] == target_lsp.format(lsp_count):
                break

        new_lsp = {}
        for key in ('from', 'to', 'name', 'lspIndex', 'pathType'):
            new_lsp[key] = lsp[key]


        new_lsp['plannedProperties'] = {
            'ero': ero
        }

        print 'Doing LSP {}'.format(target_lsp.format(lsp_count))
        response = requests.put('https://10.10.2.29:8443/NorthStar/API/v1/tenant/1/topology/1/te-lsps/' + str(new_lsp['lspIndex']),
                            json = new_lsp, headers=authHeader, verify=False)

    return best_path


def main():
    authHeader = get_auth_header()
    topology_info = get_topology_info(authHeader)
    router_coordinates = get_router_coordinates(topology_info)
    router_host_names = get_router_hostnames(topology_info)
    links = get_all_links(topology_info, router_host_names, router_coordinates)
    G = get_topology_graph(topology_info, links=links)
    interfaces = get_interfaces(topology_info)
    all_paths = get_all_paths('10.210.10.100', '10.210.10.118', [], G)
    weighted_paths = get_weighted_paths(all_paths=all_paths)
    r = redis.StrictRedis(host='10.10.4.252', port=6379, db=0)
    pubsub = r.pubsub()
    pubsub.subscribe('link_event')

    current_best_path = None
    for item in pubsub.listen():
        if item['type'] == 'message':
            if isinstance(item['data'], basestring):
                d = json.loads(item['data'])
                if d['status'] == 'failed':
                    if current_best_path == None or (d['router_id'], d['interface_address']) in current_best_path[0]:
                        links[(d['router_id'], d['interface_address'])]['status'] = False
                        links[links[(d['router_id'], d['interface_address'])]['link_back']]['status'] = False
                        links[(d['router_id'], d['interface_address'])]['fails'] += 1
                        links[links[(d['router_id'], d['interface_address'])]['link_back']]['fails'] += 1
                        current_best_path = set_ero(links, get_next_hop_paths(), interfaces, authHeader)
                    else:
                        print '---Best Path Retained---'
                elif d['status'] == 'healed':
                    links[(d['router_id'], d['interface_address'])]['status'] = True
                    links[links[(d['router_id'], d['interface_address'])]['link_back']]['status'] = True
                    current_best_path = set_ero(links, get_next_hop_paths(), interfaces, authHeader)
        else:
            current_best_path = set_ero(links, get_next_hop_paths(), interfaces, authHeader)


main()
