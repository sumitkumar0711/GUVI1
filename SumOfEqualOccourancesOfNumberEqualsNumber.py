var1 = input().split(" ")
var2 = [int(s) for s in var1]
summation = 0
for i in range(var2[0]+1):
    summation = var2[1] + var2[2]
if(summation == var2[0]):
    print("YES")
else:
     print("NO")