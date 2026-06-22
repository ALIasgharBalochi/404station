class User:
    def __init__(self, username: str, password:str,role):
        self.username = username
        self.password = password 
        self.role = role 
        
class Admin_User(User):
    def __init__(self,username,password,):
        super().__init__(username,password,"admin")
        
        
class Employer(User):
    def __init__(self,username,password,first_name,last_name,email):
        super().__init__(username,password,"employer")
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        
        
class Passenger(User):
    def __init__(self,username,password,name,email):
        super().__init__(username,password,"passenger")
        self.name = name
        self.email = email
        
        
#create authentication class To prevent code duplication
class Authentication:
    def __init__(self):
        self.admins = []
        self.employers = []    
        self.passengers = []
        
    #get user:Admin|Employer|Passenger and append to her list    
    def rigester(self, user) -> bool:
        if isinstance(user, Admin_User):
            self.admin.append(user)
            return True
        elif isinstance(user,Employer):
            self.employer.append(user)
            return True
        elif isinstance(user, Passenger):
            self.passenger.append(user)
            return True
        else:
            return False
            
        
    #get username,password,role and check its availability in the list   
    def login(self, username:str, password:str,role ) -> bool:
        if role == 'admin':
            for i in self.admins :
                if i.username == username and i.password == password:
                    return True      
                else:
                    return False
        elif role == 'employer':
            for i in self.employers:
                if i.username == username and i.password == password:
                    return True      
                else:
                    return False
        elif role == 'passenger':
            for i in self.passengers:
                if i.username == username and i.password == password:
                    return True      
                else:
                    return False
        else:
            return False
        
    
        
        
        
        
        
        
        
        
        
        
        
        
        
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    # def get_info(self) -> str :
    #     """
    #     show basic information 

    #     """
    #     return f"Name : {self.username} |  " 
        
