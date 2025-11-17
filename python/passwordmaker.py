import random

def make_password(length):
    lower = 'abcdefghijklmnopqrstuvwxyz'
    upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    nums  = '0123456789'
    
    chars = lower + upper + nums
    password = ''
    
    for i in range(length):
        password += random.choice(chars)
    return password

print(make_password(10))
