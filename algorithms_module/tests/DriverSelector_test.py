from algorithms_module.src.DriverSelector import RadiusDriverSelector, Restaurant
from algorithms_module.src.DriverSelector import Driver
from algorithms_module.src.DriverSelector import DriverSelectorType
from algorithms_module.src.DriverSelector import DriverSelectorBuilder
from algorithms_module.src.DriverSelector import GoogleMapsDriverSelector
from algorithms_module.src.DriverSelector import OpenStreetMapsDriverSelector


##############################
# --- Restaraunt Structure --- 
##############################

def test_restaraunt_set_long():
    """ Test setting the longitude field of the restaraunt structure
    
    @class: Restaraunt
    @method: N/A
    """
    rest = Restaurant(0, 0)
    rest.long = 10
    assert rest.long == 10

def test_restaraunt_get_long():
    """ Test getting the longitude field of the restaraunt structure
    
    @class: Restaraunt
    @method: getLong
    """
    rest = Restaurant(0, 0)
    rest.long = 10
    assert rest.getLong() == 10

def test_restaraunt_set_lat():
    """ Test setting the latitude field of the restaraunt structure
    
    @class: Restaraunt
    @method: N/A
    """
    rest = Restaurant(0, 0)
    rest.lat = 10
    assert rest.lat == 10

def test_restaraunt_get_lat():
    """ Test getting the latitude field of the restaraunt structure
    
    @class: Restaraunt
    @method: getLat
    """
    rest = Restaurant(0, 0)
    rest.lat = 10
    assert rest.getLat() == 10


###########################
# --- Driver Structure  --- 
###########################

def test_driver_set_long():
    """ Test setting the longitude field of the driver structure
    
    @class: Driver
    @method: N/A
    """
    driver = Driver(0, 0)
    driver.long = 10
    assert driver.long == 10

def test_driver_get_long():
    """ Test getting the longitude field of the driver structure
    
    @class: Driver
    @method: getLong
    """
    driver = Driver(0, 0)
    driver.long = 10
    assert driver.getLong() == 10

def test_driver_set_lat():
    """ Test setting the latitude field of the driver structure
    
    @class: Driver
    @method: N/A
    """
    driver = Driver(0, 0)
    driver.lat = 10
    assert driver.lat == 10

def test_driver_get_lat():
    """ Test getting the latitude field of the driver structure
    
    @class: Driver
    @method: getLat
    """
    driver = Restaurant(0, 0)
    driver.lat = 10
    assert driver.getLat() == 10


##################################
# --- Driver Selector Builder  --- 
##################################

def test_driver_builder_set_selector_type():
    """ Test setting the selector type field of the driver selector builder
    
    @class: DriverSelectorBuilder
    @method: setSelectorType
    """
    builder = DriverSelectorBuilder()
    builder.setSelectorType(DriverSelectorType.Radius)
    assert builder.selector_type == DriverSelectorType.Radius

def test_driver_selector_builder_radius():
    """ Test creation of a radius based driver selector using the driver selector 
    builder 
    
    @class: DriverSelectorBuilder
    @method: createDriverSelector
    """
    builder = DriverSelectorBuilder()
    builder.setSelectorType(DriverSelectorType.Radius)
    driver_selector = builder.createDriverSelector()
    assert isinstance(driver_selector, (RadiusDriverSelector))

def test_driver_selector_builder_google_maps():
    """ Test creation of a google maps based driver selector using the driver selector 
    builder 
    
    @class: DriverSelectorBuilder
    @method: createDriverSelector
    """
    builder = DriverSelectorBuilder()
    builder.setSelectorType(DriverSelectorType.GoogleMaps)
    driver_selector = builder.createDriverSelector()
    assert isinstance(driver_selector, (GoogleMapsDriverSelector))

def test_driver_selector_builder_open_street_maps():
    """ Test creation of a open street maps based driver selector using the 
    driver selector builder 

    @class: DriverSelectorBuilder
    @method: createDriverSelector
    """
    builder = DriverSelectorBuilder()
    builder.setSelectorType(DriverSelectorType.OpenStreetMap)
    driver_selector = builder.createDriverSelector()
    assert isinstance(driver_selector, (OpenStreetMapsDriverSelector))


##################################
# --- Radius Driver Selector   --- 
##################################

def test_radius_driver_selector_get_driver_distance():
    """ Test calculation of driver distance based on point-point distance

    @class: RadiusDriverSelector
    @method: getDriverDistance
    """
    driver = Driver(0, 0)
    restaurant = Restaurant(10,0)
    
    builder = DriverSelectorBuilder()
    builder.setSelectorType(DriverSelectorType.Radius)

    driver_selector = builder.createDriverSelector()
    assert driver_selector.getDriverDistance(driver, restaurant) == 10

def test_radius_driver_selector_get_driver_distance_negative_point():
    """ Test calculation of driver distance based on point-point distance

    @class: RadiusDriverSelector
    @method: getDriverDistance
    """
    builder = DriverSelectorBuilder()
    builder.setSelectorType(DriverSelectorType.Radius)
    driver_selector = builder.createDriverSelector()

    driver = Driver(0, 0)
    restaurant = Restaurant(-10,0)

    assert driver_selector.getDriverDistance(driver, restaurant) == 10

def test_radius_driver_selector_get_closest_driver():
    """ Test calculation of the closest driver using p2p distance

    @class: RadiusDriverSelector
    @method: getClosestDriver
    """
    builder = DriverSelectorBuilder()
    builder.setSelectorType(DriverSelectorType.Radius)
    driver_selector = builder.createDriverSelector()
    drivers = []

    # 0-99
    for i in range(100, 200):
        driver = Driver(0, i)
        drivers.append(driver)

    restaurant = Restaurant(0,0)
    closest_driver = driver_selector.getClosestDriver(drivers, restaurant)
    assert (closest_driver.getLat() == 0 and closest_driver.getLong() == 100) 

def test_radius_driver_selector_assign_driver():
    """ Test assigning closest driver (utilises mock methods) 

    @class: RadiusDriverSelector
    @method: assignDriver
    """
    builder = DriverSelectorBuilder()
    builder.setSelectorType(DriverSelectorType.Radius)
    driver_selector = builder.createDriverSelector()
    driver_selector.assignDriver("Doesnt Matter")
    pass

if __name__ == "__main__":
    pass
