

import pytest
import time
from simplified2 import Vehicle, ParkingLot

@pytest.fixture
def create_vehicle():
    current_time = time.time()
    return Vehicle(1, "ABC123", entry_time=current_time)

def test_vehicle_creation(create_vehicle):
    vehicle = create_vehicle
    assert vehicle.type == 1
    assert vehicle.plate == "ABC123"

def test_entry_time(create_vehicle):
    vehicle = create_vehicle
    current_time = time.time() 
    assert vehicle.entry_time is None or vehicle.entry_time <= current_time

def test_set_entry_time(create_vehicle):
    vehicle = create_vehicle
    current_time = time.time()
    vehicle.entry_time = current_time - 3600
    assert vehicle.entry_time == current_time - 3600

    

def test_calculate_fee():
    parking_lot = ParkingLot(10)
    vehicle = Vehicle(1, "ABC123", entry_time=time.time() - 7200)  # Vehicle parked for 2 hours
    parking_lot.spaces[0] = vehicle
    fee = parking_lot.calculate_fee(vehicle)
    assert fee == 10.0  # Assuming $5 per hour, the fee for 2 hours should be $10