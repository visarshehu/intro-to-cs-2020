print "Hello to my salary calculator v.0.1" 
print "Please input the gross salary!" 
gross_salary = input()
 
if gross_salary<=21776:
	print "Salary must be higher than the minimum (21776)"
	exit()

print "=====================================" 
print "The input salary is: ", gross_salary
#taxes defined as percentage
pension_tax=18.8
healthcare_tax=7.5
employment_tax=1.2
additional_tax=0.5

pension = gross_salary * pension_tax / 100
healthcare = gross_salary * healthcare_tax / 100
employment = gross_salary * employment_tax / 100
additional = gross_salary * additional_tax / 100

print "Pension tax:\t ", pension
print "Healthcare tax: \t", healthcare
print "Employement tax: \t", employment
print "Additional tax: \t", additional
total_taxes = pension + healthcare + employment + additional
print "TOTAL TAXES: \t", total_taxes
gross_without_taxes=gross_salary - total_taxes
print "Gross without taxes: \t", gross_without_taxes
tax_release=8228
taxable_income = gross_without_taxes - tax_release
personal_tax = 10
personal=taxable_income * personal_tax / 100
print "Taxable income: \t", taxable_income
print "Personal tax: \t", personal
print "Total taxes (including personal):\t", total_taxes+personal
net_salary = gross_without_taxes - personal
print "NET SALARY: \t", net_salary
