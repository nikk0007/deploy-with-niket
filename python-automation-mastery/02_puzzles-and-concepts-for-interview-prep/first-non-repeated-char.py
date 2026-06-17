def find_first_non_repeated_char(s):
    char_count = {}
    # Count the occurrences of each character in the string
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1

    # Find the first non-repeated character
    for char in s:
        if char_count[char] == 1:
            return char

    # Return None if no non-repeated character found
    return None

# Example usage:
input_string = "abracadabra"
result = find_first_non_repeated_char(input_string)
print("First non-repeated character:", result)  # Output: 'c'
