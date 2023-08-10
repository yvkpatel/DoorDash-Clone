from DataStructures.Driver import Driver
from Utils.GatewayUtils import GatewayUtils

# @intializes 
#           Type: Pymongo.MongoClient.DatabaseConnection
#           Description: connection to Mongo database 
class DriverGateway:

    def __init__(self, dbConn):
        self.cnx = dbConn['drivers']
        self.gatewayUtil = GatewayUtils()

    # @params
    #           Type: Driver
    #           Description: Driver object to be added to database
    # @returns
    #           Type: boolean
    #           Description: returns whether the Driver object was successfully added to the database
    def insertDriver(self, driver: Driver):
        try:
            self.cnx.insert_one({'unique_id': driver.getId(),
                                 'username': driver.getUsername(),
                                 'name': driver.getName(),
                                 'availability': driver.getAvailability(),
                                 'orders': driver.getOrders()})
            return True
        except Exception as e:
            print(e)
            return False

    # @params
    #           Type: String
    #           Description: ID corresponding to Driver object in database
    # @returns
    #           Type: Driver
    #           Description: returns Driver object corresponding to inputted ID
    def getDriverProfileFromID(self, driverID):
        response = self.cnx.find_one({"unique_id": driverID})
        driver = Driver(response['unique_id'], response['username'], response['name'],
                        response['availability'], response['orders'])
        return driver

    # @params
    #           Type: String
    #           Description: username corresponding to Driver object in database
    # @returns
    #           Type: Driver
    #           Description: returns Driver object corresponding to inputted username
    def getDriverProfileFromUsername(self, username):
        response = self.cnx.find_one({"username": username})
        driver = Driver(response['unique_id'], response['username'], response['name'],
                        response['availability'], response['orders'])
        return driver

    # @params
    #           Type: String
    #           Description: ID corresponding to Driver object in database
    #           Type: boolean
    #           Description: whether or not the driver is currently available
    # @returns
    #           Type: boolean
    #           Description: returns whether or not the driver availability was successfully updated
    def updateDriverAvailabilityFromID(self, driverID, availability: bool):
        try:
            self.cnx.update_one({'unique_id': driverID},
                                {"$set": {'availability': availability}})
            return True
        except Exception as e:
            print(e)
            return False

    # @params
    #           Type: String
    #           Description: username corresponding to Driver object in database
    #           Type: boolean
    #           Description: whether or not the driver is currently available
    # @returns
    #           Type: boolean
    #           Description: returns whether or not the driver availability was successfully updated
    def updateDriverAvailabilityFromUsername(self, username, availability: bool):
        try:
            self.cnx.update_one({'username': username},
                                {"$set": {'availability': availability}})
            return True
        except Exception as e:
            print(e)
            return False

    # @params
    #           Type: String
    #           Description: ID corresponding to Driver object in database
    #           Type: String
    #           Description: unique ID for the new order to be added
    # @returns
    #           Type: boolean
    #           Description: returns whether or not the order was successfully added to the database
    def addOrder(self, driverID, orderID):
        try:
            self.cnx.update_one({'unique_id': driverID},
                                {"$addToSet": {'orders': orderID}})
            return True
        except Exception as e:
            print(e)
            return False

    # @returns
    #           Type: Driver[]
    #           Description: returns a list of all available drivers
    def getAvailableDrivers(self):
        drivers = []
        response = self.cnx.find({"availability": True})
        for r in response:
            driver = Driver(r['unique_id'], r['username'], r['name'],
                            r['availability'], r['orders'])
            drivers.append(driver)
        return drivers
