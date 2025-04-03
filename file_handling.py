# File handling allows us to read and write files in Python.
#Writing to a File,Use "w" mode to write to a file
file = open("sample.txt", "w")
file.write("Hello, this is a file!")
file.close()

#  Reading from a File ,Use "r" mode to read from a file.
file = open("sample.txt", "r")
print(file.read())
file.close()

#  Appending to a File ,Use "a" mode to add new text without deleting the old content.
file = open("sample.txt", "a")  
file.write("\nThis is an extra line.")  
file.close()

# using with open() 
#his automatically closes the file after use.
with open("sample.txt", "r") as file:
    content = file.read()
    print(content)  # No need to call file.close()
