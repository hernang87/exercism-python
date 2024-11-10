"""Functions which helps the locomotive engineer to keep track of the train."""


def get_list_of_wagons(*args):
    """Return a list of wagons.

    :param: arbitrary number of wagons.
    :return: list - list of wagons.
    """
    return [wagon for wagon in args]


def fix_list_of_wagons(each_wagons_id, missing_wagons):
    """Fix the list of wagons.

    :param each_wagons_id: list - the list of wagons.
    :param missing_wagons: list - the list of missing wagons.
    :return: list - list of wagons.
    """
    modified_list = each_wagons_id.copy()[2:]
    for index, wagon in enumerate(missing_wagons):
        modified_list.insert(index + 1, wagon)

    modified_list.extend(each_wagons_id[:2])

    return modified_list


def add_missing_stops(*args, **kwargs):
    """Add missing stops to route dict.

    :param route: dict - the dict of routing information.
    :param: arbitrary number of stops.
    :return: dict - updated route dictionary.
    """
    result = args[0].copy()
    result['stops'] = [stop for stop in kwargs.values()]
    return result


def extend_route_information(route, more_route_information):
    """Extend route information with more_route_information.

    :param route: dict - the route information.
    :param more_route_information: dict -  extra route information.
    :return: dict - extended route information.
    """
    result = route.copy()
    for key in more_route_information:
        result[key] = more_route_information[key]
    return result


def fix_wagon_depot(wagons_rows):
    """Fix the list of rows of wagons.

    :param wagons_rows: list[list[tuple]] - the list of rows of wagons.
    :return: list[list[tuple]] - list of rows of wagons.
    """
    fixed_wagons = [list(column) for column in zip(*wagons_rows)]
    return fixed_wagons
