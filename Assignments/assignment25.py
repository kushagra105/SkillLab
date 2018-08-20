def pallindrome(str):
    str.replace(" ","")
    print("Resultant string is\n"+str[::-2])
  
str = input("Enter a string\n")
pallindrome(str)
