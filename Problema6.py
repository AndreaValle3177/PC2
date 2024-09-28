a, b = 0, 1

print(a, end=", ")

while b <= 50:
    print(b, end=", " if b < 50 else "")  
    a, b = b, a + b