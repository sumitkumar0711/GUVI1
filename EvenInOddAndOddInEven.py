waste = int(input())
var1 = input().split(" ")
var2 = [int(s) for s in var1]
for i in range(len(var2)):
    if(i%2==0):
        if(var2[i] % 2 != 0):
            print(var2[i],end=" ")
        else:
            continue
    else:
        if(var2[i] % 2 == 0):
            print(var2[i], end=" ")
        else:
            continue