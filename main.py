import subprocess

from database.database import DataBase
from services.authentication import Authentication

from classes.user import Admin_User

from panels.main_panel import MainPanel
from panels.admin_panel import AdminPanel
from panels.employer_panel import EmployerPanel
from panels.passenger_panel import PassengerPanel

def show_banner():
    subprocess.run(["bash", "train.sh"])

#show_banner()

db = DataBase()
auth = Authentication(database=db)

default_admin = Admin_User("admin", "admin")
db.create_DI(default_admin, "admins")


admin_panel = AdminPanel(db, auth)
employer_panel = EmployerPanel(db, auth)
passenger_panel = PassengerPanel(db, auth)

app = MainPanel(admin_panel, employer_panel, passenger_panel)
app.start()