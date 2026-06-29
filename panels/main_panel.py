from utilitys.cli import CLI

class MainPanel:
    def __init__(self, admin_panel, employer_panel, passenger_panel):
        self.admin_panel = admin_panel
        self.employer_panel = employer_panel
        self.passenger_panel = passenger_panel

    def start(self):
        while True:
            self.show_menu()
            choice = input("\nMikhay Koja Beri? ").strip()

            if choice == "1":
                self.admin_panel.admin_login_panel()

            elif choice == "2":
                self.employer_panel.employer_login_panel()

            elif choice == "3":
                self.passenger_panel.passenger_panel()

            elif choice == "4":
                CLI.warning("\nShab O Roozegar Khosh")
                break

            else:
                CLI.error("\nDari Eshtebah Mizani Dadash")

    def show_menu(self):
        CLI.title("\n--- Be 404 Station Khosh Omadi ---")
        CLI.info("1. Admin Panel")
        CLI.info("2. Employer Panel")
        CLI.info("3. Passenger Panel")
        CLI.info("4. Exit")