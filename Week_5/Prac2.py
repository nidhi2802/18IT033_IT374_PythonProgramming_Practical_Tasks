def get_salary_details(basic_salary):
  MA = 100
  TA = 400
  DA = basic_salary*0.7
  TS = basic_salary+DA+MA+TA
  salary = dict();
  salary['DA'] = DA
  salary['MA'] = MA
  salary['TA'] = TA
  salary['Total Salary'] = TS
  return salary

income = int(input("Enter basic salary: "))
salary_details = get_salary_details(income)
print("DA: {}\nMA: {}\nTA: {}\nTotal Salary: {}".format(salary_details["DA"],salary_details["MA"],salary_details["TA"],salary_details["Total Salary"]))
