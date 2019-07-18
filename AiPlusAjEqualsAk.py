waste = int(input())
var1 = input().split()
var2 = [int(s) for s in var1]
for i in range(len(var2)):
    for j in range(len(var2)):
        for k in range(len(var2)):
            if((var2[i] + var2[j]) == var2[k]):
                print(var2[i], end=" ")
                print(var2[j], end=" ")
                print(var2[k], end=" ")
                print()