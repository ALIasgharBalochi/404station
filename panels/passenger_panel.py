from classes.user import Passenger
from classes.payment import PaymentService
from utilitys import backButton, print_file
from classes.ticket import Ticket
from utilitys.checker import check
from utilitys.cli import CLI

from utilitys.remove_file import remove_file
class PassengerPanel:
    def __init__(self, database, authentication):
        self.db = database
        self.auth = authentication      
        self.coocke = {}
    def passenger_panel(self):
        while True:
            CLI.title("\n--- Passenger Panel ---")
            CLI.info("1. Register")
            CLI.info("2. Login")
            CLI.info("3. Back")

            i = input("\nMikhay koja beri? ").strip()

            if i == "1":
                self.register_passenger()
            elif i == "2":
                self.passenger_login_panel()
            elif i == "3":
                return
            else:
                CLI.error("\nDadash dari eshtebah mizani")
                         
    def passenger_login_panel(self):
        attempts = 1
        while attempts < 4: 
            CLI.title(f"\n--- Passenger Login (Attempt {attempts}/3) ---")
            
            username = input("Username: ").strip()
            if username.lower() == 'exit':
                return
            password = input("Password: ").strip()
            if password.lower() == 'exit':
                return
            
            passenger_auth = self.auth.login(username, password, "passenger")
            if passenger_auth["status"]:
                print('')
                CLI.success(passenger_auth["message"])
                self.coocke["username"] = username
                self.passenger_dashboard(passenger_auth["obj"])
                return
            else:
                print("")
                CLI.error(passenger_auth["message"])
                attempts += 1
                        
        CLI.error("\nAccess Denied! Too many failed attempts.")
        return
    
    def register_passenger(self):
        CLI.title("\n--- Passenger Register ---")
        username = input("Username: ").strip()
        password = input("Password: ").strip()
        name = input("Name: ").strip()
        email = input("Email: ").strip()

        if backButton.back("\ndost dary hamina ro berizi? (Y/N)"):

            passenger = Passenger(username, password, name, email)
            passenger_auth = self.auth.register(passenger)
            
            if passenger_auth["status"]:
                CLI.success(passenger_auth["message"])
                return
            else:
                CLI.error(passenger_auth["message"])
                return
                
    def passenger_dashboard(self,passenger):
        while True:
            CLI.title("\n--- Passenger Dashboard ---")
            CLI.info("1. Buy Ticket")
            CLI.info("2. Update Profile")
            CLI.info("3. Wallet / My Cards")
            CLI.info("4. Back")

            i = input("\nMikhay koja beri? ").strip()

            if i == "1":
                self.buy_ticket(passenger)
            elif i == "2":
                self.update_profile(passenger)
            elif i == "3":
                self.wallet_panel(passenger)                
            elif i == "4":
                return
            else:
                CLI.error("\nDadash dari eshtebah mizani")

    def buy_ticket(self,passenger):
        CLI.title("\n--- BUY Panel ---")

        try :

            remove_file("existed_trains.txt")
            remove_file("ticket.txt")
        except Exception as e:
            CLI.error(f"khataa: {e}")
            return

        all_lines = self.db.read_all_data("lines")
        all_trains = self.db.read_all_data("trains")
        
        if len(all_lines) < 1:
            CLI.warning("\nhanoz beliti baray frosh nist hahahahhah :)")
            return

        try:
            for line in all_lines:
                for train in all_trains:
                    if line.name == train.line:
                        is_printed = print_file.save_to_file("existed_trains.txt",destination=line.destination,train_name=train.name,ticket_cost=train.ticket_cost,train_capacity=train.capacity)
            if is_printed:
                CLI.success("\nThe information of all existed trains in the existed_trains.txt file was saved.")
        except Exception as e:
            CLI.error(f"\nkhataaaa!: {e}")
            return

        #check the train name is exist in existed train 
        all_train_names = [train.name for train in all_trains]
        train_name = input("\nesme ghatar mored nazar ra vared kon!: ")
        if not train_name in all_train_names:
            flag = True
            while flag:
                if backButton.back("\nghatar ba in nam vojod nadarad mikhay dobare bezani? (Y/N): "):
                    train_name = input("\nesme ghatar mored nazar ra vared kon!: ")
                    if train_name in all_train_names:
                        flag = False
                else:
                    flag = False
                    return

        #find train name by the input of the user
        train = [train for train in all_trains if train.name == train_name]
        if int(train[0].capacity) < 1:
            CLI.warning(f"\nghatar {train[0].name} zarfiyati nadarad")
            return

        line = self.db.read("lines",train[0].line)

        try:
            count_ticket = int(input("\nche tedad ticket mikhay?: "))
            if int(train[0].capacity) - count_ticket < 0:
                CLI.warning(f"\nghatar {train[0].name} fahgat {train[0].capacity} ta zarfiyat dare")
                flag = True
                while flag:
                    if backButton.back(f"\nghatar {count_ticket} ta zarfiyat nadarad mikhay tedad ro kamtar koni? (Y/N): "):
                        count_ticket = int(input("\nche tedad ticket mikhay?: "))
                        if not int(train[0].capacity) - count_ticket < 0:
                            flag = False
                    else:
                        flag = False
                        return
                
            self.db.update_data("trains",train[0].id,"capacity",int(train[0].capacity)-count_ticket)
            try:

                #impliment payment
                invoice = train[0].ticket_cost * count_ticket
                payment = PaymentService()
                purchase = payment.pay_from_wallet(amount=invoice,passenger=passenger)

                #if payment is failed we return user to the passenger dashboard
                if purchase == False:
                    return

                ticket = Ticket(username=self.coocke["username"],train_name=train[0].name,origin=line.origin,destination=line.destination,ticket_cost=train[0].ticket_cost,amount=count_ticket)
            except Exception as e:
                CLI.error(f"\nkhataaa: {e}")
                return
            
            

            is_printed = print_file.save_to_file("ticket.txt",username=ticket.username,train_name=ticket.train_name,origin=ticket.origin,destination=ticket.destination,ticket_cost=ticket.ticket_cost,count_ticket=ticket.amount,data=ticket.time)
            if is_printed:
                CLI.success("\nyour ticket has successfuly been created")
                self.passenger_dashboard(passenger)
            else:
                CLI.error("\nWe had a problem when creating the ticket.")
                self.passenger_dashboard(passenger)

        except Exception as e:
            CLI.error(f"\nkhataaa: {e}")
            return
        
    def wallet_panel(self,passenger):
        while True:
            CLI.title("\n--- Wallet Dashboard ---")
            CLI.info("1. My Cards")
            CLI.info("2. Charge Wallet")
            CLI.info("3. Balance")
            CLI.info("4. Back")

            i = input("\nkodomo mikhay angam bedi? ").strip()

            payment = PaymentService()

            if i == "1":
                payment.show_my_cards(passenger)
            elif i == "2":
                payment.charge_wallet(passenger)
            elif i == "3":
                payment.show_wallet_balance(passenger)               
            elif i == "4":
                return
            else:
                CLI.error("\nDadash dari eshtebah mizani")

    def update_profile(self,passenger):
        CLI.title("\n--- Update Profile ---")
        CLI.info("this is your current information:")
        CLI.info(str(passenger))
        username = passenger.username
        
        changable_attr = input("\nchi ro mikhay taghir bedi? ").strip()

        if changable_attr != "username":

            new_value = input(f"\n{changable_attr} be chi mikhay taghir bedam: ").strip()

            if changable_attr == "email":

                valid_email = check(password="",email=new_value,options="e")
                
                if not valid_email:
                    CLI.error("\nyour email address is not valid")
                    self.update_profile(passenger)

            if changable_attr == "password":

                valid_password = check(password=new_value,email="",options="p")

                if not valid_password:
                    CLI.error("\nyour password is not valid")
                    self.update_profile(passenger)    



            if backButton.back("\ney mohajer bozorg are you sure ????? (Y/N)"):
                try: 
                    updated_data = self.db.update_data( "passengers", username ,changable_attr, new_value)

                    if updated_data:
                        CLI.success("\ninformation updated!")
                        print(updated_data)
                        return
                    else:
                    
                        answer = CLI.warning("\nuser hamchin chizi nadare, mikhay edame bedi(Y/N)").lower()
                    
                        if answer == "y":
                            self.update_profile(passenger)
                        elif answer == "n":
                            self.passenger_dashboard(passenger)
                        else:
                            answer = CLI.warning("\nupdate ba khata movajeh shod, mikhay edame bedi(Y/N)").lower().strip()
                        
                            if answer == "y":
                                self.update_profile(passenger)
                            elif answer == "n":
                                self.passenger_dashboard(passenger)
                            else:
                                CLI.error("\neshtebah kardi az aval shro kon!")
                                self.passenger_dashboard(passenger)   
                except Exception as e:
                    CLI.error(f"\nkhataaaa: {e}")
                    return  
            else:
                return             
        else:
            answer = input("\nusername is unchangable,mikhay edame bedi? (Y/N)").lower().strip()
            if answer == "y":
                self.update_profile(passenger)
            
            elif answer == "n":
                self.passenger_dashboard(passenger)
            else:
                CLI.error("\neshtebah kardi az aval shro kon!")
                self.passenger_dashboard(passenger)     





