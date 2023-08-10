# -------------------------------------------------------------------------------------------------------------------------------------

# -------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------ Customer Class ---------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------------

# @intializes  
#           Type: String
#           Description: customer id 
#           Type: String
#           Description: unique username for customer
#           Type: String
#           Description: customer legal name
#           Type: list
#           Description: list of items the customer ordered 
#           Type: String
#           Description: home address for a customer 
#           Type: String
#           Description: postal code for customer address 
class Customer:

    def __init__(self, id, username, name, orders, address, postal):
        self.__id = id
        self.__username = username
        self.__name = name
        self.__orders = orders
        self.__address = address
        self.__postal = postal

    def getId(self):
        return self.__id

    def getUsername(self):
        return self.__username

    def getName(self):
        return self.__name

    def getOrders(self):
        return self.__orders

    def getAddress(self):
        return self.__address

    def getPostal(self):
        return self.__postal
