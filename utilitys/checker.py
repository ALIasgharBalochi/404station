import re

email_pattern = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"
password_pattern = r'^(?=.*[a-zA-Z])(?=.*\d)(?=.*@)(?=.*&)[a-zA-Z\d@&]{8,}$'


def check(password="",email="",options="b"):
    check_email = re.fullmatch(email_pattern,email)
    check_password = re.fullmatch(password_pattern,password)
    if options == "e":
        if check_email :
            return True
        else:
            return False
    elif options == "p":
        if  check_password:
            return True
        else:
            return False
    else:
        if check_email and check_password:
            return True
        else:
            return False
    
    

