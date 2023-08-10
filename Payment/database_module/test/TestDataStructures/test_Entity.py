# test_Entity.py

import pytest
from random_word import RandomWords
from database_module.src.DataStructures.Entity import Entity
from database_module.src.DataStructures.Driver import Driver

r = RandomWords()


def test_get_type():
    driver = Driver(r.get_random_word, r.get_random_word, r.get_random_word, r.get_random_word, r.get_random_word)
    entity = Entity(driver, driver.getId())
    assert isinstance(entity) == Driver


def test_get_id():
    driver = Driver(r.get_random_word, r.get_random_word, r.get_random_word, r.get_random_word, r.get_random_word)
    entity = Entity(driver, driver.getId())
    assert entity.getId() == driver.getId()
