import string

def scase():
    str = input("Enter a string\n")
    print("Upper case character(s) in entered string "+str+" is/are ")
    for i in str:
        if i.isupper():
            print(i)
    return

def pallindrome():
    str = input("Enter a string\n")
    m = str[::-1]
    if m == str :
        print("Entered string "+str+"is a pallindrome")
    else : 
        print("Entered string "+str+" is not a pallindrome")
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
    

print("Press")
print("1. to count and display the number of capital letters in a given string")
print("2. to check if a given string is pallindrome or not")
print("3. to count the number of each vowel in a string")
print("4. to remove all punctuation from the string provided by user\n")
ch = input("Enter your choice\n")
if ch == '1' :
    scase()
elif ch == '2' :
    pallindrome()
elif ch == '3' :
    vowel()
elif ch == '4' :
    punc()