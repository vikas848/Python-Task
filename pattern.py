for a in range(9, 0, -1):  
    for _ in range(a):     
        print(a, end=" ")  
    print()                


i = str(9)
for a in range(9, 0, -1):  
    print(a*i)
    i = str(int(i) -1)  

