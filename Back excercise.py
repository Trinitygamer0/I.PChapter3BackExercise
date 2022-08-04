''' # q1
p = int(input("Principal amount :"))
i = float(input("Enter Interest rate :"))
t = float(input("Enter time in years :"))
ans1 = (print(float((p*i*t)/100)))
'''

'''# q2
d1 = int(input("Enter Temperature on day1 :"))
d2 = int(input("Enter Temperature on day2 :"))
d3 = int(input("Enter Temperature on day3 :"))
d4 = int(input("Enter Temperature on day4 :"))
d5 = int(input("Enter Temperature on day5 :"))
d6 = int(input("Enter Temperature on day6 :"))
d7 = int(input("Enter Temperature on day7 :"))
ans2 = (print(float((d1+d2+d3+d4+d5+d6+d7)/7)))
'''

'''# q3
print("calculate the equation 4x**4 + 3y**3 + 9*z + 6pi")
print(6*3.14)
x = int(input("X :"))
y = int(input("Y :"))
z = int(input("Z :"))
xyz = 4*(x**4)+3*(y**3)+9*z+(6*3.14)
print(xyz)
'''

'''# q4
print("Convert seconds into minutes")
sec = int(input("Enter seconds :"))
conversion = print(sec//60,"Minutes",sec%60, "Seconds")
'''

'''# q5
day = int(input("Enter day:"))
month = int(input("Enter month:"))
if month == 1:
    print("day of the year is :", day)
elif month > 1 and month < 13:
    print("day of the year is :", (30*month)+(day-30))
elif month >12:
    print("error")
'''
