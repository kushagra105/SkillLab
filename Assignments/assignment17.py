# Assignment 17 : 
counter = 1
while counter <= 3:
    print(counter)
    counter += 1
print("End of Program 1")
print("To find the sum of first 10 integers:")
result = 0
for value in range(1,11):
    result = result + value
print("Sum:",result)
print("End of Program 2")
number = 1
result = 0
while number < 5:
    result = result + number
    number = number + 1
print(result)
print("End of program 3")
result = 0
for index in range(40, 10, -2):
    if(index % 5 == 0):
        result = result + index
        print(result)
print("End of program 4")
amount = 100.0
interest = 0.0
months = 1
while months < 6:
    interest = amount * 0.2
    amount = amount + interest
    months += 1
print(amount)
print("End of Program 5")

# ======================OUTPUT=========================
# 1
# 2
# 3
# End of Program 1
# To find the sum of first 10 integers:
# Sum: 55
# End of Program 2
# 10
# End of program 3
# 40
# 70
# 90
# End of program 4
# 248.83200000000002
# End of Program 5