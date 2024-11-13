# 3. Write a function in Python to count uppercase character in a text file “ABC.txt”
def count_uppercase_characters(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()  # Read the entire file content
            uppercase_count = sum(1 for char in content if char.isupper())  # Count uppercase characters
            print(f"Total number of uppercase characters: {uppercase_count}")
    except FileNotFoundError:
        print(f"The file '{filename}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Call the function with the filename
count_uppercase_characters("E:\examplepythonclass\\abc.txt")
