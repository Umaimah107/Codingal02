class Dog:
    breed = "dog"
    def __init__(self, name,age,color):
        self.name = name
        self.age = age
        self.color = color
snowy = Dog("Snowy", 6, "white")
bonnie= Dog("Bonnie", 4, "light brown")

print("Snowy is a {}".format(snowy.breed))
print("Bonnie is also a {}".format(bonnie.breed))
print("{} is {} years old".format(snowy.name, snowy.age))
print("{} is {} years old".format(bonnie.name, bonnie.age))
print("Snowy is {}".format(snowy.color))
print("While Bonnie is {}".format(bonnie.color))

