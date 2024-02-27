#Question 5: Reverse Integer
#Write a program that takes an integer as input and returns an integer with reversed digit ordering.

def reverse_digits(n):

    n = int(input("Enter an integer: "))

    s = str(n)

    reversed_s = s[::-1]

    return int(reversed_s)

result = reverse_digits(0)
print("Result:", result)
