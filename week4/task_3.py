
# Develop a program that handles multiple types of exceptions (e.g., FileNotFoundError, ValueError)
# and logs errors to a file.

def file_errors(filename):
    try:
        with open(filename, 'r') as file:   
            data = file.read()
            print("File contents:", data)
            
    except FileNotFoundError as e:
        print(f"FileNotFoundError: {e}")
        print("Error: File not found!")


def process_value(input_value):
    try:
        num = int(input_value)
        print(f"Converted to integer: {num}")

    except ValueError as e:
        print(f"ValueError: {e}")
        print("Error: Invalid input for integer conversion!")


filename = "non_existent_file.txt"   # Handle FileNotFoundError
file_errors(filename)


user_input = "abc"  # Handle ValueError :Invalid input for integer conversion
process_value(user_input)
