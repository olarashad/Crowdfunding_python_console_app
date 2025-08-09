import os
import json
from utils import load_json_file, save_json_file, validate_email_func, validate_egypt_mobile_func, hash_password_func, pause_clear

PROJECTS_FILE = "data/projects.json"

def load_projects():
    return load_json_file(PROJECTS_FILE)

def view_projects(user):
    print("\n--- My Projects ---")
    projects = load_projects()
    user_projects = [p for p in projects if p["owner_email"].lower() == user["email"].lower()]
    if not user_projects:
        print("You have no projects.")
        return
    for i, p in enumerate(user_projects, 1):
        print(f"{i}) {p['title']}")
        print(f"   Details: {p['details']}")
        print(f"   Target: {p['target']} EGP")
        print(f"   Duration: {p['start_date']} to {p['end_date']}\n")
    from sub import projects_menu
    pause_clear()
    projects_menu(user)