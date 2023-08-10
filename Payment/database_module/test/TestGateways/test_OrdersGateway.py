# test_OrdersGateway.py

from database_module.src.Gateways.OrdersGateway import OrderGateway
from database_module.src.DataStructures.Order import Order
from database_module.src.Utils.MainConnection import *
from random_word import RandomWords

r = RandomWords()


def test_insert_order():
    # create order
    order = Order(r.get_random_word(), r.get_random_word(), r.get_random_word(), r.get_random_word(), r.get_random_word(), r.get_random_word(), r.get_random_word(), r.get_random_word(), r.get_random_word(), r.get_random_word())

    # Test database access
    db_test = createDatabaseConn('TestDB')
    order_gateway = OrderGateway(db_test)

    assert order_gateway.insertOrder(order)


def test_get_order():
    order = Order(r.get_random_word(), r.get_random_word(), r.get_random_word(), r.get_random_word(), r.get_random_word(), r.get_random_word(), r.get_random_word(), r.get_random_word(), r.get_random_word(), r.get_random_word())
    id = order.getId()

    db_test = createDatabaseConn('TestDB')
    order_gateway = OrderGateway(db_test)
    order_gateway.insertOrder(order)

    assert order == order_gateway.getOrder(id)


def test_update_order_status():
    order = Order(r.get_random_word(), r.get_random_word(), r.get_random_word(), r.get_random_word(), r.get_random_word(), r.get_random_word(), r.get_random_word(), r.get_random_word(), r.get_random_word(), r.get_random_word())

    db_test = createDatabaseConn('TestDB')
    order_gateway = OrderGateway(db_test)
    order_gateway.insertOrder(order)

    # create new status and update status
    new_status = r.get_random_word()
    order_gateway.updateOrderStatus(order.getId(), new_status)

    assert new_status == order.getStatus()
