# Assignment 14 : 

bill_id=1001
customer_id=int(input("Enter Customer id"))
bill_amount=int(input("Enter the bill amount"))
if 100 < customer_id < 1000:
    if bill_amount > 500:
        bill_amount=bill_amount-(bill_amount*0.1)
print("bill_id " ,bill_id)
print("customer_id:",customer_id)
print("bill_amount Rs",bill_amount)

# ======================OUTPUT=========================
#wrong answer
