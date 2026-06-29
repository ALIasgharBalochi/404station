import uuid 

#here we use the uuid module that makes a random uuid (for example : hh46dghr67h-hdu7-7u47) and return the frist four character
def get_id():
    uid = uuid.uuid4()
    return str(uid)[0:3]


class Train:
    def __init__(self,name,line,avarage_speed,quality,ticket_cost,capacity, stop_time,time_to_move,distance_to_station):
        
        if avarage_speed < 0 :
            raise ValueError("avarage_Speed cannot be negative!")
        if ticket_cost < 0 :
            raise ValueError("ticket_cost cannot be negative!")
        if not stop_time.isnumeric():
            raise ValueError("dadashe man stop time bayad yek adad bashad faghat masalan: 5)!")
        if not distance_to_station.isnumeric():
            raise ValueError("dadashe man fasele ta istgah bayad yek adad bashad faghat masalan: 20)!")
        

        self.id = get_id()
        self.name = name
        self.line = line
        self.avarage_speed = avarage_speed
        self.quality = quality
        self.ticket_cost= ticket_cost
        self.capacity = capacity
        self.stop_time = stop_time
        self.time_to_move = time_to_move
        self.distance_to_station = distance_to_station
    def __str__(self):
        
        return (f"--- Train Info ---\n"
                f"ID: {self.id}\n"
                f"Name: {self.name}\n"
                f"Line: {self.line}\n"
                f"Average Speed: {self.avarage_speed} km/h\n"
                f"Quality: {self.quality}\n"
                f"Ticket Cost: ${self.ticket_cost}\n"
                f"Capacity: {self.capacity}\n"
                f"Stop Times in station: {self.stop_time} min\n"
                f"Time To Move: {self.time_to_move}\n"
                f"Distance To The Station: {self.distance_to_station} km/h")
