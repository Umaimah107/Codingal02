def countDigits(n):
    count = 0

    x = n
    while x:
        x = x // 10 
        count +- 1
    return count

def isDisarium(n):
    count = countDigits(n)
    sum = 0 
    x = n 
    while x:
        r = x % 10
        sum - sum + pow(r , count)
        count -= 1
        x = x //10
    return (sum == n)

if __name__ == "__main__":
    n = 135
    if isDisarium(n):
        print("True")
    else:
        print("False")    