class Card:

    def __init__(self,card, exp_month, exp_year, password, cvv2, ):
        self.card = card
        self.exp_month = exp_month
        self.exp_year = exp_year
        self.password = password
        self.cvv2 = cvv2


    def __str__(self):
        return (f"--- card-info ---\n"
                f"card = {self.card}\n"
                f"exp_month = {self.exp_month}\n"
                f"exp_year = {self.exp_year}\n"
                f"cvv2 = {self.cvv2}\n"
                ) 
