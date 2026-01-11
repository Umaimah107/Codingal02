def OddOcurring(arr):
    res = 0
    for element in arr:
        res = res^element
    return res
arr = []

n = int(input("Enter the array size: "))
while(n):
    num = int(input("Enter number: "))
    arr.append(num)
    n-=1
print("Odd occuring number is : ", OddOcurring(arr))