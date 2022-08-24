'''# q1
a = float(input("CM: "))

if a > 0:
    print(a*0.393701)
else:
    print("Error")
    '''

''''# q2
a = int(input("How many items did you buy :"))

if a < 10:
    print("Your total is", a*120, "rupees")
elif a > 10 and a < 99:
    print("Your total is", a*100, "rupees")
else:
    print("Your total is", a*70, "rupees")
'''

'''# q3
a = int(input("Enter first side: "))
b = int(input("Enter second side: "))
c = int(input("Enter third number"))

con1 = a+b>c
con2 = b+c>a
con3 = c+a>b

if con1 == True and con2 == True and con3 == True:
    print("This will  form a triangle")
else:
    print("This will not form a triangle")'''

''''# q4
a = int(input("Enter the number of hours between 1-12: "))
b = int(input("Enter number of hours ahead: "))
c = (a+b)

if c < 0:
    print(c * -1)
elif a + b > 12:
    print((a + b)-12)
else:
    print(c)'''

'''# q5
a = int(input("Enter number"))
b = int(input("Enter second number"))
c = a%b

if c == 0:
    print("First number is divisible by the second number")
else:
    print("First number is not divisible by second number")'''

''''# q6
a = int(input("Enter digit"))

if a == 0:
    print("Zero")
elif a == 1:
    print("One")
elif a == 2:
    print("Two")
elif a == 3:
    print("Three")
elif a == 4:
    print("Four")
elif a == 5:
    print("Five")
elif a == 6:
    print("Six")
elif a == 7:
    print("Seven")
elif a == 8:
    print("Eight")
elif a == 9:
    print("Nine")
else:
    print("Error")'''

'''# q7
n = int(input("Enter number"))
n2 = (n*2)-1
for i in range(n2, 0, -2):
    print(i)'''

'''# q8
a = 1
a2 = a+3
for u in range(1, 41, 3):
    print(u)
b = 1
for u in range (1, 41, 3):
    if u%2 == 0:
        print(-u)
    else:
        print(u)'''

'''# q9
a = int(input("Enter number 1: "))
b = int(input("Enter number 2:"))
c = int(input("Enter number 3:"))
d = int(input("Enter number 4:"))
e = int(input("Enter number 5:"))

avg = (a+b+c+d+e)/5
print(avg)'''

'''# q10
a = int(input("Enter number 1: "))
b = int(input("Enter number 2:"))
c = int(input("Enter number 3:"))
d = int(input("Enter number 4:"))
e = int(input("Enter number 5:"))

if a > b and a > c and a > d and a > e:
    print("Number 1 is the greatest")
elif b > a and b > c and b > d and b > e:
    print("Number 2 is the greatest")
elif c > a and c > b and c > d and c > e:
    print("Number 3 is the greatest")
elif d > a and d > b and d > c and d > e:
    print("Number 4 is the greatest")
else:
    print("Number 5 is the greatest")'''
