from GetPayInfoFromGUI import importfromjsonstring
import datetime


###This is a temporary class for the MVP of the project, to replace Stripe until it can be implemented.
# mimics the info that is sent to stripe, and what stripe does.

# looks like a payment, in reality this mimics whatever object stripe creates to handle payments. (this is why our
# code turns the object into a json and immediately turns it back, cause a json file is sent to stripe which it does
# stuff with
class StripeCharge:
    def __init__(self, m, s, r, c, e, v, p, t):
        self.payment_money = m
        self.sender_id = s
        self.recipient_id = r
        self.card_number = c
        self.card_expiry = e
        self.card_verify = v
        self.postal_code = p
        self.token = t

# for now, just check and see against our imaginary credit card valid numbers. For MVP, only one valid input number.
def validccnum(ccnum):
    if (ccnum == 4242424242424242):
        return True
    else:
        return False

#Checks if security code is valid. For mvp, only one security code.
def cvccheck(cvc):
    if (cvc == 111):
        return True
    else:
        return False

# Does nothing for now, mimics sending cash from sender account to recipient account.
# Payment only manages the transaction, theoretically up to a bank/cc company/etc. to provide account balance.
# Since we do not have actual account balances to take from, for MVP we assume that the accounts have 1000000 dollars.
# subtract money from sender acct, add to recipient acct
def sendMoney(recipient_id, sender_id, payment_money):
    senderbal = 1000000
    receiverbal = 1000000
    #abstracted check for fraudulent accounts
    fraud = False
    if (senderbal < payment_money):
        return False
    if(fraud == True):
        return False

    senderbal = senderbal - payment_money
    receiverbal = receiverbal + payment_money

    #For MVP, assume that payments always suceed, no internet outages/other errors.
    payment_succeeded = True
    return payment_succeeded


# Mimics what Stripe does
def sendTransaction(jsonstring):
    stringdata = importfromjsonstring(jsonstring)
    transinfo = StripeCharge(stringdata["payment_money"], stringdata["sender_id"], stringdata["recipient_id"],
                             stringdata["card_number"], stringdata["card_expiry"], stringdata["card_verify"],
                             stringdata["postal_code"], stringdata["token"])

    # check if cc is expired
    format = "%Y-%m-%d"
    strtodate = datetime.datetime.strptime(transinfo.card_expiry, format)
    # x = datetime.datetime()
    if (strtodate < datetime.datetime.now()):
        return False
    # bad code here
    if (validccnum(transinfo.card_number) == False):
        return False
    # also bad code here
    if (cvccheck(transinfo.card_verify) == False):
        return False

    if (transinfo.postal_code != 'null' and transinfo.token != 'null'):
        return sendMoney(transinfo.recipient_id, transinfo.sender_id, transinfo.payment_money)

    else:
        return False
