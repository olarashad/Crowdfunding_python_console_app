import os
import json
from datetime import datetime
import re
import hashlib

def load_json_file(file_path):
    if not os.path.exists(file_path):
        return []
    with open(file_path, "r") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

def save_json_file(file_path, data):
    dirpath = os.path.dirname(file_path)
    if dirpath:
        os.makedirs(dirpath, exist_ok=True)
    tmp_path = file_path + ".tmp"
    try:
        with open(tmp_path, "w") as f:
            json.dump(data, f, indent=2)
            f.flush()
            try:
                os.fsync(f.fileno())
            except:
                pass
        os.replace(tmp_path, file_path)
    except Exception as e:
        if os.path.exists(tmp_path):
            os.remove(tmp_path)
        raise e

def validate_date_func(date_text):
    try:
        return datetime.strptime(date_text, "%Y-%m-%d")
    except ValueError:
        return None

def validate_email_func(email):
    return re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", email)

def validate_egypt_mobile_func(mobile):
    return re.match(r"^(?:\+20|20|0)?1(?:0|1|2|5)\d{8}$", mobile)

def hash_password_func(pw):
    return hashlib.sha256(pw.encode()).hexdigest()

def pause_clear():
    input("Press Enter to continue...")
    os.system('clear')