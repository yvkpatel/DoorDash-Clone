
from PaymentInterface import beginTransaction
from Payment import Payment
from PaymentInterface import createReceipt

# test input for project:
x = beginTransaction(
    '{"customerName": "John Smith1 Visa","ccNumber": 4242424242424242,"CCS": 111,"ccExpiry": "2222-12-12","PostalCode": "A1A1A1","checkoutTotal": 10.00}')

print(x)
if(x == True):
    print("Transaction Completed!")
if(x == False):
    print("Transaction Failed :(")

#Commented out as current implementation creates a text file, and you might not want that for grading
payment = Payment("bob",424242424242,111,"2022-02-02","A0E2M0",17)
#createReceipt(payment)