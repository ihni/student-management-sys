from ..utilities.color import *

class Auth:
    def __init__(self, repo, number_attempts):
        self.repo = repo
        self.user = None
        self.number_attempts = number_attempts

    def login(self, id) -> str:
        print(f"{YELLOW}User is logging in{RESET}")
        if self.number_attempts < 0:
            print(f"{RED}Login blocked, number of attempts are 0{RESET}")
            return 'You have run out of attempts, Please try again later'

        print(f"{YELLOW}Fetching student with id: {id}{RESET}")
        result = self.repo.fetch_student_by_id(id)
        if result:
            print(f"{GREEN}Login successful! Saving user.{RESET}")
            self.user = result
            return 'Login successful'
        self.number_attempts -= 1
        print(f"{RED}Login failed, number of attempts left = {self.number_attempts}{RESET}")
        return 'Login failed'

    def logout(self) -> bool:
        if self.user:
            self.user = None
            return True
        return False
    
    def get_user(self) -> object:
        return self.user
    
    def reset_attempts(self):
        self.number_attempts = 3
