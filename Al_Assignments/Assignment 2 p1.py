celsius = float(input("Q1) Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius}°C is equal to {fahrenheit}°F\n")

length = float(input("Q2) Enter length: "))
width = float(input("Q2) Enter width: "))
print(f"Area of rectangle: {length * width}\n")

P = float(input("Q3) Enter principal: "))
R = float(input("Q3) Enter rate (%): "))
T = float(input("Q3) Enter time (years): "))
CI = P * (1 + R/100) ** T - P
print(f"Compound Interest: {CI}\n")

length = float(input("Q4) Enter length: "))
width = float(input("Q4) Enter width: "))
print(f"Perimeter: {2 * (length + width)}\n")

a = float(input("Q5) Enter first number: "))
b = float(input("Q5) Enter second number: "))
c = float(input("Q5) Enter third number: "))
print(f"Average: {(a + b + c) / 3}\n")

num = float(input("Q6) Enter a number: "))
print(f"Square: {num ** 2}")
print(f"Cube: {num ** 3}\n")

n = int(input("Q7) Enter total candies: "))
k = int(input("Q7) Enter total students: "))
print(f"Each student gets {n // k} candies.")
print(f"Candies left: {n % k}\n")

cp = float(input("Q8) Enter cost price: "))
sp = float(input("Q8) Enter selling price: "))
if sp > cp:
    print(f"Profit: {sp - cp}\n")
elif cp > sp:
    print(f"Loss: {cp - sp}\n")
else:
    print("No Profit No Loss\n")

marks = []
for i in range(1, 6):
    marks.append(float(input(f"Q9) Enter marks of subject {i}: ")))
total = sum(marks)
percentage = (total / 500) * 100
average = total / 5
print(f"Total Marks: {total}")
print(f"Percentage: {percentage}%")
print(f"Average: {average}\n")

basic = float(input("Q10) Enter basic salary: "))
hra = 0.20 * basic
da = 0.15 * basic
total_salary = basic + hra + da
print(f"HRA: {hra}")
print(f"DA: {da}")
print(f"Total Salary: {total_salary}\n")

age_years = int(input("Q11) Enter age in years: "))
print(f"Age in months: {age_years * 12}")
print(f"Age in days (approx.): {age_years * 365}\n")

usd = float(input("Q12) Enter amount in USD: "))
rate = 280
print(f"{usd} USD = {usd * rate} PKR\n")

n = int(input("Q13) Enter a number: "))
print(f"Sum: {n * (n + 1) / 2}\n")

total_q = int(input("Q14) Enter total questions: "))
correct_q = int(input("Q14) Enter correct answers: "))
print(f"Score: {(correct_q / total_q) * 100}%\n")

distance = float(input("Q15) Enter distance (km): "))
time = float(input("Q15) Enter time (hours): "))
print(f"Speed: {distance / time} km/h\n")

weight = float(input("Q16) Enter weight (kg): "))
height = float(input("Q16) Enter height (m): "))
print(f"BMI: {weight / (height ** 2)}\n")

minutes = int(input("Q17) Enter total minutes: "))
print(f"{minutes} minutes = {minutes // 60} hours and {minutes % 60} minutes")
