# Assignment 13 : 

bill_id=1001
customer_id=101
bill_amount=int(input("Enter the bill amount "))
if bill_amount > 1000:
    bill_amount=bill_amount-(bill_amount*0.05)
elif bill_amount > 500:
    bill_amount = bill_amount - (bill_amount * 0.05)
else:
    bill_amount = bill_amount - (bill_amount * 0.01)
print("bill_id " ,bill_id)
print("customer_id:",customer_id)
print("bill_amount Rs",bill_amount)

# ======================OUTPUT=========================
# Enter the bill amount 1200
# bill_id  1001
# customer_id: 101
# bill_amount Rs 1140.0
