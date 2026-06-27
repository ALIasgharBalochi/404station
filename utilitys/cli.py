from colorama import Fore, Style, init

init(autoreset=True)

class CLI:

    @staticmethod
    def success(message):
        print(Fore.GREEN + message)

    @staticmethod
    def error(message):
        print(Fore.RED + message)

    @staticmethod
    def warning(message):
        print(Fore.YELLOW + message)

    @staticmethod
    def info(message):
        print(Fore.CYAN + message)

    @staticmethod
    def title(message):
        print(Fore.MAGENTA + message )

    @staticmethod
    def normal(message):
        print(Style.RESET_ALL + message)