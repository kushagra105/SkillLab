# Assignment 14 : 

bill_id=1001
customer_id=int(input("Enter Customer id "))
bill_amount=int(input("Enter the bill amount "))
discounted_bill_amount = 0.0
print("bill_id " ,bill_id)
print("customer_id:",customer_id)
print("bill_amount Rs",bill_amount)
if 100 < customer_id < 1000:
    if bill_amount >= 500:
        discounted_bill_amount = bill_amount-(bill_amount*0.1)
        print("Discounted bill amount : Rs. %f" %discounted_bill_amount)
    else:
        print("No discount")
else: 
    print("Invalid customer id, customer id must be between 101 and 1000")

# ======================OUTPUT=========================
# Enter Customer id 101
# Enter the bill amount 200
# bill_id  1001
# customer_id: 101
# bill_amount Rs 200
# No discount

