from DataStructures.Order import Order
from DataStructures.Chat import Chat
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
                                     'payment_info': order.getPaymentInfo(),
                                     'payment_flag': order.getPaymentFlag(),
                                     'restaurant_id': order.getRestaurantID(),
                                     'cust_id': order.getUserID(),
                                     'driver_id': order.getDriverID(),
                                     'notifications': order.getNotifications(),
                                     'chat': order.getChat()})
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
        order = self.gatewayUtil.createOrder(response)
        return order

    # @params
    #           Type: String
    #           Description: ID corresponding to Order object in database
    # @returns
    #           Type: String
    #           Description: returns the order status for ID as inputted
    def getOrderStatus(self, orderID):
        response = self.cnx.find_one({"unique_id": orderID})
        return response['status']

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

    # @params
    #           Type: String
    #           Description: ID corresponding to Order object in database
    #           Type: Int
    #           Description: eta
    # @returns
    #           Type: boolean
    #           Description: returns whether or not the order eta was successfully added to the database
    def addETA(self, orderID, eta):
        self.cnx.update_one({'unique_id': orderID},
                            {"$set": {'ETA': eta}})

    # @params
    #
    # @returns
    #           Type: Order Array
    #           Description: returns the Orders objects that are unpaid
    def getUnpaidOrders(self):
        orders = []
        response = self.cnx.find({"payment_flag": False})
        for r in response:
            order = self.gatewayUtil.createOrder(r)
            orders.append(order)
        return orders

    # @params
    #
    # @returns
    #           Type: Order Array
    #           Description: returns the Orders objects that are unpaid
    def getUnassignedDriver(self):
        orders = []
        response = self.cnx.find({"driver_id": ""})
        for r in response:
            order = self.gatewayUtil.createOrder(r)
            orders.append(order)
        return orders

    # @params
    #
    # @returns
    #           Type: Order Array
    #           Description: returns the Orders objects that are unpaid
    def getAllOrders(self):
        orders = []
        response = self.cnx.find()
        for r in response:
            order = self.gatewayUtil.createOrder(r)
            orders.append(order)
        return orders

    # @params
    #           Type: String
    #           Description: ID corresponding to Order object in database
    #           Type: Boolean
    #           Description: if payment was successful
    # @returns
    #           Type: boolean
    #           Description: returns whether or not the order was successfully added to the database
    def updatePaymentFlag(self, orderID, paid):
        self.cnx.update_one({'unique_id': orderID},
                            {"$set": {'payment_flag': paid}})

    # @params
    #           Type: String
    #           Description: ID of menu
    #           Type: Item (see data structure)
    #           Description: item to add
    # @returns
    #           Type: boolean
    #           Description: returns whether item was added
    def pushChat(self, orderID, chat: Chat):
        try:
            self.cnx.update_one({'unique_id': orderID},
                                {"$push": {'chat': {
                                    'receiver': chat.getReceiver(),
                                    'datetime': chat.getDateTime(),
                                    'message': chat.getMessage()
                                }}})
            return True
        except Exception as e:
            print(e)
            return False

    # @params
    #           Type: String
    #           Description: ID of menu
    #           Type: Item (see data structure)
    #           Description: item to add
    # @returns
    #           Type: boolean
    #           Description: returns whether item was added
    def pushNotification(self, orderID, notification):
        try:
            self.cnx.update_one({'unique_id': orderID},
                                {"$push": {'notifications': notification}})
            return True
        except Exception as e:
            print(e)
            return False
