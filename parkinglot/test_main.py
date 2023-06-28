
#  testing main.py using pytest

import pytest
import time
from parkinglot import ParkingLot
from vehicle import Vehicle

@pytest.fixture
def create_vehicle():
    current_time = time.time()
    return Vehicle(1, "ABC123", entry_time=current_time)

@pytest.fixture
def parking_lot():
    return ParkingLot(10)

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
    entry_time = time.time() - 7200  # Two hours ago
    exit_time = time.time()  # Current time
    vehicle = Vehicle(1, "ABC123", entry_time=entry_time, exit_time=exit_time)  # Vehicle parked for 2 hours
    parking_lot.spaces[0] = vehicle
    fee = parking_lot.calculate_fee(vehicle)
    assert fee == 10  # Assuming $5 per hour, the fee for 2 hours should be $10

def test_park_vehicle(create_vehicle, parking_lot):
    vehicle = create_vehicle

    # Park the vehicle
    result = parking_lot.park_vehicle(vehicle.type, vehicle.plate)

    # Verify that the vehicle is parked successfully
    assert result is not None
    assert result.plate == vehicle.plate

    # Verify that the parking lot occupancy is updated
    assert parking_lot.occupied_spaces == 1











    # new code to test

# import pytest
# import time
# from parkinglot import ParkingLot
# from vehicle import Vehicle

# @pytest.fixture
# def create_vehicle():
#     current_time = time.time()
#     return Vehicle(1, "ABC123", entry_time=current_time)

# def test_vehicle_creation(create_vehicle):
#     vehicle = create_vehicle()
#     assert vehicle.type == 1
#     assert vehicle.plate == "ABC123"

# def test_entry_time(create_vehicle):
#     vehicle = create_vehicle()
#     current_time = time.time() 
#     assert vehicle.entry_time is None or vehicle.entry_time <= current_time

# def test_set_entry_time(create_vehicle):
#     vehicle = create_vehicle()
#     current_time = time.time()
#     vehicle.entry_time = current_time - 3600
#     assert vehicle.entry_time == current_time - 3600

# def test_calculate_fee():
#     parking_lot = ParkingLot(10)
#     vehicle = Vehicle(1, "ABC123", entry_time=time.time() - 7200)  # Vehicle parked for 2 hours
#     parking_lot.spaces[0] = vehicle
#     fee = parking_lot.calculate_fee(vehicle)
#     assert fee == 10.0  # Assuming $5 per hour, the fee for 2 hours should be $10

# def test_main_functionality(capfd):
#     parking_lot = ParkingLot(10)
#     input_values = ["1", "1", "ABC123", "4"]
#     def mock_input(prompt):
#         return input_values.pop(0)

#     def mock_time():
#         return 1624550000.0  # Mock the current time to a specific value

#     time.time = mock_time
#     builtins.input = mock_input
#     main()

#     captured = capfd.readouterr()
#     assert "Report generated and saved as parking_report_" in captured.out
#     # Add more assertions to check the program's behavior based on the specific input values.



    