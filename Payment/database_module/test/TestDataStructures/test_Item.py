# test_Item.py

import pytest
from random_word import RandomWords
from random import randint
from database_module.src.DataStructures.Item import Item

r = RandomWords()


def test_get_id():
    id = r.get_random_word()
    name = r.get_random_word()
    category = r.get_random_word()
    cost = r.get_random_word()
    prep_time = r.get_random_word()
    calories = r.get_random_word()

    item = Item(id, name, category, cost, prep_time, calories)

    assert id == item.getId()


def test_get_name():
    id = r.get_random_word()
    name = r.get_random_word()
    category = r.get_random_word()
    cost = r.get_random_word()
    prep_time = r.get_random_word()
    calories = r.get_random_word()

    item = Item(id, name, category, cost, prep_time, calories)

    assert name == item.getName()


def test_get_category():
    id = r.get_random_word()
    name = r.get_random_word()
    category = r.get_random_word()
    cost = r.get_random_word()
    prep_time = r.get_random_word()
    calories = r.get_random_word()

    item = Item(id, name, category, cost, prep_time, calories)

    assert category == item.getCategory()


def test_get_cost():
    id = r.get_random_word()
    name = r.get_random_word()
    category = r.get_random_word()
    cost = r.get_random_word()
    prep_time = r.get_random_word()
    calories = r.get_random_word()

    item = Item(id, name, category, cost, prep_time, calories)

    assert cost == item.getCost()


def test_get_prep_time():
    id = r.get_random_word()
    name = r.get_random_word()
    category = r.get_random_word()
    cost = r.get_random_word()
    prep_time = r.get_random_word()
    calories = r.get_random_word()

    item = Item(id, name, category, cost, prep_time, calories)

    assert prep_time == item.getPrepTime()


def test_get_calories():
    id = r.get_random_word()
    name = r.get_random_word()
    category = r.get_random_word()
    cost = r.get_random_word()
    prep_time = r.get_random_word()
    calories = r.get_random_word()

    item = Item(id, name, category, cost, prep_time, calories)

    assert calories == item.getCalories()
