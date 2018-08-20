n = int(input("Enter number of elements : "))
list1 = []
list2 = []
for i in range (n):
    a=input("Enter the furniture")
    list1.append(a)
for i in range (n):
    b=int(input("Enter the price of the furniture"))
    list2.append(b)
c=input("Enter the furniture to be serched")
for i in range(n):
    if list1[i] == c:
        q=int(input("Enter the quantity"))
        v=list2[i]*q
        print("The total price of the consignment is",v)
        exit(0);
print("No furniture found")
