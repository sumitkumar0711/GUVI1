x = int(input())
a = map(int,input().strip().split())
b = list(int(s)for s in a)
c = []
for i in range(len(b)):
    if(i==b[i]):
        flag=1
        c.append(b[i])
    else:
        flag = -1
if(flag == 1):
    for j in c:
        print(j,end = " ")
else:
    print("-1")