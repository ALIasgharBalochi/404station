from typing import Optional
from utilitys.checker import check
#create authentication class To prevent code duplication
class Authentication:
    def __init__(self,database):
        self.database = database

    def register(self, user) -> dict :
        """
            Registers a new user (Admin, Employer, or Passenger) into the database.

            Args:
                user: An object containing user details such as role, username, and email.

            Returns:
                dict: A dictionary containing 'status' (bool) and 'message' (str) if the 
                    user already exists or if the creation process fails/succeeds.
                bool: (Based on your logic) Returns a boolean if needed, though currently 
                    returning a dict is preferred for consistency.
        """
        if user.role == "employer":
            #data is object if be existed else is false
            data = self.database.read("employers",user.username)
            if data is False:
                #res is true or flase
                if check(user.password,user.email):
                    res = self.database.create_DI(user,"employers")
                    if res == True:
                        return {"status": True,'message': "user successfully created" }
                    else:
                        return {"status": False,'message': "failed to create user" }
                else:
                    return {"status": False,'message': "the password or email format is not valid" }    
            return {"status": False,'message': "user is existed with this username" }
        elif user.role == "passenger":
            user_email = self.database.read("passengers",user.email)
            user_username = self.database.read("passengers",user.username)
            if user_email == False and user_username is False:
                if check(user.password,user.email):
                    res = self.database.create_DI(user,"passengers")
                    if res == True:
                        return {"status": True,'message': "user successfully created" }
                    else:
                        return {"status": False,'message': "failed to create user" }
                else:
                    return {"status": False,'message': "the password or email format is not valid" }
                
            return {"status": False,'message': "user is existed with this username or email" }
        
        return {"status": False, "message": "invalid role"}


    def login(self, username:str, password:str, role:str ) -> dict:
        """
        Authenticates a user by verifying credentials against the specified role's database.

        Args:
            username (str): The unique identifier/username of the user.
            password (str): The plain-text password to be verified.
            role (str): The user role determining the target table 
                        ('admin', 'employer', or 'passenger').

        Returns:
            dict: A dictionary containing:
                - 'status' (bool): True if authentication succeeds, False otherwise.
                - 'message' (str): A descriptive message about the result.
                - 'obj' (User object, optional): The user object if login is successful.
        """
        if role == "admin":
            user = self.database.read("admins",username)
            if user:
                if user.password == password:
                    return {"status": True,"message": "login successfully","obj": user}
            return {'status': False,'message': "username or password is wrong"}

        if role == "employer":
            user = self.database.read("employers",username)
            if user:
                if user.password == password:
                    return {"status": True,"message": "login successfuly","obj": user}
            return {'status': False,'message': "username or password is wrong"}

        if role == "passenger":
            user = self.database.read("passengers",username)
            if user:
                if user.password == password:
                    return {"status": True,"message": "login successfuly","obj": user}
            return {'status': False,'message': "username or password is wrong"}
        
        return {"status": False, "message": "invalid role"}
