n = int(input())
counter = 0
for i in range(2,n//2):
    if(n%i==0):
        counter += 1
if(counter == 0):
    print("yes")
else:
    print("no")