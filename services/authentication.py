#create authentication class To prevent code duplication
class Authentication:
    def __init__(self):
        pass 
    #get user:Admin|Employer|Passenger and append to her list    
    def rigester(self, user) -> bool:
        pass
        
    #get username,password,role and check its availability in the list   
    def login(self, username:str, password:str,role ) -> bool:
        pass