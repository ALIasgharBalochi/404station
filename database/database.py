class DataBace:
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
        array = getattr(self,arrayname)
        array.append(instance)

    #here its return a list of info
    def read_all_data(self, arrayname):
        return getattr(self,arrayname)
    
    def read(self):
        pass
        
    #here we update the desired info    
    def update_data(self, arrayname, pointer ,attr, new_value): 
        array = getattr(self,arrayname,)

        key = "username"
        
        match arrayname:
            case "trains":
                key ="id"
            case "lines":
                key = "name"
        #itrating in our array and looking for the attribute to change and upd––– the value of the new attribute(with Error handling)
        try:
            for i in array:
                if i.key == pointer:
                    i.attr = new_value


        except AttributeError :
            pass            
            
                





    
    def remove_data(self, arrayname:str , attr):
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
                if i.key == attr:
                    array.remove(i)
                    return True
            return False       
        else:
            return False
             
        
        