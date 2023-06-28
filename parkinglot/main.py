
#  from simply3trial.py

import time
from vehicle import *
from parkinglot import ParkingLot



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
                # #####
                report.append(f"Parked: {vehicle.plate} ({parking_lot.get_vehicle_type(vehicle.type)}), "
                              f"Entry: {vehicle.entry_datetime}, Fee: ${vehicle.fee}")
                

        elif option == "2":
            plate = input("Enter vehicle registration number: ")
            vehicle, fee = parking_lot.exit_lot(plate)
            if vehicle is not None:
                if fee is not None:
                    print(f"Vehicle exited successfully. Fee: ${fee:.2f}")
                    report.append(f"Exited: {vehicle.plate} ({parking_lot.get_vehicle_type(vehicle.type)}), "
                                  f"Exit: {vehicle.exit_datetime}, Fee: ${fee:.2f}")
                else:
                    print("Error: Fee calculation failed.")

        elif option == "3":
            parking_lot.display_lot()


        elif option == "4":
            # Generate the report and write it to a file
            timestamp = time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime())
            filename = f"parking_report_{timestamp}.txt"

            with open(filename, "w") as file:
                for entry in report:
                    file.write(entry + "\n")


            # with open(filename, "w") as file:
            #     file.write("\n".join(report))

            print(f"Report generated and saved as {filename}.")
            break

        else:
            print("Invalid option. Please try again.")


if __name__ == '__main__':
    main()

