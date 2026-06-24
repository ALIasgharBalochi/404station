from classes.UserClass import Admin_User, Employer, Passenger, Authentication
from database.database import DataBase
from classes.line import Line
from classes.train import Train

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
                self.start()
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
            print("\nemployer Login")

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
                self.add_line()
            elif i == "2":
                self.update_line()
            elif i == "3":
                self.delete_line()
            elif i == "4":
                self.show_lines()
            elif i == "5":
              self.add_train()
            elif i == "6":
                self.update_train()
            elif i == "7":
                self.delete_train()
            elif i == "8":
                self.show_trains()
            elif i == "9":
                self.start()
            else:
                print("Dari Eshatebah Mizani Dadash")


    def add_line(self):

        line_name   = input("Line Name: ")

        check_name = self.db.read("lines",line_name)
        
        #here it checks that the line_name is not duplicate
        if check_name:
            
            print("ye chi dige bezan in esm tekrariye")
            self.add_line()
        

        origin      = input("origin: ")
        destination = input("destination: ")
        station     = input("station: (E.X: khatib zade,Asadi,shahrabi,maneyjer jan <3) ").split(sep=",")
        station_count = len(station)
        
        result = self.db.create_DI(Line(line_name,origin,destination,station,station_count),"lines")

        if result:
            print("Line dorst shod hooraa!!")
            self.employer_panel() 
        
        else:
            print("moshkely pish omad dobare talash kon") 
            self.employer_panel()   



    def update_line(self):
        Name = input("esm khati ke mikhay update koni chie? ")
        check = self.db.read("lines",Name)

        if check:

            print(check)

            changable_attr = input("eshgam chi ro mikhy avaz koni: ").lower()
            new_value = input(f"{changable_attr} be chi taghir bedam: ")
            updated_data = self.db.update_data( "lines", Name ,changable_attr, new_value)
            
            if updated_data:
                print("khatet update shod horraa!")
                print(updated_data)
            
            else:
               
                answer = input("update ba khata movajeh shod, mikhay edame bedi(Y/N)").lower()
               
                if answer == "y":
                    self.update_line()
            
                elif answer == "n":
                    self.employer_panel()
            
                else:
                    print("eshtebah kardi az aval shro kon!")
                    self.employer_panel()     
        else:
            answer = input("hamchin khati nist, mikhay edame bedi(Y/N)").lower()
               
            if answer == "y":
                self.update_line()
            
            elif answer == "n":
                self.employer_panel()
            
            else:
                print("eshtebah kardi az aval shro kon!")
                self.employer_panel()     

            
    def delete_line(self):
        Name = input("chiro mikhay hazf kon? ")
        check = self.db.remove_data("lines",Name)

        if check:
            print("heyyyy hazf kardiiiddyaa!!!")
            self.employer_panel()
        
        else:
            print("donbal chi hasti dada! hamchin chizi nist")
            
            again = input("dost dari ey bar dighe emtahan koni?(Y/N)").lower()

            if again == "y":
                self.delete_line()
            
            elif again == "n":
                self.employer_panel()
            
            else:
                print("eshtebah kardi az aval shro kon!")
                self.employer_panel()         

    def show_lines(self):

        lines = self.db.read_all_data("lines")

        if len(lines) == 0 :
            print("listet khaliye baba")

        else:
            for line in lines:
                print("---------------")
                print(line)    

    def add_train(self):

        name = input("name: ")
        line = input("line: ")
        avarage_speed = input("avarage_speed: ")
        quality = input("quality: ")
        ticket_cost = input("ticket_cost: ")
        capacity = input("capacity: ")

        
        result = self.db.create_DI(Train(name,line,avarage_speed,quality,ticket_cost,capacity),"trains")

        if result:
            print("train dorst shod hooraa!!")
            self.employer_panel() 
        
        else:
            print("moshkely pish omad dobare talash kon") 
            self.employer_panel() 

    def update_train(self):
        id = input("Id train ke mikhay update koni chie? ")
        check = self.db.read("trains",id)

        if check:
            print("---------------")
            print(check)

            changable_attr = input("eshgam chi ro mikhy avaz koni: ").lower()
            if changable_attr == "id":
                answer = input("dada chi migi , id avaz nemishe, mikhay edame bedi(Y/N)").lower()
               
                if answer == "y":
                        self.update_train()
            
                elif answer == "n":
                        self.employer_panel()
            
                else:
                    print("eshtebah kardi az aval shro kon!")
                    self.employer_panel()   
               
            new_value = input(f"{changable_attr} be chi taghir bedam: ")
            updated_data = self.db.update_data( "trains", id ,changable_attr, new_value)
            
            if updated_data:
                print("train update shod horraa!")
                print(updated_data)
                self.employer_panel()
            
            else:
               
                answer = input("update ba khata movajeh shod, mikhay edame bedi(Y/N)").lower()
               
                if answer == "y":
                    self.update_train()
            
                elif answer == "n":
                    self.employer_panel()
            
                else:
                    print("eshtebah kardi az aval shro kon!")
                    self.employer_panel()     
        else:
            answer = input("hamchin id nist, mikhay edame bedi(Y/N)").lower()
               
            if answer == "y":
                self.update_train()
            
            elif answer == "n":
                self.employer_panel()
            
            else:
                print("eshtebah kardi az aval shro kon!")
                self.employer_panel()   

    def delete_train(self):
        id = input("chiro mikhay hazf kon? ")
        check = self.db.remove_data("trains",id)

        if check:
            print("heyyyy hazf kardiiiddyaa!!!")
            self.employer_panel()
        
        else:
            print("donbal chi hasti dada! hamchin chizi nist")
            
            again = input("dost dari ey bar dighe emtahan koni?(Y/N)").lower()

            if again == "y":
                self.delete_train()
            
            elif again == "n":
                self.employer_panel()
            
            else:
                print("eshtebah kardi az aval shro kon!")
                self.employer_panel()

    def show_trains(self):
        trains = self.db.read_all_data("trains")

        if len(trains) == 0 :
            print("listet khaliye baba")

        else:
            for train in trains:
                print("---------------")
                print(train)  
                
    #Passenger
    
    def passenger_panel(self):
        while True:
            print("\nPassenger Panel")
            print("1. Register")
            print("2. Login")
            print("3. Back")

            i = input("Mikhay koja beri? ")

            if i == "1":
                self.register_passenger()
            elif i == "2":
                self.register_passenger()
            elif i == "3":
                self.start()
            else:
                print("Dadash dari eshtebah mizani")
                         
    def passenger_login_panel(self):
        print("\nPassenger Login")
        username = input("Username: ")
        password = input("Password: ")

        if self.auth.login(username, password, "passenger"):
            print("Login successful")
            pass
        else:
            print("Username or password is wrong")

    def register_passenger(self):
        print("\nPassenger Register")
        username = input("Username: ")

        old_passenger = self.db.read("passengers", username)
        if old_passenger:
            print("This username already exists")
            return

        password = input("Password: ")
        name = input("Name: ")
        email = input("Email: ")

        passenger = Passenger(username, password, name, email)

        self.auth.rigester(passenger)
        self.db.create_DI(passenger, "passengers")

        print("Passenger registered")
    
    def passenger_dashboard(self):
        while True:
            print("\nPassenger Dashboard")
            print("1. But Ticket")
            print("2. Update Profile")
            print("4. Back")

            i = input("Mikhay koja beri? ")

            if i == "1":
                pass
            elif i == "2":
                pass
            elif i == "3":
                return
            else:
                print("Dadash dari eshtebah mizani")
