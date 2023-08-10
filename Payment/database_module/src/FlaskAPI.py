from DataAccess import DataAccess
from flask import Flask, request
from distutils import util
import json

api = Flask(__name__)
inst = DataAccess("Production")


# -------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------ LANDING API ------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------------

# @returns  
#           Type: boolean  
#           Description: response is if user is valid
@api.route("/", methods=['POST'])
def authenticateUser():
    post = request.values
    return json.dumps({"reply": inst.authenticateUser(post.get('username'), post.get('passHash'))})

# -------------------------------------------------------------------------------------------------------------------------------------


# -------------------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------- CUSTOMER APIS -----------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------------

# @returns  
#           Type: Customer (see data structure)  
#           Description: customer object that was requested
@api.route("/customer/id/<id>")
def getUserFromID(id):
    return json.dumps(inst.getCustomerFromID(id).__dict__)

# @returns  
#           Type: Customer (see data structure)  
#           Description: customer object that was requested
@api.route("/customer/user/<user>")
def getCustomerFromID(user):
    return json.dumps(inst.getCustomerFromUsername(user).__dict__)


# @returns
#           Type: boolean
#           Description: returns true if customer is added successfully false otherwise
@api.route("/customer/add", methods=['POST'])
def addCustomer():
    return json.dumps({"reply": inst.addCustomer(request.values.get('username'), request.values.get('passHash'), request.values.get('name'),
                                                 request.values.get('address'), request.values.get('postal'))})

# -------------------------------------------------------------------------------------------------------------------------------------


# -------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------ DRIVER APIS ------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------------

# @returns  
#           Type: Driver (see data structure)  
#           Description: driver object that was requested
@api.route("/driver/id/<id>")
def getDriverFromID(id):
    return json.dumps(inst.getDriverFromID(id).__dict__)

# @returns
#           Type: Driver (see data structure)
#           Description: driver object that was requested
@api.route("/driver/user/<user>")
def getDriverFromUsername(user):
    return json.dumps(inst.getDriverFromUsername(user).__dict__)

# @returns
#           Type: Driver Array (see data structure)  
#           Description: drivers that are currently active
@api.route("/driver/available")
def getAvailableDrivers():
    return json.dumps([z.__dict__ for z in inst.getAvailableDrivers()])

# @returns  
#           Type: boolean
#           Description: if driver was added
@api.route("/driver/add", methods=['POST'])
def addDriver():
    return json.dumps({"reply": inst.addDriver(request.values.get('username'), request.values.get('passHash'), request.values.get('name'))})

# @returns  
#           Type: boolean
#           Description: if driver availability was updated
@api.route("/driver/updateAvailability/id", methods=['POST'])
def updateDriverAvailabilityFromID():
    return json.dumps({"reply": inst.updateDriverAvailabilityFromID(request.values.get('id'), bool(util.strtobool(request.values.get('availability'))))})

# @returns  
#           Type: boolean
#           Description: if driver availability was updated
@api.route("/driver/updateAvailability/user", methods=['POST'])
def updateDriverAvailabilityFromUsername():
    return json.dumps({"reply": inst.updateDriverAvailabilityFromUsername(request.values.get('username'), bool(util.strtobool(request.values.get('availability'))))})

# -------------------------------------------------------------------------------------------------------------------------------------


# -------------------------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------- RESTAURANT APIS ----------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------------

# @returns  
#           Type: boolean
#           Description: if restaurant was added
@api.route("/restaurant/add", methods=['POST'])
def addRestaurant():
    post=request.values
    return json.dumps({"reply": inst.addRestaurant(post.get('username'), post.get('passHash'),
                                                   post.get('name'), post.get('category'),
                                                   post.get('openHour'), post.get('closeHour'),
                                                   post.get('address'), post.get('postal'))})

# @returns  
#           Type: Restaurant (see data structure)  
#           Description: restaurant object that was requested
@api.route("/restaurant/id/<id>")
def getRestaurantFromID(id):
    return json.dumps(inst.getRestaurantFromID(id).__dict__)

# @returns  
#           Type: Restaurant (see data structure)  
#           Description: restraunt object that was requested
@api.route("/restaurant/user/<user>")
def getRestaurantFromUsername(user):
    return json.dumps(inst.getRestaurantFromUsername(user).__dict__)

# @returns  
#           Type: Restaurant Array (see data structure)  
#           Description: restaurants that belong to a category
@api.route("/restaurant/category/<category>")
def getRestaurantsFromCategory(category):
    return json.dumps([z.__dict__ for z in inst.getRestaurantsFromCategory(category)])

# @returns  
#           Type: Restaurant Array (see data structure)  
#           Description: restaurants that are currently available
@api.route("/restaurant/available")
def getAvailableRestaurants():
    return json.dumps([z.__dict__ for z in inst.getAvailableRestaurants()])

# @returns  
#           Type: boolean
#           Description: if restaurant availability was updated
@api.route("/restaurant/updateAvailability/id", methods=['POST'])
def updateRestaurantAvailabilityFromID():
    return json.dumps({"reply": inst.updateRestaurantAvailabilityFromID(request.values.get('id'), bool(util.strtobool(request.values.get('availability'))))})

# @returns  
#           Type: boolean
#           Description: if restaurant availability was updated
@api.route("/restaurant/updateAvailability/user", methods=['POST'])
def updateRestaurantAvailabilityFromUsername():
    return json.dumps({"reply": inst.updateRestaurantAvailabilityFromUsername(request.values.get('username'), bool(util.strtobool(request.values.get('availability'))))})

# @returns
#           Type: boolean
#           Description: if item was added
@api.route("/restaurant/menu/addItem", methods=['POST'])
def addItemToRestaurantMenu():
    return json.dumps({"reply": inst.addItemToRestaurant(request.values.get('restaurantID'), request.values.get('name'),
                                                         request.values.get('category'), request.values.get('cost'),
                                                         request.values.get('prepTime'), request.values.get('calories'))})

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
    return json.dumps({"reply": inst.addOrder(post.get('cost'), post.get('items'),
                                              post.get('status'), post.get('prepTime'),
                                              post.get('eta'), post.get('deliveryAddress'),
                                              post.get('restID'), post.get('custID'))})

# @returns  
#           Type: Order (see data structure)  
#           Description: order that was requested
@api.route("/order/id/<orderID>")
def getOrderFromID(orderID):
    return json.dumps(inst.getOrderFromID(orderID).__dict__)

# @returns
#           Type: boolean
#           Description: Whether driver was assigned
@api.route("/order/assignDriver", methods=['POST'])
def assignDriver():
    post = request.values
    return json.dumps({"reply": inst.assignDriverToOrder(post.get('orderID'), post.get('driverID'))})

# -------------------------------------------------------------------------------------------------------------------------------------


# -------------------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------- RUN ---------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------------

if __name__=="__main__":
    api.run(host="0.0.0.0") 

# -------------------------------------------------------------------------------------------------------------------------------------
