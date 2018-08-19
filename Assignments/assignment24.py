import string

def scase():
    str = input("Enter a string\n")
    print("Upper case character(s) in entered string "+str+" is/are ")
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
    str2 = str2.casefold()
    vowel = 'aeiou'
    count = {}.fromkeys(vowel,0)
    for i in str2:
        if i in count:
            count[i] += 1
    print(count)        
    return

def punc():
    s = input("Enter a string with punctuations\n")
    print("String with punctuations: "+s)
    exclude = set(string.punctuation)
    return print("String without punctuations: "+''.join(ch for ch in s if ch not in exclude))
    


ch = input("Enter your choice\n")
if ch == '1' :
    scase()
elif ch == '2' :
    pallindrome()
elif ch == '3' :
    vowel()
elif ch == '4' :
    punc()