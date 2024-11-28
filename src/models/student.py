class Student:
    def __init__(self, name: str, age: int, id: str, email: str, phone: str):
        self.name: str = name
        self.age: int = age
        self.id: str = id
        self.email: str = email
        self.phone: str = phone

    '''
    '
    ' Getters and Setters
    '
    '''

    @property
    def name(self):
        return self.name
    
    @property
    def age(self):
        return self.age
    
    @property
    def id(self):
        return self.id

    @property
    def email(self):
        return self.email

    @property
    def phone(self):
        return self.phone
