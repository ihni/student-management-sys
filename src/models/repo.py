from .student import Student
from ..utilities.color import *
class Repo:
    def __init__(self, file_path):
        print(f"{CYAN}Initializing repository{RESET}")
        self.file_path: str = file_path
        print(f"{CYAN}Loading users from data/students.txt into application{RESET}")
        self.container: dict = self.load_to_program()

    def add_student(self, student: object):
        self.container[student.id] = student
        self.write_all_to_file()

    def fetch_student_by_id(self, id: str) -> object:
        if id in self.container:
            return self.container[id]
        return None
    
    def fetch_all(self) -> list[object]:
        return list(self.container.values())

    def write_all_to_file(self):
        """Writes all students to the file in a formatted table with dynamic column widths."""
        print("Preparing to write to file")
        with open(self.file_path, "w") as file:
            # Define headers
            headers = ["Name", "Age", "ID", "Email", "Phone"]
            
            # Prepare rows
            rows = self.prepare_table_data()

            # Calculate column widths dynamically
            column_widths = [max(len(str(row[i])) for row in rows + [headers]) for i in range(len(headers))]
            
            # Create a format string for the table rows
            format_row = " | ".join(f"{{:<{width}}}" for width in column_widths)

            # Write the headers
            file.write(format_row.format(*headers) + "\n")
            file.write("-" * (sum(column_widths) + 3 * (len(headers) - 1)) + "\n")  # Add a separator line

            # Write the data rows
            for row in rows:
                file.write(format_row.format(*row) + "\n")

    def prepare_table_data(self) -> list[list[str]]:
        rows = []
        for student in self.container.values():
            rows.append(student.get_data())
        return rows

    def load_to_program(self) -> dict:
        container = {}
        try:
            with open(self.file_path, "r") as file:
                lines = file.readlines()

                # Skip the header and separator lines
                data_lines = lines[2:]
                
                for line in data_lines:
                    data = [item.strip() for item in line.split('|')]
                    
                    if len(data) == 5:
                        student = Student(*data)
                        container[student.id] = student
                        print(f"Loaded {student.name} with ID: {student.id}")

                print(f"{GREEN}All data has been loaded!{RESET}")
        except FileNotFoundError:
            print(f"File {self.file_path} not found. Creating new file.")
            with open(self.file_path, "w") as file:
                file.write("")
        except Exception as e:
            print(f"Error loading file: {e}")
        return container
