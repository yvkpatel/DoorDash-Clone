# test_Driver.py

import pytest
from random_word import RandomWords
from random import randint
from database_module.src.DataStructures.Driver import Driver

r = RandomWords()
name_data = r.get_random_words()
id_data = r.get_random_words()
availability_data = r.get_random_words()
username_data = r.get_random_words()
orders_data = r.get_random_words()


# test the assigned id data
@pytest.mark.parametrize("id", id_data)
def test_get_id(id):
    driver = Driver(id_data[randint(0, 49)], r.get_random_word, r.get_random_word, r.get_random_word, r.get_random_word)
    assert driver.getId() == id


# test the assigned username data
@pytest.mark.parametrize("username", username_data)
def test_get_username(username):
    driver = Driver(r.get_random_word, username_data[randint(0, 49)], r.get_random_word, r.get_random_word, r.get_random_word)
    assert driver.getUsername() == username


# test the assigned name data
@pytest.mark.parametrize("name", name_data)
def test_get_name(name):
    driver = Driver(r.get_random_word, r.get_random_word, name_data[randint(0, 49)], r.get_random_word, r.get_random_word)
    assert driver.getName() == name


# test the assigned availability data
@pytest.mark.parametrize("availability", availability_data)
def test_get_availability(availability):
    driver = Driver(r.get_random_word, r.get_random_word, r.get_random_word, availability_data[randint(0, 49)], r.get_random_word)
    assert driver.getAvailability() == availability


# test the assigned orders data
@pytest.mark.parametrize("orders", orders_data)
def test_get_orders(orders):
    driver = Driver(r.get_random_word, r.get_random_word, r.get_random_word, r.get_random_word, orders_data[randint(0, 49)])
    assert driver.getOrders() == orders


# test the set availability functionality
def test_set_availability():
    driver = Driver(r.get_random_word, r.get_random_word, r.get_random_word, r.get_random_word, r.get_random_word)
    driver.setAvailability("9-5")
    assert driver.getAvailability() == "9-5"

