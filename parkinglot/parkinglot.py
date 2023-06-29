
import time
from vehicle import Vehicle

class ParkingLot:
    def __init__(self, total_spaces): 
        # total_spaces shows # space in the lot.
        # spaces is list that represent parking spaces.
        # spaces are set to none to indicate they are not occupied.
        self.spaces = [None] * total_spaces 
        #available_spaces represent available space is in the lot.
        self.available_spaces = total_spaces
        # occupied_spaces represent number spaces being occupied.
        self.occupied_spaces = 0

    def park_vehicle(self, v_type, plate):
        # no parking spaces available, print the error code
        if self.available_spaces == 0:
            print("Error: No Available Spaces")
            return

        # below code proceeds to check for space as long as code pass above
        for i in range(len(self.spaces)):
          if self.spaces[i] is None:
                # import time module set the time for time & datetime
                current_time = time.time()
                current_datetime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                # creates the vehicle as per the arguments in the ()
                vehicle = Vehicle(v_type, plate, entry_time=current_time, entry_datetime=current_datetime)
                self.spaces[i] = vehicle
                # depending on vehicle entering & exiting,
                # below 2 spaces are updated accordingly.
                self.available_spaces -= 1
                print("Vehicle parked successfully.")
                self.occupied_spaces += 1
                return vehicle

        # if parking is full, below error will be printed.
        print("Error: Parking lot is full")
        return None

    # function that take parameter 'plate'/registration plate.
    def exit_lot(self, plate):
        for i in range(len(self.spaces)):
            # inside this nested loops, if the plate matches, 
            if self.spaces[i] and self.spaces[i].plate == plate:
                # retrieve the time
                current_time = time.time()
                # change the format to YYY/MM/DD HH:MM:SS
                current_datetime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                vehicle = self.spaces[i]
                vehicle.exit_time = current_time
                vehicle.exit_datetime = current_datetime
                # then calculate the fee and store it as 'fee'
                fee = self.calculate_fee(vehicle)
                self.spaces[i] = None
                self.available_spaces += 1
                self.occupied_spaces -= 1
                return vehicle, fee

        # # Vehicle not found and return none for the vehicle object & fee
        return None, None  

    # display status of the parkinglot
    def display_lot(self):
        print("Available spaces:", self.available_spaces)
        print("Parking Lot Status:")
        for i in range(len(self.spaces)):
            # print the following if space is occupied
            if self.spaces[i]:
                print(f"Space {i+1}: {self.spaces[i].plate} ({self.get_vehicle_type(self.spaces[i].type)})")
            else:
                print(f"Space {i+1}: Empty")


    # fee calculations
    def calculate_fee(self, vehicle):
        # this method check if the time is noe, means is not recorded
        if vehicle.entry_time is None or vehicle.exit_time is None:
            # it will then indicate that fee can't be calc.
            return None

        # if enter & exit time are recorded, substraction happens.
        duration = vehicle.exit_time - vehicle.entry_time
        # Assuming the fee calculation is $4 per hour
        fee = duration * 4 / 3600  # Convert seconds to hours
        vehicle.fee = fee
        # calculated fee is processed.
        return fee
        

    # belongs to the class rather than instance of class.
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













