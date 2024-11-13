'''
2. Write a function in Python to count and display the total number of words in a text file “ABC.txt”'''
def count_words_in_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()  # Read the entire file content
            words = content.split()  # Split the content into words
            total_words = len(words)  # Count the total number of words
            print(f"Total number of words: {total_words}")
    except FileNotFoundError:
        print(f"The file '{filename}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Call the function with the filename
count_words_in_file("E:\examplepythonclass\\abc.txt")
