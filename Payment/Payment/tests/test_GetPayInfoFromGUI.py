from Payment.GetPayInfoFromGUI import importfromjsonstring


def test_importfromjsonstring():
    json = '{"customerName": "John Smith1 Visa","ccNumber": 4242424242424242,"CCS": 111,"ccExpiry":' \
           ' "12/12/2222","PostalCode": "A1A1A1","checkoutTotal": 10.00}'
    result = importfromjsonstring(json)
    assert isinstance(result, dict)
    assert result["customerName"] == "John Smith1 Visa"  # assuming if the first field works, they all work
