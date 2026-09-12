"""
Reverse a string without using [::-1] or the reversed() function.


String = "Shakeel Nawaz"

2 Outputs:

->      zawaN leekahS

->      leekahS zawaN

"""

def rev_string(val):
    reversed_string = ""
    for char in val:
        reversed_string = char + reversed_string
    return reversed_string

a = "Shakeel Nawaz"
print(rev_string(a))            # Output:      zawaN leekahS


res = []
for i in a.split(" "):
    res.append(rev_string(i))
res = " ".join(res)
print(res)                      # Output:       leekahS zawaN