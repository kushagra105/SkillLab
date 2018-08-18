#Program Description : Write a python program to generate first n fibonacci series
def fibonacci(n):
    if(n<2):
        return n
    else:
        return (fibonacci(n-1)+fibonacci(n-2))
n = int(input("Enter number of terms:"))
print("Fibonacci sequence:")
for i in range(n):
<<<<<<< HEAD
    print (fibonacci(i))
=======
    print(fibonacci(i))
>>>>>>> a9a0c7d9ec0c864a0a87a82454e4b18250a6147b
