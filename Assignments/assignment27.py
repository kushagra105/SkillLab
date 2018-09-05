line=input("Enter text:")
words = line.split()
letters = [word[0] for word in words]
print("".join(letters))