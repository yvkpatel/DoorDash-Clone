from DataStructures.Order import Order
from DataStructures.Restaurant import Restaurant
from DataStructures.Driver import Driver
from DataStructures.Customer import Customer
from DataStructures.Menu import Menu
import json


class GatewayUtils:

    # @params
    #           Type: String
    #           Description: ID to be checked for uniqueness
    #           Type: Pymongo.MongoClient.DatabaseConnection
    #           Description: connection to Mongo database to search
    # @returns
    #           Type: boolean
    #           Description: returns whether the ID is unique or not
    @staticmethod
    def isIdUnique(id, cnx):
        response = cnx.count_documents({"unique_id": id})
        if response == 0 or cnx.count() == 0:
            return True
        else:
            return False

    # @params
    #           Type: String
    #           Description: username to be checked for uniqueness
    #           Type: Pymongo.MongoClient.DatabaseConnection
    #           Description: connection to Mongo database to search
    # @returns
    #           Type: bool
    #           Description: returns whether the user is unique
    @staticmethod
    def isUsernameUnique(username, cnx):
        response = cnx.count_documents({"username": username})
        if response == 0 or cnx.count() == 0:
            return True
        else:
            return False

    # @params
    #           Type: Restaurant
    #           Description: Restaurant object to create json dump for
    # @returns
    #           Type: String
    #           Description: returns a json formatted String
    @staticmethod
    def createRestDump(rest: Restaurant):
        return json.dumps({
            'id': rest.getId(),
            'username': rest.getUsername(),
            'name': rest.getName(),
            'orders': rest.getOrders(),
            'menuID': rest.getMenuID(),
            'category': rest.getCategory(),
            'availability': rest.getAvailability(),
            'openHour': rest.getOpenHour(),
            'closeHour': rest.getCloseHour(),
            'address': rest.getAddress(),
            'postal': rest.getPostal()
        })

    # @params
    #           Type: Restaurant
    #           Description: Restaurant object to create json dump for
    # @returns
    #           Type: String
    #           Description: returns a list of json formatted Strings
    @staticmethod
    def createRestListDump(rests):
        return json.dumps([{
            'id': rest.getId(),
            'username': rest.getUsername(),
            'name': rest.getName(),
            'orders': rest.getOrders(),
            'menuID': rest.getMenuID(),
            'category': rest.getCategory(),
            'availability': rest.getAvailability(),
            'openHour': rest.getOpenHour(),
            'closeHour': rest.getCloseHour(),
            'address': rest.getAddress(),
            'postal': rest.getPostal()
        } for rest in rests])

    # @params
    #           Type: Driver
    #           Description: Driver object to create json dump for
    # @returns
    #           Type: String
    #           Description: returns a json formatted String
    @staticmethod
    def createDriverDump(driver: Driver):
        return json.dumps({
            'id': driver.getId(),
            'username': driver.getUsername(),
            'name': driver.getName(),
            'availability': driver.getAvailability(),
            'orders': driver.getOrders(),
            'long': driver.getLong(),
            'lat': driver.getLat()
        })

    # @params
    #           Type: Driver
    #           Description: Driver object to create json dump for
    # @returns
    #           Type: String
    #           Description: returns a list of json formatted Strings
    @staticmethod
    def createDriverListDump(drivers):
        return json.dumps([{
            'id': driver.getId(),
            'username': driver.getUsername(),
            'name': driver.getName(),
            'availability': driver.getAvailability(),
            'orders': driver.getOrders(),
            'long': driver.getLong(),
            'lat': driver.getLat()
        } for driver in drivers])

    # @params
    #           Type: Customer
    #           Description: Customer object to create json dump for
    # @returns
    #           Type: String
    #           Description: returns a json formatted String
    @staticmethod
    def createCustDump(cust: Customer):
        return json.dumps({
            'id': cust.getId(),
            'username': cust.getUsername(),
            'name': cust.getName(),
            'orders': cust.getOrders(),
            'address': cust.getAddress(),
            'postal': cust.getPostal()
        })

    # @params
    #           Type: Order
    #           Description: Order object to create json dump for
    # @returns
    #           Type: String
    #           Description: returns a json formatted String
    @staticmethod
    def createOrderDump(order: Order):
        return json.dumps({
            'id': order.getId(),
            'cost': order.getCost(),
            'items': order.getItems(),
            'status': order.getStatus(),
            'prepTime': order.getPrepTime(),
            'ETA': order.getETA(),
            'deliveryAddress': order.getDeliveryAddress(),
            'paymentInfo': order.getPaymentInfo(),
            'paymentFlag': order.getPaymentFlag(),
            'restID': order.getRestaurantID(),
            'userID': order.getUserID(),
            'driverID': order.getDriverID(),
            'notifications': order.getNotifications(),
            'chat': order.getChat()
        })

    @staticmethod
    def createOrderListDump(orders):
        return json.dumps([{
            'id': order.getId(),
            'cost': order.getCost(),
            'items': order.getItems(),
            'status': order.getStatus(),
            'prepTime': order.getPrepTime(),
            'ETA': order.getETA(),
            'deliveryAddress': order.getDeliveryAddress(),
            'paymentInfo': order.getPaymentInfo(),
            'paymentFlag': order.getPaymentFlag(),
            'restID': order.getRestaurantID(),
            'userID': order.getUserID(),
            'driverID': order.getDriverID(),
            'notifications': order.getNotifications(),
            'chat': order.getChat()
        } for order in orders])

    @staticmethod
    def createMenuDump(menu: Menu):
        return json.dumps({
            'id': menu.getId(),
            'restID': menu.getRestaurantId(),
            'items': menu.getItemList()
        })

    # @params
    #           Type: JSON
    #           Description: response object from database
    # @returns
    #           Type: Customer
    #           Description: returns customer item created from JSON object.
    @staticmethod
    def createCustomer(r):
        customer = Customer(r['unique_id'], r['username'], r['name'], r['orders'],
                            r['address'], r['postal'])
        return customer

    # @params
    #           Type: JSON
    #           Description: response object from database
    # @returns
    #           Type: Driver
    #           Description: returns driver item created from JSON object.
    @staticmethod
    def createDriver(r):
        driver = Driver(r['unique_id'], r['username'], r['name'],
                        r['availability'], r['orders'], r['long'], r['lat'])
        return driver

    # @params
    #           Type: JSON
    #           Description: response object from database
    # @returns
    #           Type: Menu
    #           Description: returns menu item created from JSON object.
    @staticmethod
    def createMenu(r):
        menu = Menu(r['unique_id'],
                    r['rest_id'], r['items'])
        return menu

    # @params
    #           Type: JSON
    #           Description: response object from database
    # @returns
    #           Type: Order
    #           Description: returns order item created from JSON object.
    @staticmethod
    def createOrder(r):
        order = Order(r['unique_id'], r['cost'], r['items'], r['status'],
                      r['prep_time'], r['ETA'], r['delivery_address'],
                      r['payment_info'], r['payment_flag'], r['restaurant_id'],
                      r['cust_id'], r['driver_id'], r['notifications'], r['chat'])
        return order

    # @params
    #           Type: JSON
    #           Description: response object from database
    # @returns
    #           Type: Restaurant
    #           Description: returns restaurant item created from JSON object.
    @staticmethod
    def createRestaurant(r):
        restaurant = Restaurant(r['unique_id'], r['username'], r['name'], r['orders'], r['menu_id'],
                                r['category'], r['availability'], r['hour_open'], r['hour_close'],
                                r['address'], r['postal'])
        return restaurant
