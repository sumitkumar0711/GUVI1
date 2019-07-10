a = map(int,input().strip().split())
b = list(set(int(s) for s in a))
b.sort(reverse=True)
for i in b:
    print(i,end="")
