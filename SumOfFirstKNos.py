var1 = input().split(" ")
var2 = var1[0].split()
var3 = int(var1[1])
arr = [int(s) for s in var2]
sum = 0
for i in range(var3+1):
    sum+=i
print(sum)