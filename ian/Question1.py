#Question 1: FizzBuzz
#Write a program that prints the numbers from 1 to 100. For multiples of 3, print "Fizz"; for multiples of 5, print "Buzz"; and for numbers that are multiples of both 3 and 5, print "FizzBuzz"

def fizz_buzz():
    output = ["FizzBuzz" if i % 3 == 0 and i % 5 == 0 else "Fizz" if i % 3 == 0 else "Buzz" if i % 5 == 0 else i for i in range(1, 101)]
    for item in output:
        print(item)

fizz_buzz()
