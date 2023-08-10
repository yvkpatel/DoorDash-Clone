"use strict";
const http = require('http');
const Users = require('./users');


class Customers extends Users { 

    constructor() {
        super();
        console.log('Customer subclass instance created.');
    }

    getCustomerId = function(callback, customerId) {
  
        http.get(`http://127.0.0.1:5000/customer/id/${customerId}`, res => {
            let data = '';
            res.on('data', chunk => {
                data += chunk;
            });
            res.on('end', () => {
                data = JSON.parse(data);
                callback(data)
            })
            }).on('error', err => {
            console.error(err);
        }).end();

    }

    getCustomerUser = function(callback, customer) {

        http.get(`http://127.0.0.1:5000/customer/user/${customer}`, res => {
            let data = '';
            res.on('data', chunk => {
                data += chunk;
            });
            res.on('end', () => {
                data = JSON.parse(data);
                callback(data)
            })
            }).on('error', err => {
            console.error(err);
        }).end();

    }



}

module.exports = Customers;