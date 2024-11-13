#4. Write a function display_words() in python to read lines from a text file "story.txt", and display those words, which are less than 4 characters.

def display_words(filename):
    try:
        with open(filename, 'r') as file:
            for line in file:  # Read the file line by line
                words = line.split()  # Split each line into words
                short_words = [word for word in words if len(word) < 4]  # Find words with less than 4 characters
                print(" ".join(short_words))  # Display those words
    except FileNotFoundError:
        print(f"The file '{filename}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Call the function with the filename
display_words("E:\examplepythonclass\\abc.txt")
