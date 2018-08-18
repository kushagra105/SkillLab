bill_id=1001
customer_id=101
bill_amount=int(input("Enter the bill amount"))
if bill_amount > 500:
    bill_amount=bill_amount-(bill_amount*0.02)
else:
    bill_amount = bill_amount - (bill_amount * 0.01)
print("bill_id " ,bill_id)
print("customer_id:",customer_id)
print("bill_amount Rs",bill_amount)