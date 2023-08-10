from algorithms_module.src.DeliveryTime import DeliveryTimeEstimatorBuilder
from algorithms_module.src.DeliveryTime import DeliveryTimeEstimatorType
from algorithms_module.src.DeliveryTime import DeliveryTimeEstimator
from algorithms_module.src.DeliveryTime import Point
from algorithms_module.src.DeliveryTime import P2PTimeEstimator
from algorithms_module.src.DeliveryTime import GoogleMapsEstimator

##########################################
# --- Delivery Time Estimator Builder --- 
##########################################

def test_builder_p2p_creation():
    """ Test creation of p2p time estimator using builder
    
    @class: DeliveryTimeEstimatorBuilder
    @method: CreateDeliveryTimeEstimator
    """
    # Create builder
    builder = DeliveryTimeEstimatorBuilder()

    # Set the estimator type
    builder.setEstimatorType(DeliveryTimeEstimatorType.PersonToPerson)

    # Set the average speed
    builder.setAverageSpeed(60)

    # Create a delivery time estimator
    p2p_estimator = builder.CreateDeliveryTimeEstimator()

    assert isinstance(p2p_estimator, (P2PTimeEstimator))

def test_builder_google_maps_creation():
    """ Test creation of a google maps time estimator using builder
    
    @class: DeliveryTimeEstimatorBuilder
    @method: CreateDeliveryTimeEstimator
    """
    # Create builder
    builder = DeliveryTimeEstimatorBuilder()

    # Set the estimator type
    builder.setEstimatorType(DeliveryTimeEstimatorType.GoogleMaps)

    # Create a delivery time estimator
    maps_estimator = builder.CreateDeliveryTimeEstimator()

    assert isinstance(maps_estimator, (GoogleMapsEstimator))

def test_builder_set_average_speed():
    """ Test setting DeliveryTimeEstimator averageSpeed  
    
    @class: DeliveryTimeEstimatorBuilder
    @method: setAverageSpeed
    """
    builder = DeliveryTimeEstimatorBuilder()
    average_speed = 10
    builder.setAverageSpeed(average_speed)
    assert builder.speed == average_speed

def test_builder_set_estimator_type():
    """ Test setting DeliveryTimeEstimator estimator type
    
    @class: DeliveryTimeEstimatorBuilder
    @method: setEstimatorType
    """
    builder = DeliveryTimeEstimatorBuilder()
    estimator_type = DeliveryTimeEstimatorType.PersonToPerson
    builder.setEstimatorType(estimator_type)
    assert builder.type == estimator_type
    

#################################
# --- Delivery Time Estimator --- 
#################################

def test_p2p_time_estimator_base_case():
    """ Test point to point time estimation base case
    @class: DeliveryTimeEstimator::P2PTimeEstimator
    @method: getTimeEstimate
    """
    point_b = Point(0, 0, "START")
    point_a = Point(0, 100, "END")
    
    builder = DeliveryTimeEstimatorBuilder()
    builder.setEstimatorType(DeliveryTimeEstimatorType.PersonToPerson)
    builder.setAverageSpeed(100)

    estimator = builder.CreateDeliveryTimeEstimator()
    time = estimator.getTimeEstimate(point_a, point_b)

    # 100km straight shot at 100 km/hr = 1 hr
    assert time == 1

def test_p2p_time_estimator_negative_point():
    """ Test point to point time estimation for points with negative values
    @class: DeliveryTimeEstimator::P2PTimeEstimator
    @method: getTimeEstimate
    """
    point_b = Point(0, 0, "START")
    point_a = Point(0, -100, "END")
    
    builder = DeliveryTimeEstimatorBuilder()
    builder.setEstimatorType(DeliveryTimeEstimatorType.PersonToPerson)
    builder.setAverageSpeed(100)

    estimator = builder.CreateDeliveryTimeEstimator()
    time = estimator.getTimeEstimate(point_a, point_b)

    # 100km straight shot at 100 km/hr = 1 hr
    assert time == 1

def test_get_delivery_time_estimate_p2p():
    """ Test point-point estimation of delivery time 
    @class: DeliveryTimeEstimator
    @method: GetDeliveryTimeEstimate
    """
    customer_point = Point(0, 0, "Customer")
    restaurant_point = Point(0, 100, "Restaraunt")
    driver_point = Point(0, 200, "Driver")
    
    builder = DeliveryTimeEstimatorBuilder()
    builder.setEstimatorType(DeliveryTimeEstimatorType.PersonToPerson)
    builder.setAverageSpeed(100)

    estimator = builder.CreateDeliveryTimeEstimator()
    time = estimator.getDeliveryTimeEstimate( driver_point, restaurant_point, customer_point)

    # 100km/hr average speed
    # Driver = 100km from diner @ 100 km/hr = 1 hour
    # Diner = 100 km from customer @ 100 km/hr = 1 hour
    # Expected delivery time estimated = 2 hours
    assert time == 2

if __name__ == "__main__":
    pass
