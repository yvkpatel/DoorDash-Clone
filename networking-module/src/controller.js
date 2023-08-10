const Mediator = require('./mediatorInterface');

class Controller {
    constructor() {   
    }
 
    mediator = new Mediator.Mediator();
}


module.exports = {Controller};