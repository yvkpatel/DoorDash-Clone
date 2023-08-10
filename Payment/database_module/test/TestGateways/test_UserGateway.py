# test_UserGateway.py

from database_module.src.Gateways.UserGateway import UserGateway
from database_module.src.Utils.MainConnection import *
from random_word import RandomWords

r = RandomWords()


def test_add_user():
    # database access
    db_test = createDatabaseConn('TestDB')
    user_gateway = UserGateway(db_test)

    assert user_gateway.addUser(r.get_random_word(), r.get_random_word(), r.get_random_word())


def test_authenticate_user():
    # database access
    db_test = createDatabaseConn('TestDB')
    user_gateway = UserGateway(db_test)

    # attributes of user
    user_id = r.get_random_word()
    username = r.get_random_word()
    pass_hash = r.get_random_word

    # add user
    user_gateway.addUser(user_id, username, pass_hash)

    assert user_gateway.authenticateUser(username, pass_hash)
