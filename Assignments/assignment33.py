#Write a Python program to calculate and display the bill amount to be paid by the customer
# based on the furniture bought and quantity purchased
n = int(input("Enter number of elements : "))
list1 = []
list2 = []
print("Enter the name of furniture")
for i in range (n):
    a=input()
    list1.append(a)
print("Enter the price of furniture")
for i in range (n):
    b=int(input())
    list2.append(b)
c=input("Enter the furniture to be serched")
for i in range(n):
    if list1[i] == c:
        q=int(input("Enter the quantity"))
        v=list2[i]*q
        print("The total price of the consignment is ",v)
        exit(0);
print("No furniture found")


# ========================OUTPUT=====================
# Enter number of elements : 5
# Enter the name of furniture
# q
# w
# e
# r
# t
# Enter the price of furniture
# 12
# 12
# 12
# 12
# 12
# Enter the furniture to be serchedr
# Enter the quantity8
# The total price of the consignment is  96