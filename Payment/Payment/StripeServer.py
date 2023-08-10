# make sure to pip3 install stripe first!

from flask import Flask, render_template, jsonify, request
import requests
import json
import stripe

stripe.api_key = "sk_test_51Jm5EMCEjyrCg9BgdTmAowLjRMlFF6L7aXxELkP6eZJHDoUHIcvSEQqpJR6FOTSluNVTvZ0vpvvULxQ8x2AOJMic00Yxz26t46"

#Creates a charge object, sending the payment to Stripe to be processed.
def createCharge(dict):
    if(dict['ccnum']):
        a = stripe.Charge.create(
        amount= int(dict['money']),
        currency='cad',
        source='tok_visa',
        description='orderid',
        metadata = {'application' : 'NTTF',
                    'country' : 'Canada',
                    'city' : 'St.Johns',
                    'postal_code': dict['postcode'],
                    'name': dict['firstname']+dict['lastname'],
                    'exp_month': dict['exp'][0:1],
                    'exp_year': dict['exp'][2:5],
                    }
    )
    print("Stripe Receipt: ",a)
    return a
    #for testing


