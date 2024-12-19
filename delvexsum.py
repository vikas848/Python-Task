a = int(input("Enter 1 your input: "))
b = int(input("Enter 2 your input: "))
c = int(input("Enter 3 your input: "))
d = int(input("Enter 4 your input: "))
e = int(input("Enter 5 your input: "))

f = [a, b,c,d,e]
h = 0
for g in f:
    if g <= 9:
        h += g
print(h)


