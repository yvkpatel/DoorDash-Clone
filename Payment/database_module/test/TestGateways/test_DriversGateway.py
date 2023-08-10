# test_DriversGateway.py

from database_module.src.Gateways.DriversGateway import DriverGateway
from database_module.src.DataStructures.Driver import Driver
from database_module.src.Utils.MainConnection import *
from random_word import RandomWords

r = RandomWords()

def test_insert_driver():
    # create driver
    driver = Driver(r.get_random_word(), r.get_random_word(), r.get_random_word(), r.get_random_word(), r.get_random_word())

    # create test database and driverGateway
    db_test = createDatabaseConn('TestDB')
    driver_gateway = DriverGateway(db_test)

    assert driver_gateway.insertDriver(driver)


def test_get_driver_profile_from_id():
    # create driver
    driver = Driver(r.get_random_word(), r.get_random_word(), r.get_random_word(), r.get_random_word(), r.get_random_word())
    # local id variable
    id = driver.getId()

    # Test database access
    db_test = createDatabaseConn('TestDB')
    driver_gateway = DriverGateway(db_test)
    # add driver to database
    driver_gateway.insertDriver(driver)

    assert driver == driver_gateway.getDriverProfileFromID(id)


def test_get_driver_profile_from_username():
    driver = Driver(r.get_random_word(), r.get_random_word(), r.get_random_word(), r.get_random_word(), r.get_random_word())
    username = driver.getUsername()

    db_test = createDatabaseConn('TestDB')
    driver_gateway = DriverGateway(db_test)

    driver_gateway.insertDriver((driver))

    assert driver == driver_gateway.getDriverProfileFromUsername(username)


def test_update_driver_availability_from_id():
    driver = Driver(r.get_random_word(), r.get_random_word(), r.get_random_word(), r.get_random_word(), r.get_random_word())

    db_test = createDatabaseConn('TestDB')
    driver_gateway = DriverGateway(db_test)
    driver_gateway.insertDriver(driver)

    assert driver_gateway.updateDriverAvailabilityFromID(driver.getId(), True)


def test_update_driver_availability_from_username():
    driver = Driver(r.get_random_word(), r.get_random_word(), r.get_random_word(), r.get_random_word(), r.get_random_word())

    db_test = createDatabaseConn('TestDB')
    driver_gateway = DriverGateway(db_test)
    driver_gateway.insertDriver(driver)

    assert driver_gateway.updateDriverAvailabilityFromUsername(driver.getUsername(), True)


def test_add_order():
    driver = Driver(r.get_random_word(), r.get_random_word(), r.get_random_word(), r.get_random_word(), r.get_random_word())

    db_test = createDatabaseConn('TestDB')
    driver_gateway = DriverGateway(db_test)
    driver_gateway.insertDriver(driver)

    assert driver_gateway.addOrder(driver.getId(), driver.getOrders())


# just checks that a list is returned at the moment
def test_get_available_drivers():
    driver = Driver(r.get_random_word(), r.get_random_word(), r.get_random_word(), r.get_random_word(), r.get_random_word())

    db_test = createDatabaseConn('TestDB')
    driver_gateway = DriverGateway(db_test)
    driver_gateway.insertDriver(driver)

    assert driver_gateway.getAvailableDrivers() is list
