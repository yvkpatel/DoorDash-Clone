# -------------------------------------------------------------------------------------------------------------------------------------

# -------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------ Restaurant Class -------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------------

# @intializes  
#           Type: String
#           Description: restaurant id
#           Type: String
#           Description: restaurant username
#           Type: String
#           Description: restaurant name 
#           Type: list
#           Description: restaurant order list
#           Type: String
#           Description: restaurant menu id
#           Type: String
#           Description: restaurant category
#           Type: String
#           Description: restaurant availabilty i.e. open or closed
#           Type: String
#           Description: opening time for the restaurant
#           Type: String
#           Description: closing time for the restaurant  
#           Type: String
#           Description: restaurant address   
#           Type: String
#           Description: restaurant address postal code  
class Restaurant:
    
    def __init__(self, id, username, name, orders, menuID, category, availability, openHour, closeHour, address, postal):
        self.__id = id
        self.__username = username
        self.__name = name
        self.__orders = orders
        self.__menuID = menuID
        self.__category = category
        self.__availability = availability
        self.__openHour = openHour
        self.__closeHour = closeHour
        self.__address = address
        self.__postal = postal

    def getId(self):
        return self.__id

    def getUsername(self):
        return self.__username

    def getName(self):
        return self.__name

    def getCategory(self):
        return self.__category

    def getAvailability(self):
        return self.__availability

    def getOpenHour(self):
        return self.__openHour

    def getCloseHour(self):
        return self.__closeHour

    def getAddress(self):
        return self.__address

    def getPostal(self):
        return self.__postal

    def getOrders(self):
        return self.__orders

    def getMenuID(self):
        return self.__menuID
