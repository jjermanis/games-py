
def input_int(prompt, min_val, max_val):
    """
    :return: An int from the user input, between min and max (inclusive)
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
    Returns True or False depending on user input.  User is reprompted on invalid input
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
