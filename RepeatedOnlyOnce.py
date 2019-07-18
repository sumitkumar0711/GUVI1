waste = int(input())
var1 = input().split(" ")
var2 = [int(s) for s in var1]
var2.sort()
counter = 0
for i in range(len(var2)-1):
    if (var2[i-1] != var2[i]):
        if (var2[i] != var2[i+1]):
            print(var2[i],end = " ")
for i in var2:
    if(var2[-1] == i):
        counter += 1
if(counter == 1):
    print(var2[-1])