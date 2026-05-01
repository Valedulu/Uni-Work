def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):

    return ( has_valid_length(s) and
        starts_with_letters(s) and
        has_valid_characters(s) and
        has_valid_number_placement(s))


def has_valid_length(s):
    return 2 <= len(s) <= 6


def starts_with_letters(s):
    return len(s) >= 2 and s[0].isalpha() and s[1].isalpha()


def has_valid_characters(s):
    return s.isalnum()


def has_valid_number_placement(s):
    found_number = False

    for char in s:
        if char.isdigit():

            if not found_number and char == '0':
                return False
            found_number = True
        elif found_number:

            return False

    return True


if __name__ == "__main__":
    main()
