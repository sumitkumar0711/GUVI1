a = input().split(" ")
value = list(str(a[0].split()))
n = int(a[1]) + 2
for i in range(2):
    value.pop()
del(value[1:n])
value.pop(0)
for j in value:
    print(j, end= "")