# Assignment 28:  Operations On Tuples
head = ("CEO",)
elements = ('Air','Water','Fire','Light','Land')

print(head)
print(elements)
print(elements[3])
#elements[0]='Ice' #Cannot change content of a tuple. Tuples are immutable.
print(elements[-1])
print(elements[4])
print(elements[5]) #shows tuple index out of range.

# ==============OUTPUT==============
# ('CEO',)
# ('Air', 'Water', 'Fire', 'Light', 'Land')
# Light
# Land
# Land
# Traceback (most recent call last):
#   File "C:/Users/kush_pc/PycharmProjects/MyPythonProject2/Assignments/assignment28.py", line 11, in <module>
#     print(elements[5]) #shows tuple index out of range.
# IndexError: tuple index out of range
