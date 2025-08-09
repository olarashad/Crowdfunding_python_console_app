import os
import json
from datetime import datetime
from utils import load_json_file, save_json_file, validate_email_func, validate_egypt_mobile_func, validate_date_func, pause_clear

PROJECTS_FILE = "data/projects.json"

def load_projects():
    return load_json_file(PROJECTS_FILE)

def save_projects(projects):
    return save_json_file(PROJECTS_FILE, projects)

def validate_date(date_text):
    return validate_date_func(date_text)

def create_project(user):
    print("\n--- Create New Project ---")
    title = input("Title: ").strip()
    details = input("Details: ").strip()

    while True:
        target_str = input("Total target (EGP): ").strip()
        if target_str.isdigit() and int(target_str) > 0:
            target = int(target_str)
            break
        else:
            print("Please enter a positive number.")

    while True:
        start_date_str = input("Start date (YYYY-MM-DD): ").strip()
        start_date = validate_date(start_date_str)
        if not start_date:
            print("Invalid date format. Try again.")
            continue

        end_date_str = input("End date (YYYY-MM-DD): ").strip()
        end_date = validate_date(end_date_str)
        if not end_date:
            print("Invalid date format. Try again.")
            continue

        if end_date < start_date:
            print("End date must be after start date. Try again.")
            continue

        break

    projects = load_projects()
    import uuid
    new_project = {
        "id": str(uuid.uuid4()),
        "owner_email": user["email"],
        "title": title,
        "details": details,
        "target": target,
        "start_date": start_date_str,
        "end_date": end_date_str
    }

    projects.append(new_project)
    save_projects(projects)
    print("Project created successfully!")
    pause_clear()
    from sub import projects_menu
    projects_menu(user)
