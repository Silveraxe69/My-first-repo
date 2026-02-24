"""Functions to help Azara and Rui locate pirate treasure."""


def get_coordinate(record):
    """Return coordinate value from a (treasure, coordinate) pair."""
    return record[1]


def convert_coordinate(coordinate):
    """Split a string coordinate into its components."""
    return (coordinate[0], coordinate[1])


def compare_records(azara_record, rui_record):
    """Check whether Azara's and Rui's coordinates match."""
    azara_coord = convert_coordinate(azara_record[1])
    rui_coord = rui_record[1]
    return azara_coord == rui_coord


def create_record(azara_record, rui_record):
    """Create a combined record if coordinates match."""
    if compare_records(azara_record, rui_record):
        return (
            azara_record[0],
            azara_record[1],
            rui_record[0],
            rui_record[1],
            rui_record[2],
        )
    return "not a match"


def clean_up(combined_record_group):
    """Remove duplicate coordinates and format records into a report."""
    report = ""
    for record in combined_record_group:
        treasure, _, location, coordinate, quadrant = record
        report += f"{(treasure, location, coordinate, quadrant)}\n"
    return report