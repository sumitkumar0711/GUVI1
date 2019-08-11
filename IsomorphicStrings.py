var1 = input().split(" ")
string1 = var1[0]
string2 = var1[1]
counter1 = 0
counter2 = 0
for i in range(1,len(string1)):
    if(string1[i-1]==string1[i]):
        counter1+=1
    else:
        counter1-=1
for j in range(1,len(string2)):
    if(string2[j-1]==string2[j]):
        counter2+=1
    else:
        counter2-=1
if(counter2==counter1):
    print("yes")
else:
    print("no")