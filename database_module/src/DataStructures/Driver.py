# -------------------------------------------------------------------------------------------------------------------------------------

# -------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------ Driver Class -----------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------------

# @intializes  
#           Type: String
#           Description: driver id 
#           Type: String
#           Description: unique username for driver
#           Type: String
#           Description: driver legal name
#           Type: boolean
#           Description: driver availability status
#           Type: list
#           Description: list of orders
class Driver:
    
    def __init__(self, id, username, name, availability, orders, long, lat):
        self.__id = id
        self.__username = username
        self.__name = name
        self.__availability = availability
        self.__orders = orders
        self.__long = long
        self.__lat = lat

    def getId(self):
        return self.__id

    def getUsername(self):
        return self.__username

    def getName(self):
        return self.__name

    def getAvailability(self):
        return self.__availability

    def getOrders(self):
        return self.__orders

    def getLong(self):
        return self.__long

    def getLat(self):
        return self.__lat
