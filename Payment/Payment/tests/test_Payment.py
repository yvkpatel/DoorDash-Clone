from Payment.Payment import Payment

myPayment = Payment("John Smith1 Visa", 4242424242424242, 111, "12/12/2222", "A1A1A1", 10.00)

# for this test case, I need to know what we'd expect from this function so I can define variables that
# aren't strictly defined by the constructor, namely "test_time", "test_our_cut", "test_restaurant", etc.


def test_get_user():
    user = myPayment.get_user()
    assert user == "John Smith1 Visa"


def test_get_restaurant():
    restaurant = myPayment.get_restaurant()
    assert restaurant == "test_restaurant"  # placeholder until I know the test_restaurant data type


def test_get_amt_user_paid():
    amount = myPayment.get_amt_user_paid()
    assert amount == 10.00


def test_get_date_time_of_order():
    time = myPayment.get_date_time_of_order()
    assert time == "test_time"  # placeholder until I know the test_time data type/expected from function


def test_take_our_cut():
    our_cut = myPayment.take_our_cut()
    manual_computation = myPayment.amtuserpaid * 1.20
    assert our_cut == manual_computation  # placeholder until I know the test_our_cut data type/expected from function
