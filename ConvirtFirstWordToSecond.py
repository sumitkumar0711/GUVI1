var = input().split(" ")
value1 = list(var[0])
value1_length = len(value1)
value2 = list(var[1])
value2_length = len(value2)

counter = 0
n = value2_length - value1_length

if(value1_length <= value2_length):
    for i in range(0,value1_length):
        if (value1[i] == value2[i]):
            break
        else:
            counter += 1
if(value2_length == value1_length):
    if(value1[-2]==value2[-2]):
        counter+=1

print(counter+n)
