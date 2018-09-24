# Assignment 40: Use of common Python functions
text = "I am a Python Developer"
text1 = "       I am also a java  Developer            "
print(text.endswith("Developer"))
print(text.upper())
print(text.lower())
print(text.replace("is", "was"))
print(text1.strip())
print(text.replace("Python", "Javascript"))
print(text.find("a"))
print(text.startswith("Developer"))

# =========================OUTPUT=========================
# True
# I AM A PYTHON DEVELOPER
# i am a python developer
# I am a Python Developer
# I am also a java  Developer
# I am a Javascript Developer
# 2
# False