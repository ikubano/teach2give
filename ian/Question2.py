#Question 2: Fibonacci Sequence
#Write a program to generate the Fibonacci sequence up to 100

n = 10
num1 = 0
num2 = 1
next_number = num2 
count = 1

while count <= n:
	print(next_number, end=" ")
	count += 1
	num1, num2 = num2, next_number
	next_number = num1 + num2
print()
