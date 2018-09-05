import string

def scase(str2):
    for i in str2:
        if i.isupper():
            str1 = str1+i
    return        
            
def vowel():
    str2 = input("Enter a string\n")
    scase(str2)
    str2 = str2.casefold()
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
