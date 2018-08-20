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
