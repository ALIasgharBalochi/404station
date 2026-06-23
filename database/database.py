#changin match to map
# keys = {
#     "admins": "username",
#     "passengers": "username",
#     "employers": "username",
#     "trains": "id",
#     "lines": "name",
# }


class DataBase:
    #every array saves a instance of an class
    def __init__(self):
        self.admins = []
        self.employers = []
        self.passengers = []
        self.trains = []
        self.lines = []
        self.tickets = []

    #create a data instance
    def create_DI(self,instance,arrayname):
        #specifying the obj with its name with a variable
        if hasattr(self, arrayname):
            array = getattr(self, arrayname)
            array.append(instance)
            return True
        return False

    #here its return a list of info
    def read_all_data(self, arrayname):
        return getattr(self,arrayname)
    
    def read(self, arrayname, pointer):
        key = "username"
        array = getattr(self, arrayname)
        match arrayname:
            case "trains":
                key ="id"
            case "lines":
                 key = "name"
        
        for i in array:
            if getattr(i, key) == pointer:
                return i
        return False
                 
        
        
    #here we update the desired info    
    def update_data(self, arrayname, pointer ,attr, new_value): 
        array = getattr(self,arrayname)

        key = "username"
        
        match arrayname:
            case "trains":
                key ="id"
            case "lines":
                key = "name"
        #itrating in our array and looking for the attribute to change and upd––– the value of the new attribute(with Error handling)
        try:
            for i in array:
                if getattr(i,key) == pointer:
                    setattr(i, attr, new_value)  # output of setatter is None
                    return i
            return False
            



        except AttributeError :
            return False    
            
                





    
    def remove_data(self, arrayname:str , pointer):
        #here we specify that the array we looking for exsits
        if hasattr(self,arrayname):
           
            key = "username"
        
            match arrayname:
                case "trains":
                    key ="id"
                case "lines":
                    key = "name"
            # here we looking for an attr in our desired array   
            array = getattr(self,arrayname)
            for i in array:
                if getattr(i, key) == pointer:
                    array.remove(i)
                    return True
            return False       
        else:
            return False
             
        
        