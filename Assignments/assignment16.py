#Assignment 16 : 

emp_id = int(input("Enter ID "))
salary = int(input("Enter Salary "))
print("Employee ID", emp_id)
allowances = 6000
print("Allowances ",allowances)
gross_salary = salary + allowances
print("Gross salary",gross_salary)
net_salary = 0
if 5000 < salary < 10000:
    net_salary = gross_salary - (gross_salary * 0.1)
    print("Income tax percentage : 10%")
    print("Income tax",(0.1*gross_salary))
elif 10000 < salary < 20000:
    net_salary = gross_salary - (gross_salary * 0.2)
    print("Income tax percentage : 20%")
    print("Income tax",(0.2*gross_salary))
elif salary > 20000:
    net_salary = gross_salary - (gross_salary * 0.3)
    print("Income tax percentage : 30%")
    print("Income tax",(0.3*gross_salary))
else:
    print("No Salary Deductions")
print("Net Salary ", net_salary)

# ======================OUTPUT=========================
# Enter ID 1001
# Enter Salary 21000
# Employee ID 1001
# Allowances  6000
# Gross salary 27000
# Income tax percentage : 30%
# Income tax 8100.0
# Net Salary  18900.0
