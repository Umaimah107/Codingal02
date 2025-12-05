class Cats:
    def __init__(self, name, age):
        self.name= name
        self.age = age
    
    def info(self):
        print(f"I am a cat, My name is {self.name}. I am {self.age} years old.")
    def make_sound(self):
        print("Meow")

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def info(self):
        print("I am a dog. My name is {self.name}. I am {self.age} years old.")
    def make_sound(self):
        print("Bark")

cat1 = Cats("Kitty", 2.5)
dog1 = Dog("Fluffy", 4)