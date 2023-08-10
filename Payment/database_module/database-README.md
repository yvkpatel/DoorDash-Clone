# NoTimeToFry Database

### Notes
>Welcome to the data team's module.\
Please see all callable endpoints at the end of this document.\
To make a connection to our module please follow the steps below:

### FOR ALL DEVS:
>[1] Install pip3
>> On Ubuntu: sudo apt-get -y install python3-pip \
 On Mac: sudo easy_install pip3 \
 On Windows: Google it
 
>[2] Install pymongo
>> $ pip3 install "pymongo[srv]" \
 if necessary run using sudo 

>[3] Install dnspython
>> $ pip3 install dnspython \
 if necessary run using sudo 

>[4] Install Flask
>> $ pip3 install Flask \
 if necessary run using sudo 

>[5] Run Flask Application Local
>> $ cd (repo)/NTTF/database_module/src\
$ export FLASK_APP=FlaskAPI\
$ export FLASK_ENV=development\
$ flask run

>[6] Done!
> Now the Flask application is running locally and any calls made to it will return JSON object.

### Endpoints
##### LANDING API
> Route: / \
Request: POST\
@POST Data \
           "username"\
           "passHash"\
@returns  \
           Type: boolean \
           Description: authenticate user
           
##### CUSTOMER APIs
> Route: /customer/id/\<id\> \
Request: GET\
@params \
           \<id\>\
@returns  \
           Type: Customer (see data structure)   \
           Description: customer object that was requested
            
> Route: /customer/user/\<user\> \
Request: GET\
@params \
           \<username\>\
@returns  \
           Type: Customer (see data structure)   \
           Description: customer object that was requested

> Route: /customer/add \
Request: POST\
@POST Data \
           "username"\
           "passHash"\
           "name"\
           "address"\
           "postal"\
@returns  \
           Type: boolean \
           Description: if customer was added
 
##### DRIVER APIS
> Route: /driver/id/\<id\> \
Request: GET\
@params \
           \<id\>\
@returns  \
           Type: Driver (see data structure)   \
           Description: driver object that was requested
            
> Route: /driver/user/\<user\> \
Request: GET\
@params \
           \<username\>\
@returns  \
           Type: Driver (see data structure)   \
           Description: driver object that was requested
 
> Route: /driver/available \
Request: GET\
@returns  \
           Type: Driver Array (see data structure)   \
           Description: drivers that are currently active

> Route: /driver/add \
Request: POST\
@POST Data \
           "username"\
           "passHash"\
           "name"\
@returns  \
           Type: boolean \
           Description: if driver was added
 
> Route: /driver/updateAvailability/id \
Request: POST\
@POST Data \
           "id"\
           "availability"\
@returns  \
           Type: boolean \
           Description: if driver availability was updated
 
> Route: /driver/updateAvailability/user \
Request: POST\
@POST Data \
           "username"\
           "availability"\
@returns  \
           Type: boolean \
           Description: if driver availability was updated
 
 ##### RESTAURANT APIs
> Route: /restaurant/add \
Request: POST\
@POST Data \
           "username"\
           "passHash"\
           "name"\
           "category"\
           "openHour"\
           "closeHour"\
           "address"\
           "postal"\
@returns  \
           Type: boolean \
           Description: if restaurant was added
 
> Route: /restaurant/id/\<id\> \
Request: GET\
@params \
           \<id\>\
@returns  \
           Type: Restaurant (see data structure)   \
           Description: restaurant object that was requested
            
> Route: /restaurant/user/\<user\> \
Request: GET\
@params \
           \<username\>\
@returns  \
           Type: Restaurant (see data structure)   \
           Description: restaurant object that was requested
 
> Route: /restaurant/category/\<category\> \
Request: GET\
@params \
           \<category\>\
@returns  \
           Type: Restaurant Array (see data structure)   \
           Description: restaurants that belong to a category
           
> Route: /restaurant/available \
Request: GET\
@returns  \
           Type: Restaurant Array (see data structure)   \
           Description: restaurant that are currently active

> Route: /restaurant/updateAvailability/id \
Request: POST\
@POST Data \
           "id"\
           "availability"\
@returns  \
           Type: boolean \
           Description: if restaurant availability was updated
 
> Route: /restaurant/updateAvailability/user \
Request: POST\
@POST Data \
           "username"\
           "availability"\
@returns  \
           Type: boolean \
           Description: if restaurant availability was updated
 
> Route: /restaurant/menu/addItem \
Request: POST\
@POST Data \
           "restaurantID"\
           "name"\
           "category"\
           "cost"\
           "prepTime"\
           "calories"\
@returns  \
           Type: boolean \
           Description: if item was added

 ##### ORDER APIs
> Route: /order/add \
Request: POST\
@POST Data \
           "cost"\
           "items"\
           "status"\
           "prepTime"\
           "eta"\
           "deliveryAddress"\
           "restID"\
           "custID"\
@returns  \
           Type: String \
           Description: order id
 
> Route: /order/assignDriver \
Request: POST\
@POST Data \
           "orderID"\
           "driverID"\
@returns  \
           Type: boolean \
           Description: if driver was assigned

> Route: /order/id/\<id\> \
Request: GET\
@params \
           \<id\>\
@returns  \
           Type: Order (see data structure)   \
           Description: order object that was requested
 
 
