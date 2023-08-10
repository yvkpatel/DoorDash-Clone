# test_Order.py

from random_word import RandomWords
from database_module.src.DataStructures.Order import Order

r = RandomWords()


def test_get_id():
    id = r.get_random_word()
    cost = r.get_random_word()
    items = r.get_random_word()
    status = r.get_random_word()
    prep_time = r.get_random_word()
    eta = r.get_random_word()
    delivery_address = r.get_random_word()
    rest_id = r.get_random_word()
    user_id = r.get_random_word()
    driver_id = r.get_random_word()

    order = Order(id, cost, items, status, prep_time, eta, delivery_address, rest_id, user_id, driver_id)

    assert id == order.getId()


def test_get_cost():
    id = r.get_random_word()
    cost = r.get_random_word()
    items = r.get_random_word()
    status = r.get_random_word()
    prep_time = r.get_random_word()
    eta = r.get_random_word()
    delivery_address = r.get_random_word()
    rest_id = r.get_random_word()
    user_id = r.get_random_word()
    driver_id = r.get_random_word()

    order = Order(id, cost, items, status, prep_time, eta, delivery_address, rest_id, user_id, driver_id)

    assert cost == order.getCost()


def test_get_items():
    id = r.get_random_word()
    cost = r.get_random_word()
    items = r.get_random_word()
    status = r.get_random_word()
    prep_time = r.get_random_word()
    eta = r.get_random_word()
    delivery_address = r.get_random_word()
    rest_id = r.get_random_word()
    user_id = r.get_random_word()
    driver_id = r.get_random_word()

    order = Order(id, cost, items, status, prep_time, eta, delivery_address, rest_id, user_id, driver_id)

    assert items == order.getItems()


def test_get_status():
    id = r.get_random_word()
    cost = r.get_random_word()
    items = r.get_random_word()
    status = r.get_random_word()
    prep_time = r.get_random_word()
    eta = r.get_random_word()
    delivery_address = r.get_random_word()
    rest_id = r.get_random_word()
    user_id = r.get_random_word()
    driver_id = r.get_random_word()

    order = Order(id, cost, items, status, prep_time, eta, delivery_address, rest_id, user_id, driver_id)

    assert status == order.getStatus()


def test_get_prep_time():
    id = r.get_random_word()
    cost = r.get_random_word()
    items = r.get_random_word()
    status = r.get_random_word()
    prep_time = r.get_random_word()
    eta = r.get_random_word()
    delivery_address = r.get_random_word()
    rest_id = r.get_random_word()
    user_id = r.get_random_word()
    driver_id = r.get_random_word()

    order = Order(id, cost, items, status, prep_time, eta, delivery_address, rest_id, user_id, driver_id)

    assert prep_time == order.getPrepTime()


def test_get_eta():
    id = r.get_random_word()
    cost = r.get_random_word()
    items = r.get_random_word()
    status = r.get_random_word()
    prep_time = r.get_random_word()
    eta = r.get_random_word()
    delivery_address = r.get_random_word()
    rest_id = r.get_random_word()
    user_id = r.get_random_word()
    driver_id = r.get_random_word()

    order = Order(id, cost, items, status, prep_time, eta, delivery_address, rest_id, user_id, driver_id)

    assert eta == order.getETA()


def test_get_delivery_address():
    id = r.get_random_word()
    cost = r.get_random_word()
    items = r.get_random_word()
    status = r.get_random_word()
    prep_time = r.get_random_word()
    eta = r.get_random_word()
    delivery_address = r.get_random_word()
    rest_id = r.get_random_word()
    user_id = r.get_random_word()
    driver_id = r.get_random_word()

    order = Order(id, cost, items, status, prep_time, eta, delivery_address, rest_id, user_id, driver_id)

    assert delivery_address == order.getDeliveryAddress()


def test_get_restaurant_id():
    id = r.get_random_word()
    cost = r.get_random_word()
    items = r.get_random_word()
    status = r.get_random_word()
    prep_time = r.get_random_word()
    eta = r.get_random_word()
    delivery_address = r.get_random_word()
    rest_id = r.get_random_word()
    user_id = r.get_random_word()
    driver_id = r.get_random_word()

    order = Order(id, cost, items, status, prep_time, eta, delivery_address, rest_id, user_id, driver_id)

    assert rest_id == order.getRestaurantID()


def test_get_user_id():
    id = r.get_random_word()
    cost = r.get_random_word()
    items = r.get_random_word()
    status = r.get_random_word()
    prep_time = r.get_random_word()
    eta = r.get_random_word()
    delivery_address = r.get_random_word()
    rest_id = r.get_random_word()
    user_id = r.get_random_word()
    driver_id = r.get_random_word()

    order = Order(id, cost, items, status, prep_time, eta, delivery_address, rest_id, user_id, driver_id)

    assert user_id == order.getUserID()


def test_get_driver_id():
    id = r.get_random_word()
    cost = r.get_random_word()
    items = r.get_random_word()
    status = r.get_random_word()
    prep_time = r.get_random_word()
    eta = r.get_random_word()
    delivery_address = r.get_random_word()
    rest_id = r.get_random_word()
    user_id = r.get_random_word()
    driver_id = r.get_random_word()

    order = Order(id, cost, items, status, prep_time, eta, delivery_address, rest_id, user_id, driver_id)

    assert driver_id == order.getDriverID()
