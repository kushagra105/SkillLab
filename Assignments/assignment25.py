def pallindrome(str):
    str2 = str.replace(" ","")
    print(str2)
    print("Resultant string is\n"+str2[::-2])
  
str = input("Enter a string\n")
pallindrome(str)
