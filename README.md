# Student Registration System
A simple student registration system for managing student records made with Python and Tkinter

## Features
- **Login system**: Allows users to log in and access the student dashboard.
- **View Students**: Display all students in a table with details such as ID, name, age, email, and phone number.
- **Register Students**: Allows for the registration of new students.
- **Search Students**: Provides a search functionality to look up students by name or ID.
- **Profile**: View and manage the logged-in user's profile.

## Prerequisites
- [Python] (version 3.13 above)

## Installation

1. Clone the repository:
    ```bash
    git clone https://github/ihni/student-regis.git
    ```

2. Navigate to the project directory:
    ```bash
    cd student-regis
    ```
3. Install dependencies:
    ```bash
    pip install -r requirements.txt

## Usage
1. Run the application
    ```bash
    python main.py
    ```
2. After the login screen appears, enter a user id:
    - for this example, feel free to use: `root`
3. After logging in, you will be taken to the dashboard, where you can view, register, and search students.

## Project Structure

```graphql
student-regis/
├── data/                              # Contains data files for the application.
│   └── students.txt                   # Stores student data.
├── gui/                               # Graphical User Interface (GUI) components.
│   ├── config/                        # Configuration files for UI settings.
│   │   ├── attributes.py              # UI-related attributes and settings.
│   │   └── color.py                   # Color constants used throughout the UI.
│   ├── contents/                      # Contains different GUI frames.
│   │   ├── profile_frame.py           # Frame for viewing and editing student profiles.
│   │   ├── register_student_frame.py  # Frame for registering new students.
│   │   ├── search_student_frame.py    # Frame for searching students.
│   │   └── view_all_students_frame.py # Frame for displaying all students.
│   ├── dashboard_frame.py       # Dashboard frame that houses the main interface.
│   ├── login_frame.py           # Login frame for user authentication.
│   ├── root_window.py           # Main window that initializes the GUI.
│   └── utils.py                 # Utility functions for the GUI.
├── src/                         # Backend logic and models.
│   ├── auth/                    # Authentication logic for handling user login.
│   │   ├── auth.py              # Authentication handling.
│   │   └── __init__.py          # Initialization of the auth package.
│   ├── controllers/             # Controllers to handle business logic.
│   │   ├── student_controller.py# Handles student-related logic.
│   │   └── __init__.py          # Initialization of the controllers package.
│   ├── models/                  # Data models for application entities.
│   │   ├── student.py           # Student model for managing student data.
│   │   ├── repo.py              # Repository for managing data storage operations.
│   │   └── __init__.py          # Initialization of the models package.
│   ├── utilities/               # Helper functions for backend tasks.
│   │   ├── color.py             # Utility for handling color-related tasks.
│   │   └── __init__.py          # Initialization of the utilities package.
│   └── __init__.py              # Initialization of the src package.
├── .gitignore                   # Git ignore configuration for excluded files.
├── main.py                      # Entry point to run the application.
├── README.md                    # Project documentation.
└── requirements.txt             # List of required Python libraries for the project.

```