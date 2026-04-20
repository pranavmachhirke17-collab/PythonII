file = open("file.txt", "w")
file.write("Hello, This is the first line.\n")
file.write("This is the second line.\n")
file.close()
print("Data written successfully.\n")

file = open("file.txt", "r")
content = file.read()
print("Content of the file:", content)
file.close()

file = open("file.txt", "a")
file.write("This is a third line.\n")
print("Data appended successfully.\n")

file = open("file.txt", "r")
content_updated = file.read()
print("Updated content of the file:", content_updated)
file.close()