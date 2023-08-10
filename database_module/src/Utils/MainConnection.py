import pymongo
import ssl

# @params
#           Type: String
#           Description: type of the database
# @returns
#           Type: Pymongo.MongoClient.DatabaseConnection
#           Description: returns connection to Pymongo database
def createDatabaseConn(db):
    try:
        client = pymongo.MongoClient(
            "mongodb+srv://dev_acc:trHyvl68qMfSw5NO@notimetofry.19wk2.mongodb.net/myFirstDatabase?retryWrites=true&w=majority",
            ssl_cert_reqs=ssl.CERT_NONE)

        return client[db]

    except Exception as e:
        print(e)

# @returns
#           Type: boolean
#           Description: returns whether the test is a success
def test():
    try:
        db = createDatabaseConn('TestDB')
        collection = db['entit_properties']

        test_driver = collection.find_one(
            {"user_type": "Driver", "unique_id": "1234567"})

        if test_driver["unique_id"] == "1234567":
            return True
        else:
            return False
    except:
        return False
