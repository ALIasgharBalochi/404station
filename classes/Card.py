class Card:

    def __init__(self,card, exp_month, exp_year, password, cvv2, ):
        self.card = card
        self.exp_month = exp_month
        self.exp_year = exp_year
        self.password = password
        self.cvv2 = cvv2


    def __str__(self):
        return (f"______card-info________"
                f"card = {self.card}"
                f"exp_month = {self.exp_month}"
                f"exp_year = {self.exp_year}"
                f"cvv2 = {self.cvv2}"
                ) 
