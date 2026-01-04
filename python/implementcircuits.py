a=1
b=0
c=0

aAndb = a & b
bXORc = b ^ c
bORc= b | c
g= bXORc & bORc
final = aAndb ^ g
print("q = ", final)