def scase(str):
    
    for i in str:
        if i.isupper():
            print(i)
    return

def pallindrome():
    n = input("Enter a number\n")
    m = n[::-1]
    if m == n :
        print("Entered number "+n+"is a pallindrome")
    else : 
        print("Entered number "+n+" is not a pallindrome")
    return    

def vowel():
    str2 = input("Enter a string\n")
    for i in str2:
        if i.isvowel():
            print(i)
    return


ch = input("Enter your choice\n")
if ch == '1' :
    str = input("Enter a string\n")
    scase(str)
elif ch == '2' :
    pallindrome()
elif ch == '3' :
    vowel()