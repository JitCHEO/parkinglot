
import time

class Vehicle:
    def __init__(self, v_type, plate, entry_time=None, exit_time=None, fee=None, entry_datetime=None, exit_datetime=None):
        self.type = v_type # vehicle type
        self.plate = plate # registration number
        self.entry_time = entry_time if entry_time is not None else time.time() 
        # entry_time indicates time vehicle enter the lot, 
        # not provided it defaults to the time imported.
        self.exit_time = exit_time # exit time
        self.fee = fee # stores parking fee, set to None
        self.entry_datetime = entry_datetime 
        # additional attributes to store them as datetime objects.
        self.exit_datetime = exit_datetime





