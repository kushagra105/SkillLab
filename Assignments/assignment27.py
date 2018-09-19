# Assignment 27 :

line=input("Enter text:")
words = line.split()
letters = [word[0] for word in words]
print("".join(letters))

# ======================OUTPUT=========================
# Enter text:python is a programming language
# piapl
