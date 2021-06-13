class Person:
    arian = True
    def __init__(self, n, f):
        self.name = n
        self.family = f
    def salary(self):
        print("NO MONRY FOR STUDENT!!!")

class Teacher(Person):
    def __init__(self, n, f, h):
        super().__init__(n, f)
        self.hour = h
    def salary(self):
        print(f'{self.name} catch {self.hour * 10}$')

class Student(Person):
    def __init__(self, n, f, g):
        super().__init__(n, f)
        self.grade = g


d = Teacher('David', 'Lennon', 10)
d.salary()

a = Student('Amir', 'Farivar', 7)
a.salary()

print(Person.arian)