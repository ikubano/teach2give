#Question 3: Power of Two
#Write a program that takes an integer as input and returns true if the input is a power of two.


n = int(input("Enter number: "))
count = 0

for m in range(n):
    if n == 2 ** m:
        count += 1

if count == 0:
    print(False)
else:
    print(True)
