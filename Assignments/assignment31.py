#Assignment 31 : Write a python program to generate first n fibonacci series
def fibonacci(n):
    if(n<2):
        return n
    else:
        return (fibonacci(n-1)+fibonacci(n-2))
n = int(input("Enter number of terms: "))
print("Fibonacci sequence: ")
for i in range(n):
    print (fibonacci(i))

# ================OUTPUT==============
# Enter number of terms: 5
# Fibonacci sequence:
# 0
# 1
# 1
# 2
# 3