

import time

class Vehicle:
   def __init__(self, v_type, plate, entry_time=None, exit_time=None, fee=None):
        self.type = v_type
        self.plate = plate
        self.entry_time = entry_time
        self.exit_time = exit_time
        self.fee = fee



class ParkingLot:
    def __init__(self, total_spaces): 
        self.spaces = [None] * total_spaces
        self.avail_spaces = total_spaces

    def park_vehicle(self, v_type, plate):
        if self.avail_spaces == 0:
            print("Error: No Available Spaces")
            return

        for i in range(len(self.spaces)):
          if self.spaces[i] is None:
                current_time = time.time()
                vehicle = Vehicle(v_type, plate, entry_time=current_time)
                self.spaces[i] = vehicle
                self.avail_spaces -= 1
                print("Vehicle parked successfully.")
                # self.calculate_fee(vehicle)  # Calculate the fee for the parked vehicle
                return vehicle

        print("Error: Parking lot is full")
        return None

    def exit_lot(self, plate):
        for i in range(len(self.spaces)):
            if self.spaces[i] and self.spaces[i].plate == plate:
                current_time = time.time()
                vehicle = self.spaces[i]
                vehicle.exit_time = current_time
                fee = self.calculate_fee(vehicle)  # Calculate the fee for the exiting vehicle
                self.spaces[i] = None
                self.avail_spaces += 1
                print("Vehicle exited successfully.")
                if fee is not None:
                    print(f"Fee: ${fee:.2f}")  # Display the fee
                else:
                    print("Error: Fee calculation failed.")
                return

# PROBABLY REMOVE THIS
# MIGHT REMOVE FUNCTION 4 THAT CHECK FEE CALC.
    # def exit_lot(self, plate):
    #     for i in range(len(self.spaces)):
    #         if self.spaces[i] and self.spaces[i].plate == plate:
    #             current_time = time.time()
    #             vehicle = self.spaces[i]
    #             vehicle.exit_time = current_time
    #             self.calculate_fee(vehicle) #calc fee for exit veh.
    #             self.spaces[i] = None
    #             self.avail_spaces += 1
    #             print("Vehicle exited successfully.")
    #             return

        print("Error: Vehicle not found in the parking lot.")
        return None

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


def main():
    total_spaces = int(input("Enter the total number of parking spaces: "))
    parking_lot = ParkingLot(total_spaces)

    report = []  # List to store the report entries

    while True:
        print("\nPlease select an option:")
        print("1. Park a vehicle")
        print("2. Exit the parking lot")
        print("3. Display parking lot status")
        print("4. Quit")

        option = input("> ")

        if option == "1":
            print("\nSelect a vehicle type:")
            print("1. Car")
            print("2. Truck")
            print("3. Motorcycle")

            v_type = int(input("> "))
            plate = input("Enter vehicle registration number: ")

            vehicle = parking_lot.park_vehicle(v_type, plate)
            if vehicle is not None:
                print(f"Vehicle parked successfully. Fee: ${vehicle.fee}")

        elif option == "2":
            plate = input("Enter vehicle registration number: ")
            vehicle = parking_lot.exit_lot(plate)
            if vehicle is not None:
                fee = parking_lot.calculate_fee(vehicle)
                if fee is not None:
                    print(f"Vehicle exited successfully. Fee: ${fee:.2f}")
                else:
                    print("Error: Fee calculation failed.")


                # parking_lot.calculate_fee(vehicle)
                # print(f"Vehicle exited successfully. Fee: ${vehicle.fee}")

        elif option == "3":
            parking_lot.display_lot()

# REMOVE THIS ELIF AS PROBABLY NOT NEEDED FOR MY CODE
        # elif option == "4":
        #     plate = input("Enter vehicle registration number: ")
        #     for space in parking_lot.spaces:
        #         if space and space.plate == plate:
        #             fee = parking_lot.calculate_fee(space)
        #             if fee is not None:
        #                 print(f"Vehicle fee for {space.plate}: ${fee}")
        #             else:
        #                 print(f"Fee not calculated for {space.plate}.")
        #             break
        #     else:
        #         print("Error: Vehicle not found in the parking lot.")


# USE THIS CODE HERE
        # elif option == "4":
        #     break


        elif option == "4":
            # Generate the report and write it to a file
            timestamp = time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime())
            filename = f"parking_report_{timestamp}.txt"

            with open(filename, "w") as file:
                file.write("Parking Lot Report\n")
                file.write("-------------------\n")
                for entry in report:
                    file.write(entry + "\n")

            print(f"Report generated and saved as {filename}.")
            break


        else:
            print("Invalid option. Please try again.")


if __name__ == '__main__':
    main()


