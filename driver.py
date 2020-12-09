"""Drivers for the simulation"""

from location import Location, manhattan_distance
from rider import Rider


class Driver:
    """A driver for a ride-sharing service.

    === Attributes ===
    id: A unique identifier for the driver.
    location: The current location of the driver.
    is_idle: True if the driver is idle and False otherwise.
    """

    id: str
    location: Location
    speed: int
    is_idle: bool
    passenger: Rider
    destination: Location

    def __init__(self, identifier: str, location: Location, speed: int) -> None:
        """Initialize a Driver.

        """
        self.id = identifier
        self.location = location
        self.speed = speed
        self.passenger = None
        self.is_idle = True
        self.destination = None

    def __str__(self) -> str:
        """Return a string representation.

        """
        return "{} at location {}".format(self.id, self.location)

    def __eq__(self, other: object) -> bool:
        """Return True if self equals other, and false otherwise.

        """
        if type(other) != Driver:
            return False
        else:
            return self.id == other.id and self.location == other.location \
                and self.is_idle == other.is_idle

    def get_travel_time(self, destination: Location) -> int:
        """Return the time it will take to arrive at the destination,
        rounded to the nearest integer.

        """
        dist = manhattan_distance(self.location, destination)
        time = dist / self.speed
        return round(time)

    def start_drive(self, location: Location) -> int:
        """Start driving to the location.
        Return the time that the drive will take.

        """
        self.is_idle = False
        self.destination = location
        return self.get_travel_time(location)

    def end_drive(self) -> None:
        """End the drive and arrive at the destination.

        Precondition: self.destination is not None.

        """
        self.location = self.destination
        self.is_idle = True
        self.destination = None

    def start_ride(self, rider: Rider) -> int:
        """Start a ride and return the time the ride will take.

        """
        self.location = self.destination
        self.destination = rider.destination
        self.passenger = rider
        return self.get_travel_time(self.destination)

    def end_ride(self) -> None:
        """End the current ride, and arrive at the rider's destination.

        Precondition: The driver has a rider.
        Precondition: self.destination is not None.

        """
        self.passenger.origin = self.destination
        self.location = self.destination
        self.passenger = None


if __name__ == '__main__':
    import python_ta
    python_ta.check_all(
        config={'extra-imports': ['location', 'rider']})
