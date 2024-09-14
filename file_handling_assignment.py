
try:
    with open('my_file.txt', 'w') as file:
        file.write("it is fun studing PLP.\n")
        file.write("Thanks alot to all the instructors.\n")
        file.write("For good guidance through the course.\n")
except Exception as e:
    print(f"An error occurred while writing to the file: {e}")


try:
    with open('my_file.txt', 'r') as file:
        contents = file.read()
        print("File Contents:")
        print(contents)
except FileNotFoundError:
    print("The file 'my_file.txt' does not exist.")
except PermissionError:
    print("You do not have permission to read 'my_file.txt'.")
except Exception as e:
    print(f"An error occurred while reading the file: {e}")

# Append to the file
try:
    with open('my_file.txt', 'a') as file:
        file.write("Python is greate \n")
        file.write("Am enjoing this\n")
        file.write("I hope to be better\n")
except PermissionError:
    print("You do not have permission to append to 'my_file.txt'.")
except Exception as e:
    print(f"An error occurred while appending to the file: {e}")
