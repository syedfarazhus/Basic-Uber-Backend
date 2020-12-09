"""Dispatcher for the simulation"""

from typing import Optional, List
from driver import Driver
from rider import Rider


class Dispatcher:
    """A dispatcher fulfills requests from riders and drivers for a
    ride-sharing service.

    When a rider requests a driver, the dispatcher assigns a driver to the
    rider. If no driver is available, the rider is placed on a waiting
    list for the next available driver. A rider that has not yet been
    picked up by a driver may cancel their request.

    When a driver requests a rider, the dispatcher assigns a rider from
    the waiting list to the driver. If there is no rider on the waiting list
    the dispatcher does nothing. Once a driver requests a rider, the driver
    is registered with the dispatcher, and will be used to fulfill future
    rider requests.

    """
    drivers: List[Driver]
    waitlist: List[Rider]

    def __init__(self) -> None:
        """Initialize a Dispatcher.

        """
        self.drivers = []
        self.waitlist = []

    def __str__(self) -> str:
        """Return a string representation.

        """
        return "Dispatcher has {0} registered driver(s) and {1} wait " \
               "listed rider(s)".format(len(self.drivers), len(self.waitlist))

    def request_driver(self, rider: Rider) -> Optional[Driver]:
        """Return a driver for the rider, or None if no driver is available.

        Add the rider to the waiting list if there is no available driver.

        """
        count = 0
        if not self.drivers:
            self.waitlist.append(rider)
            return None
        for driver in self.drivers:
            if not driver.is_idle:
                count += 1
        if count == len(self.drivers):
            self.waitlist.append(rider)
            return None
        best = self.drivers[0]
        for dr in self.drivers:
            if dr.is_idle:
                if dr.get_travel_time(rider.origin) < \
                        best.get_travel_time(rider.origin):
                    best = dr
        return best

    def request_rider(self, driver: Driver) -> Optional[Rider]:
        """Return a rider for the driver, or None if no rider is available.

        If this is a new driver, register the driver for future rider requests.

        """
        if driver not in self.drivers:
            self.drivers.append(driver)
        if not self.waitlist:
            return None
        else:
            return self.waitlist.pop(0)

    def cancel_ride(self, rider: Rider) -> None:
        """Cancel the ride for rider.

        """
        if rider in self.waitlist:
            self.waitlist.remove(rider)


if __name__ == '__main__':
    import python_ta
    python_ta.check_all(config={'extra-imports': ['typing', 'driver', 'rider']})
