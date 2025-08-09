# register.py
import os
import json
import re
import uuid
import hashlib
from getpass import getpass
from utils import load_json_file, save_json_file, validate_email_func, validate_egypt_mobile_func, hash_password_func ,pause_clear


USERS_FILE = "data/users.json"

def load_users():
    return load_json_file(USERS_FILE)


def save_users(users):
    return save_json_file(USERS_FILE, users)

def validate_email(email):
    
    return validate_email_func(email)



def validate_egypt_mobile(m):
    
    return validate_egypt_mobile_func(m)



def hash_password(pw):
  
    return hash_password_func(pw)


def generate_activation_code():
    
    return str(uuid.uuid4()).split("-")[0]



def find_user_by_email(users, email):
    for u in users:
        if u["email"].lower() == email.lower():
            return u
    return None



def register_user():
    print("\n=== Register New Account ===")
    first = input("First name: ").strip()
    last = input("Last name: ").strip()

    users = load_users()
    while True:
        email = input("Email: ").strip()
        if not validate_email(email):
            print("Invalid email format. Try again.")
            continue
        if find_user_by_email(users, email):
            print("Email already registered. Try logging in or use another email.")
            pause_clear()
            return None
        break

    while True:
        mobile = input("Mobile (Egyptian): ").strip()
        if not validate_egypt_mobile_func(mobile):
            print("Invalid Egyptian mobile. Example: 01012345678 or +201012345678")
            continue
        break


    while True:
        pw = getpass("Password (min 6 chars): ")
        if len(pw) < 6:
            print("Password too short. Min 6 characters.")
            continue
        pw_confirm = getpass("Confirm password: ")
        if pw != pw_confirm:
            print("Passwords do not match. Try again.")
            continue
        break

    hashed = hash_password(pw)
    activation_code = generate_activation_code()
    new_user = {
        "id": str(uuid.uuid4()),
        "first": first,
        "last": last,
        "email": email,
        "password": hashed,
        "mobile": mobile,
        "activated": False,
        "activation_code": activation_code
    }

    users.append(new_user)
    save_users(users)

    print("\n Account created!")
    print("Activation code (simulate email):", activation_code)
    print("Now run Activate to activate your account.\n")
    print("Redirecting to login page...")
    pause_clear()
    

    return email 
    pause_clear()
