import sys

def count_code_lines(filename):
    
    code_lines = 0

    with open(filename, 'r') as file:
        for line in file:
            stripped_line = line.strip()
            # Skip empty lines and comment lines
            if stripped_line and not stripped_line.startswith('#'):
                code_lines += 1

    return code_lines


def main():
    # Check command-line arguments
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    filename = sys.argv[1]

    # Validate file extension
    if not filename.endswith('.py'):
        sys.exit('Not a Python file')

    # Count lines and handle errors
    try:
        line_count = count_code_lines(filename)
        print(line_count)
    except FileNotFoundError:
        sys.exit('File does not exist')


if __name__ == "__main__":
    main()
