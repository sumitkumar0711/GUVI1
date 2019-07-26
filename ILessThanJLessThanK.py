var = input().split(" ")
arr = [int(s) for s in var]
counter = 0
for i in range(0,len(arr)):
    for j in range(i+1,len(arr)):
        for k in range(i+2,len(arr)):
            if(arr[i]<arr[j]<arr[k]):
                counter+=1
print(counter)