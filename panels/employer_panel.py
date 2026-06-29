from classes.line import Line
from classes.train import Train
from utilitys.cli import CLI   
from utilitys import backButton,iscolision   


class EmployerPanel:
    def __init__(self, db, auth):
        self.db = db
        self.auth = auth

    def employer_login_panel(self):
        attempts = 1
        while attempts < 4 :
            CLI.title(f"\n--- Employer Login (Attempt {attempts}/3) ---")


            username = input("username: ").strip()
            if username.lower() == 'exit':
                    return
            password = input("password: ").strip()
            if username.lower() == 'exit':
                    return
                        

            login = self.auth.login(username, password, "employer")
            if login["status"]:
                CLI.success(login["message"])
                self.employer_panel()
                return
                
            else:
                CLI.error(login["message"])

                attempts += 1
                CLI.warning(f"\nEshtebah shod! {4 - attempts}attempts left.")
                    
                
        CLI.error("\n Access Denied! soookhtiiii heheheheheh")
        return
    
    
    def employer_panel(self):
        while True:
            CLI.title("\n--- Panel employer ---")
            CLI.info("1. Add Line")
            CLI.info("2. Update Line")
            CLI.info("3. Delete Line")
            CLI.info("4. Show Line")
            CLI.info("5. Add Train")
            CLI.info("6. Update Train")
            CLI.info("7. Delete Train")
            CLI.info("8. Show Train")
            CLI.info("9. Sign Out")

            

            i = input("\nMikhay Koja Beri? ").strip()

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
                CLI.error("\nDari Eshatebah Mizani Dadash")


    def add_line(self):
        CLI.title("\n--- Add Line ---")

        line_name   = input("Line Name: ").strip()

        check_name = self.db.read("lines",line_name)
        
        #here it checks that the line_name is not duplicate
        if check_name:
            
            CLI.warning("\nye chi dige bezan in esm tekrariye")
            self.add_line()
        

        origin      = input("origin: ").strip()
        destination = input("destination: ").strip()
        station     = input("station: (E.X: khatib zade,Asadi,shahrabi,maneyjer jan <3) ").split(sep=",")
        station.insert(0,origin)
        station.append(destination)
        station_count = len(station)
        
        if backButton.back("\ndost dari hmin bashe?(Y/N)"):

            result = self.db.create_DI(Line(line_name,origin,destination,station,station_count),"lines")

            if result:
                CLI.success("\nLine dorst shod hooraa!!")
                return
            
            else:
                CLI.error("\nmoshkely pish omad dobare talash kon") 
                return   
        else:
            return


    def update_line(self):
        CLI.title("\n--- Update Line ---")
        Name = input("\nesm khati ke mikhay update koni chie? ").strip()
        check = self.db.read("lines",Name)

        if check:

            CLI.info(str(check))

            # changable_attr = input("eshgam chi ro mikhy avaz koni: ").lower().strip()
            # new_value = input(f"{changable_attr} be chi taghir bedam: ").strip()

            # if backButton.back("motmaeniiiiiii? (Y/N)"):

            changable_attr = input("\neshgam chi ro mikhy avaz koni: ").lower()
                
                #if user want to change the station we change the input format
            if changable_attr == "station":
                new_value = input("\nstation: (E.X: khatib zade,Asadi,shahrabi,maneyjer jan <3) ").split(sep=",")
            else:
                new_value = input(f"\n{changable_attr} be chi taghir bedam: ")

            if backButton.back("\nmotmaeniiiiiii? (Y/N)"):
                updated_data = self.db.update_data( "lines", Name ,changable_attr, new_value)
                
                if updated_data:

                    #if uesr want change the station we updated the station count
                    if changable_attr == "station":
                        self.db.update_data("lines",Name,"station_count",len(new_value))
                    
                    #if user change the destination or origin we updated the station list 
                    if changable_attr == "destination" or changable_attr == "origin":
                        if changable_attr == "origin":
                            line = self.db.read("lines",Name)
                            stations = line.station
                            stations[0] = new_value 
                            self.db.update_data("lines",Name,"station",stations)
                        else:
                            line = self.db.read("lines",Name)
                            stations = line.station
                            stations[-1] = new_value 
                            self.db.update_data("lines",Name,"station",stations)
                    
                    CLI.success("\nkhatet update shod horraa!")
                    print(updated_data)
                    return
            
                else:

                        answer = input("\nupdate ba khata movajeh shod, mikhay edame bedi(Y/N)").lower().strip()
                    
                        if answer == "y":
                            return
                    
                        elif answer == "n":
                            return
                    
                        else:
                            CLI.error("\neshtebah kardi az aval shro kon!")
                            return   
            else:
                return             

            
    def delete_line(self):
        CLI.title("\n--- Delete Line ---")
        Name = input("\nchiro mikhay hazf kon? ").strip()
        check = self.db.remove_data("lines",Name)

        if check:

            if backButton.back("\ndada dari hazfesh mikoni, motmaeni? (Y/N)"):

                
                removed = self.db.remove_data("lines",Name)
                if removed:
                    CLI.success("\nheyyyy hazf kardiiiddyaa!!!")
                    return
                else:
                    CLI.error("\nhasf kardan khat ba khata movajeh shod!")
                    return
            else:
                return      
        
        else:
            CLI.warning("donbal chi hasti dada! hamchin chizi nist")
            
            again = input("\ndost dari ey bar dighe emtahan koni?(Y/N)").lower().strip()

            if again == "y":
                return
            
            elif again == "n":
                return
            
            else:
                CLI.error("\neshtebah kardi az aval shro kon!")
                return         

    def show_lines(self):
        CLI.title("\n--- Show Line ---")

        lines = self.db.read_all_data("lines")

        if len(lines) == 0 :
            CLI.warning("\nlistet khaliye baba")

        else:
            for line in lines:
                CLI.info("---------------")
                CLI.info(str(line))
    

    def add_train(self):

        try:
            
            CLI.title("\n--- Adding New Train ---")
            
            name = input("name: ")

            #get all lines
            lines = self.db.read_all_data("lines") 

            #check we have any line or not 
            if len(lines) < 1:
                CLI.warning("lotfan aval line ra besazid! ")
                return

            a = [_line.name for _line in lines]
            CLI.info(f"existed lines: {a}")

            line = input("line: ")

            if line not in a:
                flag = True
                #We will keep the user logged in until they enter the correct value or exit completely.
                while flag:
                    CLI.title("\nthe line is not exist please chose from existed line")
                    choise = input("\nmikhay edame bedi? (Y,N): ").lower()
                    if choise == 'y':
                        a = [_line.name for _line in lines]
                        CLI.info(f"existed lines: {a}")
                        line = input("line: ")
                        if line in a:
                            flag = False
                    elif choise == 'n':
                        flag = False
                        return

            avarage_speed = float(input("avarage_speed: "))
            quality = input("quality: ")
            ticket_cost = float(input("ticket_cost: "))
            capacity = int(input("capacity: "))
            
            stop_time = input("stop in station (5): ")

            time_to_move = input("saat harekat ghatar(10:30): ")
            check_format = time_to_move.split(":")

            if len(check_format) == 2:
                if check_format[0].isnumeric() and check_format[1].isnumeric():
                    pass
                else:
                    print("format saat eshtehah ast")
                    return
            else:
                print("format saat eshtehah ast")
                return

            distance_to_station = input("fasele ta istgah(20): ")

            if backButton.back("dost dari ina ezafe she? (Y/N)"):
                train = Train(name, line, avarage_speed, quality, ticket_cost, capacity, stop_time,time_to_move,distance_to_station)

                colision = iscolision.isColision(db=self.db,new_train=train)
                if colision:
                    print("in ghatar ba in moshakhasat namitavanad roy in khat harekat konad baes barkhord ba ghatar digari mishavad")
                    return
                result = self.db.create_DI(
                    train,
                    "trains"
                )

                if result:
                    CLI.success("\ntrain dorst shod hooraa!!")
                    return 
                
                else:
                    CLI.error("\nmoshkely pish omad dobare talash kon") 
                    return 
            else:
                return         
                    
            
                # else:
                #     print("moshkely pish omad dobare talash kon") 
                #     #self.employer_panel() 
                
        except ValueError as e :
            CLI.error(f"\nError dar vorodiha: {e}")
            
        except Exception as   e:
            CLI.error(f"\nError gheire montazere: {e}")
            
        return       
        

    def update_train(self):
        CLI.title("\n--- Update Train ---")
        id = input("Id train ke mikhay update koni chie? ").strip()
        check = self.db.read("trains",id)

        if check:
            CLI.info("---------------")
            CLI.info(str(check))


            changable_attr = input("\neshgam chi ro mikhy avaz koni: ").lower().strip()
            if changable_attr == "id":
                answer = input("\ndada chi migi , id avaz nemishe, mikhay edame bedi(Y/N)").lower().strip()
               
                if answer == "y":
                        return
            
                elif answer == "n":
                        return
            
                else:
                    CLI.error("\neshtebah kardi az aval shro kon!")
                    return   
            #check if user chose change line we show ghe existed line
            if changable_attr == "line":
                lines = self.db.read_all_data("lines") 

                #check we have any line or not 
                if len(lines) < 1:
                    CLI.warning("\nlotfan aval line ra besazid! ")
                    return

                a = [_line.name for _line in lines]
                print(f"\nexisted lines: ",a)

            new_value = input(f"{changable_attr} be chi taghir bedam: ")
            
            #checke if user choise line to change and the her choise is not in existed line print message and get the value again
            if changable_attr == "line" and new_value not in a:
                flag = True
                #We will keep the user logged in until they enter the correct value or exit completely.
                while flag:
                    CLI.warning("please choose a line from existed lines.")
                    choise = input("\nmikhay edame bedi? (Y,N): ").lower()
                    if choise == 'y':
                        lines = self.db.read_all_data("lines") 
                        a = [_line.name for _line in lines]
                        print(f"\nexisted lines: ",a)
                        new_value = input(f"\n{changable_attr} be chi taghir bedam: ")
                        if new_value in a:
                            flag = False
                    elif choise == 'n':
                        flag = False
                        return

            if backButton.back("\ndost dari ina ezafe she? (Y/N)"):            

                updated_data = self.db.update_data( "trains", id ,changable_attr, new_value)
                
                if updated_data:
                    CLI.success("\ntrain update shod horraa!")
                    print(updated_data)
                    return
                
                else:
                
                    CLI.error("\nupdate ba khata movajeh shod, dobare bezan marddd!!!")
                    return
                   
            else:
                return 

        else:
            answer = input("\nhamchin id nist, mikhay edame bedi(Y/N)").lower().strip()
               
            if answer == "y":
                return
            
            elif answer == "n":
                return
            
            else:
                CLI.error("\neshtebah kardi az aval shro kon!")
                return   


    def delete_train(self):
        try:
            CLI.title("\n--- Delete Train ---")

            trains = self.db.read_all_data("trains")
            if not trains:
                CLI.warning("list khaliye baba!!!!!")
                return
            
            for train in trains:
                CLI.info(str(train))
            
            id = input("chiro mikhay hazf kon? ").strip()
            check = self.db.read("trains",id)

            if check:
                if backButton.back("motmaenii? (Y/N)"):
                    remove_data = self.db.remove_data("trains",id)
                    if remove_data :
                        CLI.success("heyyyy hazf kardiiiddyaa!!!")
                        return
                    else:
                        CLI.error("error khordi khob")
                        self.employer_panel()      
            
            else:
                CLI.warning("\ndonbal chi hasti dada! hamchin chizi nist")
                
                again = input("\ndost dari ey bar dighe emtahan koni?(Y/N)").lower().strip()

                if again == "y":
                    return
                
                elif again == "n":
                    return
                
                else:
                    CLI.error("\neshtebah kardi az aval shro kon!")
                    CLI.error("hazf kardan ba khata movajeh shod")
                    # print("train dorst shod hooraa!!")
                    return
                    # else:
                    #     print("moshkely pish omad dobare talash kon") 

                # else:
                #     if backButton.back("dost dari dobare bezani? (Y/n) "):
                #         self.add_train()
                #     else:
                #         return          
                
        except ValueError as e :
            print(f" Error dar vorodiha: {e}")
        
        except Exception as e:
            print(f" Error gheire montazere: {e}")
        
        return

            
    def show_trains(self):
        CLI.title("\n--- Show Train ---")
        trains = self.db.read_all_data("trains")

        if len(trains) == 0 :
            CLI.warning("\nlistet khaliye baba")

        else:
            for train in trains:
                CLI.info("---------------")
                CLI.info(str(train))

