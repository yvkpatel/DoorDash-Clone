from database_module.src.DataAccess import DataAccess

# --------------------------------- LOCAL TEST ---------------------------------
dataConn = DataAccess('Production')

restID = "R763567026"
custID = "C235771756"
dataConn.updateDriverAvailabilityFromUsername("newdriver02", True)
dataConn.updateRestaurantAvailabilityFromID("R763567026", True)

# TEST ADDs
print("--------------- ADD ---------------")
print(dataConn.addCustomer("hb", "this is my passowrd", "Hirthik B", "10 Baltimore", "A1B 3B7"))
print(dataConn.addDriver("newdriver02", "this is my passowrd", "John Driver"))
print(dataConn.addRestaurant("rest 1", "this is my passowrd", "Sushi Island", "Japanese",
                             "11h00", "22h00", "Water Street", "A1B 8H2"))
print(dataConn.addOrder(10, ["hello", "testing"], "Delivered", 10, 10,
                        "my house", restID, custID))
print("-----------------------------------")

# TEST GETs
print("--------------- GET ---------------")
print(dataConn.getCustomerFromUsername("hb").getName())
print(dataConn.getCustomerFromID("C235771756").getName())

print(dataConn.getDriverFromUsername("newdriver02").getName())
print(dataConn.getDriverFromID("D276241747").getName())
print(dataConn.getAvailableDrivers()[0].getName())

print(dataConn.getRestaurantFromUsername("rest 1").getName())
print(dataConn.getRestaurantFromID("R763567026").getName())
print(dataConn.getRestaurantsFromCategory("Japanese")[0].getName())
print(dataConn.getAvailableRestaurants()[0].getName())

print(dataConn.getOrderFromID("O616296448").getStatus())
print("-----------------------------------")

# TEST UPDATESs
print("-------------- UPDATE -------------")
print(dataConn.updateDriverAvailabilityFromID("D276241747", False))
print(dataConn.updateDriverAvailabilityFromUsername("newdriver01", True))

print(dataConn.updateRestaurantAvailabilityFromUsername("rest 1", False))
print(dataConn.updateRestaurantAvailabilityFromID("R763567026", True))
print("-----------------------------------")

# TEST AUTHENTICATE
print("----------- Authenticate ----------")
print(dataConn.authenticateUser("hb", "this is my passowrd"))
print(dataConn.authenticateUser("newdriver02", "this is my passowrd"))
print("-----------------------------------")
# ------------------------------------------------------------------------------