var1 = input()
var1_length = len(var1)

var2 = input()
var2_length = len(var2)

counter = 0
value1 = 0
value2 = 0
if(var1_length>=var2_length):

    for i in range(len(var2)):
        counter += (ord(var2[i]) - ord(var1[i]))

    for j in range(var1_length):
        value1 += (ord(var1[j])-96)

    for k in range(var2_length):
        value2 += (ord(var1[k])-96)
    x = counter + value1 - value2
    if (x >= 0):
        print(x)
    else:
        print(-x)


else:

    for i in range(len(var1)):
        counter += (ord(var1[i]) - ord(var2[i]))

    for j in range(var2_length):
        value1 += (ord(var2[j])-96)

    for k in range(var1_length):
        value2 += (ord(var2[k])-96)
    x = counter + value1 - value2
    if (x >= 0):
        print(x)
    else:
        print(-x)
