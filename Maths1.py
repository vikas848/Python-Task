# b = []
# for a in range(0, 6, 1):
#         a=int(input())
#         b.append(a)
 
# print(b[1::2])
# print(b[0::2])


b = []
for a in range(0, 6, 1):
        a=int(input())
        if a%2==0:
                print(a)
        else:
                b.append(a)
print(b)