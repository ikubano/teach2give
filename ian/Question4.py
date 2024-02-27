#Question 4: Capitalize Words
#Write a program that accepts a string as input, capitalizes the first letter of each word in the string, and then returns the result string


def capitalize_first_letter_of_each_word(s):
   
    s = input("Enter a string: ")

    words = s.split()

    for i in range(len(words)):
        
        words[i] = words[i][0].upper() + words[i][1:]

    return ' '.join(words)

result = capitalize_first_letter_of_each_word("")
print("Result:", result)

