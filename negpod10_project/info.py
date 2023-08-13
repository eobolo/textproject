#!/usr/bin/python3
from employer_data import *
from employers import Employers
from employee_data import *
from employees import Employees

employer = read_employer_data_from_file()
employee = read_employee_data_from_file()
print(employee[0].email)
print(employee[0].name)
print(employee[0].password, employee[0].dob)
print(employee[0].age, employee[0].phnum)
