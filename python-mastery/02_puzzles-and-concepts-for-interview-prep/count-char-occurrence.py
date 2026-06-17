def count_characters(s):
    char_count = {}
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1
    return char_count

# Example usage:
input_string = "hello"
result = count_characters(input_string)
print(result)  # Output: {'h': 1, 'e': 1, 'l': 2, 'o': 1}