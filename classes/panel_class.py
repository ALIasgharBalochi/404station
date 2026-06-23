from classes.UserClass import Admin_User, Employer, Passenger, Authentication
from database.database import DataBase


class Panel:
    def __init__(self):
        self.auth = Authentication()
        self.db   = DataBase()

        #Default admin username and password
        admin = Admin_User("admin", "admin")
        self.auth.rigester(admin)
        self.db.create_DI(admin, "admins")

    def start(self):
        while True:
            print("\nBe 404 Station Khosh Omadi")
            print("1. Admin Panel")
            print("2. Employer")
            print("3. Passenger")
            print("4. Exit")

            choice = input("Mikhay Koja Beri? ")

            if choice == "1":
                self.admin_login_panel()
            elif choice == "2":
                pass
            elif choice == "3":
                pass
            elif choice == "4":
                print("Shab O RoozegaR Khosh")
                break
            else:
                print("Dari Eshatebah Mizani Dadash")

    def admin_login_panel(self):
        while True:
            print("\nAdmin Login")

            username = input("username: ")
            password = input("password: ")

            if self.auth.login(username, password, "admin"):
                print("Admin login succesfull.")
                self.admin_panel()
            else:
                print("username or password is wrong")

    def admin_panel(self):
        while True:
            print("\nPanel Modiriati")
            print("1. Add Emplouyer")
            print("2. Remove Employer")
            print("3. Show Employers")
            print("4. Back")

            i = input("Mikhay Koja Beri? ")

            if i == "1":
                self.add_employer()
            elif i == "2":
                self.remove_employer()
            elif i == "3":
                self.show_employer()
            elif i == "4":
                return
            else:
                print("Dari Eshatebah Mizani Dadash")

    def add_employer(self):
        print("\nAdd employer")
        username = input("Username: ")

        #use db classes to read employers list
        old_employer = self.db.read("employers", username)
        if old_employer:
            print("this username already exist")
            return
        

        password = input("Password: ")
        first_name = input("First name: ")
        last_name = input("Last Name: ")
        email = input("Email: ")

        employer = Employer(username, password, first_name, last_name, email)

        #use authentication class to register a employer and added to the list
        self.auth.rigester(employer)
        self.db.create_DI(employer, "employers")

        print(f"Employer {username} with {password} is created ")


    def remove_employer(self):
        username = input("Enter employer who we should remove")
        
        # chek if exist(if exist can be a method) remove from list

    def show_employer(self):
        if len == 0:
            print("user nout found")
            return
        
        #for on employer

# we can write some metohd like if username exist and others 