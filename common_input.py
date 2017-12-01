"""
Methods to get specifically formatted user values via the input() prompt.
"""


def input_int(prompt, min_val, max_val):
    """
    Gets integer user input, between the specified values.  User is reprompted is value is out of range
    :param prompt: Prompt to display to the user for the input
    :param min_val: Minimum accepted value
    :param max_val: Maximum accepted value
    :return: User-entered integer, between the specified values.
    """
    error_prompt = f"Please enter a whole number between {min_val} and {max_val}"
    while True:
        try:
            result = int(input(prompt))
            if result < min_val or result > max_val:
                print(error_prompt)
            else:
                return result
        except ValueError:
            print(error_prompt)


def input_yes_no(prompt):
    """
    Prompts the user for a yes or no response.  Only the first letter is checked, so "yes", "yep", and "yellow"
    will all evaluate to True.  User will be reprompted for invalid input.
    :param prompt: Prompt to display to the user for the input
    :return: True if the user enters yes, False if the user enters no
    """
    while True:
        result = input(prompt)
        if result and result[0] == 'y':
            return True
        elif result and result[0] == 'n':
            return False
        else:
            print("Not understood - please respond yes or no.")


def input_letter(prompt, valid_values=None):
    """
    Prompts the user for a single letter.  An optional set of valid letters can be specified, otherwise any
    character (not just letters) are accepted.  Only the first letter is evaluated: "apple" will be treated
    the same as "a".  Case-insenstive.  User will be reprompted for invalid input.
    :param prompt: Prompt to display to the user for the input
    :param valid_values: Optional list of valid letters.
    :return: User entered valid letter
    """
    while True:
        result = input(prompt)[0].upper()
        if valid_values and valid_values.find(result) >= 0:
            return result
        else:
            print("That's not a valid choice.  Please try again.")
