"""
CP1404/CP5632 - Practical
Password checker "skeleton" code to help you get started
"""
MIN_LENGTH = 5
MAX_LENGTH = 15
SPECIAL_CHARS_REQUIRED = True
SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"
def main():
    """Program to get and check a user's password."""
    print("Please enter a valid password")
    print("Your password must be between", MIN_LENGTH, "and", MAX_LENGTH,
          "characters, and contain:")
    print("\t1 or more uppercase characters")
    print("\t1 or more lowercase characters")
    print("\t1 or more numbers")
    if SPECIAL_CHARS_REQUIRED:
        print("\tand 1 or more special characters: ", SPECIAL_CHARACTERS)
    password = input("> ")
    while not is_valid_password(password):
        print("Invalid password!")
        password = input("> ")
    print("Your {}-character password is valid: {}".format(len(password),
                                                           password))
    print("*"*len(password))

def is_valid_password(password):
    count_lower = 0
    count_upper = 0
    count_digit = 0
    count_special = 0
    """Determine if the provided password is valid."""
    # TODO: if length is wrong, return False
    if len(password) < 5 or len(password) > 15:
        return False
    else:
        for char in password:
            # TODO: count each kind of character (use str methods like isdigit)
            if char.isupper():
                count_upper += 1
            elif char.islower():
                count_lower += 1
            elif char.isdigit():
                count_digit += 1
    # TODO: if any of the 'normal' counts are zero, return False
        if count_upper <1 or count_lower <1 or count_digit <1:
            return False
        else:
            for char in password:
                if char in SPECIAL_CHARACTERS:
                    count_special += 1
            if count_special < 1:
                return False
            else:
                return True

main()