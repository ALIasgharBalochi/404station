class MainPanel:
    def __init__(self, admin_panel, employer_panel, passenger_panel):
        self.admin_panel = admin_panel
        self.employer_panel = employer_panel
        self.passenger_panel = passenger_panel

    def start(self):
        while True:
            print("\nBe 404 Station Khosh Omadi")
            print("1. Admin Panel")
            print("2. Employer")
            print("3. Passenger")
            print("4. Exit")

            choice = input("Mikhay Koja Beri? ")

            if choice == "1":
                self.admin_login_panel()
            elif choice == "2":
                self.employer_login_panel()
            elif choice == "3":
                self.passenger_panel()
            elif choice == "4":
                print("Shab O RoozegaR Khosh")
                exit()
            else:
                print("Dari Eshatebah Mizani Dadash")
