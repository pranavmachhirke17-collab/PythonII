filename = input("Enter your file:")

try: 
    with open(filename,"r") as file:
        contents = file.read()
        print("file opened succsessfully !")
        print("Contents of the file:")
        print(contents)

except FileNotFoundError:
    print(f"error: the file {filename} does not exist.")

except PermissionError:
    print(f"error: the file {filename} does not hage permission. ")