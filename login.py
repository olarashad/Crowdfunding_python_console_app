import os
import json
import hashlib
from sub import projects_menu
from getpass import getpass
from activate import activate_account
from register import load_users, hash_password, find_user_by_email  
from utils import load_json_file, save_json_file, validate_email_func, validate_egypt_mobile_func, pause_clear
USERS_FILE = "data/users.json"

def login():
    print("\n=== Login ===")
    email = input("Email: ").strip()
    password = getpass("Password: ")

    users = load_users()
    user = find_user_by_email(users, email)

    if not user:
        print("User not found. Please register first.")
        print("Redirecting to registration page...")
        pause_clear()
        from register import register_user
        register_user()
        return False

    if not user.get("activated", False):
        print("Account not activated. Please activate your account first.")
        activate_account(email)
        return False

    hashed_pw = hash_password(password)
    if hashed_pw == user["password"]:
        print("Login successful!")
        pause_clear()
        print(f"Welcome back, {user['first']}!")

        projects_menu(user)
        return True
    else:
        print("Wrong password.")
        return False


if __name__ == "__main__":
    login()
