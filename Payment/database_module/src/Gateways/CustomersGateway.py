from Utils.GatewayUtils import GatewayUtils
from DataStructures.Customer import Customer

# @intializes 
#           Type: Pymongo.MongoClient.DatabaseConnection
#           Description: connection to Mongo database 
class CustomerGateway:

    def __init__(self, dbConn):
        self.cnx = dbConn['customers']
        self.gatewayUtil = GatewayUtils()


    # @params
    #           Type: Customer
    #           Description: Customer object to add to database
    # @returns
    #           Type: boolean
    #           Description: returns whether the Customer object has successfully been added to the database
    def insertCustomer(self, customer: Customer):
        try:
            self.cnx.insert_one({'unique_id': customer.getId(),
                                 'username': customer.getUsername(),
                                 'name': customer.getName(),
                                 'address': customer.getAddress(),
                                 'postal': customer.getPostal(),
                                 'orders': customer.getOrders()})
            return True
        except Exception as e:
            print(e)
            return False

    # @params
    #           Type: String
    #           Description: ID to find customer from
    # @returns
    #           Type: Customer
    #           Description: returns the Customer object corresponding to the ID
    def getCustomerProfileFromID(self, custID):
        response = self.cnx.find_one({"unique_id": custID})
        customer = Customer(response['unique_id'], response['username'], response['name'], response['orders'],
                            response['address'], response['postal'])
        return customer

    # @params
    #           Type: String
    #           Description: username to find customer from
    # @returns
    #           Type: Customer
    #           Description: returns the Customer object corresponding to the username
    def getCustomerProfileFromUsername(self, username):
        response = self.cnx.find_one({"username": username})
        customer = Customer(response['unique_id'], response['username'], response['name'], response['orders'],
                            response['address'], response['postal'])
        return customer

    # @params
    #           Type: String
    #           Description: customer ID corresponding to order
    #           Type: String
    #           Description: ID corresponding to new order
    # @returns
    #           Type: boolean
    #           Description: returns whether the order was successfully added
    def addOrder(self, custID, orderID):
        try:
            self.cnx.update_one({'unique_id': custID},
                                {"$addToSet": {'orders': orderID}})
            return True
        except Exception as e:
            print(e)
            return False
