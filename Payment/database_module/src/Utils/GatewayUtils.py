class GatewayUtils:

    # @params
    #           Type: String
    #           Description: ID to be checked for uniqueness
    #           Type: Pymongo.MongoClient.DatabaseConnection
    #           Description: connection to Mongo database to search
    # @returns
    #           Type: boolean
    #           Description: returns whether the ID is unique or not
    def isIdUnique(self, id, cnx):
        response = cnx.count_documents({"unique_id": id})
        if response == 0 or cnx.count() == 0:
            return True
        else:
            return False

    # @params
    #           Type: String
    #           Description: username to be checked for uniqueness
    #           Type: Pymongo.MongoClient.DatabaseConnection
    #           Description: connection to Mongo database to search
    # @returns
    #           Type: bool
    #           Description: returns whether the user is unique
    def isUsernameUnique(self, username, cnx):
        response = cnx.count_documents({"username": username})
        if response == 0 or cnx.count() == 0:
            return True
        else:
            return False
