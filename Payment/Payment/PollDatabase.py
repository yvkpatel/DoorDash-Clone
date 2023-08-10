from PaymentInterface import beginTransaction
from DataTest import getOrderFromID
import time

#Main loop for Payment Module (Continuously running)
def poll_database():
    while True:
        orders = getOrderFromID()
        if orders:
            for order in orders:
                beginTransaction(order)
        else:
            print("All orders Paid!")
            time.sleep(30)

poll_database()
