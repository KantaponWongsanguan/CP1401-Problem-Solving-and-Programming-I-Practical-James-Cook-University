
# Write code that asks the user for their name,
# then opens a file called "name.txt"
# and writes that name to it. Remember to close your file.

FILENAME = "name.txt"
name_file = open(FILENAME, 'w')

name_of_user = str(input("Your name is: "))

print(name_of_user, file=name_file)

name_file.close()

# (In the same file, but as if it were a separate program)
# Write code that opens "name.txt"
# and reads the name (as above) then prints,
# "Your name is Bob" (or whatever the name is in the file).

infile_name = open(FILENAME, 'r')
name_in_file = infile_name.read().title()
infile_name.close()
print(f"Your name is {name_in_file}")

# Create a text file called numbers.txt
# Write code that opens "numbers.txt",
# reads only the first two numbers and
# adds them together then prints the result, which should be... 59.

infile_number = open("numbers.txt", 'r')
first_number = int(infile_number.readline())
second_number = int(infile_number.readline())
infile_number.close()
print(first_number + second_number)

# Now write a fourth block of code that prints the total for all lines in numbers.txt
# or a file with any number of numbers.

in_file_sum = open("numbers.txt", "r")
total_number = 0
for line in in_file_sum:
    number = int(line)
    total_number += number
in_file_sum.close()
print(total_number)
