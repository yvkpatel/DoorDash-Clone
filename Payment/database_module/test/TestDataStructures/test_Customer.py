# test_Customer.py

import pytest
from database_module.src.DataStructures.Customer import Customer
id_data = {"unique_id", "wrong_id", "dumb_id", "fake_id"}
username_data = {"joe_username", "ben_username", "bradley_username", "Reza_username"}
name_data = {"joe", "ben", "bradley", "Reza"}
orders_data = [["swag", "swimmer"], ["french", "english"], ["fries", "onions"], ["a", "b"]]
address_data = {"mun", "home", "dusk", "moon"}
postal_data = {"abc123", "123456", "correct", "A1N2F5"}


# test the assigned id data
@pytest.mark.parametrize("id", id_data)
def test_get_id(id):
    customer = Customer("unique_id", "Reza_username", "Reza", ["fries", "onions"], "home", "correct")
    assert customer.getId() == id


# test the assigned username data
@pytest.mark.parametrize("username", username_data)
def test_get_username(username):
    customer = Customer("unique_id", "Reza_username", "Reza", ["fries", "onions"], "home", "correct")
    assert customer.getUsername() == username


# test the assigned name data
@pytest.mark.parametrize("name", orders_data)
def test_get_name(name):
    customer = Customer("unique_id", "Reza_username", "Reza", ["fries", "onions"], "home", "correct")
    assert customer.getName() == name


# test the assigned orders data
@pytest.mark.parametrize("orders", orders_data)
def test_get_orders(orders):
    customer = Customer("unique_id", "Reza_username", "Reza", ["fries", "onions"], "home", "correct")
    assert customer.getOrders() == orders


# test the assigned address data
@pytest.mark.parametrize("address", address_data)
def test_get_address(address):
    customer = Customer("unique_id", "Reza_username", "Reza", ["fries", "onions"], "home", "correct")
    assert customer.getAddress() == address


# test the assigned postal code data
@pytest.mark.parametrize("postal", postal_data)
def test_get_postal(postal):
    customer = Customer("unique_id", "Reza_username", "Reza", ["fries", "onions"], "home", "correct")
    assert customer.getPostal() == postal
