class MainPanel:
    def __init__(self, admin_panel, employer_panel, passenger_panel):
        self.admin_panel = admin_panel
        self.employer_panel = employer_panel
        self.passenger_panel = passenger_panel

    def start(self):
        while True:
            self.show_menu()
            choice = input("Mikhay Koja Beri? ").strip()

            if choice == "1":
                self.admin_panel.admin_login_panel()

            elif choice == "2":
                self.employer_panel.employer_login_panel()

            elif choice == "3":
                self.passenger_panel.passenger_panel()

            elif choice == "4":
                print("Shab O Roozegar Khosh")
                break

            else:
                print("Dari Eshtebah Mizani Dadash")

    def show_menu(self):
        print("\nBe 404 Station Khosh Omadi")
        print("1. Admin Panel")
        print("2. Employer Panel")
        print("3. Passenger Panel")
        print("4. Exit")