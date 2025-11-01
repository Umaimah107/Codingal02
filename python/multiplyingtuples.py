def multiply_tuple(numbers):
    product = 1
    for num in numbers:
        product *= num
    return product

my_tuple = (2, 3, 4, 5)

result = multiply_tuple(my_tuple)

print("The product of the tuple is:", result)
