# Question 2
# get the two test scores
test1 = float(input("Enter first test score: "))
test2 = float(input("Enter second test score: "))

# calculate average
avg = (test1 + test2) / 2

# determine grade using logic operators
if avg >= 90:
grade = "A+"
elif avg < 90 and avg > 80:
grade = "A-"
elif avg < 80 and avg > 70:
grade = "B+"
elif avg < 70 and avg > 60:
grade = "B-"
elif avg < 60 and avg > 55:
grade = "C"
else:
grade = "D"

print("Average:", avg)
print("Grade:", grade)
