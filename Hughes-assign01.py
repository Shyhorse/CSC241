#problem 1
s1 ='&'
s2 = '#'

a=(s1*2+s2)
b=(s1*4+s2*2)
c=(s1*3+s2)*2
d=(s1*10)
e=(s1*2+s2*2)*3
f=(s1*5+s2*5)*3
 

#spacer
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)

#problem 2

first =input("Please input your first name :")
last = input("Please input your last name :")
print(f"Your name is {last}, {first}")
#print("Your name is ", last, ", ", first)

#spacer


#problem 3
bill= float(input("Enter bill here :"))
tip= int(input("Enter tip amount here :"))
Total= (float(bill*(tip/100)+bill))
print(Total)
print(f"The tip for a bill of {bill} at {tip}% is {Total}")