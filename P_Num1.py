#1). Write a program to reverse an integer in Python.

a=123
temp=0
while a>0:
	b = a % 10
	temp = temp * 10 + b
	a =a//10
print("reverse number is :" + str(temp))