import uuid 

#here we use the uuid module that makes a random uuid (for example : hh46dghr67h-hdu7-7u47) and return the frist four character
def get_id():
    uid = uuid.uuid4()
    return str(uid)[0:3]


class Train:
    def __init__(self,name,line,avarage_speed,quality,ticket_cost,capacity, stop_time):
        
        if avarage_speed < 0 :
            raise ValueError("avarage_Speed cannot be negative!")
        if ticket_cost < 0 :
            raise ValueError("ticket_cost cannot be negative!")
        
        if not isinstance(stop_time, dict):
            raise ValueError("stop_time must be a dictionary!")

        for station, minutes in stop_time.items():
            if minutes < 0:
                raise ValueError(f"stop time for {station} cannot be negative!")
        
        self.id = get_id()
        self.name = name
        self.line = line
        self.avarage_speed = avarage_speed
        self.quality = quality
        self.ticket_cost= ticket_cost
        self.capacity = capacity
        self.stop_time = stop_time
    def __str__(self):
        

        stop_text = "\n".join(
            f"{station}: {minutes} minutes"
            for station, minutes in self.stop_time.items()
        )

        
        return (f"--- Train Info ---\n"
                f"ID: {self.id}\n"
                f"Name: {self.name}\n"
                f"Line: {self.line}\n"
                f"Average Speed: {self.avarage_speed} km/h\n"
                f"Quality: {self.quality}\n"
                f"Ticket Cost: ${self.ticket_cost}\n"
                f"Capacity: {self.capacity}\n"
                f"Stop Times:\n{stop_text}\n")
