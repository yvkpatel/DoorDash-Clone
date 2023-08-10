import requests
import flask
from PollDatabase import poll_database
from DataTest import updatePaymentFlag, getOrderFromID
from PaymentInterface import beginTransaction
from StripeServer import createCharge

#Script to be run to print test outputs to show functionality. Must be connected to database and have flask installed to function.

#sets payment flag in database to false. Both of these are done as at moment of submission there is a bug in the database
#that takes all boolean inputs as strings, so "False" could be read as True since it is a string that contains something.
updatePaymentFlag('O724516036', False)
updatePaymentFlag('O724516036','')
#fetch unpaid orders from database
orders = getOrderFromID()
#pay unpaid orders. For this assignment submission, print statements are uncommented to show intermediate outputs.
for order in orders:
    beginTransaction(order)
