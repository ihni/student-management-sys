from ..models import Student
from ..utilities.color import *

class StudentController:
    def __init__(self, repo):
        print(f"{CYAN}Initializing student controller{RESET}")
        self.repo = repo

    def add_student(self, name, age, id, email, phone):
        print(f"{YELLOW}Creating a student with these attributes:{RESET}")
        print(
            f"Name: {name if name else None}\n"
            f"Age: {age if age else None}\n"
            f"ID: {id if id else None}\n"
            f"Email: {email if email else None}\n"
            f"Phone: {phone if phone else None}"
        )
        errors = {}

        if not name:
            errors['name'] = 'Name is required'
        if not age:
            errors['age'] = 'Age is required'
        if not id:
            errors['id'] = 'ID is required'
        if not email:
            errors['email'] = 'Email is required'

        if not phone:
            errors['phone'] = 'A phone number is required'

        print(f"{YELLOW}Looking for duplicate ID ({RESET}{id}{YELLOW}) in repo:{RESET}")
        if not self.repo.fetch_student_by_id(id):
            errors['duplicate'] = 'Duplicate ID found'

        if errors:
            print(f"{RED}An error occured adding a student in the student controller{RESET}")
            for _, value in errors.items():
                print(f"{RED}{BOLD}Error:{RESET} {RED}{value}{RESET}")
            return errors

        student = Student(name, age, id, email, phone)
        self.repo.add_student(student)
        self.repo.write_all_to_file()
        print(f"{GREEN}{student.name} was successfully created and stored in the repo!{RESET}")
        return {'success' : f'Student {name} added successfully'}

    def fetch_student_by_id(self, id):
        print(f"{CYAN}Fetching for studeny with id: {id}{RESET}")
        result = self.repo.fetch_student_by_id(id)
        if result:
            print(f"{GREEN}Result: Found student id: {id}!{RESET}")
            return result
        print(f"{YELLOW}Result: Could not finid studentwith id: {id}{RESET}")
        return f'Student ID {id} not found'

    def fetch_all_students(self):
        print(f"{CYAN}Fetching all students...{RESET}")
        return self.repo.fetch_all()
