class Subjects:
    def __init__(self, name, teacher):
        self.name = name
        self.teacher = teacher

    def get_subject(self):
        return f"{self.name} is taught by {self.teacher}"
    
test = print("test")