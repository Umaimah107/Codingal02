list1 = [1,2,3,4,5,6,7,8,9,10]

evennums = [x for x in list1 if x%2==0]
print("List of even numbers from original are: ",evennums)


def square_numbers():
    numbers = [1,3,5,7,9,11]
    print("Original numbers:", numbers)

    squares = [num*num for num in numbers]
    print("squares of the numbers are:",squares )

square_numbers()

def cube_numbers():
    original = [2,4,6,8,10,12]
    print("Original numbers are:", original)

    cubes = [num*num*num for num in original]
    print("Cubes of the following numbers are", cubes)
cube_numbers()


