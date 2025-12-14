def ONSquaretime(n):
    iteration = 0
    for i in range (0,n):
        for j in range(0,n):
            print("*", end = " ")
            iteration+=1
        print("")
    print("\n When n is ",n," Iterations = ", iteration,"\n")

ONSquaretime(5)
ONSquaretime(4)
ONSquaretime(3)
print("\nWith every 'n' the time taken equals n^2")
print("O(n^2)")