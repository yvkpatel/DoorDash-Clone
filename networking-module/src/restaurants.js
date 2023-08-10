"use strict";

const http = require('http');
const Users = require('./users'); 

class Restaurants extends Users {
    constructor() {
        super();
    }  

    getRestaurantId = function(callback, restaurantId) {
        http.get(`http://127.0.0.1:5000/restaurant/id/${restaurantId}`, res => {
            let data = '';
            res.on('data', chunk => {
                data += chunk;
            });
            res.on('end', () => {
                data = JSON.parse(data);
                callback(data)
            })
            }).on('error', err => {
                console.log(err);
        }).end();
    }

    getRestaurantUser = function(callback, user) {
        
        http.get(`http://127.0.0.1:5000/restaurant/user/${user}`, res => {
            let data = '';
            res.on('data', chunk => {
                data += chunk;
            });
            res.on('end', () => {
                data = JSON.parse(data);
                callback(data)
            })
            }).on('error', err => {
                console.log(err);
        }).end();

    }


}


module.exports = Restaurants;