from datetime import datetime
import uuid




class Ticket:
    def __init__(self, username, train_name,origin, destination, ticket_cost, amount,):
        self.id = self.generate_id()
        self.username = self.validate_string(username, "Username")
        self.train_name = self.validate_string(train_name, "Train name")
        self.origin = self.validate_string(origin, "Origin")
        self.destination = self.validate_string(destination, "Destination")
        self.ticket_cost = self.validate_positive(ticket_cost, "Ticket post") 
        self.amount = self.validate_positive(amount, "Amout",  allow_zero=False) 
        self.total_price = amount * ticket_cost
        self.time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        
        
    def generate_id(self):
        """Generate a short 4-character unique ticket ID."""
        return str(uuid.uuid4())[0:4].upper()
    
    def validate_string(self, value, field_name):
        """
        Validate that the given value is a non-empty string.

        Args:
            value: The value to validate.
            field_name: Name of the field for error messages.

        Returns:
            A cleaned string without leading/trailing spaces.
        """
        
        if not isinstance(value, str):
            raise TypeError(f"{field_name} must be a string!")
        value = value.strip()  
        if not value:
            raise ValueError(f"{field_name} cannot be empty!")
        return value
    
    def validate_positive(self, value, field_name, allow_zero=False):
        if isinstance(value, bool):
            raise TypeError(f"{field_name} must be a number, not bool!")
        if not isinstance(value, (int, float)):
            raise TypeError(f"{field_name} must be a number!")
        
        value = float(value)
        
        if allow_zero:
            if value < 0:
                raise ValueError(f"{field_name} cannot be negative!")
        else:
            if value <= 0:
                raise ValueError(f"{field_name} must be positive!")
        return value
    
        
        
    #def info_save(self):
        #pass

        
