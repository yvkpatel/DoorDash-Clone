
def getAvailableDrivers():
    from algorithms_module.src.DriverSelector import Driver
    drivers = []
    for i in range(100, 200):
        for j in range(100, 200):
            drivers.append(Driver(i, j))

    return drivers

def assignDriverToOrder(order_id, driver):
    print(f"Algorithms Mock Assign Driver Called")
    print(f"    Driver assigned for {order_id}")
    print(f"    Driver: ({driver.getLat()}, {driver.getLong()})")

def getRestaurantFromId(order_id):
    from algorithms_module.src.DriverSelector import Restaurant
    return Restaurant(201, 201)

def generateAlert(order_id):
    print("Algorithms Mock Generate Alert - ALERT GENERATED")

