# test_CustomerGateway.py

import pytest
from database_module.src.Gateways.CustomersGateway import CustomerGateway
from database_module.src.DataStructures.Customer import Customer
from database_module.src.Utils.MainConnection import *
from random_word import RandomWords


r = RandomWords()


def test_insert_customer():
    # create customer
    customer = Customer(r.get_random_word(), r.get_random_word(), r.get_random_word(), r.get_random_word(), r.get_random_word(), r.get_random_word())

    # Test database access
    db_test = createDatabaseConn('TestDB')
    customer_gateway = CustomerGateway(db_test)

    # insertCustomer returns True for valid assertion
    assert customer_gateway.insertCustomer(customer)


def test_get_customer_profile_from_id():
    # create customer
    customer = Customer(r.get_random_word(), r.get_random_word(), r.get_random_word(), r.get_random_word(), r.get_random_word(), r.get_random_word())
    # local id variable
    id = customer.getId()

    # Test database access
    db_test = createDatabaseConn('TestDB')
    customer_gateway = CustomerGateway(db_test)
    # add customer to database
    customer_gateway.insertCustomer(customer)

    # assert that the customer equals the return
    assert customer == customer_gateway.getCustomerProfileFromID(id)


def test_get_customer_profile_from_username(customer_username):
    customer = Customer(r.get_random_word(), r.get_random_word(), r.get_random_word(), r.get_random_word(), r.get_random_word(), r.get_random_word())

    username = customer.getUsername()

    db_test = createDatabaseConn('TestDB')
    customer_gateway = CustomerGateway(db_test)

    customer_gateway.insertCustomer(customer)

    assert customer == customer_gateway.getCustomerProfileFromUsername(username)


def test_add_order():
    customer = Customer(r.get_random_word(), r.get_random_word(), r.get_random_word(), r.get_random_word(), r.get_random_word(), r.get_random_word())

    # create test database and customerGateway
    db_test = createDatabaseConn('TestDB')
    customer_gateway = CustomerGateway(db_test)

    customer_gateway.insertCustomer(customer)

    assert customer_gateway.addOrder(customer.getId(), customer.getOrders())
