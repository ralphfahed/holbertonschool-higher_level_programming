#!/usr/bin/python3

def roman_to_int(roman_string):
    # Check if the input is a valid string, and not None
    if not isinstance(roman_string, str) or roman_string is None:
        return 0  # Return 0 if input is invalid (not a string or None)

    # A dictionary that maps Roman numeral characters to their integer values
    roman_dict = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
    }

    total = 0  # This will store the resulting integer value
    prev_value = 0  # To track the value of the previous Roman numeral character

    # Iterate through the Roman numeral string in reverse order (starting from the last character)
    for char in reversed(roman_string):
        # Get the integer value of the current Roman numeral character
        value = roman_dict.get(char, 0)  # Default to 0 if character is invalid

        # If the character is invalid (not in roman_dict), return 0
        if value == 0:
            return 0

        # Check if the current value is smaller than the previous value
        # (This handles cases like IV, IX, etc. where we subtract the smaller number)
        if value < prev_value:
            total -= value  # Subtract if the current value is less than the previous value
        else:
            total += value  # Add if the current value is greater than or equal to the previous value

        # Update prev_value for the next iteration
        prev_value = value

    # Return the total integer value corresponding to the Roman numeral
    return total
