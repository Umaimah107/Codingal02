def squares():
    list1 = [2,4,9,16,25,36,49,64,81,100]
    print("Original list:",list1)

    even = []
    odd = []

    for num in list1:
        if num % 2 == 0:
            even.append(num)
        else:
            odd.append(num)
    
    print("Even numbers:", even)
    print("Odd numbers:", odd)

squares()

            