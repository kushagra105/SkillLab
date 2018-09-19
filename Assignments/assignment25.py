# Assignment 25 : 

def pallindrome(str):
    str2 = str.replace(" ","")
    print(str2)
    print("Resultant string is\n"+str2[::-2])
  
str = input("Enter a string\n")
pallindrome(str)

# ======================OUTPUT=========================
# Enter a string
# python is a programming language
# pythonisaprogramminglanguage
# Resultant string is
# eagagimropsnhy
