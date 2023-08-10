import abc
import enum
import math
from typing import List

from algorithms_module.src.DatabaseRequestsMock import \
generateAlert,       \
getAvailableDrivers, \
getRestaurantFromId, \
assignDriverToOrder  

class Restaurant:
    def __init__(self, lat, long):
        self.lat = lat
        self.long = long

    def getLat(self):
        return self.lat

    def getLong(self):
        return self.long


class Driver:
    def __init__(self, lat, long):
        self.lat = lat
        self.long = long

    def getLat(self):
        return self.lat

    def getLong(self):
        return self.long


def distanceBetweenPoints(ax: float, ay: float, bx: float, by: float) -> float:
    """Returns distance between two points on a 2d plane"""
    return math.sqrt((bx - ax)**2 + (by - ay)**2)

class DriverSelectorType(enum.Enum):
    """Enum for types of driver selectors"""
    Radius = enum.auto()
    OpenStreetMap = enum.auto()
    GoogleMaps = enum.auto()


class DriverSelector(abc.ABC):
    """Driver selector abstract base class"""
    def __init__(self):
        pass

    def getClosestDriver(self, drivers, restaurant) -> Driver:
        """Algorithm to find driver closest to restaurant"""
        if len(drivers) == 0:
            # No driver to assign
            return
        closest = drivers[0]
        closest_distance = self.getDriverDistance(drivers[0], restaurant)
        for driver in drivers:
            distance = self.getDriverDistance(driver, restaurant)
            if distance < closest_distance:
                closest = driver
                closest_distance = distance
        return closest

    def assignDriver(self, order_id):
        """Gets list of drivers that are available to take order"""

        drivers = getAvailableDrivers()
        restaurant = getRestaurantFromId(order_id)
        closest_driver = self.getClosestDriver(drivers, restaurant)

        assignDriverToOrder(order_id, closest_driver)

        # This is the alert that networking wants, maybe implement
        # observer/subscriber
        generateAlert(order_id)

    @abc.abstractmethod
    def getDriverDistance(self, driver, restaurant):
        pass


class DriverSelectorBuilder:
    """Builder class for creating derived driver selector objects"""
    def __init__(self):
        self.selector_type = DriverSelectorType.Radius

    def setSelectorType(self, selector_type: DriverSelectorType):
        self.selector_type = selector_type

    def createDriverSelector(self) -> DriverSelector:
        """Creates correct type of driver selector based off of type"""
        if self.selector_type == DriverSelectorType.Radius:
            return RadiusDriverSelector()
        elif self.selector_type == DriverSelectorType.OpenStreetMap:
            return OpenStreetMapsDriverSelector()
        elif self.selector_type == DriverSelectorType.GoogleMaps:
            return GoogleMapsDriverSelector() 


class TimeDriverSelector(DriverSelector):
    def __init__(self):
        super().__init__()

    def getDriverDistance(self):
        """@override"""
        # Get driving time estimate for each driver, select shortest one
        # and add driver to order
        pass

    @abc.abstractmethod
    def getDriverTime(self, driver, restaurant):
        pass


class GoogleMapsDriverSelector(TimeDriverSelector):
    def __init__(self):
        super().__init__()

    def getDriverTime(self):
        """ @override """
        pass


class OpenStreetMapsDriverSelector(TimeDriverSelector):
    def __init__(self):
        super().__init__()

    def getDriverTime(self):
        """ @override """
        pass


class RadiusDriverSelector(DriverSelector):
    def __init__(self):
        pass

    def getDriverDistance(self, driver, restaurant):
        """@override"""
        distance = distanceBetweenPoints(restaurant.getLat(), restaurant.getLong(), driver.getLat(), driver.getLong())
        return distance


if __name__ == '__main__':
    # Example usage
    builder = DriverSelectorBuilder()
    selector_type = DriverSelectorType.Radius
    builder.setSelectorType(selector_type)

    selector = builder.createDriverSelector()
    selector.assignDriver(1)
