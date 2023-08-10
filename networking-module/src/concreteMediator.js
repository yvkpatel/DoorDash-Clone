const Drivers = require('./drivers');
const Customers = require('./customers');
const Restaurants = require('./restaurants');


class ConcreteMediator {
    constructor() {
        controller = new Controller();
    }

    drivers = new Drivers();
    restaurants = new Restaurants();
    customers = new Customers();

    chatHandler = () => {}    
    notificationHandler = () => {}
    orderHandler = () => {}
    assignDriver = () => {}
}

module.exports = ConcreteMediator;