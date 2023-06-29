
#  testing main.py using pytest

import pytest
import time
from parkinglot import ParkingLot
from vehicle import Vehicle


#pytest fixture, function that can used to manage apps states & dependencies
@pytest.fixture
def create_vehicle():
    # to get current time
    current_time = time.time()
    # initialize vehicle as car with plate of ABC123 with a current time
    return Vehicle(1, "ABC123", entry_time=current_time)


@pytest.fixture
def parking_lot():
    # capacity of 10 parkinglot
    return ParkingLot(10)


def test_vehicle_creation(create_vehicle):
    vehicle = create_vehicle
    # assertion to verify attributes matches expected values.
    assert vehicle.type == 1
    assert vehicle.plate == "ABC123"

# check if entry_time is either None or valid time value
def test_entry_time(create_vehicle):
    # create_vehicle obtain 'Vehicle' object name 'vehicle'
    vehicle = create_vehicle
    # time.time() is to get current time and store in it.
    current_time = time.time() 
    assert vehicle.entry_time is None or vehicle.entry_time <= current_time

# check if entry_time can be set to specific value and retains the value correctly.
def test_set_entry_time(create_vehicle):
    vehicle = create_vehicle
    current_time = time.time()
    # # to represent a time that is an hours earlier than current time
    vehicle.entry_time = current_time - 3600
    assert vehicle.entry_time == current_time - 3600

    
def test_calculate_fee():
    # parking capacity of 10
    parking_lot = ParkingLot(10)
    # representing time vehicle entered the parkinglot
    entry_time = time.time() - 7200  # Two hours ago
    exit_time = time.time()  # Current time
    # vehicle parked 2 hours
    vehicle = Vehicle(1, "ABC123", entry_time=entry_time, exit_time=exit_time) 
    parking_lot.spaces[0] = vehicle
    # to calc parking fee based on duration of vehicle parking
    fee = parking_lot.calculate_fee(vehicle)
    assert fee == 10  # Assuming $4 per hour, the fee for 2 hours should be $8

def test_park_vehicle(create_vehicle, parking_lot):
    vehicle = create_vehicle
    # Park the vehicle
    result = parking_lot.park_vehicle(vehicle.type, vehicle.plate)
    # Verify that the vehicle is parked successfully
    assert result is not None
    # is not None indicate vehicle parked successfully
    assert result.plate == vehicle.plate
    # to make sure the correct vehicle is parked

    # indicate 1 parking space is now occupied
    assert parking_lot.occupied_spaces == 1








    