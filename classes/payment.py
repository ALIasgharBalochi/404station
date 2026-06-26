from classes.Card import Card
from BANK import API
from classes.user import Passenger
from classes.Wallet import Wallet

class PaymentService:
    def __init__(self) -> None:
        self.bank = API()
        
    def charge_wallet(self, passenger):
        print("\nCharge Walllet")
        
        try:
            amount = int(input("Cheghadr charge mikhaye?"))
            
            if amount <= 0:
                print("mablagh vared shode bayad bishtar az 0 bashad")
                return
        
            card_number = input("shomare cartet chande?").strip()
            exp_month = int(input("mahe enghezaye kartet chiye?").strip())
            exp_year = int(input("sale enghezaye kartet chiye?").strip())
            password = int(input("password kartet chiye?").strip())
            cvv2 = int(input("cvv2 enghezaye kartet chiye?").strip())
            
            payment = self.bank.pay(card_number, exp_month, exp_year, password, cvv2, amount)

            passenger.wallet += amount

            print("wallet charged succesfully")
            print("payment ID:", payment)
        
        except ValueError as error:
            print("payment failed:", error)
    
    def pay_from_wallet(self,amount,passenger):
        if passenger.wallet < amount:
            print("your balance is not enough")
            return False 
        passenger.wallet -= amount


    def show_wallet_balance(self, passenger):
        print("\nWallet Balance")
        print(f"your walllet amount is {passenger.wallet}")
        
    
         
            
            
