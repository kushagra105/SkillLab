# Assignment 42 : 

empid=[1001,1002,1003,1004,1005]
id=input("Enter employee id ")
try:
    id[2] = 1002
except :
    print("Already present")

p_id=input("Which employee id you want to search? ")

try:
    print(empid[p_id])
except:
    print("Not present")

# ===================OUTPUT====================
# Enter employee id 1002
# Already present
# Which employee id you want to search? 5
# Not present