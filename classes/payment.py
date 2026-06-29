from classes.Card import Card
from BANK import API
from utilitys.cli import CLI

class PaymentService:
    def __init__(self) -> None:
        self.bank = API()
    
    def show_my_cards(self, passenger):
        CLI.title("\n--- My Cards ---")
        if not passenger.cards:
            CLI.warning("No saved cards yet")
            return
        for index, saved_card in enumerate(passenger.cards, start=1):
            print(f"{index}. {saved_card}")
    
    def _read_amount(self):
        try:
            amount_str = input("amount: ").strip()
            if not amount_str:
                CLI.warning("\nAmount cannot be empty!")
                return None
            
            amount = int(amount_str)
            
            if amount <= 0:
                CLI.error("\nInvalid amount! Please enter a number greater than 0")
                return None
            
            return amount
        except ValueError:
            CLI.error("Error: Please enter a valid number")
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
            CLI.error("invalid card")
            return None
        
        
    def _get_card_for_payment(self, passenger):
        if passenger.cards:
            CLI.info("\n1. use saved card")
            CLI.info("2. add new card")
            choice = input("\nchoose: ").strip()
            
            if choice == "1":
                return self._choose_saved_Card(passenger), False
            if choice == "2":
                return self._read_new_card(), True
            
            CLI.error("invalid choice")
            return None, False
        return self._read_new_card(), True
        
    def _choose_saved_Card(self, passenger):
        if not passenger.cards:
            CLI.warning("you dont have any card")
            return None
        print(" ")
        self.show_my_cards(passenger)
        
        try:
            print(" ")
            choice = int(input("choose card number: ").strip())
            if 1 <= choice <= len(passenger.cards):
                return passenger.cards[choice -1]
        except ValueError:
            pass
        CLI.error("invalid card choice")
        return None
    
    def charge_wallet(self, passenger):
        CLI.title("\n--- Charge Walllet ---")
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
            CLI.success("wallet charged succesfully")
            print("payment ID:", payment_id)
            return True
        except ValueError as error:
            CLI.error("payment failed:", error)
            return False
            
    def pay_from_wallet(self,amount,passenger):
        if passenger.wallet < amount:
            needed = amount - passenger.wallet
            CLI.warning(f"your balance is not enough then you need {needed} more.")
            return False 
        passenger.wallet -= amount
        CLI.success(f"payment successful! new balance: {passenger.wallet}")
        return True
    
        
    def show_wallet_balance(self, passenger):
        CLI.title("\n--- Wallet Balance ---")
        print(f"your walllet amount is {passenger.wallet}")
    
  
    
         
            
            
