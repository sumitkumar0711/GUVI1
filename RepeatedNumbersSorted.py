n = int(input())
arr = (input().split())
a = [int(s) for s in arr]
a.sort()
li=[]

for i in range(len(a)-1):
    for j in range(i+1,len(a)):
        if (a[i]==a[j]):
            li.append(a[i])
if(len(li)==0):
    print("unique")
else:
    for k in range(len(li)):
        print(li[k], end=" ")
