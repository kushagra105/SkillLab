# Assignment 15 : 
emp_id = 1001
salary = 15000
allowances = 6000
if salary > 10000:
    gross_salary = salary + allowances
    net_salary = salary - (salary * 0.2)
else:
    print("No Salary Deductions")
print("Employee ID", emp_id)
print("Basic salary ",salary)
print("Gross salary ",gross_salary)
print("Allowances ",allowances)
print("Income tax ",(0.2*gross_salary))
print("Salary after tax deductions ",net_salary)

# ======================OUTPUT=========================
# Employee ID 1001
# Basic salary  15000
# Gross salary  21000
# Allowances  6000
# Income tax  4200.0
# Salary after tax deductions  12000.0
