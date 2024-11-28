import sys
from src import Repo
from src.auth.auth import Auth
from src.controllers.student_controller import StudentController
from src.gui import GUI

def main():
    repo = Repo("data/students.txt")
    auth = Auth(repo, number_attempts=3)
    student_controller = StudentController(repo)

    app = GUI(auth, student_controller)
    app.run()

if __name__ == "__main__":
    main()
