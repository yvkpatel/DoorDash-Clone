from distutils import util
from cerberus import Validator

class DataValidator:
    def __init__(self):
        self.v = Validator()
    def validateData(self, endpoint, params):
        schema = {}
        if endpoint == '/':
            authenticateUserParams = {'username': params.values.get('username'),
                                      'passHash': params.values.get('passHash')}
            schema = {'username': {'type': 'string', 'empty': False},
                      'passHash':{'type': 'string', 'empty': False}}
            self.v.validate(authenticateUserParams, schema)
            return None

        elif endpoint == '/customer/add':
            addCustomerParams = {'username': params.values.get('username'),
                                 'passHash': params.values.get('passHash'),
                                 'name': params.values.get('name'),
                                 'address': params.values.get('address'),
                                 'postal': params.values.get('postal')}
            schema = {'username': {'type': 'string', 'empty': False},
                      'passHash':{'type': 'string', 'empty': False},
                      'name': {'type': 'string', 'empty': False},
                      'address': {'type': 'string', 'empty': False},
                      'postal': {'type': 'string', 'empty': False}}
            self.v.validate(addCustomerParams, schema)
            return self.v.errors

        elif endpoint == '/driver/add':
            addDriverParams = {'username': params.values.get('username'),
                               'passHash': params.values.get('passHash'),
                               'name': params.values.get('name')}
            schema = {'username': {'type': 'string', 'empty': False},
                      'passHash': {'type': 'string', 'empty': False},
                      'name': {'type': 'string', 'empty': False}}
            self.v.validate(addDriverParams, schema)
            return self.v.errors

        elif endpoint == '/driver/updateAvailability/id':
            updateDriverAvailabilityFromIDParams = {'id': params.values.get('id'),
                                                    'availability': bool(util.strtobool(params.values.get('availability')))}
            schema = {'id': {'type': 'string', 'contains': 'D'},
                      'availability': {'type': 'boolean'}}
            self.v.validate(updateDriverAvailabilityFromIDParams, schema)
            return self.v.errors

        elif endpoint == '/driver/location':
            setDriverLocationParams = {'driverID': params.values.get('driverID'),
                                       'long': params.values.get('long', type=float),
                                       'lat': params.values.get('lat', type=float)}
            schema = {'driverID': {'type': 'string', 'contains': 'D'},
                      'long': {'type': 'float', 'empty': False},
                      'lat': {'type': 'float', 'empty': False}}
            self.v.validate(setDriverLocationParams, schema)
            return self.v.errors
        
        elif endpoint == '/driver/updateAvailability/user':
            updateDriverAvailabilityFromUsernameParams = {'username': params.values.get('username'),
                                                          'availability': bool(util.strtobool(params.values.get('availability')))}
            schema = {'username': {'type': 'string', 'empty': False},
                      'availability': {'type': 'boolean'}}
            self.v.validate(updateDriverAvailabilityFromUsernameParams, schema)
            return self.v.errors

        elif endpoint == '/restaurant/add':
            addRestaurantParams = {'username': params.values.get('username'),
                                   'passHash': params.values.get('passHash'),
                                   'name': params.values.get('name'),
                                   'openHour': params.values.get('openHour'),
                                   'closeHour': params.values.get('closeHour'),
                                   'address': params.values.get('address'),
                                   'postal': params.values.get('postal')}
            schema = {'username': {'type': 'string', 'empty': False},
                      'passHash': {'type': 'string', 'empty': False},
                      'name': {'type': 'string', 'empty': False},
                      'openHour': {'type': 'string', 'regex': '^[0-23]{2}h[0-59]{2}'},
                      'closeHour': {'type': 'string', 'regex': '^[0-23]{2}h[0-59]{2}'},
                      'address': {'type': 'string', 'empty': False},
                      'postal': {'type':'string', 'empty': False}}
            self.v.validate(addRestaurantParams, schema)
            return self.v.errors

        elif endpoint == '/restaurant/updateAvailability/id':
            updateRestaurantAvailabilityFromIDParams = {'id': params.values.get('id'),
                                                        'availability': bool(util.strtobool(params.values.get('availability')))}
            schema = {'id': {'type': 'string', 'contains': 'R'},
                      'availability': {'type': 'boolean'}}
            self.v.validate(updateRestaurantAvailabilityFromIDParams, schema)
            return self.v.errors

        elif endpoint == '/restaurant/updateAvailability/user':
            updateRestaurantAvailabilityFromUsernameParams = {'username': params.values.get('username'),
                                                              'availability': bool(util.strtobool(params.values.get('availability')))}
            schema = {'username': {'type': 'string', 'empty': False},
                      'availability':{'type': 'boolean'}}
            self.v.validate(updateRestaurantAvailabilityFromUsernameParams, schema)
            return self.v.errors
        
        elif endpoint == '/restaurant/menu/addItem':
            addItemToRestaurantParams = {'restaurantID': params.values.get('restaurantID'),
                                         'name': params.values.get('name'),
                                         'category': params.values.get('category'),
                                         'cost': params.values.get('cost', type=float),
                                         'prepTime': params.values.get('prepTime'),
                                         'calories': params.values.get('calories', type=int),
                                         'description': params.values.get('description'),
                                         'imageLink': params.values.get('imageLink')}
            schema = {'restaurantID': {'type': 'string', 'contains': 'R'},
                      'name': {'type': 'string', 'empty': False},
                      'category':{'type': 'string', 'empty': False},
                      'cost':{'type': 'float'},
                      'prepTime': {'type': 'string', 'empty': False},
                      'calories':{'type': 'integer'},
                      'description': {'type': 'string', 'empty': False},
                      'imageLink': {'type': 'string', 'empty': False}}
            self.v.validate(addItemToRestaurantParams, schema)
            return self.v.errors
        
        elif endpoint == '/order/add':
            addOrderParams = {'cost': params.values.get('cost', type=float),
                              'items': params.values.get('items', type=list),
                              'status': params.values.get('status'),
                              'prepTime': params.values.get('prepTime', type=int),
                              'eta': params.values.get('eta', type=int),
                              'deliveryAddress': params.values.get('deliveryAddress'),
                              'ccNumber': params.values.get('ccNumber', type=int),
                              'cvv': params.values.get('cvv', type=int),
                              'exp': params.values.get('exp'),
                              'firstName': params.values.get('firstName'),
                              'lastName': params.values.get('lastName'),
                              'postal': params.values.get('postal'),
                              'restID': params.values.get('restID'),
                              'custID': params.values.get('custID')}
            schema = {'cost': {'type': 'float'},
                      'items': {'type': 'list'},
                      'status': {'type': 'string', 'empty': False},
                      'prepTime': {'type': 'integer'},
                      'eta': {'type': 'integer'},
                      'deliveryAddress': {'type': 'string', 'empty': False},
                      'ccNumber': {'type': 'integer', 'regex': '(\s*\d\s*){16}'},
                      'cvv': {'type': 'integer', 'regex': '^[0-9]{3,4}$'},
                      'exp': {'type': 'string', 'empty': False},
                      'firstName': {'type': 'string', 'empty': False},
                      'lastName': {'type': 'string', 'empty': False},
                      'postal': {'type': 'string', 'empty': False},
                      'restID': {'type': 'string', 'contains': 'R'},
                      'custID': {'type': 'string', 'contains': 'C'}}
            self.v.validate(addOrderParams, schema)
            return self.v.errors

        elif endpoint == '/order/assignDriver':
            assignDriverParams = {'orderID': params.values.get('orderID'),
                                  'driverID': params.values.get('driverID')}
            schema = {'orderID': {'type': 'string', 'contains': 'O'},
                      'driverID':{'type': 'string', 'contains': 'D'}}
            self.v.validate(assignDriverParams, schema)
            return self.v.errors
        
        elif endpoint == '/order/updateStatus':
            updateOrderStatusParams = {'orderID': params.values.get('orderID'),
                                       'status': params.values.get('status')}
            schema = {'orderID': {'type': 'string', 'contains': 'O'},
                      'status': {'type': 'string', 'empty': False}}
            self.v.validate(updateOrderStatusParams, schema)
            return self.v.errors
        
        elif endpoint == '/order/addETA':
            addETAtoOrderParams = {'orderID': params.values.get('orderID'),
                                   'eta': params.values.get('eta', type=int)}
            schema = {'orderID': {'type': 'string', 'contains': 'O'},
                      'eta': {'type': 'integer'}}
            self.v.validate(addETAtoOrderParams, schema)
            return self.v.errors
        
        elif endpoint == 'order/payment/update':
            updatePaymentFlagParams = {'orderID': params.values.get('orderID'),
                                       'paid': bool(util.strtobool(params.values.get('paid')))}
            schema = {'orderID': {'type': 'string', 'contains': 'O'},
                      'paid': {'type': 'boolean'}}
            self.v.validate(updatePaymentFlagParams, schema)
            return self.v.errors

        elif endpoint == '/order/push/notification':
            pushNotificationParams = {'orderID': params.values.get('orderID'),
                                      'notification': params.values.get('notification')}
            schema = {'orderID': {'type': 'string', 'contains': 'O'},
                      'notification': {'type': 'string'}}
            self.v.validate(pushNotificationParams, schema)
            return self.v.errors
        elif endpoint == '/order/push/chat':
            pushChatParams = {'reply': params.values.get('reply'),
                              'orderID': params.values.get('orderID'),
                              'receiver': params.values.get('receiver'),
                              'datetime': params.values.get('datetime'),
                              'message': params.values.get('message')}
            schema = {'reply': {'type': 'string'},
                      'orderID': {'type': 'string', 'contains': 'O'},
                      'receiver': {'type': 'string', 'empty': False},
                      'datetime': {'type': 'string', 'empty': False},
                      'message': {'type': 'string', 'empty': False}}
            self.v.validate(pushChatParams, schema)
            return self.v.errors
        
        
