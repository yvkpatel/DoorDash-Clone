# test_Restaurant.py

from random_word import RandomWords
from database_module.src.DataStructures.Restaurant import Restaurant

r = RandomWords()


def test_get_id():
    id = r.get_random_word()
    username = r.get_random_word()
    name = r.get_random_word()
    orders = r.get_random_word()
    menu_id = r.get_random_word()
    category = r.get_random_word()
    availability = r.get_random_word()
    open_hour = r.get_random_word()
    close_hour = r.get_random_word()
    address = r.get_random_word()
    postal = r.get_random_word()

    restaurant = Restaurant(id, username, name, orders, menu_id, category, availability, open_hour, close_hour, address, postal)

    assert id == restaurant.getId()


def test_get_username():
    id = r.get_random_word()
    username = r.get_random_word()
    name = r.get_random_word()
    orders = r.get_random_word()
    menu_id = r.get_random_word()
    category = r.get_random_word()
    availability = r.get_random_word()
    open_hour = r.get_random_word()
    close_hour = r.get_random_word()
    address = r.get_random_word()
    postal = r.get_random_word()

    restaurant = Restaurant(id, username, name, orders, menu_id, category, availability, open_hour, close_hour, address, postal)

    assert username == restaurant.getUsername()


def test_get_name():
    id = r.get_random_word()
    username = r.get_random_word()
    name = r.get_random_word()
    orders = r.get_random_word()
    menu_id = r.get_random_word()
    category = r.get_random_word()
    availability = r.get_random_word()
    open_hour = r.get_random_word()
    close_hour = r.get_random_word()
    address = r.get_random_word()
    postal = r.get_random_word()

    restaurant = Restaurant(id, username, name, orders, menu_id, category, availability, open_hour, close_hour, address, postal)

    assert name == restaurant.getName()


def test_get_category():
    id = r.get_random_word()
    username = r.get_random_word()
    name = r.get_random_word()
    orders = r.get_random_word()
    menu_id = r.get_random_word()
    category = r.get_random_word()
    availability = r.get_random_word()
    open_hour = r.get_random_word()
    close_hour = r.get_random_word()
    address = r.get_random_word()
    postal = r.get_random_word()

    restaurant = Restaurant(id, username, name, orders, menu_id, category, availability, open_hour, close_hour, address, postal)

    assert category == restaurant.getCategory()


def test_get_availability():
    id = r.get_random_word()
    username = r.get_random_word()
    name = r.get_random_word()
    orders = r.get_random_word()
    menu_id = r.get_random_word()
    category = r.get_random_word()
    availability = r.get_random_word()
    open_hour = r.get_random_word()
    close_hour = r.get_random_word()
    address = r.get_random_word()
    postal = r.get_random_word()

    restaurant = Restaurant(id, username, name, orders, menu_id, category, availability, open_hour, close_hour, address, postal)

    assert availability == restaurant.getAvailability()


def test_get_open_hour():
    id = r.get_random_word()
    username = r.get_random_word()
    name = r.get_random_word()
    orders = r.get_random_word()
    menu_id = r.get_random_word()
    category = r.get_random_word()
    availability = r.get_random_word()
    open_hour = r.get_random_word()
    close_hour = r.get_random_word()
    address = r.get_random_word()
    postal = r.get_random_word()

    restaurant = Restaurant(id, username, name, orders, menu_id, category, availability, open_hour, close_hour, address, postal)

    assert open_hour == restaurant.getOpenHour()


def test_get_close_hour():
    id = r.get_random_word()
    username = r.get_random_word()
    name = r.get_random_word()
    orders = r.get_random_word()
    menu_id = r.get_random_word()
    category = r.get_random_word()
    availability = r.get_random_word()
    open_hour = r.get_random_word()
    close_hour = r.get_random_word()
    address = r.get_random_word()
    postal = r.get_random_word()

    restaurant = Restaurant(id, username, name, orders, menu_id, category, availability, open_hour, close_hour, address, postal)

    assert close_hour == restaurant.getCloseHour()


def test_get_address():
    id = r.get_random_word()
    username = r.get_random_word()
    name = r.get_random_word()
    orders = r.get_random_word()
    menu_id = r.get_random_word()
    category = r.get_random_word()
    availability = r.get_random_word()
    open_hour = r.get_random_word()
    close_hour = r.get_random_word()
    address = r.get_random_word()
    postal = r.get_random_word()

    restaurant = Restaurant(id, username, name, orders, menu_id, category, availability, open_hour, close_hour, address, postal)

    assert address == restaurant.getAddress()


def test_get_postal():
    id = r.get_random_word()
    username = r.get_random_word()
    name = r.get_random_word()
    orders = r.get_random_word()
    menu_id = r.get_random_word()
    category = r.get_random_word()
    availability = r.get_random_word()
    open_hour = r.get_random_word()
    close_hour = r.get_random_word()
    address = r.get_random_word()
    postal = r.get_random_word()

    restaurant = Restaurant(id, username, name, orders, menu_id, category, availability, open_hour, close_hour, address, postal)

    assert postal == restaurant.getPostal()


def test_get_orders():
    id = r.get_random_word()
    username = r.get_random_word()
    name = r.get_random_word()
    orders = r.get_random_word()
    menu_id = r.get_random_word()
    category = r.get_random_word()
    availability = r.get_random_word()
    open_hour = r.get_random_word()
    close_hour = r.get_random_word()
    address = r.get_random_word()
    postal = r.get_random_word()

    restaurant = Restaurant(id, username, name, orders, menu_id, category, availability, open_hour, close_hour, address, postal)

    assert orders == restaurant.getOrders()


def test_get_menu_id():
    id = r.get_random_word()
    username = r.get_random_word()
    name = r.get_random_word()
    orders = r.get_random_word()
    menu_id = r.get_random_word()
    category = r.get_random_word()
    availability = r.get_random_word()
    open_hour = r.get_random_word()
    close_hour = r.get_random_word()
    address = r.get_random_word()
    postal = r.get_random_word()

    restaurant = Restaurant(id, username, name, orders, menu_id, category, availability, open_hour, close_hour, address, postal)

    assert menu_id == restaurant.getMenuID()
