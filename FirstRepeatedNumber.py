waste = int(input())
var1 = input().split(" ")
var2 = [int(s) for s in var1]
list1 = []
for i in range(len(var2)-1):
    for j in range(i+1,len(var2)):
        if (var2[i] == var2[j]):
            list1.append(var2[i])
print(list1[0])
