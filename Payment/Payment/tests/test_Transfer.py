from Payment.Transfer import transfer, transfer_maker, doAll
from Payment.Payment import Payment

myPayment = Payment("John Smith1 Visa", 4242424242424242, 111, "12/12/2222", "A1A1A1", 10.00)

my_transfer = transfer(10.00, "John Smith1 Visa", "test_restaurant", 4242424242424242,
                       "12/12/2222", 111, "A1A1A1", "tok_visa_debit")


def test_print(): # test that all the values for my_Transfer are populated correctly.
    my_transfer.print()


def test_transfer_maker():
    my_transfer_maker = transfer_maker(myPayment)
    money_to_us = my_transfer_maker.transfer1.payment_money
    manually_computed = 1.20 * myPayment.get_amt_user_paid()
    assert money_to_us == manually_computed  # assert that we're receiving the original payment * 1.20

    money_to_restaurant = my_transfer_maker.transfer2.payment_money
    manually_computed = myPayment.get_amt_user_paid()
    assert money_to_restaurant == manually_computed  # assert that we're sending original payment to restaurant


def test_doAll():
    payment_array = doAll(myPayment)
    assert isinstance(payment_array[0], dict)
    assert isinstance(payment_array[1], dict)
