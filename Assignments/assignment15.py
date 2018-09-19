# Assignment 15 : 
emp_id = int(input("Enter ID"))
salary = int(input("Enter Salary"))
allowances = 6000
if salary > 10000:
    salary = salary + allowances
    salary = salary - (salary * 0.2)
else:
    print("No Salary Deductions")
print("Employee ID", emp_id)
print("Salary after tax deductions", salary)

# ======================OUTPUT=========================
# wrong