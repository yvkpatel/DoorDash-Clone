//jshint esversion:6
const Customers = require('./networking-module/customers')
const Users = require('./networking-module/users');

// These are external packages / modules needed to run the project. 

const express = require('express');
const bodyParser = require('body-parser');
const _ = require('lodash');
const getLocation = require('./networking-module/users');
const app  = express();
const server = require('http').createServer(app);
const io = require('socket.io')(server, {
    cors: {
        origin: "*",
    }
});

const users = new Users();
const customers = new Customers();

app.use(express.static('test-frontend'));

app.get('/', (req, res) => {
    res.sendFile(`${__dirname}/test-frontend/index.html`);
});

// This will send back the customerID for future usage
app.get('/customer/:customerID', (req, res) => {
    const customerID = req.params.customerID;

    customers.getCustomerById(function(result) {
        res.json(result);
    }, customerID);

});

// This will send a location back to the Algorithms team as requested
app.get('/:userString/location/', (req, res) => {
    const userString = req.params.userString;

    users.getLocation(function(result) {
        res.json(result)
    }, userString)
});



io.on('connection', (socket) => {
    // Will emit a message to all user in the terminal
    socket.emit('message', 'Please be respectful to all parties involved.');

    socket.broadcast.emit('message', 'A user on chat');

    socket.on('disconnect', () => {
        io.emit('message', 'A user has left chat');
    });

    socket.on('chat', (text) => {
        io.emit('message', text);
    });
});

//This will work for the sockets 
server.listen(3000, () => {
    console.log('Server that allows for Sockets now listening on PORT 3000...');
});
