# Write a python program to perform below mentioned operations
customer_details = {1001:"John", 1004:"Jill",1005:"Joe",1003:"Jack"}
print ("Customer details are : ",customer_details)
print ("Number of customers are : ",len(customer_details))
print ("Customer names in ascending order : ",sorted(customer_details.values()))
del(customer_details[1005])
print ("Customer details after deleting customer 1005 : ",customer_details)
customer_details[1003] = "Mary"
print ("Customer details after updating the name of customer with customer id : 1003 are : ",customer_details)
if((1002 in customer_details) == False):
    print ("Customer with customer id 1002 doesn't exist")
elif((1002 in customer_details) == True):
    print ("Customer with customer id 1002 exist")