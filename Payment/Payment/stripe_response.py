
# the "charge" parameter is a charge created by stripe.
# If the charge was successfully created, return true. Else, return false.
def stripe_response(charge):
    if charge is True:
        return True
    else:
        return False
