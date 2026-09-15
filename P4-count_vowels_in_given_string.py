"""
Count Number of Vowels in Given String
"""

string = "Shakeel Nawaz"

# Brute Force
vowels = ['a','e','i','o','u','A','E','I','O','U']
total_vowels = 0
for char in string:
    if char in vowels:
        total_vowels +=1

print(total_vowels)


# using tuple method
vowels = ['a','e','i','o','u','A','E','I','O','U']
total_vowel = sum(1 for char in string if char in vowels)               # (1,1,1,1,1)
print(total_vowel)