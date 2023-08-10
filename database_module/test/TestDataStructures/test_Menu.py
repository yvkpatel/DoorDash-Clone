# test_Menu.py

from random_word import RandomWords
from database_module.src.DataStructures.Menu import Menu

r = RandomWords()


def test_get_id():
    id = r.get_random_word()
    rest_id = r.get_random_word()
    item_list = r.get_random_word()
    menu = Menu(id, rest_id, item_list)
    assert id == menu.getId()


def test_get_restaurant_id():
    id = r.get_random_word()
    rest_id = r.get_random_word()
    item_list = r.get_random_word()
    menu = Menu(id, rest_id, item_list)
    assert rest_id == menu.getRestaurantId()


def test_get_item_list():
    id = r.get_random_word()
    rest_id = r.get_random_word()
    item_list = r.get_random_word()
    menu = Menu(id, rest_id, item_list)
    assert item_list == menu.getItemList()
