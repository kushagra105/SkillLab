import string

def scase(str3):
    print("ashdjasgd")
    for i in str3:
        if i.isupper():
            print(i)
    return        
            
def vowel():
    str2 = input("Enter a string\n")
    str2 = str2.casefold()
    scase(str2)
    vowel = 'aeiou'
    count = {}.fromkeys(vowel,0)
    list1 = []
    for i in str2:
        if i in count:
            count[i] += 1
    for i in count :
        if count[i] > 1 :
            list1.append(count)
    print(count)
    return

vowel()
