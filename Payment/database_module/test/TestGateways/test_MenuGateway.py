# test_MenuGateway.py

from database_module.src.Gateways.MenuGateway import MenuGateway
from database_module.src.DataStructures.Menu import Menu
from database_module.src.Utils.MainConnection import *
from random_word import RandomWords

r = RandomWords()


def test_insert_menu():
    # create menu
    menu = Menu(r.get_random_word, r.get_random_word(), r.get_random_word())

    # create test database and gateway
    db_test = createDatabaseConn('TestDB')
    menu_gateway = MenuGateway(db_test)

    assert menu_gateway.insertMenu(menu)


def test_get_menu():
    # create menu
    menu = Menu(r.get_random_word, r.get_random_word(), r.get_random_word())
    # local id
    id = menu.getId()

    # create test database and gateway
    db_test = createDatabaseConn('TestDB')
    menu_gateway = MenuGateway(db_test)
    menu_gateway.insertMenu(menu)

    assert menu == menu_gateway.getMenu(id)
