from classes.line import Line
from classes.train import Train
from utilitys import backButton    


class EmployerPanel:
    def __init__(self, db, auth):
        self.db = db
        self.auth = auth

    def employer_login_panel(self):
        
        attempts = 1
        
        while attempts < 4 :
            print(f"\n--- Employer Login (Attempt {attempts}/3) ---")


            username = input("username: ").strip()
            if username.lower() == 'exit':
                    return
            password = input("password: ").strip()
            if username.lower() == 'exit':
                    return
                        

            login = self.auth.login(username, password, "employer")
            if login["status"]:
                print(login["message"])
                self.employer_panel()
                return
                
            else:
                print(login["message"])

                attempts += 1
                print(f"Eshtebah shod! {4 - attempts}attempts left.")
                    
                
        print("\n Access Denied! soookhtiiii heheheheheh")
        return
    
    
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

            

            i = input("Mikhay Koja Beri? ").strip()

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
                return
            else:
                print("Dari Eshatebah Mizani Dadash")


    def add_line(self):

        line_name   = input("Line Name: ").strip()

        check_name = self.db.read("lines",line_name)
        
        #here it checks that the line_name is not duplicate
        if check_name:
            
            print("ye chi dige bezan in esm tekrariye")
            self.add_line()
        

        origin      = input("origin: ").strip()
        destination = input("destination: ").strip()
        station     = input("station: (E.X: khatib zade,Asadi,shahrabi,maneyjer jan <3) ").split(sep=",")
        station.insert(0,origin)
        station.append(destination)
        station_count = len(station)
        
        if backButton.back("dost dari hmin bashe?(Y/N)"):

            result = self.db.create_DI(Line(line_name,origin,destination,station,station_count),"lines")

            if result:
                print("Line dorst shod hooraa!!")
                self.employer_panel() 
            
            else:
                print("moshkely pish omad dobare talash kon") 
                self.employer_panel()   
        else:
            if backButton.back("dost dari dobare bezani? (Y/n) "):
                self.add_line()
            else:
                return  


    def update_line(self):
        Name = input("esm khati ke mikhay update koni chie? ").strip()
        check = self.db.read("lines",Name)

        if check:

            print(check)

            # changable_attr = input("eshgam chi ro mikhy avaz koni: ").lower().strip()
            # new_value = input(f"{changable_attr} be chi taghir bedam: ").strip()

            # if backButton.back("motmaeniiiiiii? (Y/N)"):

            changable_attr = input("eshgam chi ro mikhy avaz koni: ").lower()
                
                #if user want to change the station we change the input format
            if changable_attr == "station":
                new_value = input("station: (E.X: khatib zade,Asadi,shahrabi,maneyjer jan <3) ").split(sep=",")
            else:
                new_value = input(f"{changable_attr} be chi taghir bedam: ")

            if backButton.back("motmaeniiiiiii? (Y/N)"):
                updated_data = self.db.update_data( "lines", Name ,changable_attr, new_value)
                
                if updated_data:

                    #if uesr want change the station we updated the station count
                    if changable_attr == "station":
                        self.db.update_data("lines",Name,"station_count",len(new_value))

                    print("khatet update shod horraa!")
                    print(updated_data)
            
                else:
                
                    answer = input("update ba khata movajeh shod, mikhay edame bedi(Y/N)").lower()
                
                    if answer == "y":
                        self.update_line()
                
                    elif answer == "n":
                        self.employer_panel()
                
                    else:
                    
                        answer = input("update ba khata movajeh shod, mikhay edame bedi(Y/N)").lower().strip()
                    
                        if answer == "y":
                            self.update_line()
                    
                        elif answer == "n":
                            self.employer_panel()
                    
                        else:
                            print("eshtebah kardi az aval shro kon!")
                            self.employer_panel()   
            else:
                if backButton.back("dost dari dobare bezani? (Y/n) "):
                    self.update_line()
                else:
                    self.employer_panel()              

        else:
            answer = input("hamchin khati nist, mikhay edame bedi(Y/N)").lower().strip()
               
            if answer == "y":
                self.update_line()
            
            elif answer == "n":
                self.employer_panel()
            
            else:
                print("eshtebah kardi az aval shro kon!")
                self.employer_panel()     

            
    def delete_line(self):
        Name = input("chiro mikhay hazf kon? ").strip()
        check = self.db.remove_data("lines",Name)

        if check:

            if backButton.back("dada dari hazfesh mikoni, motmaeni? (Y/N)"):

                print("heyyyy hazf kardiiiddyaa!!!")
                self.employer_panel()
            else:
                if backButton.back("dost dari dobare hazf koni? (Y/n) "):
                    self.delete_line()
                else:
                    self.employer_panel()      
        
        else:
            print("donbal chi hasti dada! hamchin chizi nist")
            
            again = input("dost dari ey bar dighe emtahan koni?(Y/N)").lower().strip()

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

        # name = input("name: ").strip()
        # line = input("line: ").strip()
        # avarage_speed = input("avarage_speed: ").strip()
        # quality = input("quality: ").strip()
        # ticket_cost = input("ticket_cost: ").strip()
        # capacity = input("capacity: ").strip()

       
        try:
            
            print("\n--- Adding New Train ---")
            
            name = input("name: ")

            #get all lines
            lines = self.db.read_all_data("lines") 

            #check we have any line or not 
            if len(lines) < 1:
                print("lotfan aval line ra besazid! ")
                self.employer_panel()

            a = [_line.name for _line in lines]
            print(f"existed lines: ",a)
            line = input("line: ")

            if line not in a:
                flag = True
                #We will keep the user logged in until they enter the correct value or exit completely.
                while flag:
                    print("the line is not exist please chose from existed line")
                    choise = input("mikhay edame bedi? (Y,N): ").lower()
                    if choise == 'y':
                        a = [_line.name for _line in lines]
                        print(f"existed lines: ",a)
                        line = input("line: ")
                        if line in a:
                            flag = False
                    elif choise == 'n':
                        flag = False
                        self.employer_panel()

            avarage_speed = float(input("avarage_speed: "))
            quality = input("quality: ")
            ticket_cost = float(input("ticket_cost: "))
            capacity = int(input("capacity: "))

            if backButton.back("dost dari ina ezafe she? (Y/N)"):

                result = self.db.create_DI(Train(name,line,avarage_speed,quality,ticket_cost,capacity),"trains")

                if result:
                    print("train dorst shod hooraa!!")
                    self.employer_panel() 
                
                else:
                    print("moshkely pish omad dobare talash kon") 
                    self.employer_panel() 
            else:
                if backButton.back("dost dari dobare bezani? (Y/n) "):
                    self.add_train()
                else:
                    self.employer_panel()          
                    
            
                # else:
                #     print("moshkely pish omad dobare talash kon") 
                #     #self.employer_panel() 
                
        except ValueError as e :
            print(f" Error dar vorodiha: {e}")
            
        except Exception as   e:
            print(f" Error gheire montazere: {e}")
            
        return       
        

    def update_train(self):
        id = input("Id train ke mikhay update koni chie? ").strip()
        check = self.db.read("trains",id)

        if check:
            print("---------------")
            print(check)

            changable_attr = input("eshgam chi ro mikhy avaz koni: ").lower().strip()
            if changable_attr == "id":
                answer = input("dada chi migi , id avaz nemishe, mikhay edame bedi(Y/N)").lower().strip()
               
                if answer == "y":
                        self.update_train()
            
                elif answer == "n":
                        self.employer_panel()
            
                else:
                    print("eshtebah kardi az aval shro kon!")
                    self.employer_panel()   
            #check if user chose change line we show ghe existed line
            if changable_attr == "line":
                lines = self.db.read_all_data("lines") 

                #check we have any line or not 
                if len(lines) < 1:
                    print("lotfan aval line ra besazid! ")
                    self.employer_panel()

                a = [_line.name for _line in lines]
                print(f"existed lines: ",a)

            new_value = input(f"{changable_attr} be chi taghir bedam: ")
            
            #checke if user choise line to change and the her choise is not in existed line print message and get the value again
            if changable_attr == "line" and new_value not in a:
                flag = True
                #We will keep the user logged in until they enter the correct value or exit completely.
                while flag:
                    print("please choise line in existed line . ")
                    choise = input("mikhay edame bedi? (Y,N): ").lower()
                    if choise == 'y':
                        lines = self.db.read_all_data("lines") 
                        a = [_line.name for _line in lines]
                        print(f"existed lines: ",a)
                        new_value = input(f"{changable_attr} be chi taghir bedam: ")
                        if new_value in a:
                            flag = False
                    elif choise == 'n':
                        flag = False
                        self.employer_panel()

            if backButton.back("dost dari ina ezafe she? (Y/N)"):            

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
                        self.employer_panel()
                   
            else:
                if backButton.back("dost dari dobare bezani? (Y/n) "):
                    self.update_train()
                else:
                    self.employer_panel()  

        else:
            answer = input("hamchin id nist, mikhay edame bedi(Y/N)").lower().strip()
               
            if answer == "y":
                self.update_train()
            
            elif answer == "n":
                self.employer_panel()
            
            else:
                print("eshtebah kardi az aval shro kon!")
                self.employer_panel()   

    def delete_train(self):
        id = input("chiro mikhay hazf kon? ").strip()
        check = self.db.remove_data("trains",id)

        if check:
            if backButton.back("motmaenii? (Y/N)"):

                print("heyyyy hazf kardiiiddyaa!!!")
                self.employer_panel()

            else:
                if backButton.back("dost dari dobare bezani? (Y/n) "):
                    self.delete_train()
                else:
                    self.employer_panel()      
        
        else:
            print("donbal chi hasti dada! hamchin chizi nist")
            
            again = input("dost dari ey bar dighe emtahan koni?(Y/N)").lower().strip()

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