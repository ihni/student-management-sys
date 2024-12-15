from src.models import Repo
from src.auth import Auth
from src.controllers.student_controller import StudentController

from gui.root_window import RootWindow

''' Initializing models and controllers and data'''

repo = Repo("data/students.txt")
auth = Auth(repo, number_attempts=3)
student_controller = StudentController(repo)

result = student_controller.add_student(
    name = "John",
    age = 99,
    id = "root",
    email = "root@root.com",
    phone = "N/A",
)

if type(result) == object:
    repo.add_student()

# ----------- Declaring root window -----------
app = RootWindow()
app.root.mainloop()