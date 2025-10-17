try:
    num1, num2 = eval(input("Enter 2 numbers, both seperated by a comma"))
    result = num1 / num2
    print("Result is", result)

except ZeroDivisionError:
    print("Division by 0 is an error!!")

except SyntaxError:
    print("Comma is missing. Enter numbers separated by a comma like this: , 2")

except:
    print("Wrong input")

else:
    print("No exceptions")

finally:
    print("This will execute no matter what")                