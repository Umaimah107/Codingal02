x = float(input("Enter the base(x):"))
n = int(input("Enter the number of terms (n):"))

sum_series = 0 

print("\nPower series:")

for i in range(n):
    term = x**i
    print(f"{x}^{i} = {term}")
    sum_series += term

print(f"\nSum of the power series: {sum_series}")