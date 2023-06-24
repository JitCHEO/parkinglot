import time

class Vehicle:
    def __init__(self, vehicle_type, plate):
        self.type = vehicle_type
        self.plate = plate
        self.entry_time = time.time()

    def get_type(self):
        return self.type

    def get_type_string(self):
        if self.type == 1:
            return "Car"
        if self.type == 2:
            return "Truck"
        else:
            return "motorcycle"
        # return "Car" if self.type == 1 else "Truck" if self.type == 2 else "Motorcycle"

    def get_plate(self):
        return self.plate

    def get_entry_time(self):
        return self.entry_time

    def set_entry_time(self, new_time):
        self.entry_time = new_time

    def get_vehicle(self):
        return self.type, self.plate, self.entry_time


class Space:
    def __init__(self):
        self.vehicle = None
        self.occupied = False

    def add_vehicle(self, vehicle):
        self.vehicle = vehicle
        self.occupied = True

    def remove_vehicle(self):
        vehicle_exit = self.vehicle
        self.vehicle = None
        self.occupied = False
        return vehicle_exit

    def vehicle_info(self):
        return self.vehicle

    def is_available(self):
        return self.occupied


def print_row(spaces, space_count, row):
    output = "|"
    for s in range(space_count * row, space_count * (row + 1)):
        if not spaces[s].is_available():
            output += "[ ]"
        else:
            output += "["
            output += "c" if spaces[s].vehicle_info().get_type() == 1 \
                else "t" if spaces[s].vehicle_info().get_type() == 2 \
                else "m"
            output += "]"
        if s < space_count * (row + 1) - 1:
            output += " "
    output += "|"

    return output


def display_lot(spaces, avail_spaces, rows, space_count):
    output = "SPOTS AVAILABLE: " + str(avail_spaces) + "\n"
    border = ""

    output += border

    for row in range(rows):
        output += print_row(spaces, space_count, row) + "\n"

    output += border

    print(output)


def display_row_selection(spaces, avail_spaces, rows, space_count):
    output = "SPOTS AVAILABLE: " + str(avail_spaces) + "\n"
    border = ""

    output += border
    for row in range(rows):
        output += print_row(spaces, space_count, row)
        output += " <" + str(row) + ">\n"
    output += border

    print(output)


def display_space_selection(spaces, rows, space_count, row):
    output = "VIEWING ROW: " + str(row) + "\n"
    border = ""

    output += border
    output += print_row(spaces, space_count, int(row)) + "\n"

    output += " "
    for count in range(space_count):
        if count < 10:
            output += "<" + str(count) + "> "
        else:
            output += "<" + str(count) + ">"

    output += "\n"
    output += border

    print(output)

    return space_count


def enter_vehicle(v_type, plate, row, space, spaces, avail_spaces):
    if avail_spaces == 0:
        display_lot(spaces, avail_spaces, space)
        print("Parking lot is full.")
        return

    if not spaces.is_available():
        # display_space_selection(spaces, rows, space_count, row)
        print("Space")


def main_menu():
    print("Please Select An Option:\n"
          "P - Park a Vehicle\n"
          "E - Exit the Lot\n"
          "V - View a Parked Vehicle\n"
          "R - Display Vehicle Rates\n"
          "Q - Quit Application\n")

def process_user_input(input_str):
    input_str = input_str.lower()
    if input_str == "p":
        # Handle parking a vehicle
        pass
    elif input_str == "e":
        # Handle exiting the lot
        pass
    elif input_str == "v":
        # Handle viewing a parked vehicle
        pass
    elif input_str == "r":
        # Handle displaying vehicle rates
        pass
    elif input_str == "q":
        # Handle quitting the application
        pass
    else:
        print("Invalid input. Please try again.")

def run_parking_lot():
    while True:
        main_menu()
        user_input = input("Enter your choice: ")
        process_user_input(user_input)
        # You can add additional logic based on user input as needed

run_parking_lot()
