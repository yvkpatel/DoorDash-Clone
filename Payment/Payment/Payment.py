
#Payment object is created after we are passed info from function call and the string is decoded.
class Payment:

    def __init__(self, user, ccnum, cvc, ccexpiry, postalcode, amtuserpaid):
        self.ccnum = ccnum
        self.user = user
        self.cvc = cvc
        self.ccexpiry = ccexpiry
        self.postalcode = postalcode
        self.amtuserpaid = amtuserpaid

    #Some empty methods, to be implemented if we need to in the future.
    def get_user(self):
        return self.user

    def get_restaurant(self):
        pass

    def get_amt_user_paid(self):
        return self.amtuserpaid

    def get_date_time_of_order(self):
        pass

    def take_our_cut(self):
        #current cut is 20% of order price. TODO: For not MVP, make sure this is done in Algo and is displayed to user beforehand as part of cost.
        self.totalordercost = self.amtuserpaid * 1.2


