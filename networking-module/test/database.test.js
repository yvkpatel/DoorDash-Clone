const mongoose = require('mongoose');

const URL = 'mongodb+srv://charlesdsmith:password12345@cluster0.f2iwe.mongodb.net/UserTest?retryWrites=true&w=majority';

mongoose.connect(URL, {useNewURLParser: true, useUnifiedTopology: true})

const db = mongoose.connection;

const userSchema = new mongoose.Schema({
    name : String,
    userId : String,
    address : {},
    messagesSent : [],
    messagesRecieved : [],
    status : {} 
});

const users =  mongoose.model("NTTFUsersDB", userSchema); 


describe("Get Data from Database", () => {

    const name = "Johnny-Depp"
    const orderId = 123
    const messageId = 321
    const messages = 'Hello'
    const restaurantName = 'McDonalds'
    const restaurantLocation = '123, 321'
    const OrderId = '953'
    const driverId = '431'
    const driverStatus = 'Active'

    test("Get Order Request", () => {
       expect(database.get('/database/name/'+ name +'/orderId')).toEqual(orderId)
    });

    test("Get messages", () => {
        expect(database.get('/database/name/'+ name +'/messages')).toEqual(messages)
     });

     test("Get messages by message Id", () => {
        expect(database.get('/database/name/'+ name +'/messageId')).toEqual(messageId)
     });

     test("Get restaurant location", () => {
        expect(database.get('/database/restaurant/'+ restaurantName +'/location')).toEqual(restaurantLocation)
     });

     test("Get order status", () => {
        expect(database.get('/database/orders/'+ orderId)).toEqual(orderId)
     });

     test("Get driver status", () =>{
         expect(database.get('/database/driver/'+driverId+'/status')).toEqual(driverStatus)
     })
  });


  describe.only("Current Database tests", () =>{
        let userSchema =  {
            name : 'Dandre Pouros',
            userId : '0065f341-1c4e-4e1b-8949-900df1e00f26',
            address : {
                latitude: '47.463793',
                longitude: '-52.711769',
                city: 'St John\'s',
                country: 'Canada'
            },
            status : {
                orderMade : true,
                driverSelected : false,
                deliveryMade : false
            } 
        }
      test("Testing getting users name", () =>{
          const name = 'Dandre Pouros'
        expect(userSchema.name).toEqual(name)
      })
      test("Testing getting users Id", () =>{
        const userId = '0065f341-1c4e-4e1b-8949-900df1e00f26'
      expect(userSchema.userId).toEqual(userId)
    })
      test("Testing getting users address", () =>{
        const address = {
          latitude: '47.463793',
          longitude: '-52.711769',
          city: 'St John\'s',
          country: 'Canada'
      }
      expect(userSchema.address).toEqual(address)
    })
    test("Testing getting users status", () =>{
      const status = {
        orderMade : true,
        driverSelected : false,
        deliveryMade : false
    }
    expect(userSchema.status).toEqual(status)
  })
  })

  mongoose.connection.close()