"""
Count the frequency of every character in a string and return it.
"""

name = "Shakeel n Nawaz"

def frequency_char(string):
    frequency = {}
    for char in string:
        if char.isalpha():
            frequency[char.lower()] = frequency.get(char.lower(),0) + 1
    return frequency

print(frequency_char(name))


# or


freq = {}
for i in name:
    if i.isalpha():    
        if i.lower() in freq:
            freq[i.lower()] += 1
        else:
            freq[i.lower()] = 1

print(freq)