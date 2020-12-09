"""Locations for the simulation"""

from __future__ import annotations


class Location:
    """A two-dimensional location.
    Attributes:
        row: the row an object is located on
        col: the column an object is located on
    """
    row: int
    col: int

    def __init__(self, row: int, column: int) -> None:
        """Initialize a location.

        """
        self.row = row
        self.col = column

    def __str__(self) -> str:
        """Return a string representation.

        """
        return str(self.row) + ',' + str(self.col)

    def __eq__(self, other: Location) -> bool:
        """Return True if self equals other, and false otherwise.

        """
        return (self.row == other.row) and (self.col == other.col)


def manhattan_distance(origin: Location, destination: Location) -> int:
    """Return the Manhattan distance between the origin and the destination.

    """
    x = abs(destination.col - origin.col)
    y = abs(destination.row - origin.row)
    return x + y


def deserialize_location(location_str: str) -> Location:
    """Deserialize a location.

    location_str: A location in the format 'row,col'
    """
    data = location_str.split(',')
    loc = Location(int(data[0]), int(data[1]))
    return loc


if __name__ == '__main__':
    import python_ta
    python_ta.check_all()
