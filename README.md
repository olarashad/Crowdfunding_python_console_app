
```markdown
# Crowd-Funding Console App

## About
This is a console-based crowdfunding application that allows users to register, activate their account, login, and manage fundraising projects. Users can create, view, edit, and delete their projects with start and end dates, targets, and detailed descriptions.

## Features
- **User Authentication**
  - User registration with validation (email, Egyptian mobile)
  - Account activation via activation code
  - Secure password hashing
  - Login system with activation check

- **Project Management**
  - Create fundraising projects with title, details, target, start and end dates
  - View user's own projects
  - Edit existing projects
  - Delete projects
  - Input validation and date checks

- **User Experience**
  - Clean and structured menus
  - Clear screen and pause prompts for smooth navigation

## Technologies Used
- Python 3.x
- JSON for data storage
- hashlib for password hashing
- uuid for unique IDs

## How to Run
1. Clone the repo:
```

git clone <your-repo-url>

```
2. Navigate to the project directory:
```

cd Crowd-Funding-console-app

```
3. Run the application:
```

python3 app.py

```

## Project Structure
```

├── app.py                # Main entry point with main menu
├── utils.py              # Utility functions for validation, file I/O, screen clear, pause
├── register.py           # User registration logic
├── login.py              # User login logic
├── activate.py           # Account activation logic
├── create_project.py     # Logic for creating projects
├── view_projects.py      # Logic for viewing projects
├── edit_project.py       # Logic for editing projects
├── delete_project.py     # Logic for deleting projects
├── sub.py                # Project menu handling
├── data/                 # JSON files for storing users and projects
│   ├── users.json
│   └── projects.json
└── README.md

```

## Notes
- The activation code is simulated and printed after registration (no email sending).
- Data is stored locally in JSON files.
- Designed for Linux terminals but can be adapted for Windows by modifying `clear_screen()` in `utils.py`.


This project was developed by **Ola Rashad** during the **ITI Python Course** as part of learning and practicing programming skills.


---
