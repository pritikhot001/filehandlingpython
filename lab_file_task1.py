
#
'''1. Write a function in python to read the content from a text file "ABC.txt" line by line and display the same on screen. '''

#opens the file anudip.txt in write mode
fileobj = open("E:\examplepythonclass\\abc.txt","w")
if fileobj:
    print("File Created successfully")

with open("E:\examplepythonclass\\abc.txt", "r") as file:
    for line in file:
        print(line.strip()) # Strip newline characters

# Specify the path to the file you want to search in
file_path = "E:\examplepythonclass\\abc.txt"
# Specify the keyword or phrase you want to search for
search_keyword = input("Enter the text which you want to search: ")
with open(file_path, "r") as file:
    # Read each line of the file
    for line in file:
        # Check if the keyword exists in the line (case-insensitive search)
        if search_keyword.lower() in line.lower():
            print(line.strip()) # Print matching lines without leading/trailingwhitespace
print(f"Search for '{search_keyword}' completed.")                           




