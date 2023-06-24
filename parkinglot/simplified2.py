

import time

class Vehicle:
    def __init__(self, v_type, plate, entry_time = None):
        self.type = v_type
        self.plate = plate
        self.entry_time = entry_time


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
                self.spaces[i] = Vehicle(v_type, plate)
                self.avail_spaces -= 1
                print("Vehicle parked successfully.")
                return

        print("Error: Parking lot is full")

    def exit_lot(self, plate):
        for i in range(len(self.spaces)):
            if self.spaces[i] and self.spaces[i].plate == plate:
                self.spaces[i] = None
                self.avail_spaces += 1
                print("Vehicle exited successfully.")
                return

        print("Error: Vehicle not found in the parking lot.")

    def display_lot(self):
        print("Available spaces:", self.avail_spaces)
        print("Parking Lot Status:")
        for i in range(len(self.spaces)):
            if self.spaces[i]:
                print(f"Space {i+1}: {self.spaces[i].plate} ({self.get_vehicle_type(self.spaces[i].type)})")
            else:
                print(f"Space {i+1}: Empty")

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

            parking_lot.park_vehicle(v_type, plate)

        elif option == "2":
            plate = input("Enter vehicle registration number: ")
            parking_lot.exit_lot(plate)

        elif option == "3":
            parking_lot.display_lot()

        elif option == "4":
            break

        else:
            print("Invalid option. Please try again.")


if __name__ == '__main__':
    main()


