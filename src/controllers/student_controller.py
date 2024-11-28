from ..models import Student

class StudentController:
    def __init__(self, repo):
        self.repo = repo

    def add_student(self, name, age, id, email, phone='N/A'):
        errors = {}

        if not name:
            errors['name'] = 'Name is required'
        if not age:
            errors['age'] = 'Age is required'
        if not id:
            errors['id'] = 'ID is required'
        if not email:
            errors['email'] = 'Email is required'

        if self.repo.fetch_student_by_id(id):
            errors['duplicate'] = 'Duplicate ID found'
        
        if errors:
            return errors

        student = Student(name, age, id, email, phone)
        self.repo.add_student(student)
        return {'success' : f'Student {name} added successfully'}

    def fetch_student_by_id(self, id):
        result = self.repo.fetch_student_by_id(id)
        return result if result else f'Student ID {id} not found'

    def fetch_all_students(self):
        return self.repo.fetch_all()
