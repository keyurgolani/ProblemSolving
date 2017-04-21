import time
import math
import configuration as cfg


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
    # Invalid Input Check
    if not isinstance(size, int) or not isinstance(has_handicapped_placard, bool) or ((size == 1 or size == 4) and has_handicapped_placard) or size > 4 or size < 1:
        # Invalid Input
        raise InvalidInputError
    # Valid Input
    else:
        # Waiting to acquire the lock
        while cfg.lock < 1:
            pass
        # When the lock is released
        else:
            # Acquire the lock
            cfg.lock = 0
            # Switch based on the vehicle size
            if size == 1:
                # Try to get specifically a motorcycle space
                available_space = get_next_motorcycle_space()
                # If not, fallback to a little costlier option, small car space
                if available_space == None:
                    available_space = next_small_car_space()
                    # If not, fallback to an even costlier option, large car space
                    if available_space == None:
                        available_space = get_next_large_car_space()
            elif size == 2:
                if has_handicapped_placard:
                    # If handicapped, ignore the size first and try for a handicapped space
                    available_space = get_next_handicapped_space()
                    # If not, fallback to a large car space
                    if available_space == None:
                        available_space = get_next_large_car_space()
                        # If not, fallback to a small car space
                        if available_space == None:
                            available_space = get_next_small_car_space()
                else:
                    # If not handicapped, try for a cheaper option, small car space
                    available_space = next_small_car_space()
                    # If not, try for a little costlier option, large car space
                    if available_space == None:
                        available_space = get_next_large_car_space()
            elif size == 3:
                if has_handicapped_placard:
                    # If handicapped, ignore the size first and try for a handicapped space
                    available_space = get_next_handicapped_space()
                    # If not, fallback to a large car space
                    if available_space == None:
                        available_space = get_next_large_car_space()
                else:
                    # If not handicapped, just try for a large car space
                    available_space = get_next_large_car_space()
            else:
                # Get next available bus space
                available_space = get_next_bus_space()
            # If available space is actually 'available' only then
            # perform any reservation operation on it
            if available_space != None:
                # If bus, reserve 5 consecutive spaces and tag the place with 'bus'
                if size == 4:
                    for idx in range(5):
                        cfg.parking_construct[available_space[0]][available_space[1]][available_space[2] + idx]['available'] = False
                    cfg.parking_construct[available_space[0]][available_space[1]][available_space[2]]['bus'] = True
                # else reserve only one space without any tags
                else:
                    cfg.parking_construct[available_space[0]][available_space[1]][available_space[2]]['available'] = False
                # Record the parking start time
                cfg.parking_construct[available_space[0]][available_space[1]][available_space[2]]['start_time'] = time.time()
            # Release the lock
            cfg.lock = 1
            # Converting 0 based index tuple to 1 based (level, row, space) tuple
            return (available_space[0] + 1, available_space[1] + 1, available_space[2] + 1)


def unpark(location):
    """
    Return the charge for parking at this location based on location type and time spent. Parking time is rounded up to the nearest MINIMUM_PARKING_INTERVAL_SECONDS. Amount charged to rounded up to the nearest penny.
    :param location: parking space the vehicle was parked at as tuple (level, row, space) :type location: tuple(`int`,`int`,`int`)
    :returns: The amount that the parker should be charged.
    :rtype:  oat
    :raises InvalidInputError: if location invalid or empty.
    """
    # Converting 1 based (level, row, space) tuple to 0 based index tuple
    loc = (location[0] - 1, location[1] - 1, location[2] - 1)
    # Check if space was actually reserved or not
    # In other words, check valid input
    if not cfg.parking_construct[loc[0]][loc[1]][loc[2]]['available']:
        # Valid Input
        # Waiting to acquire the lock
        while cfg.lock < 1:
            pass
        # Lock was released
        else:
            # Acquire the lock
            cfg.lock = 0
            # Calculate the total chargable time rounded up to
            # higher multiple of MINIMUM_PARKING_INTERVAL_SECONDS
            time_interval = math.ceil((time.time() - cfg.parking_construct[loc[0]][loc[1]][loc[2]]['start_time']) / cfg.MINIMUM_PARKING_INTERVAL_SECONDS) * cfg.MINIMUM_PARKING_INTERVAL_SECONDS
            # Get the rate of the used parking space
            rate = cfg.price_mapping[cfg.parking_construct[loc[0]][loc[1]][loc[2]]['size']]
            # Check if it was a bus
            if 'bus' in cfg.parking_construct[loc[0]][loc[1]][loc[2]].keys() and cfg.parking_construct[loc[0]][loc[1]][loc[2]]['bus']:
                # If bus
                # Remove the bus tag
                del cfg.parking_construct[loc[0]][loc[1]][loc[2]]['bus']
                # make all 5 consecutive spaces available
                for idx in range(5):
                    cfg.parking_construct[loc[0]][loc[1]][loc[2] + idx]['available'] = True
                # Release the lock
                cfg.lock = 1
                # Return the amount charged for 5 spaces rounded off to nearest penny
                return round((time_interval * rate) / 3600 * 5, 2)
            else:
                # If not bus, just release the space
                cfg.parking_construct[loc[0]][loc[1]][loc[2]]['available'] = True
                # Release the lock
                cfg.lock = 1
                # Return the amount charged for single space rounded off to nearest penny
                return round((time_interval * rate) / 3600, 2)
    else:
        # Invalid Input
        raise InvalidInputError


def get_next_motorcycle_space():
    """
    Return next available motorcycle parking space
    :returns: next available motorcycle parking space
    :rtype: tuple(level, row, space)
    """
    # Check all the motorcycle parking spaces
    for space in get_all_parking_spaces(size=1):
        if cfg.parking_construct[space[0]][space[1]][space[2]]['available']:
            # If available, return it
            return space
    # If out of luck, return None
    return None


def get_next_small_car_space():
    """
    Return next available small car parking space
    :returns: next available small car parking space
    :rtype: tuple(level, row, space)
    """
    # Check all the small car parking spaces
    for space in get_all_parking_spaces(size=2):
        if cfg.parking_construct[space[0]][space[1]][space[2]]['available']:
            # If available, return it
            return space
    # If out of luck, return None
    return None


def get_next_large_car_space():
    """
    Return next available large car parking space
    :returns: next available large car parking space
    :rtype: tuple(level, row, space)
    """
    # First make sure not to give out a space from a block
    # of 5 consecutive empty spaces to save them for bus
    for space in get_all_parking_spaces(size=3):
        if cfg.parking_construct[space[0]][space[1]][space[2]]['available']:
            # If available, check if it is a part of any
            # consecutive empty block of 5 spaces
            if not any(map(lambda s: all([cfg.parking_construct[s[0]][s[1]][s[2] + 4]['available'] and not cfg.parking_construct[s[0]][s[1]][s[2] + 4]['handi'], cfg.parking_construct[s[0]][s[1]][s[2] + 3]['available'] and not cfg.parking_construct[s[0]][s[1]][s[2] + 3]['handi'], cfg.parking_construct[s[0]][s[1]][s[2] + 2]['available'] and not cfg.parking_construct[s[0]][s[1]][s[2] + 2]['handi'], cfg.parking_construct[s[0]][s[1]][s[2] + 1]['available'] and not cfg.parking_construct[s[0]][s[1]][s[2] + 1]['handi'], cfg.parking_construct[s[0]][s[1]][s[2]]['available'] and not cfg.parking_construct[s[0]][s[1]][s[2]]['handi']]), give_surrounding_spaces(space))):
                # If not, return it
                return space
    # Then fallback to giving out any available large car space
    for space in get_all_parking_spaces(size=3):
        if cfg.parking_construct[space[0]][space[1]][space[2]]['available']:
            return space
    return None


def get_next_bus_space():
    """
    Return next available bus parking space
    :returns: next available bus parking space
    :rtype: tuple(level, row, space)
    """
    # Check in all large car parking spaces
    for space in get_all_parking_spaces(size=3):
        try:
            # Check the availability of the block of 5 consecutive spaces
            consecutive_available = cfg.parking_construct[space[0]][space[1]][space[2]]['available'] and not cfg.parking_construct[space[0]][space[1]][space[2]]['handi'] and cfg.parking_construct[space[0]][space[1]][space[2] + 1]['available'] and not cfg.parking_construct[space[0]][space[1]][space[2] + 1]['handi'] and cfg.parking_construct[space[0]][space[1]][space[2] + 2]['available'] and not cfg.parking_construct[space[0]][space[1]][space[2] + 2]['handi'] and cfg.parking_construct[space[0]][space[1]][space[2] + 3]['available'] and not cfg.parking_construct[space[0]][space[1]][space[2] + 3]['handi'] and cfg.parking_construct[space[0]][space[1]][space[2] + 4]['available'] and not cfg.parking_construct[space[0]][space[1]][space[2] + 4]['handi']
        # If space is one of the last 4 spaces in a row, just ignore them
        except IndexError:
            continue
        else:
            if consecutive_available:
                # If the space and next 4 spaces are available
                # return it
                return space
    # If out of luck, return None
    return None


def get_next_handicapped_space():
    """
    Return next available handicapped parking space
    :returns: next available handicapped parking space
    :rtype: tuple(level, row, space)
    """
    # Check all the handicapped parking spaces
    for space in get_all_parking_spaces(is_handicapped=is_handicapped):
        if cfg.parking_construct[space[0]][space[1]][space[2]]['available']:
            # If available, return it
            return space
    # If out of luck, return None
    return None


def get_all_parking_spaces(size=0, is_handicapped=False):
    """
    Return all parking spaces available inside the parking_construct
    based on the parameters passed
    :param size: parking space size. This is 1=motorcycle, 2=small car, 3=large car, 0=all
    :type size: `int`
    :param is_handicapped: if True, provide handicapped spaces
    :type is_handicapped: `bool`
    :returns: parking locations. list of tuples of (level, row, space)
    :rtype: list
    """
    # If handicapped, ignore the size (Because invalid input is already checked)
    if is_handicapped:
        for level, level_details in enumerate(cfg.parking_construct):
            for row, row_details in enumerate(level_details):
                for space, space_details in enumerate(row_details):
                    if space_details['available'] and space_details['handi']:
                        yield (level, row, space)
    # Else yield the spaces matching passed size
    else:
        for level, level_details in enumerate(cfg.parking_construct):
            for row, row_details in enumerate(level_details):
                for space, space_details in enumerate(row_details):
                    if space_details['available'] and not space_details['handi']:
                        if size == 0:
                            yield (level, row, space)
                        elif size == space_details["size"]:
                            yield (level, row, space)


def give_surrounding_spaces(space):
    """
    Return a list of start spaces of 5 space blocks
    that given space could be included in.
    :param space: location of a space
    :type space: tuple(`int`,`int`,`int`)
    :returns: A list of spaces
    :rtype: list of tuples
    """
    return [cfg.parking_construct[space[0]][space[1]][space[2] - 4], cfg.parking_construct[space[0]][space[1]][space[2] - 3], cfg.parking_construct[space[0]][space[1]][space[2] - 2], cfg.parking_construct[space[0]][space[1]][space[2] - 1], cfg.parking_construct[space[0]][space[1]][space[2]]]


def init():
    """
    Called on system initialization before any park/unpark function is called.
    """
    pass


def main():
    print park(4, False)
    print unpark((1, 1, 1))

if __name__ == '__main__':
    main()
