class Panel:
    def __init__(self):
        pass
        
    def start(self):
        while True:
            print("\n Be 404 Station Khosh Omadi")
            print("1. Admin Panel")
            print("2. Employer")
            print("\n Be 404 Station Khosh Omadi")

    
class Start_Panel(Panel):
    def __init__(self, menu:dict ) :
        super().__init__(menu)
        
class Admin_Panel(Panel):
    def __init__(self, menu:dict ) :
        super().__init__(menu)
        
        
class Employer_Panel(Panel):
    def __init__(self, menu:dict ) :
        super().__init__(menu)
          
    
class Passenger_Panel(Panel):
    def __init__(self, menu:dict ) :
        super().__init__(menu)
        

class Buy_Panel(Panel):
    def __init__(self, menu:dict ) :
        super().__init__(menu) 
    