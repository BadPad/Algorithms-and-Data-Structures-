# This is a class understanding program

class dog:
    Species = "Canis Familiars"
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is a {self.age} years old"

D = dog("joj", 7)
print(D.age)
print(D.name)
print(D)

class car:
    def __init__(self):
        pass
