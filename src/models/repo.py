from .student import Student

class Repo:
    def __init__(self, file_path):
        self.file_path: str = file_path
        self.container: dict = self.load_to_program()

    def add_student(self, student: object):
        self.container[student.id] = student

    def fetch_student_by_id(self, id: str) -> object:
        if id in self.container:
            return self.container[id]
        return None
    
    def fetch_all(self) -> list[object]:
        students = [student for student in self.container.values()]
        return students

    def write_to_file(self, student):
        with open(self.file_path, "a") as file:
            name, age, id, email, phone = student.get_data()
            file.write(f"{name};{age};{id};{email};{phone}\n")

    def load_to_program(self) -> dict:
        container = {}

        try:
            with open(self.file_path, "r") as file:
                for line in file.readlines():
                    data: list = line.strip().split(';')
                    if len(data) == 5:
                        student = Student(*data)
                        container[student.id] = student
        except FileNotFoundError:
            print(f"File {self.file_path} not found. Creating new file.")
            with open(self.file_path, "w") as file:
                file.write("")
        except Exception as e:
            print(f"Error loading file: {e}")
        return container
