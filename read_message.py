

file_name = "my_message.txt"

with open(file_name, "r") as file:
    contents = file.read()
    lines = contents.split("\n") # converts string to list
    print("THERE ARE", len(lines), "LINES IN THIS FILE")
    for line in lines:
        print("LINE:", line)

        