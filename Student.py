class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"{self.name}({self.age})"

p1 = Student("Emerson Espela", 22)
p2 = Student("Kobe James", 23)

print(p1)
print("Name: ", p1.name)
print("Age: ", p1.age)

print("Name: ", p2.name)
print("Age: ", p2.age)