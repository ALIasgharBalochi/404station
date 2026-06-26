from classes.Card import Card
from BANK import API

class PaymentService:
    def __init__(self) -> None:
        self.bank = API()
    
    def show_my_cards(self, passenger):
        print("\nMy Cards")
        if not passenger.cards:
            print("No saved cards yet")
            return
        for index, saved_card in enumerate(passenger.cards, start=1):
            print(f"{index}. {saved_card}")
    
    def _read_amount(self):
        try:
            amount = int(input("amount: ").strip())
            if amount <= 0:
                print("amount not be 0 ")
                return None
            return amount
        except ValueError:
            ("amount not valid")
            return None
         
    def _read_new_card(self):
        try:
            card_number = input("Card Number: ").strip()
            exp_month = int(input("Exp Month: ").strip())
            exp_year = int(input("Exp Year: ").strip())
            password = input("Password: ").strip()
            cvv2 = input("CVV2: ").strip()
            
            
            return Card(card_number, exp_month, exp_year, password, cvv2)
        except ValueError:
            print("invalid card")
            return None
        
        
    def _get_card_for_payment(self, passenger):
        if passenger.cards:
            print("1. use saved card")
            print("2. add new card")
            choice = input("choose: ").strip()
            
            if choice == "1":
                return self._choose_saved_Card(passenger), False
            if choice == "2":
                return self._read_new_card(), True
            
            print("invalid choice")
            return None, False
        return self._read_new_card(), True
        
    def _choose_saved_Card(self, passenger):
        if not passenger.cards:
            print("you dont have any card")
            return None
        self.show_my_cards(passenger)
        
        try:
            choice = int(input("choose card number: ").strip())
            if 1 <= choice <= len(passenger.cards):
                return passenger.cards[choice -1]
        except ValueError:
            pass
        print("invalid card choice")
        return None
    
    def charge_wallet(self, passenger):
        print("\nCharge Walllet")
        amount = self._read_amount()
        if amount is None:
            return False
        
        selected_card, should_save = self._get_card_for_payment(passenger)
        if selected_card is None:
            return False
        
        try:
            payment_id = self.bank.pay(
                selected_card.card,
                selected_card.exp_month,
                selected_card.exp_year,
                selected_card.password,
                selected_card.cvv2,
                amount
            )
            passenger.wallet += amount
            if should_save:
                passenger.cards.append(selected_card)
            print("wallet charged succesfully")
            print("payment ID:", payment_id)
            return True
        except ValueError as error:
            print("payment failed:", error)
            return False
            
    def pay_from_wallet(self,amount,passenger):
        if passenger.wallet < amount:
            print("your balance is not enough")
            return False 
        passenger.wallet -= amount
    
        
    def show_wallet_balance(self, passenger):
        print("\nWallet Balance")
        print(f"your walllet amount is {passenger.wallet}")
    
    def show_my_card(self, passenger):
        return passenger.cards
        
    
         
            
            
