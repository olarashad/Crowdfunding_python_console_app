

from utils import pause_clear


def projects_menu(user):
    while True:
        print("\n=== Projects Menu ===")
        print("1) Create Project")
        print("2) View My Projects")
        print("3) Edit Project")
        print("4) Delete Project")
        print("5) Logout")
        choice = input("Choose an option: ").strip()
        if choice == "1":
            from create_project import create_project
            print("Redirecting to create project page...")
            pause_clear()
            create_project(user)
        elif choice == "2":
            from view_projects import view_projects
            print("Redirecting to view projects page...")
            pause_clear()
            view_projects(user)
        elif choice == "3":
            from edit_project import edit_project
            print("Redirecting to edit project page...")
            pause_clear()
            edit_project(user)
        elif choice == "4":
            from delete_project import delete_project
            print("Redirecting to delete project page...") 
            pause_clear()
            delete_project(user)
        elif choice == "5":
            print("Logging out...")
            from app import main_menu
            print("Redirecting to main menu...")
            pause_clear()
            main_menu()
            break
        else:
            print("Invalid choice, try again.")
