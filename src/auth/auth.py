class Auth:
    def __init__(self, repo, number_attempts):
        self.repo = repo
        self.user = None
        self.number_attempts = number_attempts

    def login(self, id) -> str:
        if self.number_attempts < 0:
            return 'You have run out of attempts, Please try again later'

        result = self.repo.fetch_student_by_id(id)
        if result:
            self.user = result
            return 'Login successful'
        self.number_attempts -= 1
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
