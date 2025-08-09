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

def edit_project(user):
    projects = load_projects()
    user_projects = [p for p in projects if p["owner_email"].lower() == user["email"].lower()]
    if not user_projects:
        print("You have no projects to edit.")
        pause_clear()
        return

    print("\n--- Edit Project ---")
    for i, p in enumerate(user_projects, 1):
        print(f"{i}) {p['title']}")

    choice_str = input("Select project number to edit: ").strip()
    if not choice_str.isdigit() or not (1 <= int(choice_str) <= len(user_projects)):
        print("Invalid choice.")
        return

    project = user_projects[int(choice_str) - 1]
    print(f"Editing project: {project['title']}")

    title = input(f"New title (leave blank to keep '{project['title']}'): ").strip()
    details = input(f"New details (leave blank to keep current '{project['details']}'): ").strip()

    while True:
        target_str = input(f"New target (leave blank to keep {project['target']}): ").strip()
        if target_str == "":
            target = project["target"]
            break
        elif target_str.isdigit() and int(target_str) > 0:
            target = int(target_str)
            break
        else:
            print("Please enter a positive number or leave blank.")

    while True:
        start_date_str = input(f"New start date (YYYY-MM-DD, leave blank to keep {project['start_date']}): ").strip()
        if start_date_str == "":
            start_date_str = project["start_date"]
            start_date = validate_date(start_date_str)
            break
        else:
            start_date = validate_date(start_date_str)
            if not start_date:
                print("Invalid date format. Try again.")
                continue
            break

    while True:
        end_date_str = input(f"New end date (YYYY-MM-DD, leave blank to keep {project['end_date']}): ").strip()
        if end_date_str == "":
            end_date_str = project["end_date"]
            end_date = validate_date(end_date_str)
            break
        else:
            end_date = validate_date(end_date_str)
            if not end_date:
                print("Invalid date format. Try again.")
                continue
            break

    if end_date < start_date:
        print("End date must be after start date. Edit cancelled.")
        return

    project["title"] = title if title else project["title"]
    project["details"] = details if details else project["details"]
    project["target"] = target
    project["start_date"] = start_date_str
    project["end_date"] = end_date_str

    for i, p in enumerate(projects):
        if p["id"] == project["id"]:
            projects[i] = project
            break

    save_projects(projects)
    print("Project updated successfully!")
    pause_clear()
    from sub import projects_menu
    projects_menu(user)
    
