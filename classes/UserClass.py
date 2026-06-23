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
        
    def __str__(self):
        return super().__str__() + f"Name: {self.name}\nEmail:{self.email}"   
        
#create authentication class To prevent code duplication
class Authentication:
    def __init__(self):
        self.admins = []
        self.employers = []    
        self.passengers = []
        
    #get user:Admin|Employer|Passenger and append to her list    
    def rigester(self, user) -> bool:
        if isinstance(user, Admin_User):
            self.admins.append(user)
            return True
        elif isinstance(user,Employer):
            self.employers.append(user)
            return True
        elif isinstance(user, Passenger):
            self.passengers.append(user)
            return True
        else:
            return False
            
        
    #get username,password,role and check its availability in the list   
    def login(self, username:str, password:str,role ) -> bool:
        if role == 'admin':
            for i in self.admins :
                if i.username == username and i.password == password:
                    return True      
            return False
        elif role == 'employer':
            for i in self.employers:
                if i.username == username and i.password == password:
                    return True      
            return False
        elif role == 'passenger':
            for i in self.passengers:
                if i.username == username and i.password == password:
                    return True      
            return False
        else:
            return False
        
    
        
        
        
        
        
        
        
        
        
        
        
        
        
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    # def get_info(self) -> str :
    #     """
    #     show basic information 

    #     """
    #     return f"Name : {self.username} |  " 
        
