arr = (input().split())
a = [int(s) for s in arr]
a.sort(reverse=True)
for i in range(len(a)):
    print(a[i],end="")