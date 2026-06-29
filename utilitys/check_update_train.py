from utilitys.cli import CLI
def check_update_Train(chang_attr,new_valiue):

    match chang_attr:
        case "avarage_speed":
            if int(new_valiue) < 0 :
                CLI.error("avarage_Speed cannot be negative!")
                return False
        case "ticket_cost":
            if int(new_valiue) < 0 :
                CLI.error("ticket_cost cannot be negative!")
                return False
        case "quality":
            if int(new_valiue) < 0 :
                CLI.error("quality cannot be negative!") 
                return False
        case "capacity":
            if int(new_valiue)< 0:
                CLI.error("capacity cannot be negative!")
                return False
        case "stop_time":
            if not int(new_valiue).isnumeric():
                CLI.error("dadashe man stop time bayad yek adad bashad faghat masalan: 5)!")
                return False
        case "distance_to_station":
            if not int(new_valiue).isnumeric():
                CLI.error("dadashe man fasele ta istgah bayad yek adad bashad faghat masalan: 20)!")
                return False
        case "time_to_move":
            check_format = new_valiue.split(":")

            if len(check_format) == 2:
                if check_format[0].isnumeric() and check_format[1].isnumeric():
                    pass
                else:
                    CLI.error("format saat eshtehah ast")
                    return False
            else:
                CLI.error("format saat eshtehah ast")
                return False
    return True
