# Question 3
# get the user's age and income
age = int(input("Enter your age: "))
income = float(input("Enter your income: "))

# check the conditions and print the right message
if age < 18:
print("You must be at least 18 years old to qualify.")
elif age >= 18 and income < 30000:
print("You qualify for financial assistance.")
else:
print("Your income is too high to qualify for assistance.")
