# Question 1
# get the two test scores
test1 = float(input("Enter first test score: "))
test2 = float(input("Enter second test score: "))

# calculate average
avg = (test1 + test2) / 2

# determine grade
if avg >= 90:
grade = "A"
elif avg >= 75:
grade = "B"
elif avg >= 60:
grade = "C"
else:
grade = "D"

print("Average:", avg)
print("Grade:", grade)

