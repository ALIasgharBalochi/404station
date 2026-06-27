from classes.user import Employer
from utilitys import backButton
from utilitys.cli import CLI


class AdminPanel:

    def __init__(self, database, authentication):
        self.db = database
        self.auth = authentication      

    def admin_login_panel(self):
        attempts = 1
        while attempts < 4:
            CLI.title(f"\n--- Admin Login (Attempt {attempts}/3) ---")
            

            username = input("username: ").strip()
            #password = input("password: ").strip()

            password = input("password: ").strip()
            if password.lower() == 'exit':
                return

            login = self.auth.login(username, password, "admin")
            if login["status"]:
                print("")
                print(login["message"])
                self.admin_panel()
                return
            else:
                print("")
                print(login["message"])
                attempts += 1

    def admin_panel(self):
        while True:
            CLI.title("\n--- Panel Modiriati ---")
            CLI.info("1. Add Emplouyer")
            CLI.info("2. Remove Employer")
            CLI.info("3. Show Employers")
            CLI.info("4. Back")

            i = input("\nMikhay Koja Beri? ").strip()

            if i == "1":
                self.add_employer()
            elif i == "2":
                self.remove_employer()
            elif i == "3":
                self.show_employer()
            elif i == "4":
                return
                # Exit the current panel and return to the previous caller, 
                # avoiding unnecessary recursion or stack overflow.
            else:
                print("\nDari Eshatebah Mizani Dadash")

    def add_employer(self):
        CLI.title("\n--- Add employer ---")
        username = input("Username: ").strip()

        #use db classes to read employers list
        # old_employer = self.db.read("employers", username)
        # if old_employer:
        #     print("this username already exist")
        #     return
        

        password = input("Password: ").strip()
        first_name = input("First name: ").strip()
        last_name = input("Last Name: ").strip()
        email = input("Email: ").strip()

        if backButton.back("\ndost dary inaro sabt bokoni asalam? (Y/n) "):

            employer = Employer(username, password, first_name, last_name, email)

            #use authentication class to register a employer and added to the list
            #self.auth.rigester(employer)
            #self.db.create_DI(employer, "employers")
            register = self.auth.register(employer)

            #use authentication class to register a employer and added to the list
            # self.auth.rigester(employer)
            # self.db.create_DI(employer, "employers")
            if register["status"]:
                print("")
                print(register["message"])
                self.admin_panel()
            else:
                print("")
                print(register["message"])
                return
            # print(f"Employer {username} with {password} is created ")

                print(f"Employer {username} with {password} is created ")
        else:
            if backButton.back("\ndost dari dobare bezani? (Y/n) "):
                self.add_employer()
            else:
                self.admin_panel()    
        
    def remove_employer(self):
        CLI.title("\n--- Remove Employer ---")
        username = input("Enter employer username: ").strip()

        employer = self.db.read("employers", username)
        
        #check red method if return use remove data method to delete
        if employer:
            if backButton.back("\nba hazfe karmad ok hasty? (Y/N) "):

                self.db.remove_data("employers", username)
                print("\nEmployer is removed")

            else:
                if backButton.back("\ndost dari dobare hazf koni? (Y/n) "):
                    self.remove_employer()
                else:
                    self.admin_panel()     
        else:
            print("\nusername not found")
    
    def show_employer(self):
        CLI.title("\n--- Current Employer ---")
        employers = self.db.read_all_data("employers")
        if len(employers) == 0:
            print("\nwe don`t have employer yet")
            return
        
        for employer in employers:
            print("-------------------")
            print("username: ", employer.username)
            print("name: ", employer.first_name, employer.last_name)
            print("username: ", employer.email)
