# @intializes 
#           Type: Pymongo.MongoClient.DatabaseConnection
#           Description: connection to Mongo database 
class UserGateway:

    def __init__(self, dbConn):
        self.cnx = dbConn['user_auth']

    # @params
    #           Type: String
    #           Description: ID corresponding to user to be added
    #           Type: String
    #           Description: username of user to be added
    #           Type: String
    #           Description: password of user to be added
    # @returns
    #           Type: Restaurant
    #           Description: returns whether the user was successfully added to the database
    def addUser(self, userID, username, passHash):
        self.cnx.insert_one({'unique_id': userID,
                             'username': username,
                             'password': passHash})
        return True

    # @params
    #           Type: String
    #           Description: username for user
    #           Type: String
    #           Description: password corresponding to user
    # @returns
    #           Type: Restaurant
    #           Description: returns whether the restaurant availability was successfully updated
    def authenticateUser(self, username, passHash):
        response = self.cnx.count_documents({"username": username,
                                             "password": passHash})
        if response == 1:
            return True
        else:
            return False
