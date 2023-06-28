
import time

class Vehicle:
    def __init__(self, v_type, plate, entry_time=None, exit_time=None, fee=None, entry_datetime=None, exit_datetime=None):
        self.type = v_type
        self.plate = plate
        self.entry_time = entry_time if entry_time is not None else time.time()
        self.exit_time = exit_time
        self.fee = fee
        self.entry_datetime = entry_datetime
        self.exit_datetime = exit_datetime





