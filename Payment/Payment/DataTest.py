#Requests relies on having database files downloaded and a connection to database on the local machine
#Therefore this file will not run without an active connection to the database on the local machine it is being run on,
#and as such cannot be tested for MVP
# If you want to run this code for evaluation, the database module is required.


from flask import Flask, request
import requests
import json

def getCustomerFromID(customerID):
    mainURL = "http://localhost:5000/customer/id/"

    r = requests.get(url=(mainURL + str(customerID)))
    cust = r.json()
    return cust



def getRestaurantFromID(restaurantID):
    mainURL1 = "http://localhost:5000/restaurant/id/"

    r1 = requests.get(url=(mainURL1 + str(restaurantID)))
    restaurant= r1.json()
    return restaurant




def getDriverFromID(driverID):
    mainURL2 = "http://localhost:5000/driver/id/"

    r2 = requests.get(url=(mainURL2 + str(driverID)))
    driver = r2.json()
    return driver




#Fetches all unpaid orders from the database
def getOrderFromID():
    mainURL3 = "http://localhost:5000/order/payment/getOrdersUnpaid"

    r3 = requests.get(url=(mainURL3)) # + str(orderID)))
    print(r3)
    if r3.ok:
        return r3.json()
    else:
        return None

#Updates the payment flag within the database to either true or false
def updatePaymentFlag(orderID,isPaid: bool):
    url = "http://localhost:5000/order/payment/update"
    data = {'orderID': orderID, 'paid': isPaid}
    r = requests.post(url, data)
    print(r.json()['reply'])
    return r.json()['reply']




#For testing, fetches all orders from database.
def getAll():
    url = "http://localhost:5000/order/all"
    r = requests.get(url)
    return r.json()

#testing
    #print(getAll())
    #O321764897
    #O252073901
    #O724516036
    #updatePaymentFlag('O724516036','')
    #print(getOrderFromID())



