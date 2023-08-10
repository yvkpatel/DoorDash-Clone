from Payment import Payment
from GetPayInfoFromGUI import importfromjsonstring
from Transfer import doAll
from PaymentProcess import sendTransaction
from Receipt import *

# Interface Function to be called when Payment is initiated
# Returns a boolean (true/false) if payment goes through.
def beginTransaction(jsoninput):
    # Takes in the Json String input from GUI
    stringdata = importfromjsonstring(jsoninput)
    # Create a payment object with the info provided
    inter_Payment = Payment(stringdata["customerName"], stringdata["ccNumber"], stringdata["CCS"],
                            stringdata["ccExpiry"], stringdata["PostalCode"], stringdata["checkoutTotal"])

    # Create two transactions from the payment object, one from user to us and one from us to restaurant.
    inter_json_string = doAll(inter_Payment)

    # for testing
    # print(sendTransaction(inter_json_string[0]))
    # Mimics sending the transaction to Stripe.
    # TODO: For future mvp, also perform second transaction. (for mvp, just make sure one is done)
    # TODO: For final product, replace this with Stripe.
    return (sendTransaction(inter_json_string[0]))

#creates a receipt with information from database.
#TODO: for mvp this is a simple text file, for future versions integrate with GUI.
def createReceipt(payment):
    #For future implementation beyond MVP, receipt will take info from DataTest.py
    #For now, it just uses dummy values.
    Receipt.create_receipt(payment)




