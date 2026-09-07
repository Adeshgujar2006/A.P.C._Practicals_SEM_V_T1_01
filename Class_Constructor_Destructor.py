#to use the concept of constructor and destructor
class Student:
    def __init__(self, name, roll_no):
        print("Constructor called: creating a Student object")
        self.name = name
        self.roll_no = roll_no

s = Student("Adesh:", 1)
print(s.name, s.roll_no)

class Student:
    def __init__(self, name):
        print(f"Constructor: {name} created")
        self.name = name

    def __del__(self):
        print(f"Destructor: {self.name} is being destroyed")

obj = Student("Adesh's")
del obj  