import subprocess
from classes.panel_class import Panel

def show_banner():
    subprocess.run(["bash", "train.sh"])

show_banner()

panel = Panel()
panel.start()