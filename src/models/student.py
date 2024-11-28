class Student:
    def __init__(self, name: str, age: str, id: str, email: str, phone: str):
        self.name: str = name
        self.age: str = age
        self.id: str = id
        self.email: str = email
        self.phone: str = phone

    '''
    '
    ' Getters and Setters
    '
    '''
    
    def get_data(self) -> list[str]:
        return ( 
            self.name,
            self.age,
            self.id,
            self.email,
            self.phone
        )