# test_RestaurantsGateway.py

from database_module.src.Gateways.RestaurantsGateway import RestaurantGateway
from database_module.src.DataStructures.Restaurant import Restaurant
from database_module.src.Utils.MainConnection import *
from random_word import RandomWords

r = RandomWords()


def test_insert_restaurant():
    restaurant = Restaurant(r.get_random_word(), r.get_random_word(), r.get_random_word(), r.get_random_word(), r.get_random_word(), r.get_random_word(), r.get_random_word(), r.get_random_word(), r.get_random_word(), r.get_random_word(), r.get_random_word())

    db_test = createDatabaseConn('TestDB')
    restaurant_gateway = RestaurantGateway(db_test)

    assert restaurant_gateway.insertRestaurant(restaurant)


# just checks that a list is returned at the moment
def test_get_restaurants_by_category():
    restaurant = Restaurant(r.get_random_word(), r.get_random_word(), r.get_random_word(), r.get_random_word(), r.get_random_word(), r.get_random_word(), r.get_random_word(), r.get_random_word(), r.get_random_word(), r.get_random_word(), r.get_random_word())

    db_test = createDatabaseConn('TestDB')
    restaurant_gateway = RestaurantGateway(db_test)
    restaurant_gateway.insertRestaurant(restaurant)

    assert restaurant_gateway.getRestaurantsByCategory() is list


def test_get_restaurant_from_id():
    restaurant = Restaurant(r.get_random_word(), r.get_random_word(), r.get_random_word(), r.get_random_word(), r.get_random_word(), r.get_random_word(), r.get_random_word(), r.get_random_word(), r.get_random_word(), r.get_random_word(), r.get_random_word())
    id = restaurant.getId()

    db_test = createDatabaseConn('TestDB')
    restaurant_gateway = RestaurantGateway(db_test)
    restaurant_gateway.insertRestaurant(restaurant)

    assert restaurant == restaurant_gateway.getRestaurantFromID(id)


def test_get_restaurant_from_username():
    restaurant = Restaurant(r.get_random_word(), r.get_random_word(), r.get_random_word(), r.get_random_word(), r.get_random_word(), r.get_random_word(), r.get_random_word(), r.get_random_word(), r.get_random_word(), r.get_random_word(), r.get_random_word())
    username = restaurant.getUsername()

    db_test = createDatabaseConn('TestDB')
    restaurant_gateway = RestaurantGateway(db_test)
    restaurant_gateway.insertRestaurant(restaurant)

    assert restaurant == restaurant_gateway.getRestaurantFromID(username)


# just checks that a list is returned at the moment
def test_get_available_restaurants():
    restaurant = Restaurant(r.get_random_word(), r.get_random_word(), r.get_random_word(), r.get_random_word(), r.get_random_word(), r.get_random_word(), r.get_random_word(), r.get_random_word(), r.get_random_word(), r.get_random_word(), r.get_random_word())

    db_test = createDatabaseConn('TestDB')
    restaurant_gateway = RestaurantGateway(db_test)
    restaurant_gateway.insertRestaurant(restaurant)

    assert restaurant_gateway.getAvailableRestaurants() is list


def test_update_restaurant_availability_from_id():
    restaurant = Restaurant(r.get_random_word(), r.get_random_word(), r.get_random_word(), r.get_random_word(),r.get_random_word(), r.get_random_word(), r.get_random_word(), r.get_random_word(),r.get_random_word(), r.get_random_word(), r.get_random_word())

    db_test = createDatabaseConn('TestDB')
    restaurant_gateway = RestaurantGateway(db_test)
    restaurant_gateway.insertRestaurant(restaurant)

    assert restaurant_gateway.updateRestaurantAvailabilityFromID(restaurant.getId(), True)


def test_update_restaurant_availability_from_username():
    restaurant = Restaurant(r.get_random_word(), r.get_random_word(), r.get_random_word(), r.get_random_word(),r.get_random_word(), r.get_random_word(), r.get_random_word(), r.get_random_word(),r.get_random_word(), r.get_random_word(), r.get_random_word())

    db_test = createDatabaseConn('TestDB')
    restaurant_gateway = RestaurantGateway(db_test)
    restaurant_gateway.insertRestaurant(restaurant)

    assert restaurant_gateway.updateRestaurantAvailabilityFromUsername(restaurant.getUsername(), True)


def test_add_order():
    restaurant = Restaurant(r.get_random_word(), r.get_random_word(), r.get_random_word(), r.get_random_word(),r.get_random_word(), r.get_random_word(), r.get_random_word(), r.get_random_word(),r.get_random_word(), r.get_random_word(), r.get_random_word())

    db_test = createDatabaseConn('TestDB')
    restaurant_gateway = RestaurantGateway(db_test)
    restaurant_gateway.insertRestaurant(restaurant)

    assert restaurant_gateway.addOrder(restaurant.getId(), restaurant.getOrders())
