
import time
from vehicle import Vehicle

class ParkingLot:
    def __init__(self, total_spaces): 
        self.spaces = [None] * total_spaces
        self.avail_spaces = total_spaces
        self.occupied_spaces = 0

    def park_vehicle(self, v_type, plate):
        if self.avail_spaces == 0:
            print("Error: No Available Spaces")
            return

        for i in range(len(self.spaces)):
          if self.spaces[i] is None:
                current_time = time.time()
                current_datetime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                vehicle = Vehicle(v_type, plate, entry_time=current_time, entry_datetime=current_datetime)
                self.spaces[i] = vehicle
                self.avail_spaces -= 1
                print("Vehicle parked successfully.")
                self.occupied_spaces += 1
                return vehicle

        print("Error: Parking lot is full")
        return None

    def exit_lot(self, plate):
        for i in range(len(self.spaces)):
            if self.spaces[i] and self.spaces[i].plate == plate:
                current_time = time.time()
                current_datetime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                vehicle = self.spaces[i]
                vehicle.exit_time = current_time
                vehicle.exit_datetime = current_datetime
                fee = self.calculate_fee(vehicle)
                self.spaces[i] = None
                self.avail_spaces += 1
                self.occupied_spaces -= 1
                return vehicle, fee

        return None, None  # Vehicle not found


    def display_lot(self):
        print("Available spaces:", self.avail_spaces)
        print("Parking Lot Status:")
        for i in range(len(self.spaces)):
            if self.spaces[i]:
                print(f"Space {i+1}: {self.spaces[i].plate} ({self.get_vehicle_type(self.spaces[i].type)})")
            else:
                print(f"Space {i+1}: Empty")


    # fee calculations
    def calculate_fee(self, vehicle):
        if vehicle.entry_time is None or vehicle.exit_time is None:
            return None

        duration = vehicle.exit_time - vehicle.entry_time
        # Assuming the fee calculation is $5 per hour
        fee = duration * 5 / 3600  # Convert seconds to hours
        vehicle.fee = fee
        return fee
        

    @staticmethod
    def get_vehicle_type(v_type):
        if v_type == 1:
            return "Car"
        elif v_type == 2:
            return "Truck"
        elif v_type == 3:
            return "Motorcycle"
        else:
            return "Unknown"













