# Assiganment 32 : Write a program to sort the elements using bubble sort and display them in descemding order
n = int(input("Enter number of elements : "))
list1 = []
for i in range (n):
    a=int(input("Enter element : "))
    list1.append(a)
for i in range(n-1):
    for j in range(n-1):
        if(list1[j]<list1[j+1]):
            temp = list1[j]
            list1[j] = list1[j+1]
            list1[j+1] = temp
for i in range(n):
    print(list1[i])

# ====================OUTPUT==================
# Enter number of elements : 4
# Enter element : 4
# Enter element : 3
# Enter element : 2
# Enter element : 1
# 4
# 3
# 2
# 1