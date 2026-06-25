from classes.user import Passenger
from utilitys import backButton


class PassengerPanel:
    def __init__(self, database, authentication):
        self.db = database
        self.auth = authentication      

    def passenger_panel(self):
        while True:
            print("\nPassenger Panel")
            print("1. Register")
            print("2. Login")
            print("3. Back")

            i = input("Mikhay koja beri? ").strip()

            if i == "1":
                self.register_passenger()
            elif i == "2":
                self.register_passenger()
            elif i == "3":
                self.start()
            else:
                print("Dadash dari eshtebah mizani")
                         
    def passenger_login_panel(self):
        attempts = 1
        while attempts < 4: 
            print(f"\n--- Passenger Login (Attempt {attempts}/3) ---")
            
            username = input("Username: ").strip()
            if username.lower() == 'exit':
                return
            password = input("Password: ").strip()
            if username.lower() == 'exit':
                return
            
            passenger_auth = self.auth.login(username, password, "passenger")
            if passenger_auth["status"]:
                print(passenger_auth["message"])
                self.passenger_dashboard()
            else:
                print(passenger_auth["message"])
                attempts += 1
                        
        print("Access Denied! Too many failed attempts.")
        return
    
    def register_passenger(self):
        print("\nPassenger Register")
        username = input("Username: ").strip()
        password = input("Password: ").strip()
        name = input("Name: ").strip()
        email = input("Email: ").strip()

        if backButton.back("dost dary hamina ro berizi? (Y/N)"):

            passenger = Passenger(username, password, name, email)
            passenger_auth = self.auth.register(passenger)
            
            if passenger_auth["status"]:
                print(passenger_auth["message"])
                self.passenger_panel()
            else:
                print(passenger_auth["message"])
                return
                
    def passenger_dashboard(self):
        while True:
            print("\n--- Passenger Dashboard ---")
            print("1. But Ticket")
            print("2. Update Profile")
            print("4. Back")

            i = input("Mikhay koja beri? ").strip()

            if i == "1":
                pass
            elif i == "2":
                pass
            elif i == "3":
                payment_service = PaymentService()
                payment_service.charge_wallet(Passenger)                
            elif i == "4":
                return
            else:
                print("Dadash dari eshtebah mizani")
