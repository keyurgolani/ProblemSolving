import sys
from collections import defaultdict

class Graph:
	def __init__(self):
		self.nodes = set()
		self.edges = defaultdict(list)
		self.distances = {}

	def add_node(self, value):
		self.nodes.add(value)

	def add_edge(self, from_node, to_node, distance):
		self.edges[from_node].append(to_node)
		self.edges[to_node].append(from_node)
		self.distances[(from_node, to_node)] = distance


def dijsktra(graph, initial):
	visited = {initial: 1}
	path = {}

	nodes = set(graph.nodes)

	while nodes:
		min_node = None
		for node in nodes:
			if node in visited:
				if min_node is None:
					min_node = node
				elif visited[node] < visited[min_node]:
					min_node = node

		if min_node is None:
			break

		nodes.remove(min_node)
		current_weight = visited[min_node]

		for edge in graph.edges[min_node]:
			weight = current_weight + graph.distances[(min_node, edge)]
			if edge not in visited or weight < visited[edge]:
				visited[edge] = weight
				path[edge] = min_node

	return visited


def answer(maze):
	path_graph = Graph()
	width = len(maze[0])
	height = len(maze)
	nodes = [(x, y) for x in range(width) for y in range(height)]
	for node in nodes:
		path_graph.add_node(node)
		if node[1] > 0:
			path_graph.add_edge(node, (node[0], node[1] - 1), 1 if maze[node[1] - 1][node[0]] == 0 else 10000)
		if node[1] < height - 1:
			path_graph.add_edge(node, (node[0], node[1] + 1), 1 if maze[node[1] + 1][node[0]] == 0 else 10000)
		if node[0] > 0:
			path_graph.add_edge(node, (node[0] - 1, node[1]), 1 if maze[node[1]][node[0] - 1] == 0 else 10000)
		if node[0] < width - 1:
			path_graph.add_edge(node, (node[0] + 1, node[1]), 1 if maze[node[1]][node[0] + 1] == 0 else 10000)


	SPFs = dijsktra(path_graph, (0, 0))
	min_distance = sys.maxsize
	if SPFs[nodes[-1]] < 10000 and SPFs[nodes[-1]] < min_distance:
		min_distance = SPFs[nodes[-1]]
	walls = [node for node in nodes if maze[node[1]][node[0]] == 1]
	for wall in walls:
		SPFs[wall] = SPFs[wall] + dijsktra(path_graph, wall)[nodes[-1]] - 10000
		if SPFs[wall] < min_distance:
			min_distance = SPFs[wall]
	return min_distance




def main():
	# print answer([[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 1, 0], [1, 1, 1, 0]])
	print answer([[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]])
	# print answer([[0, 1, 1, 1, 0], [0, 1, 1, 1, 0], [0, 0, 0, 0, 0], [0, 1, 0, 1, 1], [0, 1, 0, 1, 0], [0, 1, 1, 0, 0]])
	# print answer([[0, 1, 0, 0, 0], [0, 1, 0, 1, 0], [0, 0, 0, 0, 0], [0, 0, 0, 1, 0]])
	# print answer([[0, 0, 1, 0], [0, 0, 0, 0], [1, 1, 0, 0]])
	# print answer([[0, 1, 0, 1], [0, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 1]])
	# print answer([[0, 0, 0, 0], [0, 0, 0, 0], [1, 1, 1, 1], [0, 0, 0, 0]])
	# print answer([[0, 1], [1, 0]])
	# print answer([[0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 1], [0, 1, 0, 0, 1, 0]])


main()
