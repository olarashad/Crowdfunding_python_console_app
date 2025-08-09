import os
import json
from utils import load_json_file, save_json_file, validate_email_func, validate_egypt_mobile_func, validate_date_func,pause_clear

PROJECTS_FILE = "data/projects.json"

def load_projects():
    return load_json_file(PROJECTS_FILE)

def save_projects(projects):
    return save_json_file(PROJECTS_FILE, projects)

def delete_project(user):
    projects = load_projects()
    user_projects = [p for p in projects if p["owner_email"].lower() == user["email"].lower()]
    if not user_projects:
        print("You have no projects to delete.")
        pause_clear()
        return

    print("\n--- Delete Project ---")
    for i, p in enumerate(user_projects, 1):
        print(f"{i}) {p['title']}")

    choice_str = input("Select project number to delete: ").strip()
    if not choice_str.isdigit() or not (1 <= int(choice_str) <= len(user_projects)):
        print("Invalid choice.")
        return

    project_to_delete = user_projects[int(choice_str) - 1]

    confirm = input(f"Are you sure you want to delete '{project_to_delete['title']}'? (y/n): ").strip().lower()
    if confirm != 'y':
        print("Deletion cancelled.")
        pause_clear()
        return

    projects = [p for p in projects if p["id"] != project_to_delete["id"]]
    save_projects(projects)
    print("Project deleted successfully!")
    pause_clear()
    from sub import projects_menu
    projects_menu(user)