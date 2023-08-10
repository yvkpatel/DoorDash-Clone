# -------------------------------------------------------------------------------------------------------------------------------------

# -------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------ Menu Class -------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------------

# @intializes  
#           Type: String
#           Description: menu id 
#           Type: String
#           Description: restaurant id
#           Type: list
#           Description: list of items in menu
class Menu:
    
    def __init__(self, id, restaurantId, itemList):
        self.__id = id
        self.__restaurantId = restaurantId
        self.__itemList = itemList

    def getId(self):
        return self.__id

    def getRestaurantId(self):
        return self.__restaurantId

    def getItemList(self):
        return self.__itemList
