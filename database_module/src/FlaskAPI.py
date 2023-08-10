from DataAccess import DataAccess
from Utils.GatewayUtils import GatewayUtils

from flask import Flask, request
from distutils import util
from Utils.DataValidator import DataValidator
import json

api = Flask(__name__)
inst = DataAccess("Production")
gatewayUtils = GatewayUtils()
v = DataValidator()


# -------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------ LANDING API ------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------------

# @returns  
#           Type: boolean  
#           Description: response is if user is valid
@api.route("/", methods=['POST'])
def authenticateUser():
    validation = v.validateData("/", request)
    if not validation:
        return json.dumps({"reply": inst.authenticateUser(request.values.get('username'), request.values.get('passHash'))})
    else:
        return str(validation), 400
# -------------------------------------------------------------------------------------------------------------------------------------


# -------------------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------- CUSTOMER APIS -----------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------------

# @returns  
#           Type: Customer (see data structure)  
#           Description: customer object that was requested
@api.route("/customer/id/<id>")
def getUserFromID(id):
    cust = inst.getCustomerFromID(id)
    return gatewayUtils.createCustDump(cust)


# @returns  
#           Type: Customer (see data structure)  
#           Description: customer object that was requested
@api.route("/customer/user/<user>")
def getCustomerFromID(user):
    cust = inst.getCustomerFromUsername(user)
    return gatewayUtils.createCustDump(cust)


# @returns
#           Type: boolean
#           Description: returns true if customer is added successfully false otherwise
@api.route("/customer/add", methods=['POST'])
def addCustomer():
    validation = v.validateData("/customer/add", request)
    if not validation:
        return json.dumps({"reply": inst.addCustomer(request.values.get('username'), request.values.get('passHash'), request.values.get('name'),
                                                     request.values.get('address'), request.values.get('postal'))})
    else:
        return str(validation), 400
# -------------------------------------------------------------------------------------------------------------------------------------


# -------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------ DRIVER APIS ------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------------

# @returns  
#           Type: Driver (see data structure)  
#           Description: driver object that was requested
@api.route("/driver/id/<id>")
def getDriverFromID(id):
    driver = inst.getDriverFromID(id)
    return gatewayUtils.createDriverDump(driver)

# @returns
#           Type: Driver (see data structure)
#           Description: driver object that was requested
@api.route("/driver/user/<user>")
def getDriverFromUsername(user):
    driver = inst.getDriverFromUsername(user)
    return gatewayUtils.createDriverDump(driver)

# @returns
#           Type: Driver Array (see data structure)  
#           Description: drivers that are currently active
@api.route("/driver/available")
def getAvailableDrivers():
    drivers = inst.getAvailableDrivers()
    return gatewayUtils.createDriverListDump(drivers)

# @returns  
#           Type: boolean
#           Description: if driver was added
@api.route("/driver/add", methods=['POST'])
def addDriver():
    validation = v.validateData("/driver/add", request)
    if not validation:
        return json.dumps({"reply": inst.addDriver(request.values.get('username'), request.values.get('passHash'), request.values.get('name'))})
    else:
        return str(validation), 400

# @returns  
#           Type: boolean
#           Description: if driver availability was updated
@api.route("/driver/updateAvailability/id", methods=['POST'])
def updateDriverAvailabilityFromID():
    validation = v.validateData("/driver/updateAvailability/id", request)
    if not validation:
        return json.dumps({"reply": inst.updateDriverAvailabilityFromID(request.values.get('id'), bool(util.strtobool(request.values.get('availability'))))})
    else:
        return str(validation), 400

# @returns  
#           Type: boolean
#           Description: if driver availability was updated
@api.route("/driver/updateAvailability/user", methods=['POST'])
def updateDriverAvailabilityFromUsername():
    validation = v.validateData("/driver/updateAvailability/user", request)
    if not validation:
        return json.dumps({"reply": inst.updateDriverAvailabilityFromUsername(request.values.get('username'), bool(util.strtobool(request.values.get('availability'))))})
    else:
        return str(validation), 400

# @returns
#           Type: Order Array
#           Description: All orders that a driver has
@api.route("/driver/getOrders/<driverID>")
def getDriverOrders(driverID):
    orders = inst.getDriverOrders(driverID)
    return gatewayUtils.createOrderListDump(orders)

# @returns
#           Type: Location
#           Description:
@api.route("/driver/location/<driverID>")
def getDriverLocation(driverID):
    location = inst.getDriverLocation(driverID)
    return json.dumps(location)

# @returns
#           Type: Location
#           Description:
@api.route("/driver/location", methods=['POST'])
def setDriverLocation():
    validation = v.validateData("/driver/location", request)
    if not validation:
        return json.dumps({"reply": inst.setDriverLocation(request.values.get('driverID'),
                                                           request.values.get('long', type=float),
                                                           request.values.get('lat', type=float))})
    else:
        return str(validation), 400
# -------------------------------------------------------------------------------------------------------------------------------------


# -------------------------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------- RESTAURANT APIS ----------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------------

# @returns  
#           Type: boolean
#           Description: if restaurant was added
@api.route("/restaurant/add", methods=['POST'])
def addRestaurant():
    post = request.values
    validation = v.validateData("/restaurant/add", request)
    if not validation:
        return json.dumps({"reply": inst.addRestaurant(post.get('username'), post.get('passHash'),
                                                       post.get('name'), post.get('category'),
                                                       post.get('openHour'), post.get('closeHour'),
                                                       post.get('address'), post.get('postal'))})
    else:
        return str(validation), 400

# @returns  
#           Type: Restaurant (see data structure)  
#           Description: restaurant object that was requested
@api.route("/restaurant/id/<id>")
def getRestaurantFromID(id):
    rest = inst.getRestaurantFromID(id)
    return gatewayUtils.createRestDump(rest)

# @returns  
#           Type: Restaurant (see data structure)  
#           Description: restaurant object that was requested
@api.route("/restaurant/user/<user>")
def getRestaurantFromUsername(user):
    rests = inst.getRestaurantFromUsername(user)
    return gatewayUtils.createRestDump(rests)

# @returns  
#           Type: Restaurant Array (see data structure)  
#           Description: restaurants that belong to a category
@api.route("/restaurant/category/<category>")
def getRestaurantsFromCategory(category):
    rests = inst.getRestaurantsFromCategory(category)
    return gatewayUtils.createRestListDump(rests)

# @returns  
#           Type: Restaurant Array (see data structure)  
#           Description: restaurants that are currently available
@api.route("/restaurant/available")
def getAvailableRestaurants():
    rests = inst.getAvailableRestaurants()
    return gatewayUtils.createRestListDump(rests)

# @returns  
#           Type: boolean
#           Description: if restaurant availability was updated
@api.route("/restaurant/updateAvailability/id", methods=['POST'])
def updateRestaurantAvailabilityFromID():
    validation = v.validateData("/restaurant/updateAvailability/id", request)
    if not validation:
        return json.dumps({"reply": inst.updateRestaurantAvailabilityFromID(request.values.get('id'), bool(util.strtobool(request.values.get('availability'))))})
    else:
        return str(validation), 400
        
# @returns  
#           Type: boolean
#           Description: if restaurant availability was updated
@api.route("/restaurant/updateAvailability/user", methods=['POST'])
def updateRestaurantAvailabilityFromUsername():
    validation = v.validateData("/restaurant/updateAvailability/user", request)
    if not validation:
        return json.dumps({"reply": inst.updateRestaurantAvailabilityFromUsername(request.values.get('username'), bool(util.strtobool(request.values.get('availability'))))})
    else:
        return str(validation), 400

# @returns
#           Type: boolean
#           Description: if item was added
@api.route("/restaurant/menu/addItem", methods=['POST'])
def addItemToRestaurantMenu():
    validation = v.validateData("/restaurant/menu/addItem", request)
    if not validation:
        return json.dumps({"reply": inst.addItemToRestaurant(request.values.get('restaurantID'), request.values.get('name'),
                                                         request.values.get('category'), request.values.get('cost'),
                                                         request.values.get('prepTime'), request.values.get('calories'),
                                                         request.values.get('description'), request.values.get('imageLink'))})
    else:
        return str(validation), 400

# @returns
#           Type: Order Array
#           Description: All orders that a restaurant has
@api.route("/restaurant/getOrders/<restID>")
def getRestaurantOrders(restID):
    orders = inst.getRestaurantOrders(restID)
    return gatewayUtils.createOrderListDump(orders)

# @returns
#           Type: Menu
#           Description: restaurant menu
@api.route("/restaurant/menu/<restID>")
def getRestaurantMenu(restID):
    menu = inst.getRestaurantMenu(restID)
    return gatewayUtils.createMenuDump(menu)

# -------------------------------------------------------------------------------------------------------------------------------------


# -------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------- ORDER APIS ------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------------

# how to push items
# @returns  
#           Type: string 
#           Description: order id
@api.route("/order/add", methods=['POST'])
def addOrder():
    post = request.values
    validation = v.validateData("/order/add", request)
    if not validation:
        return json.dumps({"orderID": inst.addOrder(post.get('cost'), post.get('items'),
                                                    post.get('status'), post.get('prepTime', type=int),
                                                    post.get('eta', type=int), post.get('deliveryAddress'),
                                                    post.get('ccNumber', type=int), post.get('cvv', type=int), post.get('exp'),
                                                    post.get('firstName'), post.get('lastName'), post.get('postal'),
                                                    post.get('restID'), post.get('custID'))})
    else:
        return str(validation), 400

# @returns  
#           Type: Order (see data structure)  
#           Description: order that was requested
@api.route("/order/id/<orderID>")
def getOrderFromID(orderID):
    order = inst.getOrderFromID(orderID)
    return gatewayUtils.createOrderDump(order)

# @returns
#           Type: boolean
#           Description: Whether driver was assigned
@api.route("/order/assignDriver", methods=['POST'])
def assignDriver():
    post = request.values
    validation = v.validateData("/order/assignDriver", request)
    if not validation:
        return json.dumps({"reply": inst.assignDriverToOrder(post.get('orderID'), post.get('driverID'))})
    else:
        return str(validation), 400

# @returns
#           Type: boolean
#           Description: Whether order status was updated
@api.route("/order/updateStatus", methods=['POST'])
def updateOrderStatus():
    post = request.values
    validation = v.validateData("/order/updateStatus", request)
    if not validation:
        return json.dumps({"reply": inst.updateOrderStatus(post.get('orderID'), post.get('status'))})
    else:
        return str(validation), 400

# @returns
#           Type: boolean
#           Description: Whether eta was updated
@api.route("/order/addETA", methods=['POST'])
def addETAtoOrder():
    post = request.values
    validation = v.validateData("/order/addETA", request)
    if not validation:
        return json.dumps({"reply": inst.addETAtoOrder(post.get('orderID'), post.get('eta', type=int))})
    else:
        return str(validation), 400

# @returns
#           Type: Order Array
#           Description: All orders that are unpaid
@api.route("/order/payment/getOrdersUnpaid")
def getUnpaidOrders():
    orders = inst.getUnpaidOrders()
    return gatewayUtils.createOrderListDump(orders)

# @returns
#           Type: Order Array
#           Description: All orders that have not been assigned a driver
@api.route("/order/getUnassignedDriver")
def getUnassignedDriver():
    orders = inst.getOrdersUnassignedDriver()
    return gatewayUtils.createOrderListDump(orders)

# @returns
#           Type: Order Array
#           Description: all orders
@api.route("/order/all")
def getAllOrders():
    orders = inst.getAllOrders()
    return gatewayUtils.createOrderListDump(orders)

# @returns
#           Type: boolean
#           Description: Whether driver was assigned
@api.route("/order/payment/update", methods=['POST'])
def updatePaymentFlag():
    post = request.values
    validation = v.validateData("/order/payment/update", request)
    if not validation:
        return json.dumps({"reply": inst.updatePaymentFlag(post.get('orderID'), bool(util.strtobool(post.get('paid'))))})
    else:
        return str(validation), 400

# @returns
#           Type: boolean
#           Description: Whether notification was pushed
@api.route("/order/push/notification", methods=['POST'])
def pushNotification():
    post = request.values
    validation = v.validateData("/order/push/notification", request)
    if not validation:
        return json.dumps({"reply": inst.pushNotification(post.get('orderID'), post.get('notification'))})
    else:
        return str(validation), 400
# @returns
#           Type: boolean
#           Description: Whether notification was pushed
@api.route("/order/push/chat", methods=['POST'])
def pushChat():
    post = request.values
    validation = v.validateData("/order/push/chat", request)
    if not validation:
        return json.dumps({"reply": inst.pushChat(post.get('orderID'), post.get('receiver'), post.get('datetime'), post.get('message'))})
    else:
        return str(validation), 400
# -------------------------------------------------------------------------------------------------------------------------------------


# -------------------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------- RUN ---------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------------

if __name__ == "__main__":
    api.run(host="0.0.0.0", port=5000)

# -------------------------------------------------------------------------------------------------------------------------------------
