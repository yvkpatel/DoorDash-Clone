# -------------------------------------------------------------------------------------------------------------------------------------

# -------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------ Order Class ------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------------

# @intializes  
#           Type: String
#           Description: order id 
#           Type: double
#           Description: total cost of order
#           Type: list
#           Description: list of items ordered
#           Type: String
#           Description: order status  i.e.(in-progress, out for delivery, delivered) 
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
#           Type: String
#           Description: driver id  
class Order:
    
    def __init__(self, id, cost, items, status, prepTime, ETA, deliveryAddress, paymentInfo, paymentFlag, restID, userID, driverID, notifications, chat):
        self.__id = id
        self.__cost = cost
        self.__items = items
        self.__status = status
        self.__prepTime = prepTime
        self.__ETA = ETA
        self.__deliveryAddress = deliveryAddress
        self.__paymentInfo = paymentInfo
        self.__paymentFlag = paymentFlag
        self.__restID = restID
        self.__userID = userID
        self.__driverID = driverID
        self.__notifications = notifications
        self.__chat = chat

    def getId(self):
        return self.__id

    def getCost(self):
        return self.__cost

    def getItems(self):
        return self.__items

    def getStatus(self):
        return self.__status

    def getPrepTime(self):
        return self.__prepTime

    def getETA(self):
        return self.__ETA

    def getDeliveryAddress(self):
        return self.__deliveryAddress

    def getPaymentInfo(self):
        return self.__paymentInfo

    def getPaymentFlag(self):
        return self.__paymentFlag

    def getRestaurantID(self):
        return self.__restID

    def getUserID(self):
        return self.__userID

    def getDriverID(self):
        return self.__driverID

    def getNotifications(self):
        return self.__notifications

    def getChat(self):
        return self.__chat
