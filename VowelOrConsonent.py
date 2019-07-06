string='aeiou'
var=input()
flag=0
if(var.isalpha()==True):
    for i in string:
        if(i==var):
            print("Vowel")
            break
        else:
            print("Consonent")
            break
else:
    print("invalid")