

import pytest
import time
from main import Vehicle, Space

@pytest.fixture
def create_vehicle():
    return Vehicle(1, "ABC123")

@pytest.fixture
def create_space():
    return Space()

def test_vehicle_creation(create_vehicle):
    vehicle = create_vehicle
    assert vehicle.get_type() == 1
    assert vehicle.get_plate() == "ABC123"

def test_space_availability(create_space, create_vehicle):
    space = create_space
    assert not space.is_available()

    vehicle = create_vehicle
    space.add_vehicle(vehicle)
    assert space.is_available()

    removed_vehicle = space.remove_vehicle()
    assert not space.is_available()
    assert removed_vehicle == vehicle

def test_vehicle_info(create_space, create_vehicle):
    space = create_space
    assert space.vehicle_info() is None

    vehicle = create_vehicle
    space.add_vehicle(vehicle)
    assert space.vehicle_info() == vehicle

def test_entry_time(create_vehicle):
    vehicle = create_vehicle
    current_time = time.time()
    assert vehicle.get_entry_time() <= current_time

def test_set_entry_time(create_vehicle):
    vehicle = create_vehicle
    current_time = time.time()
    vehicle.set_entry_time(current_time - 3600)
    assert vehicle.get_entry_time() == current_time - 3600


# import pytest
# from main import Space, Vehicle

# # def test_enter_vehicle():
# #     space = Space()
# #     vehicle = Vehicle(1, "abc123")
# #     space.add_vehicle(vehicle)
# #     assert not space.is_available()
# #     assert space.vehicle_info() == vehicle

# # def test_exit_lot():
# #     space = Space()
# #     vehicle = Vehicle(1, "abc123")
# #     space.add_vehicle(vehicle)
# #     removed_vehicle = space.remove_vehicle()
# #     assert space.is_available()
# #     assert space.vehicle_info() is None
# #     assert removed_vehicle == vehicle

# # def test_exit_lot_empty_space():
# #     space = Space()
# #     assert not space.is_available()
# #     assert space.vehicle_info() is None

# # def test_enter_vehicle_invalid_plate():
# #     space = Space()
# #     vehicle = Vehicle(1, "abc123")
# #     space.add_vehicle(vehicle)
# #     new_vehicle = Vehicle(2, "abc123")
# #     ret_val = space.add_vehicle(new_vehicle)
# #     assert ret_val == -1
# #     assert not space.is_available()
# #     assert space.vehicle_info() == vehicle

# # def test_exit_lot_invalid_space():
# #     space = Space()
# #     with pytest.raises(IndexError):
# #         space.remove_vehicle()


# def test_enter_vehicle():
#     space = Space()
#     vehicle = Vehicle(1, "abc123")
#     space.add_vehicle(vehicle)
#     assert space.is_available() == False
#     assert space.vehicle_info() == vehicle

# def test_exit_lot():
#     space = Space()
#     vehicle = Vehicle(1, "abc123")
#     space.add_vehicle(vehicle)
#     assert space.is_available() == False
#     assert space.vehicle_info() == vehicle

#     removed_vehicle = space.remove_vehicle()
#     assert space.is_available() == True
#     assert space.vehicle_info() == None
#     assert removed_vehicle == vehicle

# def test_exit_lot_empty_space():
#     space = Space()
#     assert space.is_available() == False
#     assert space.vehicle_info() == None

#     removed_vehicle = space.remove_vehicle()
#     assert space.is_available() == False
#     assert space.vehicle_info() == None
#     assert removed_vehicle == None

# def test_enter_vehicle_invalid_space():
#     space = Space()
#     vehicle = Vehicle(1, "abc123")
#     space.add_vehicle(vehicle)
#     assert space.is_available() == False
#     assert space.vehicle_info() == vehicle

#     new_vehicle = Vehicle(2, "xyz789")
#     ret_val = space.add_vehicle(new_vehicle)
#     assert ret_val == -1
#     assert space.is_available() == False
#     assert space.vehicle_info() == vehicle

# def test_enter_vehicle_invalid_plate():
#     space = Space()
#     vehicle = Vehicle(1, "abc123")
#     space.add_vehicle(vehicle)
#     assert space.is_available() == False
#     assert space.vehicle_info() == vehicle

#     new_vehicle = Vehicle(2, "abc123")
#     ret_val = space.add_vehicle(new_vehicle)
#     assert ret_val == -1
#     assert space.is_available() == False
#     assert space.vehicle_info() == vehicle

# def test_exit_lot_invalid_space():
#     space = Space()
#     assert space.is_available() == False
#     assert space.vehicle_info() == None

#     with pytest.raises(IndexError):
#         space.remove_vehicle()

# def test_enter_vehicle_type_string():
#     vehicle = Vehicle(1, "abc123")
#     assert vehicle.get_type_string() == "Car"

#     vehicle = Vehicle(2, "xyz789")
#     assert vehicle.get_type_string() == "Truck"

#     vehicle = Vehicle(3, "def456")
#     assert vehicle.get_type_string() == "Motorcycle"

# def test_enter_vehicle_get_plate():
#     vehicle = Vehicle(1, "abc123")
#     assert vehicle.get_plate() == "abc123"

# def test_enter_vehicle_get_entry_time():
#     vehicle = Vehicle(1, "abc123")
#     assert vehicle.get_entry_time() is not None

# def test_set_entry_time():
#     vehicle = Vehicle(1, "abc123")
#     entry_time = vehicle.get_entry_time()
#     vehicle.set_entry_time(1234567890)
#     assert vehicle.get_entry_time() == 1234567890
#     assert vehicle.get_entry_time() != entry_time

# def test_enter_vehicle_get_vehicle():
#     vehicle = Vehicle(1, "abc123")
#     assert vehicle.get_vehicle() == (1, "abc123", vehicle.get_entry_time())
