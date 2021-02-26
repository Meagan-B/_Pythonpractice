# Exercise 2: Figure out which line of the below program is still not properly guarded. See if you can construct a text file which
# causes the program to fail and then modify the program so that the line is properly guarded and test it to make sure it handles your
# new text file.

usr_dir = input('ENTER file name >>> ')
fhand = open(usr_dir)
count = 0
for line in fhand:
    words = line.split()
    # print('Debug:', words)
    if len(words) == 0 : continue
    if words[0] != 'From' : continue
    print(words[2])


# Exercise 3: Rewrite the guardian code in the above example without two if statements. Instead, use a compound logical expression
# using the or logical operator with a single if statement.
