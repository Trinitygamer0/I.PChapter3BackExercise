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




