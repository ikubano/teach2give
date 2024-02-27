#Question 6: Count Vowels
#Write a program that counts the number of vowels in a sentence.

def count_vowels(sentence):
 
    vowels = {'a', 'e', 'i', 'o', 'u'}

    count = 0

    for c in sentence:
    
        if c.lower() in vowels:
        
            count += 1
            
    return count

user_input = input("Enter a sentence: ")

result = count_vowels(user_input)
print("Number of vowels in the sentence:", result)
