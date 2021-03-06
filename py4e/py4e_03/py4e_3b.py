# Program to prompt for a score between 0.0 and 1.0.
# If score is out of range, print an error.
# If the score is between 0.0 and 1.0, print a grade using:
    # >= 0.9 A
    # >= 0.8 B
    # >= 0.7 C
    # >= 0.6 D
    # < 0.6 F
# For the test, enter a score of 0.85.
#
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# a try loop to handle a user input (number between 0.0 and 1.0), if it works, converts user input to a float value, returns the string within the () below
try:
    score = float(input('please enter score, be between 0.0 and 1.0:'))
except:
    print('please enter a valid value, between 0.0 and 1.0')

#----
# if loop to determine letter grade based on user input, starting with a protection against inappropriate user inputs, elifs dictate the letter grade by comparison. if precceding statements are NOT met, else
if score < 0.0 or score > 1.0 :
    print('invalid score, please enter a value between 0.0 and 1.0 ')
elif score >= 0.9 :
    print(score, ' = ', 'A')
elif score >= 0.8 :
    print(score, ' = ', 'B')
elif score >= 0.7 :
    print(score, ' = ', 'C')
elif score >= 0.6 :
    print(score, ' = ', 'D')
else :
    print(score, ' = ', 'F')

#..................
