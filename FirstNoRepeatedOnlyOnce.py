waste = int(input())
arr1 = input().split(" ")
list2 = [int(s) for s in arr1]
list1 = []
for i in range(len(list2)-1):
    for j in range(i+1,len(list2)):
        if (list2[i] == list2[j]):
            list1.append(list2[i])
print(list1[0])
