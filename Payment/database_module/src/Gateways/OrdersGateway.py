from DataStructures.Order import Order
from Utils.GatewayUtils import GatewayUtils

# @intializes 
#           Type: Pymongo.MongoClient.DatabaseConnection
#           Description: connection to Mongo database 
class OrderGateway:

    def __init__(self, dbConn):
        self.cnx = dbConn['orders']
        self.gatewayUtil = GatewayUtils()

    # @params
    #           Type: Order
    #           Description: Order object to add to database
    # @returns
    #           Type: boolean
    #           Description: returns whether or not the order was successfully added to the database
    def insertOrder(self, order: Order):
        if self.gatewayUtil.isIdUnique(order.getId(), self.cnx):
            try:
                self.cnx.insert_one({'unique_id': order.getId(),
                                     'cost': order.getCost(),
                                     'items': order.getItems(),
                                     'status': order.getStatus(),
                                     'prep_time': order.getPrepTime(),
                                     'ETA': order.getETA(),
                                     'delivery_address': order.getDeliveryAddress(),
                                     'restaurant_id': order.getRestaurantID(),
                                     'user_id': order.getUserID(),
                                     'driver_id': order.getDriverID()})
                return True
            except Exception as e:
                print(e)
                return False
        else:
            print("Id is not unique and cannot be inserted")
            return False

    # @params
    #           Type: String
    #           Description: ID corresponding to Order object in database
    # @returns
    #           Type: Order
    #           Description: returns the Order object with ID as inputted
    def getOrder(self, orderID):
        response = self.cnx.find_one({"unique_id": orderID})
        order = Order(response['unique_id'], response['cost'], response['items'], response['status'],
                      response['prep_time'], response['ETA'], response['delivery_address'],
                      response['restaurant_id'], response['user_id'], response['driver_id'])
        return order

    # @params
    #           Type: String
    #           Description: ID corresponding to Driver object in database
    #           Type: boolean
    #           Description: new order status to update the database with
    # @returns
    #           Type: boolean
    #           Description: returns whether or not the order was successfully added to the database
    def updateOrderStatus(self, orderID, status):
        self.cnx.update_one({'unique_id': orderID},
                            {"$set": {'status': status}})

    # @params
    #           Type: String
    #           Description: ID corresponding to Order object in database
    #           Type: String
    #           Description: ID corresponding to Driver in database
    # @returns
    #           Type: boolean
    #           Description: returns whether or not the order was successfully added to the database
    def assignDriver(self, orderID, driverID):
        self.cnx.update_one({'unique_id': orderID},
                            {"$set": {'driver_id': driverID}})
