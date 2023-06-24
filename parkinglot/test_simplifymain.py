
# import time
# import pytest
# from simplifymain import Vehicle, Space

# @pytest.fixture
# def create_vehicle():
#     return Vehicle(1, "ABC123")

# @pytest.fixture
# def create_space():
#     return Space()

# def test_vehicle_creation(create_vehicle):
#     vehicle = create_vehicle
#     assert vehicle.get_type() == 1
#     assert vehicle.get_plate() == "ABC123"

# def test_space_availability(create_space, create_vehicle):
#     space = create_space
#     assert not space.is_available()

#     vehicle = create_vehicle
#     space.add_vehicle(vehicle)
#     assert space.is_available()

#     removed_vehicle = space.remove_vehicle()
#     assert not space.is_available()
#     assert removed_vehicle == vehicle

# def test_vehicle_info(create_space, create_vehicle):
#     space = create_space
#     assert space.vehicle_info() is None

#     vehicle = create_vehicle
#     space.add_vehicle(vehicle)
#     assert space.vehicle_info() == vehicle

# def test_entry_time(create_vehicle):
#     vehicle = create_vehicle
#     current_time = time.time()
#     assert vehicle.get_entry_time() <= current_time

# def test_set_entry_time(create_vehicle):
#     vehicle = create_vehicle
#     current_time = time.time()
#     vehicle.set_entry_time(current_time - 3600)
#     assert vehicle.get_entry_time() == current_time - 3600
