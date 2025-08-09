
from login import login
from utils import pause_clear


def main_menu():

    while True:
        print("-------- welcome to crowdfunding ! --------")
        print("1. Login")
        print("2. Exit")
        choice = input("Please enter your choice (1-2): ")  
   

        if choice == "1":
            print("Redirecting to login page...")
            pause_clear()
            login()
        elif choice == "2":
            print("Thank you for using the crowdfunding app!")
            print("Exiting the application. Goodbye!")
        
            break

        else:
            print("Invalid choice. Please try again.")  



if __name__ == "__main__":
    main_menu()