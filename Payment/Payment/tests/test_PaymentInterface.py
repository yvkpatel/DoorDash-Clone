from Payment.PaymentInterface import beginTransaction


def test_begin_transaction():
    # assumes that all values passed in are valid
    correctJson = {"customerName": "John Smith1 Visa", "ccNumber": 4242424242424242, "CCS": 111,
                   "ccExpiry": "12/12/2222", "PostalCode": "A1A1A1", "checkoutTotal": 10.00}
    success = beginTransaction(correctJson)
    assert success is True


def missing_name():
    # assumes that the customer did not input a name into the field
    missingName = {"customerName": "", "ccNumber": 4242424242424242, "CCS": 111, "ccExpiry": "12/12/2222",
                   "PostalCode": "A1A1A1", "checkoutTotal": 10.00}
    success = beginTransaction(missingName)
    assert success is False


def expired_card():
    # assumes that the credit card is expired
    invalidCard = {"customerName": "John Smith1 Visa", "ccNumber": 4242424242424242, "CCS": 111,
                   "ccExpiry": "12/12/1999", "PostalCode": "A1A1A1", "checkoutTotal": 10.00}
    success = beginTransaction(invalidCard)
    assert success is False


def invalid_card():
    # assumes that the credit card is invalid
    invalidCard = {"customerName": "John Smith1 Visa", "ccNumber": 1111111111111111, "CCS": 111,
                   "ccExpiry": "12/12/2222", "PostalCode": "A1A1A1", "checkoutTotal": 10.00}
    success = beginTransaction(invalidCard)
    assert success is False
