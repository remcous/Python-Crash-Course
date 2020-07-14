file_name = 'text_files/pi_digits.txt'

# Read entire file contents as a string
with open(file_name) as file_object:
    contents = file_object.read()
    print(contents.rstrip())

print()

# Read the file line by line
with open(file_name) as file_object:
    for line in file_object:
        print(line.rstrip())

print()

# Store lines in a list
with open(file_name) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())