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
                self.employer_login_panel()
            elif choice == "3":
                pass
            elif choice == "4":
                print("Shab O RoozegaR Khosh")
                break
            else:
                print("Dari Eshatebah Mizani Dadash")

    # Admin

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
        username = input("Enter employer username: ")

        employer = self.db.read("employers", username)
        
        #check red method if return use remove data method to delete
        if employer:
            self.db.remove_data("employers", username)
            self.auth.employers.remove(employer)
            print("Employer is removed")
        else:
            print("username not found")
    
    def show_employer(self):
        employers = self.db.read_all_data("employers")
        if len(employers) == 0:
            print("we don`t have employer yet")
            return
        
        for employer in employers:
            print("-------------------")
            print("username: ", employer.username)
            print("name: ", employer.first_name, employer.last_name)
            print("username: ", employer.email)

    # Employer

    def employer_login_panel(self):
        while True:
            print("\employer Login")

            username = input("username: ")
            password = input("password: ")

            if self.auth.login(username, password, "employer"):
                print("employer login succesfull.")
                self.employer_panel()
            else:
                print("username or password is wrong")

    def employer_panel(self):
        while True:
            print("\nPanel employer")
            print("1. Add Line")
            print("2. Update Line")
            print("3. Delete Line")
            print("4. Show Line")
            print("5. Add Train")
            print("6. Update Train")
            print("7. Delete Train")
            print("8. Show Train")
            print("9. Sign Out")

            

            i = input("Mikhay Koja Beri? ")

            if i == "1":
                pass
            elif i == "2":
                pass
            elif i == "3":
                pass
            elif i == "4":
                pass
            elif i == "5":
              pass
            elif i == "6":
                pass
            elif i == "7":
                pass
            elif i == "8":
                pass
            elif i == "9":
                return
            else:
                print("Dari Eshatebah Mizani Dadash")
