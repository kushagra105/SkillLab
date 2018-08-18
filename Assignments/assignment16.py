emp_id = int(input("Enter ID"))
salary = int(input("Enter Salary"))
allowances = 6000
if 5000 < salary < 10000:
    salary = salary + allowances
    salary = salary - (salary * 0.1)
elif 10000 < salary < 20000:
    salary = salary + allowances
    salary = salary - (salary * 0.2)
elif 20000 < salary:
    salary = salary + allowances
    salary = salary - (salary * 0.3)
else:
    print("No Salary Deductions")
print("Employee ID", emp_id)
print("Salary after tax deductions", salary)
