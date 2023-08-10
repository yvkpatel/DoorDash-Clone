"use strict";

const Users = require('./users/');


class Drivers extends Users {
    constructor() {
        super();
    }

    getDriverId = function(callback, driverId) {
  
        http.get(`http://127.0.0.1:5000/driverId/id/${driverId}`, res => {
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

    getDriverUser = function(callback, user) {

        http.get(`http://127.0.0.1:5000/driverId/user/${user}`, res => {
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

module.exports = Drivers;