import uuid 

#here we use the uuid module that makes a random uuid (for example : hh46dghr67h-hdu7-7u47) and return the frist four character
def get_id():
    uid = uuid.uuid4()
    return str(uid)[0:3]


class Train:
    def __init__(self,name,line,avarage_speed,quality,ticket_cost,capacity):
        self.id = get_id()
        self.name = name
        self.line = line
        self.avarage_speed = avarage_speed
        self.quality = quality
        self.ticket_cost= ticket_cost
        self.capacity = capacity
    def __str__(self):
        return f"id: {self.id}\nName: {self.name}\nLine: {self.line}\nAvarage_speed: {self.avarage_speed}\nQuality: {self.quality}\nticket_cost: {self.ticket_cost}\nCapacity: {self.capacity}\n"

