
import os
import json
from utils import load_json_file, pause_clear, save_json_file, validate_email_func, validate_egypt_mobile_func, validate_date_func

USERS_FILE = "data/users.json"

def load_users():
    return load_json_file(USERS_FILE)

def save_users(users):
    return save_json_file(USERS_FILE, users)
 

def activate_account(email):
    users = load_users()
    user = None
    for u in users:
        if u["email"].lower() == email.lower():
            user = u
            break

    if not user:
        print("User not found.")
        return False

    if user.get("activated", False):
        print("Account already activated.")
        from login import login 
        login()                 

        return True

    code_input = input("Enter your activation code: ").strip()
    if code_input == user.get("activation_code", ""):
        user["activated"] = True

        user["activation_code"] = ""
        save_users(users)
        print("Account activated successfully!")
        print("Redirecting to login page...")
        pause_clear()
        from login import login 
        login()                 
        return True
    else:
        print("Incorrect activation code.")
        print("Redirecting to main page...")
        pause_clear()
        return False

if __name__ == "__main__":
    email = input("Enter your email to activate: ").strip()
    activate_account(email)
