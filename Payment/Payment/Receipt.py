from Payment import Payment  # placeholder value for Payment class

# This class is designed to take core information from a passed in payment object, and create a
# .txt file containing this information for use by the GUI module.
class Receipt:
    # Inputs: Receipt self, Payment payment
    # Outputs: None
    # Expected: Set variables paymentID and totalCost to the userID and the amount the user is paying
    #           respectively.
    def __init__(self, payment):
        self.this_payment = payment
        self.paymentID = self.this_payment.get_user()
        self.totalCost = self.this_payment.get_amt_user_paid()

    # Inputs: Receipt self
    # Outputs: float totalCost
    # Expected: Returns the totalCost of the payment if initialized, otherwise returns 0.00.
    def get_total_cost(self):
        return self.totalCost

    # Inputs: Receipt self
    # Outputs: A .txt file in the same directory as the .py file.
    # Expected: A .txt file named after the UserID of the payment should be created in the same directory
    #           as the Receipt.py file, with core information such as the paymentID and the totalCost populated.
    def create_receipt(self):
        f = open(str(self.paymentID) + ".txt", "w+")
        f.write("ID " + str(self.paymentID) + "\n")
        f.write("Cost " + str(self.totalCost) + "\n")

    # Variables of the Receipt Class:
    # Payment this_payment
    # string paymentID
    # float totalCost
    this_payment = Payment("John Smith1 Visa", 4242424242424242, 111, "12/12/2222", "A1A1A1", 10.00)
    paymentID = ""
    totalCost = 0.00
