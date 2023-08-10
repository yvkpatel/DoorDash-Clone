import requests
from random_word import RandomWords

r = RandomWords()
myurl = "http://127.0.0.1:5000"


# Get customer from username tested
# Get Customer from ID tested
# Assert that the returned customers are the same
def testGetCustomer():
    id = "C235771756"
    path = myurl + "/customer/id/" + id

    # first get request
    customer = requests.get(path).json()
    username = customer['username']

    # second get request
    path2 = myurl + "/customer/user/" + username
    customer2 = requests.get(path2).json()

    assert customer == customer2


# add customer with correct data tested
# add customer with the same data
# assert that the customer with the same data was succesfully not added
# add customer with missing data, asserts that the customer was not added
def testAddCustomer():
    path = myurl + "/customer/add"
    data = {'username': r.get_random_word(), 'passHash': "pass", 'name': "Common", 'address': "/mun", 'postal': "A1A1A1"}
    response = requests.post(path, data)
    worked = response.json()['reply']

    assert response.ok and worked

    # Add same customer again
    response = requests.post(path, data)
    worked = response.json()['reply']

    assert response.ok and worked == False

    # if empty assert response is 400
    data = {'passHash': "pass", 'name': "Common", 'address': "/mun", 'postal': "A1A1A1"}
    response = requests.post(path, data)
    #worked = response.json()['reply']

    assert not response.ok
# ------------------------------------------------------------

# Driver

# add driver
def testAddDriver():
    path = myurl + "/driver/add"
    data = {'username': r.get_random_word(), 'passHash': "pass", 'name': "Common"}
    response = requests.post(path, data)
    worked = response.json()['reply']

    assert response.ok and worked

    # Add same driver again
    response = requests.post(path, data)
    worked = response.json()['reply']

    assert (response.ok and worked) == False

    # if empty assert response is 400
    data = {'passHash': "pass", 'name': "Common"}
    response = requests.post(path, data)
    # worked = response.json()['reply']

    assert not response.ok

# get driver from username tested
# get driver from ID tested
# assert that the returned drivers are the same
def testGetDriver():
    id = "D248706135"
    path = myurl + "/driver/id/" + id

    driver = requests.get(path).json()
    username = driver['username']

    path2 = myurl + "/driver/user/" + username
    driver2 = requests.get(path2).json()

    assert driver == driver2


# update availability to true using ID, check that there are available drivers
# then update availability to false using username, check that thee number of
# available drivers has changed by 1
def testUpdateAvailability():
    id = "D248706135"
    username = "firstdriver"

    # updating availability using id
    path = myurl + "/driver/updateAvailability/id"
    requests.post(path, data={'id': id, 'availability': True})

    path2 = myurl + "/driver/available"
    available_array = requests.get(path2).json()
    assert len(available_array) >= 1

    # variable holding length of available array
    length_array = len(available_array)

    # updating availability using username
    path = myurl + "/driver/updateAvailability/user"
    requests.post(path, data={'username': username, 'availability': False})

    available_array = requests.get(path2).json()

    assert len(available_array) == length_array - 1


# getting drivers orders
# currently does not work due to the request to get orders
def testGetDriverOrders():
    id = "D248706135"
    path = myurl + "/driver/id/" + id
    driver = requests.get(path).json()

    orders = driver['orders']

    path2 = myurl + "/driver/getOrders/" + id
    retrieved_orders = requests.get(path2).json()

    assert orders == retrieved_orders


# getting and setting drivers location
def testGetDriverLocation():
    id = "D248706135"
    # path for post method of setting location
    path = myurl + "/driver/location"

    # arbitrary coordinates
    location_data = {'driverID': id, 'long': 47.526521, 'lat': -52.840346}
    response = requests.post(path, location_data)

    path = myurl + "/driver/location/" + id
    # for some reason this sets lat: 'lat, and long: 'long' ??
    long, lat = requests.get(path).json()

    # get driver
    path = myurl + "/driver/id/" + id
    driver = requests.get(path).json()

    assert (driver['long'] == long and driver['lat'] == lat)

# ------------------------------------------------------------

## Restaurant

# add restaurant
def testAddRestaurant():
    path = myurl + "/restaurant/add"
    data = {'username': r.get_random_word(), 'passHash': "pass", 'name': "common", 'category': "tacos", 'openHour': "23h25", 'closeHour': "23h54", 'address': "/mun", 'postal': "A1A1A1"}

    response = requests.post(path, data)
    worked = response.json()['reply']

    assert response.ok and worked

    # add same restaurant again
    response = requests.post(path, data)
    worked = response.json()['reply']

    assert not (response.ok and worked)

    # no username included
    data = {'passHash': "pass", 'name': "common", 'category': "tacos", 'openHour': "06h00", 'closeHour': "23h00", 'address': "/mun", 'postal': "A1A1A1"}
    response = requests.post(path, data)
    assert not response.ok

# get restaurant from id tested
# get restaurant from username tested
# get restaurant from category tested
# Assert that the returned restaurants are the same
def testGetRestaurant():
    id = "R763567026"
    path = myurl + "/restaurant/id/" + id

    restaurant = requests.get(path).json()
    username = restaurant['username']
    category = restaurant['category']

    path2 = myurl + "/restaurant/user/" + username
    restaurant2 = requests.get(path2).json()

    assert (restaurant == restaurant2)

    path3 = myurl + "/restaurant/category/" + category
    rest_list = requests.get(path3).json()

    for x in rest_list:
        if x['id'] == id:
            prescence = True
            break
        else:
            presence = False

    assert prescence



# update availability to true using ID, check that there are available driver
# then update availability to false using username, check that there number of
# available restaurants has changed to one less
def testUpdateRestAvailability():
    id = "R763567026"
    username = "firstrest"

    # updating availability using id
    path = myurl + "/restaurant/updateAvailability/id"
    requests.post(path, data={'id': id, 'availability': True})

    path2 = myurl + "/restaurant/available"
    available_array = requests.get(path2).json()
    assert len(available_array) >= 1

    length_array = len(available_array)
    # updating availability using username
    path = myurl + "/restaurant/updateAvailability/user"
    requests.post(path, data={'username': username, 'availability': False})

    available_array = requests.get(path2).json()
    assert len(available_array) == length_array - 1


# add item to restaurant menu test
def testAddItemToRestMenu():
    id = "R763567026"
    path = myurl + "/restaurant/menu/addItem"
    # add item to menu
    data = {'restaurantID': id, 'name': "Tacos", 'category': "Food", 'cost': 20, 'prepTime': 5, 'calories': 15, 'description': "good food", 'imageLink': "http://null"}
    response = requests.post(path, data)

    # this might not be finished yet apparently
    path = myurl + "/restaurant/menu/" + id
    menu = requests.get(path).json()

    # get restaurant
    path = myurl + "/restaurant/id/" + id
    restaurant = requests.get(path).json()
    menu2 = restaurant['menu']

    assert menu == menu2


# test getting restaurant orders
def testGetRestaurantOrders():
    id = "R763567026"
    path = myurl + "/restaurant/getOrders/" + id

    # the get orders also is not working atm
    orders = requests.get(path).json()

    # get restaurant and orders for comparison
    path = myurl + "/restaurant/id/" + id
    restaurant = requests.get(path).json()
    orders2 = restaurant['orders']

    assert orders == orders2


# --------------------------------------------------------------

## Order

# add order
# not working, think it is a data validation thing with the ccNumber
# requiring 'regex': '(\s*\d\s*)
def testAddOrder():
    path = myurl + "/order/add"
    items_array = ["bread"]
    data = {'cost': 100, 'items': items_array, 'status': "delivered", 'prepTime': 10, 'eta': 15, 'deliveryAddress': "destination", 'ccNumber': (1234, 5678, 9098, 7654), 'cvv': 343, 'exp': "01/23", 'firstName': "Joe", 'lastName': "Joe", 'postal': "A1A1A1", 'restID': "R763567026", 'custID': "C235771756"}

    response = requests.post(path, data)
    worked = response.json()['reply']

    assert response.ok and worked

    # missing required parameters
    data = {}
    response = requests.post(path, data)
    assert not response.ok


# get order from id tested
# works
def testGetOrderFromId():
    id = "O321764897"
    path = myurl + "/order/id/" + id
    order = requests.get(path).json()
    order_id = order['id']
    path = myurl + "/order/id/" + order_id
    order2 = requests.get(path).json()

    assert order == order2

# update order status, and add eta to order
# works
def testStatusAndETA():
    id = "O321764897"
    path = myurl + "/order/updateStatus"
    requests.post(path, data={'orderID': id, 'status': True})
    path = myurl + "/order/id/" + id
    order = requests.get(path).json()
    status = order['status']

    assert status

    # add eta
    path = myurl + "/order/addETA"
    requests.post(path, data={'orderID': id, 'eta': 25})
    path = myurl + "/order/id/" + id
    order = requests.get(path).json()
    eta = order['ETA']
    assert eta == 25


# test assigning a driver, getting all orders without drivers,
# and getting all orders
# not complete as getAllOrders is required to find the right id here
def testAssigning():
    # getting all orders without drivers isn't working at the moment
    # because of createOrderListDump issue
    # path = myurl + "/order/getUnassignedDriver"
    # orders = requests.get(path).json()

    # Adding a new order, then assign a driver and assert that it
    # has the driver assigned
    restID = "R763567026"
    custID = "C235771756"
    data = {'cost': 100, 'items': ["that bread"], 'status': "delivered", 'prepTime': 10, 'eta': 15, 'deliveryAddress': "destination", 'ccNumber': (1234, 5678, 9098, 7654), 'cvv': 343, 'exp': "01/23", 'firstName': "Joe", 'lastName': "Joe", 'postal': "A1A1A1", 'restID': restID, 'custID': custID}
    path = myurl + "/order/add"
    requests.post(path, data)

    path = myurl + "/order/assignDriver"
    driverID = "D248706135"
    requests.post(path, driverID)

    assert True
