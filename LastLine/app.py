import time
import math
import parking_construct as pc


class InvalidInputError(Exception):
    """
    Raised if the provided API input is invalid.
    """


def park(size, has_handicapped_placard):
    """
    Return the most appropriate available parking space for this vehicle. The most appropriate space is always the cheapest valid available space for the vehicle. Spaces closer to the entrance are preferred (lower levels, rows and spaces are closest to the entrance - eg: level 1 row 4 space 5 is closer than level 2 row 3 space 1), unless returning a closer space is not the cheapest or will result in less available bus parking.
    :param size: vehicle size. For now this is 1=motorcycle, 2=compact car, 3=large car, 4=bus
    :type size: `int`
    :param has_handicapped_placard: if True, provide handicapped space (if available). :type has_handicapped_placard: `bool`
    :returns: parking location. tuple of (level, row, space), or None if no spaces available.
    Level, row and space numbers start at 1.
    :rtype: tuple(`int`,`int`,`int`)
    :raises InvalidInputError: if size invalid.
    """
    if not isinstance(size, int) or not isinstance(has_handicapped_placard, bool) or ((size == 1 or size == 4) and has_handicapped_placard) or size > 4 or size < 1:
        raise InvalidInputError
    else:
        while pc.lock < 1:
            pass
        else:
            pc.lock = 0
            if size == 1:
                available_space = next_motorcycle_space()
            elif size == 2:
                available_space = next_small_car_space(has_handicapped_placard)
            elif size == 3:
                available_space = next_large_car_space(has_handicapped_placard)
            else:
                available_space = next_bus_space()
            if size == 4:
                for idx in range(5):
                    pc.parking_construct[available_space[0]][available_space[1]][available_space[2] + idx]['available'] = False
                pc.parking_construct[available_space[0]][available_space[1]][available_space[2]]['bus'] = True
            else:
                pc.parking_construct[available_space[0]][available_space[1]][available_space[2]]['available'] = False
            pc.parking_construct[available_space[0]][available_space[1]][available_space[2]]['start_time'] = time.time()
            pc.lock = 1
            return available_space


def unpark(location):
    """
    Return the charge for parking at this location based on location type and time spent. Parking time is rounded up to the nearest MINIMUM_PARKING_INTERVAL_SECONDS. Amount charged to rounded up to the nearest penny.
    :param location: parking space the vehicle was parked at as tuple (level, row, space) :type location: tuple(`int`,`int`,`int`)
    :returns: The amount that the parker should be charged.
    :rtype:  oat
    :raises InvalidInputError: if location invalid or empty.
    """
    if not pc.parking_construct[location[0]][location[1]][location[2]]['available']:
        while pc.lock < 1:
            pass
        else:
            pc.lock = 0
            time_interval = math.ceil((time.time() - pc.parking_construct[location[0]][location[1]][location[2]]['start_time']) / pc.MINIMUM_PARKING_INTERVAL_SECONDS) * pc.MINIMUM_PARKING_INTERVAL_SECONDS
            rate = pc.price_mapping[pc.parking_construct[location[0]][location[1]][location[2]]['size']]
            if 'bus' in pc.parking_construct[location[0]][location[1]][location[2]].keys() and pc.parking_construct[location[0]][location[1]][location[2]]['bus']:
                del pc.parking_construct[location[0]][location[1]][location[2]]['bus']
                for idx in range(5):
                    pc.parking_construct[location[0]][location[1]][location[2] + idx]['available'] = True
                pc.lock = 1
                return (time_interval * rate) / 3600 * 5
            else:
                pc.parking_construct[location[0]][location[1]][location[2]]['available'] = True
                pc.lock = 1
                return (time_interval * rate) / 3600
    else:
        raise InvalidInputError


def next_motorcycle_space():
    for space in get_all_parking_spaces(size=1):
        if pc.parking_construct[space[0]][space[1]][space[2]]['available']:
            return space
    for space in get_all_parking_spaces(size=2):
        if pc.parking_construct[space[0]][space[1]][space[2]]['available']:
            return space
    for space in get_all_parking_spaces(size=3):
        if pc.parking_construct[space[0]][space[1]][space[2]]['available']:
            return space
    return None


def next_small_car_space(is_handicapped):
    if is_handicapped:
        for space in get_all_parking_spaces(is_handicapped=is_handicapped):
            if pc.parking_construct[space[0]][space[1]][space[2]]['available']:
                return space
        for space in get_all_parking_spaces(size=3):
            if pc.parking_construct[space[0]][space[1]][space[2]]['available']:
                return space
        for space in get_all_parking_spaces(size=2):
            if pc.parking_construct[space[0]][space[1]][space[2]]['available']:
                return space
    else:
        for space in get_all_parking_spaces(size=2):
            if pc.parking_construct[space[0]][space[1]][space[2]]['available']:
                return space
        for space in get_all_parking_spaces(size=3):
            if pc.parking_construct[space[0]][space[1]][space[2]]['available']:
                return space
    return None


def next_large_car_space(is_handicapped):
    for space in get_all_parking_spaces(is_handicapped=is_handicapped):
        if pc.parking_construct[space[0]][space[1]][space[2]]['available']:
            return space
    for space in get_all_parking_spaces(size=3):
        if pc.parking_construct[space[0]][space[1]][space[2]]['available']:
            if not any(map(lambda s: all([pc.parking_construct[s[0]][s[1]][s[2] + 4]['available'] and not pc.parking_construct[s[0]][s[1]][s[2] + 4]['handi'], pc.parking_construct[s[0]][s[1]][s[2] + 3]['available'] and not pc.parking_construct[s[0]][s[1]][s[2] + 3]['handi'], pc.parking_construct[s[0]][s[1]][s[2] + 2]['available'] and not pc.parking_construct[s[0]][s[1]][s[2] + 2]['handi'], pc.parking_construct[s[0]][s[1]][s[2] + 1]['available'] and not pc.parking_construct[s[0]][s[1]][s[2] + 1]['handi'], pc.parking_construct[s[0]][s[1]][s[2]]['available'] and not pc.parking_construct[s[0]][s[1]][s[2]]['handi']]), give_surrounding_spaces(space))):
                return space
    for space in get_all_parking_spaces(size=3):
        if pc.parking_construct[space[0]][space[1]][space[2]]['available']:
            return space
    return None


def next_bus_space():
    consecutive_count = 0
    last_consecutive_space = get_all_parking_spaces(size=3).next()
    for space in get_all_parking_spaces(size=3):
        try:
            consecutive_available = pc.parking_construct[space[0]][space[1]][space[2]]['available'] and not pc.parking_construct[space[0]][space[1]][space[2]]['handi'] and pc.parking_construct[space[0]][space[1]][space[2] + 1]['available'] and not pc.parking_construct[space[0]][space[1]][space[2] + 1]['handi'] and pc.parking_construct[space[0]][space[1]][space[2] + 2]['available'] and not pc.parking_construct[space[0]][space[1]][space[2] + 2]['handi'] and pc.parking_construct[space[0]][space[1]][space[2] + 3]['available'] and not pc.parking_construct[space[0]][space[1]][space[2] + 3]['handi'] and pc.parking_construct[space[0]][space[1]][space[2] + 4]['available'] and not pc.parking_construct[space[0]][space[1]][space[2] + 4]['handi']
        except IndexError:
            continue
        else:
            if consecutive_available:
                return space
    return None


def get_all_parking_spaces(size=0, is_handicapped=False):
    if is_handicapped:
        for level, level_details in enumerate(pc.parking_construct):
            for row, row_details in enumerate(level_details):
                for space, space_details in enumerate(row_details):
                    if space_details['available'] and space_details['handi']:
                        yield (level, row, space)
    else:
        for level, level_details in enumerate(pc.parking_construct):
            for row, row_details in enumerate(level_details):
                for space, space_details in enumerate(row_details):
                    if space_details['available'] and not space_details['handi']:
                        if size == 0:
                            yield (level, row, space)
                        elif size == space_details["size"]:
                            yield (level, row, space)


def give_surrounding_spaces(space):
    return [pc.parking_construct[space[0]][space[1]][space[2] - 4], pc.parking_construct[space[0]][space[1]][space[2] - 3], pc.parking_construct[space[0]][space[1]][space[2] - 2], pc.parking_construct[space[0]][space[1]][space[2] - 1], pc.parking_construct[space[0]][space[1]][space[2]]]


def init():
    """
    Called on system initialization before any park/unpark function is called.
    """
    pass


def main():
    pass

if __name__ == '__main__':
    main()
