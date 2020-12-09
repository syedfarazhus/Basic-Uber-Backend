"""
The rider module contains the Rider class. It also contains
constants that represent the status of the rider.

=== Constants ===
WAITING: A constant used for the waiting rider status.
CANCELLED: A constant used for the cancelled rider status.
SATISFIED: A constant used for the satisfied rider status
"""

from location import Location

WAITING = "waiting"
CANCELLED = "cancelled"
SATISFIED = "satisfied"


class Rider:

    """A rider for a ride-sharing service.

    Attributes:
        id: a unique identifier
        patience: The number of time units that the rider will wait to be picked
                  up before they cancel their ride
        origin: Where the rider is
        destination: Where the rider wants to go
        status: if the rider is waiting to
                be picked up, cancelled, or satisfied
    """
    id: str
    patience: int
    origin: Location
    destination: Location
    status: str

    def __init__(self, identifier: str, patience: int, origin: Location,
                 destination: Location) -> None:
        """Initialize a Rider.

        """
        self.id = identifier
        self.patience = patience
        self.origin = origin
        self.destination = destination
        self.status = WAITING

    def __str__(self) -> str:
        """Return a string representation.

        """
        return "{0} at location {1}".format(self.id, self.origin)


if __name__ == '__main__':
    import python_ta
    python_ta.check_all(config={'extra-imports': ['location']})
