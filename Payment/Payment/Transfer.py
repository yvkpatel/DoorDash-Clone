import json

#class containing all the information required to make a transaction in Stripe
#contains the total amount being paid, sender and recipient, as well as the sender's card information
class transfer:
           
    #initializes all the values when given
    #parameters:
    #m - money - float or int
    #s - sender - string
    #r - recipient - string
    #c - card number - int
    #e - expiry date - string
    #v - verification (CCV/CSV) - int
    #p - postal code - string
    #t = token - string
    def __init__(self, m, s, r, c, e, v, p, t):
        self.payment_money = m
        self.sender_id = s
        self.recipient_id = r 
        self.card_number = c
        self.card_expiry = e
        self.card_verify = v
        self.postal_code = p
        self.token = t
    
    #print function which displays all the info about the transfer, mostly used in testing/debugging
    def print(self):
       print("Transfer Information")
       print(self.payment_money)
       print(self.sender_id)
       print(self.recipient_id) 
       print(self.card_number)
       print(self.card_expiry)
       print(self.card_verify)
       print(self.postal_code)
       print(self.token)
       print()


	###########################################################################
	#end of transfer
	###########################################################################

#class that will be responsible for making the two tranfers to send to Stripe
#transfer maker is a class that takes in information from Payment and turn them into 2 tranfers
#one transfer is from the customer to NTTF, and one transfer from NTTF to the restaurant
class transfer_maker:


    #constructor that takes all the values from the Payment and puts them into the transfer_maker class
    def __init__(self, Payment):

        #TODO make this work for total user paid
        #multiplies the total money by 100 to get the cost in cents
        #multiples money user paid by 1.2 to add our cut to the total charge
        self.total_money = Payment.amtuserpaid*120
        self.customer = Payment.user
        #TODO make this take an actual restaurant
        self.restaurant = "test_restaurant"
        self.card_num = Payment.ccnum
        self.expire = Payment.ccexpiry
        self.verify = Payment.cvc
        self.postal  = Payment.postalcode
        #TODO make sure this is right
        self.token = "tok_visa_debit"
        
        
        
    #this function creates the two transfers 
    #One between the customer and NTTF, one between NTTF and the restaurant
    def make_transfers(self):
        #creating transfer from customer to NTTF
        pay1 = int(self.total_money)
        self.transfer1 = transfer(pay1, self.customer, "NTTF", self.card_num, self.expire, self.verify, self.postal, self.token)
        #creates transfer from NTTF to restaurant
        pay2 = self.total_money *5/6
        self.transfer2 = transfer(pay2, "NTTF", self.restaurant, 5555555555554444, "12/12/2222", 333, "A1A1A1", "tok_mastercard")
        
        
#function that takes an input Payment and moves the information into seperate transactions, or transfers which are converted into json strings         
def doAll(Payment):
    #initialize the tranfer maker
    tm = transfer_maker(Payment)
    #create two transfers
    tm.make_transfers()
    #convert each transfer into a json
    json1 = json.dumps(tm.transfer1.__dict__)
    json2 = json.dumps(tm.transfer2.__dict__)
    #store both json into an array and return
    array = [json1, json2]
    return array	
    

