from ..utilities.color import *

class Auth:
    def __init__(self, repo, disable_login_attempts, number_attempts):
        self.repo = repo
        self.user = None
        self.number_attempts = number_attempts
        self.disable_login_attempts = disable_login_attempts

    def login(self, id) -> int:
        result = self.repo.fetch_student_by_id(id)
        if self.number_attempts <= 1 and not result:
            print(f"{RED}{BOLD}Login blocked, number of attempts are 0{RESET}")
            return -1

        print(f"{YELLOW}User is logging in{RESET}")
        print(f"{YELLOW}Fetching student with id: {id}{RESET}")
        if result:
            print(f"{GREEN}Login successful! Saving user.{RESET}")
            self.user = result
            return 1
        
        self.number_attempts -= 1 if self.disable_login_attempts else 0
        print(f"{RED}Login failed, number of attempts left = {self.number_attempts}{RESET}")
        return 0

    def logout(self) -> bool:
        if self.user:
            self.user = None
            return True
        return False
    
    def get_user(self) -> object:
        return self.user
    
    def reset_attempts(self):
        self.number_attempts = 3
