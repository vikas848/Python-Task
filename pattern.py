for a in range(9, 0, -1):  
    for _ in range(a):                          # int type
        print(a, end=" ")  
    print()                


i = str(9)
for a in range(9, 0, -1):  
    print(a*i)                               # str type
    i = str(int(i) -1)  

