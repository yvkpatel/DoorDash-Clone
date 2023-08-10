from DataStructures.Menu import Menu
from DataStructures.Item import Item
from Utils.GatewayUtils import GatewayUtils

# @intializes 
#           Type: Pymongo.MongoClient.DatabaseConnection
#           Description: connection to Mongo database 
class MenuGateway:

    def __init__(self, dbConn):
        self.cnx = dbConn['menus']
        self.gatewayUtil = GatewayUtils()

    # @params
    #           Type: Menu
    #           Description: Menu object to be added
    # @returns
    #           Type: boolean
    #           Description: returns whether or not the Menu was successfully added to the database
    def insertMenu(self, menu: Menu):
        if self.gatewayUtil.isIdUnique(menu.getId(), self.cnx):
            try:
                self.cnx.insert_one({'unique_id': menu.getId(),
                                     'restaurant_id': menu.getRestaurantId(),
                                     'items': menu.getItemList()})
                return True
            except Exception as e:
                print(e)
        else:
            print("Id is not unique and cannot be inserted")
            return False

    # @params
    #           Type: String
    #           Description: ID of menu to get
    # @returns
    #           Type: Menu
    #           Description: returns Menu object corresponding to menuID
    def getMenu(self, menuID):
        items = []
        response = self.cnx.find_one({"unique_id": menuID})
        for item in response['items']:
            itemObj = Item(item['id'], item['name'], item['category'],
                           item['cost'], item['prepTime'], item['cals'])
            items.append(itemObj)

        menu = Menu(response['unique_id'],
                    response['rest_id'], items)
        return menu

    # @params
    #           Type: String
    #           Description: ID of menu
    #           Type: Item (see data structure)
    #           Description: item to add
    # @returns
    #           Type: boolean
    #           Description: returns whether item was added
    def addItem(self, menuID, item: Item):
        try:
            self.cnx.update_one({'unique_id': menuID},
                                {"$push": {'items': item.__dict__}})
            return True
        except Exception as e:
            print(e)
            return False
