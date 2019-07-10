var = map(int,input().strip().split())
a = list(int(s) for s in var)
unique1=[]
unique2=[]
for i in a:
    if(i not in unique1):
        unique1.append(i)
    else:
        unique2.append(i)
for i in unique2:
    unique1.remove(i)
print(unique1)

