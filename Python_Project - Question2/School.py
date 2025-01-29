from Student import Student

class School(Student):
  def __init__(self, name, age, grade, school):
      super().__init__(name, age, grade)
      self.school = school

  def SchoolStudentDisplay(self):
      print(f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}, School: {self.school}")