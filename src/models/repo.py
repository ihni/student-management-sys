from .models import Student

class Repo:
    def __init__(self):
        self.container: dict = {}

    def add_student(self, student: object):
        self.containter[student.id] = student

    def fetch_student_by_id(self, id: str) -> object:
        if id in self.container:
            return self.container[id]
        return None
