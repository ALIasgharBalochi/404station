class User:
    def __init__(self, username: str, password:str,role):
        self.username = username
        self.password = password 
        self.role = role 
    def __str__(self):
        return f"username: {self.username}\n"   
        
class Admin_User(User):
    def __init__(self,username,password,):
        super().__init__(username,password,"admin")
        
        
class Employer(User):
    def __init__(self,username,password,first_name,last_name,email):
        super().__init__(username,password,"employer")
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
    
    def __str__(self):
        return super().__str__() + f"First Name: {self.first_name}\nLast Name: {self.last_name}\nEmail:{self.email}"   
        
class Passenger(User):
    def __init__(self,username,password,name,email):
        super().__init__(username,password,"passenger")
        self.name = name
        self.email = email
        self.wallet = 0
        self.cards = []
       
        
    def __str__(self):
        return super().__str__() + f"Name: {self.name}\nEmail:{self.email}"        
    
        
        
        
        
        
        
        
        
        
        
        
        
        
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    # def get_info(self) -> str :
    #     """
    #     show basic information 

    #     """
    #     return f"Name : {self.username} |  " 
        
