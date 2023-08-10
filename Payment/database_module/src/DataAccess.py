from random import randint
import Utils.MainConnection as conn
from Utils.GatewayUtils import GatewayUtils

from Gateways.UserGateway import UserGateway

from Gateways.CustomersGateway import CustomerGateway
from DataStructures.Customer import Customer

from Gateways.DriversGateway import DriverGateway
from DataStructures.Driver import Driver

from Gateways.RestaurantsGateway import RestaurantGateway
from DataStructures.Restaurant import Restaurant

from Gateways.OrdersGateway import OrderGateway
from DataStructures.Order import Order

from Gateways.MenuGateway import MenuGateway
from DataStructures.Menu import Menu
from DataStructures.Item import Item

# -------------------------------------------------------------------------------------------------------------------------------------

# -------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------ Data Access Class ------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------------

# @intializes  
#           Type: String
#           Description: data base name requested.
class DataAccess:
  
    def __init__(self, serverType):
        self.cnx = conn.createDatabaseConn(serverType)

        self.authGateway = UserGateway(self.cnx)
        self.authGatewayCNX = self.authGateway.cnx

        self.customerGateway = CustomerGateway(self.cnx)
        self.driverGateway = DriverGateway(self.cnx)
        self.restaurantGateway = RestaurantGateway(self.cnx)

        self.orderGateway = OrderGateway(self.cnx)
        self.menuGateway = MenuGateway(self.cnx)

        self.gatewayUtil = GatewayUtils()

    # -------------------------------------------------------------------------------------------------------------------------------------

    # -------------------------------------------------------------------------------------------------------------------------------------
    # ------------------------------------------------------ Customer Access --------------------------------------------------------------
    # -------------------------------------------------------------------------------------------------------------------------------------
   
    # @params
    #           Type: String
    #           Description: requested customer id
    # @returns
    #           Type: Customer (see data structure)
    #           Description: returns a customer
    def getCustomerFromID(self, custID):
        try:
            customer = self.customerGateway.getCustomerProfileFromID(custID)
            if customer.getId() is None:
                return None
            return customer
        except Exception as e:
            print(e)
            return None

    # @params
    #           Type: String
    #           Description: requested customer username
    # @returns
    #           Type: Customer (see data structure)
    #           Description: returns a customer
    def getCustomerFromUsername(self, username):
        try:
            customer = self.customerGateway.getCustomerProfileFromUsername(username)
            if customer.getId() is None:
                return None
            return customer
        except Exception as e:
            print(e)
            return None
    
    # @params
    #           Type: String
    #           Description: customer username
    #           Type: String
    #           Description: customer password
    #           Type: String
    #           Description: customer name 
    #           Type: String
    #           Description: customer home address   
    #           Type: String
    #           Description: customer home address postal code  
    # @returns
    #           Type: boolean
    #           Description: returns true if customer is added successfully false otherwise
    def addCustomer(self, username, passHash, name, address, postal):
        try:
            if self.gatewayUtil.isUsernameUnique(username, self.authGatewayCNX):
                custID = "C" + str(randint(100000000, 999999999))
                newCustomer = Customer(custID, username, name, [], address, postal)
                self.customerGateway.insertCustomer(newCustomer)
                return self.authGateway.addUser(custID, username, passHash)
            else:
                print("Username is not unique and cannot be inserted")
                return False
        except Exception as e:
            print(e)
            return False

    # -------------------------------------------------------------------------------------------------------------------------------------

    # -------------------------------------------------------------------------------------------------------------------------------------
    # ------------------------------------------------------ Driver Access ----------------------------------------------------------------
    # -------------------------------------------------------------------------------------------------------------------------------------

    # @params
    #           Type: String
    #           Description: requested driver id
    # @returns
    #           Type: Driver (see data structure)
    #           Description: returns a driver from id
    def getDriverFromID(self, driverID):
        try:
            driver = self.driverGateway.getDriverProfileFromID(driverID)
            if driver.getId() is None:
                return None
            return driver
        except Exception as e:
            print(e)
            return None

    # @params
    #           Type: String
    #           Description: requested driver username
    # @returns
    #           Type: Driver (see data structure)
    #           Description: returns a driver from username
    def getDriverFromUsername(self, username):
        try:
            driver = self.driverGateway.getDriverProfileFromUsername(username)
            if driver.getId() is None:
                return None
            return driver
        except Exception as e:
            print(e)
            return None
    
    # @params
    #           Type: String
    #           Description: driver username
    #           Type: String
    #           Description: driver password
    #           Type: String
    #           Description: driver name  
    # @returns
    #           Type: boolean
    #           Description: returns true if driver is added successfully false otherwise.
    def addDriver(self, username, passHash, name):
        try:
            if self.gatewayUtil.isUsernameUnique(username, self.authGatewayCNX):
                driverID = "D" + str(randint(100000000, 999999999))
                newDriver = Driver(driverID, username, name, False, [])
                self.driverGateway.insertDriver(newDriver)
                return self.authGateway.addUser(driverID, username, passHash)
            else:
                print("Username is not unique and cannot be inserted")
                return False
        except Exception as e:
            print(e)
            return False
    
    # @params
    #           Type: String
    #           Description: driver id to update
    #           Type: boolean
    #           Description: driver availability
    # @returns
    #           Type: boolean
    #           Description: Whether the driver availability has been updated
    def updateDriverAvailabilityFromID(self, driverID, availability: bool):
        try:
            return self.driverGateway.updateDriverAvailabilityFromID(driverID, availability)
        except Exception as e:
            print(e)
            return False

    # @params
    #           Type: String
    #           Description: driver username to update
    #           Type: boolean
    #           Description: driver availability
    # @returns
    #           Type: boolean
    #           Description: Whether the driver availability has been updated
    def updateDriverAvailabilityFromUsername(self, username, availability: bool):
        try:
            return self.driverGateway.updateDriverAvailabilityFromUsername(username, availability)
        except Exception as e:
            print(e)
            return False

    
    # @returns
    #           Type: Driver []
    #           Description: returns a list of all available drivers
    def getAvailableDrivers(self):
        try:
            return self.driverGateway.getAvailableDrivers()
        except Exception as e:
            print(e)
            return None

    # -------------------------------------------------------------------------------------------------------------------------------------

    # -------------------------------------------------------------------------------------------------------------------------------------
    # ------------------------------------------------------ Restaurant Access ------------------------------------------------------------
    # -------------------------------------------------------------------------------------------------------------------------------------

    # @params
    #           Type: String
    #           Description: restaurant username
    #           Type: String
    #           Description: restaurant password
    #           Type: String
    #           Description: restaurant name 
    #           Type: String
    #           Description: the category the restaurant belongs to
    #           Type: String
    #           Description: opening time for the restaurant
    #           Type: String
    #           Description: closing time for the restaurant  
    #           Type: String
    #           Description: restaurant address   
    #           Type: String
    #           Description: restaurant address postal code  
    # @returns
    #           Type: boolean
    #           Description: returns true if restaurant is added successfully false otherwise
    def addRestaurant(self, username, passHash, name, category, openHour, closeHour, address, postal):
        try:
            if self.gatewayUtil.isUsernameUnique(username, self.authGatewayCNX):
                restID = "R" + str(randint(100000000, 999999999))
                menuID = "M" + str(randint(100000000, 999999999))

                menu = Menu(menuID, restID, [])
                if self.menuGateway.insertMenu(menu):
                    newRestaurant = Restaurant(restID, username, name, [], menuID, category,
                                               False, openHour, closeHour, address, postal)
                    self.restaurantGateway.insertRestaurant(newRestaurant)
                    return self.authGateway.addUser(restID, username, passHash)
                else:
                    return False
            else:
                print("Username is not unique and cannot be inserted")
                return False
        except Exception as e:
            print(e)
            return False

    # @params
    #           Type: String
    #           Description: requested restaurant id
    # @returns
    #           Type: Restaurant (see data structure)
    #           Description: returns a restaurant from id
    def getRestaurantFromID(self, restID):
        try:
            restaurant = self.restaurantGateway.getRestaurantFromID(restID)
            if restaurant.getId() is None:
                return None
            return restaurant
        except Exception as e:
            print(e)
            return None

    # @params
    #           Type: String
    #           Description: requested restaurant username
    # @returns
    #           Type: Restaurant (see data structure)
    #           Description: returns a restaurant from username
    def getRestaurantFromUsername(self, username):
        try:
            restaurant = self.restaurantGateway.getRestaurantFromUsername(username)
            if restaurant.getId() is None:
                return None
            return restaurant
        except Exception as e:
            print(e)
            return None

    # @params
    #           Type: String
    #           Description: restaurant category
    # @returns
    #           Type: Restaurant (see data structure)
    #           Description: returns a restaurant from category
    def getRestaurantsFromCategory(self, category):
        try:
            restaurants = self.restaurantGateway.getRestaurantsByCategory(category)
            if restaurants[0].getId() is None:
                return None
            return restaurants
        except Exception as e:
            print(e)
            return None

    # @returns
    #           Type: Restaurant []
    #           Description: returns a list of all available restaurant
    def getAvailableRestaurants(self):
        try:
            return self.restaurantGateway.getAvailableRestaurants()
        except Exception as e:
            print(e)
            return None

    # @params
    #           Type: String
    #           Description: restaurant id to update
    #           Type: boolean
    #           Description: restaurant availability
    # @returns
    #           Type: boolean
    #           Description: Whether the restaurant availability has been updated
    def updateRestaurantAvailabilityFromID(self, restID, availability: bool):
        try:
            return self.restaurantGateway.updateRestaurantAvailabilityFromID(restID, availability)
        except Exception as e:
            print(e)
            return False

    # @params
    #           Type: String
    #           Description: restaurant username to update
    #           Type: boolean
    #           Description: restaurant availability
    # @returns
    #           Type: boolean
    #           Description: Whether the restaurant availability has been updated
    def updateRestaurantAvailabilityFromUsername(self, username, availability: bool):
        try:
            return self.restaurantGateway.updateRestaurantAvailabilityFromUsername(username, availability)
        except Exception as e:
            print(e)
            return False

    # @params
    #           Type: String
    #           Description: restaurant id
    #           Type: String
    #           Description: item name
    #           Type: String
    #           Description: item category
    #           Type: Double
    #           Description: Cost
    #           Type: Integer
    #           Description: Prep time
    #           Type: Integer
    #           Description: Calories
    # @returns
    #           Type: boolean
    #           Description: Whether the item was added
    def addItemToRestaurant(self, restaurantID, name, category, cost, prepTime, calories):
        try:
            itemID = "I" + str(randint(100, 999))
            item = Item(itemID, name, category, cost, prepTime, calories)
            menuID = self.restaurantGateway.getRestaurantFromID(restaurantID).getMenuID()
            return self.menuGateway.addItem(menuID, item)
        except Exception as e:
            print(e)
            return False

    # -------------------------------------------------------------------------------------------------------------------------------------

    # -------------------------------------------------------------------------------------------------------------------------------------
    # ------------------------------------------------------ Order Access -----------------------------------------------------------------
    # -------------------------------------------------------------------------------------------------------------------------------------

    # @params
    #           Type: double
    #           Description: order total cost
    #           Type: list
    #           Description: list of items in the order
    #           Type: String
    #           Description: order status i.e. (in-progress, out for delivery, delivered) 
    #           Type: String
    #           Description: estimated preparation time
    #           Type: Integer
    #           Description: estimated time of arrival for order in minutes
    #           Type: String
    #           Description: address to be delivered to  
    #           Type: String
    #           Description: restaurant id   
    #           Type: String
    #           Description: customer id  
    # @returns
    #           Type: String
    #           Description: returns the order id
    def addOrder(self, cost, items, status, prepTime, eta, deliveryAddress, restID, custID):
        try:
            orderID = "O" + str(randint(100000000, 999999999))
            newOrder = Order(orderID, cost, items, status, prepTime, eta, deliveryAddress, restID, custID, "")
            orderPlaced = self.orderGateway.insertOrder(newOrder)
            if orderPlaced:
                self.customerGateway.addOrder(custID, orderID)
                self.restaurantGateway.addOrder(restID, orderID)
                return orderID
            else:
                return None
        except Exception as e:
            print(e)
            return None
    
    # @params
    #           Type: String
    #           Description: order id 
    # @returns
    #           Type: Order (see data structure)
    #           Description: returns a order from id
    def getOrderFromID(self, orderID):
        try:
            order = self.orderGateway.getOrder(orderID)
            if order.getId() is None:
                return None
            return order
        except Exception as e:
            print(e)
            return None

    # @params
    #           Type: String
    #           Description: order id
    #           Type: String
    #           Description: driver id
    # @returns
    #           Type: Order (see data structure)
    #           Description: returns a order from id
    def assignDriverToOrder(self, orderID, driverID):
        try:
            self.orderGateway.assignDriver(orderID, driverID)
            return True
        except Exception as e:
            print(e)
            return False

    # -------------------------------------------------------------------------------------------------------------------------------------

    # -------------------------------------------------------------------------------------------------------------------------------------
    # ------------------------------------------------------ Authenticate Database Access -------------------------------------------------
    # -------------------------------------------------------------------------------------------------------------------------------------
    
    # @params
    #           Type: String
    #           Description: order total cost
    #           Type: list
    #           Description: list of items in the order
    # @returns
    #           Type: boolean
    #           Description:  Wether the user has been authenticated
    def authenticateUser(self, username, passHash):
        try:
            return self.authGateway.authenticateUser(username, passHash)
        except Exception as e:
            print(e)
            return False
