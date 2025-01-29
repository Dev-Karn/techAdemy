class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def get_grade(self):
        return self.grade

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}")