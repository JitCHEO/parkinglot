
#  from simply3trial.py

import time
from vehicle import *
from parkinglot import ParkingLot

def main():
    # user input number of parking spaces
    total_spaces = int(input("Enter the total number of parking spaces: "))
    parking_lot = ParkingLot(total_spaces)
    # List to store the report entries
    report = []  

    # while loop to keep repeating until quit is selected.
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
                # if vehicle is parked, report on information of v_plate, entry & exit time & fee will 
                # be generated.
                report.append(f"Parked: {vehicle.plate} ({parking_lot.get_vehicle_type(vehicle.type)}), "
                              f"Entry: {vehicle.entry_datetime}, Fee: ${vehicle.fee}")
                

        elif option == "2":
            plate = input("Enter vehicle registration number: ")
            # 2 arguments as vehicle & fee
            vehicle, fee = parking_lot.exit_lot(plate)
            if vehicle is not None:
                if fee is not None:
                     # if vehicle & fee returns correct value,
                    print(f"Vehicle exited successfully. Fee: ${fee:.2f}")
                    # generate repprt on exiting infos
                    report.append(f"Exited: {vehicle.plate} ({parking_lot.get_vehicle_type(vehicle.type)}), "
                                  f"Exit: {vehicle.exit_datetime}, Fee: ${fee:.2f}")
                else:
                    print("Error: Fee calculation failed.")
            
            else:
                print("Error: Vehicle registration number not provided.")

        # display status of the parking lot whether is full or empty
        elif option == "3":
            parking_lot.display_lot()

        # option 4 is quitting the terminal app
        elif option == "4":
            # Generate the report and write it to a file
            # strftime format the date to YYY-MM-DD_HH:MM:SS
            timestamp = time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime())
            filename = f"parking_report_{timestamp}.txt"

            # file open in written mode, 'with' will ensure that file is properly closed
            with open(filename, "w") as file:
                # loop iterates the report, entry report is written with a newline
                for entry in report:
                    file.write(entry + "\n")
            
            # success message printed indicated report generated & saved.
            print(f"Report generated and saved as {filename}.")
            break

        else:
            print("Invalid option. Please try again.")


# using the same code as original repo, 
# from reading, check current script run directly or imported
# Way to ensure certain code runs only when script is run direxctly,
# not when is imported as module.
if __name__ == '__main__':
    main()

