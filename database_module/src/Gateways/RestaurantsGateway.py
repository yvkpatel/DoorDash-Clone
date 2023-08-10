from DataStructures.Restaurant import Restaurant
from DataStructures.Menu import Menu
from DataStructures.Item import Item
from Utils.GatewayUtils import GatewayUtils

# @intializes 
#           Type: Pymongo.MongoClient.DatabaseConnection
#           Description: connection to Mongo database 
class RestaurantGateway:

    def __init__(self, dbConn):
        self.cnx = dbConn['restaurants']
        self.gatewayUtil = GatewayUtils()

    # @params
    #           Type: Restaurant
    #           Description: Restaurant object to be added to database
    # @returns
    #           Type: boolean
    #           Description: returns whether or not the Restaurant was successfully added to the database
    def insertRestaurant(self, restaurant: Restaurant):
        try:
            self.cnx.insert_one({'unique_id': restaurant.getId(),
                                 'username': restaurant.getUsername(),
                                 'name': restaurant.getName(),
                                 'orders': restaurant.getOrders(),
                                 'menu_id': restaurant.getMenuID(),
                                 'category': restaurant.getCategory(),
                                 'availability': restaurant.getAvailability(),
                                 'hour_open': restaurant.getOpenHour(),
                                 'hour_close': restaurant.getCloseHour(),
                                 'address': restaurant.getAddress(),
                                 'postal': restaurant.getPostal()})
            return True
        except Exception as e:
            print(e)

    # @params
    #           Type: String
    #           Description: category of restaurants to be obtained from database
    # @returns
    #           Type: Restaurant[]
    #           Description: returns a list of all restaurants filed under the inputted category
    def getRestaurantsByCategory(self, category):
        restaurants = []
        response = self.cnx.find({"category": category})
        for r in response:
            restaurant = self.gatewayUtil.createRestaurant(r)
            restaurants.append(restaurant)
        return restaurants

    # @params
    #           Type: String
    #           Description: ID corresponding to Restaurant object in database
    # @returns
    #           Type: Restaurant
    #           Description: returns Restaurant object corresponding to inputted ID
    def getRestaurantFromID(self, restID):
        response = self.cnx.find_one({"unique_id": restID})
        restaurant = self.gatewayUtil.createRestaurant(response)
        return restaurant

    # @params
    #           Type: String
    #           Description: username corresponding to Restaurant object in database
    # @returns
    #           Type: Restaurant
    #           Description: returns Restaurant object corresponding to inputted username
    def getRestaurantFromUsername(self, username):
        response = self.cnx.find_one({"username": username})
        restaurant = self.gatewayUtil.createRestaurant(response)
        return restaurant

    # @returns
    #           Type: Restaurant[]
    #           Description: returns a list of all restaurants that are currently available
    def getAvailableRestaurants(self):
        restaurants = []
        response = self.cnx.find({"availability": True})
        for r in response:
            restaurant = self.gatewayUtil.createRestaurant(r)
            restaurants.append(restaurant)
        return restaurants

    # @params
    #           Type: String
    #           Description: ID corresponding to Restaurant object in database
    #           Type: boolean
    #           Description: what to update the availability of the restaurant to
    # @returns
    #           Type: Restaurant
    #           Description: returns whether the restaurant availability was successfully updated
    def updateRestaurantAvailabilityFromID(self, restID, availability: bool):
        try:
            self.cnx.update_one({'unique_id': restID},
                                {"$set": {'availability': availability}})
            return True
        except Exception as e:
            print(e)
            return False

    # @params
    #           Type: String
    #           Description: username corresponding to Restaurant object in database
    #           Type: boolean
    #           Description: what to update the availability of the restaurant to
    # @returns
    #           Type: Restaurant
    #           Description: returns whether the restaurant availability was successfully updated
    def updateRestaurantAvailabilityFromUsername(self, username, availability: bool):
        try:
            self.cnx.update_one({'username': username},
                                {"$set": {'availability': availability}})
            return True
        except Exception as e:
            print(e)
            return False

    # @params
    #           Type: String
    #           Description: ID corresponding to Restaurant object in database
    #           Type: String
    #           Description: unique ID for the new order to be added
    # @returns
    #           Type: boolean
    #           Description: returns whether or not the order was successfully added to the database
    def addOrder(self, restID, orderID):
        try:
            self.cnx.update_one({'unique_id': restID},
                                {"$addToSet": {'orders': orderID}})
            return True
        except Exception as e:
            print(e)
            return False

    # @params
    #           Type: String
    #           Description: ID corresponding to Restaurant object in database
    # @returns
    #           Type: String Array
    #           Description: array containing order IDs
    def getOrderIDs(self, restID):
        try:
            rest = self.cnx.find_one({'unique_id': restID})
            return rest['orders']
        except Exception as e:
            print(e)
            return None

    # @params
    #           Type: String
    #           Description: ID corresponding to Restaurant object in database
    # @returns
    #           Type: String Array
    #           Description: array containing order IDs
    def getMenuID(self, restID):
        try:
            rest = self.cnx.find_one({'unique_id': restID})
            return rest['menu_id']
        except Exception as e:
            print(e)
            return None
