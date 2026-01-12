num = int(input("Enter your original number: "))

original = num
reversed_num = 0

while num > 0:
    reversed_num = reversed_num << 1
    reversed_num = reversed_num | (num & 1)
    num = num >> 1

print(f"Original number: {original} ({bin(original)[2:]})")
print(f"Reversed Number : {reversed_num} ({bin(reversed_num)[2:]})")
