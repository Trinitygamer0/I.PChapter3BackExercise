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
