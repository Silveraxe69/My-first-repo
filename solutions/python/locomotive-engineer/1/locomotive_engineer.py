def get_list_of_wagons(*wagons):
    return list(wagons)

def fix_list_of_wagons(each_wagons_id, missing_wagons):
    first_two, _, rest = each_wagons_id[0:2], each_wagons_id[2], each_wagons_id[3:]
    return [1, *missing_wagons, *rest, *first_two]

def add_missing_stops(route, *args, **kwargs):
    stops = []
    for arg in args:
        stops.extend(arg.values())
    stops.extend(kwargs.values())
    route["stops"] = stops
    return route

def extend_route_information(route, more_route_information):
    return {**route, **more_route_information}

def fix_wagon_depot(wagons_rows):
    # Unpack all 3 rows into separate color groups
    row1, row2, row3 = wagons_rows
    # Transpose using zip() - each new row gets one wagon from each color group
    return [list(row) for row in zip(row1, row2, row3)]
