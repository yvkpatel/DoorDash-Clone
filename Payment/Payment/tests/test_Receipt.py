import os.path

from Payment.Receipt import Receipt
from Payment.Payment import Payment

def test_get_total_cost():
    myPayment = Payment("John Smith1 Visa", 4242424242424242, 111, "12/12/2222", "A1A1A1", 20.00)

    # test Receipt class initialized with myPayment
    myReceipt = Receipt(myPayment)
    assert myReceipt.totalCost == 20.00
    assert myReceipt.paymentID == "John Smith1 Visa"


def test_create_receipt():
    myPayment = Payment("John Smith1 Visa", 4242424242424242, 111, "12/12/2222", "A1A1A1", 20.00)
    myReceipt = Receipt(myPayment)

    myReceipt.create_receipt()
    assert os.path.isfile(myReceipt.paymentID) is True
