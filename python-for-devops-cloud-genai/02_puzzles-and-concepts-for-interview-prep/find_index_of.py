# Write a python code to find an index of a string, like S="This is a table". Find the index of "is" ?

s = "This is a table"
substring = "is"

try:
    index = s.index(substring)
    print("Substring found at index:", index)
except ValueError:
    print("Substring not found in the string.")
