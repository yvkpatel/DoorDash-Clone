import enum
import math
import abc


class Point:
    """A class that stores a lat and lon pair"""

    def __init__(self, a, b, name):
        """Initializing this class requires a lat, lon, and name of the point"""
        self.lat = a
        self.lon = b
        self.name = name


class DeliveryTimeEstimatorType(enum.Enum):
    """Enum types for DeliveryTimeEstimator"""

    GoogleMaps = 0
    PersonToPerson = 1


class DeliveryTimeEstimatorBuilder:
    """The builder for Delivery Time Estimation"""

    def __init__(self):
        """Init takes in the Estimator Type and sets average speed to 0 by default"""
        self.type = DeliveryTimeEstimatorType.PersonToPerson
        self.speed = 0

    def setEstimatorType(self, type):
        self.type = type

    def setAverageSpeed(self, newSpeed):
        """This method is shared by both Estimator types, and sets the average speed"""
        self.speed = newSpeed

    def CreateDeliveryTimeEstimator(self):
        """Creates a Delivery Time Estimator based on a type"""
        if self.type == DeliveryTimeEstimatorType.PersonToPerson:
            return P2PTimeEstimator(self.speed)

        elif self.type == DeliveryTimeEstimatorType.GoogleMaps:
            return GoogleMapsEstimator()


class DeliveryTimeEstimator(abc.ABC):
    """The class that extands the builder"""

    def __init__(self):
        """The init method here calls the init method of the builder"""
        pass

    @abc.abstractmethod
    def getTimeEstimate(self, PointA, PointB):
        """Abstract method that is overridden by subclasses"""
        pass

    def getDeliveryTimeEstimate(self, PointA, PointB, PointC):
        """Obtains a time estiamte for an order using the restaurant, driver, and customer locations"""
        time1 = self.getTimeEstimate(PointA, PointB)
        time2 = self.getTimeEstimate(PointB, PointC)
        return (time1 + time2)


class P2PTimeEstimator(DeliveryTimeEstimator):
    """The P2PTimeEstimator extends the DeliveryTimeEstimator"""

    def __init__(self, speed):
        """This init method sets the speed and calls __init__ of the superclass"""
        super().__init__()
        self.speed = speed

    def getTimeEstimate(self, PointA, PointB):
        """Obtains a time estimate based on point to point distance"""
        lat = abs(PointA.lat - PointB.lat)
        lon = abs(PointA.lon - PointB.lon)
        distance = math.sqrt(lat ** 2 + lon ** 2)
        return (distance / self.speed)


class GoogleMapsEstimator(DeliveryTimeEstimator):
    def __init__(self):
        super().__init__()

    def getTimeEstimate(self):
        """ @override """
        pass


"""getDeliveryTimeEstimate function will take (self, OrderID) and call...

   time1 = getTimeEstimate(   getDriverLocation(getDriver(OrderID).ID)   , getRestaurant(OrderID)   ) and...
   time2 = getTimeEstimate(   getRestaurant(OrderID)   , getCustomer(OrderID)   )
   return (time1 + time2)"""

if __name__ == '__main__':
    builder = DeliveryTimeEstimatorBuilder()
    builder.setEstimatorType(DeliveryTimeEstimatorType.PersonToPerson)
    builder.setAverageSpeed(2)
    Estimator = builder.CreateDeliveryTimeEstimator()

    restaurant = Point(0, 0, "Restaurant")
    customer = Point(3, 4, "Customer")
    driver = Point(6, 8, "Driver")
    print("Total time is: " + str(Estimator.getDeliveryTimeEstimate(driver, restaurant, customer)) + " hr")
