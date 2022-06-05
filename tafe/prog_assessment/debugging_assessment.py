print("Please enter your 5 marks below.")

# create array/list with five marks
marksList = []

# read 5 inputs
for i in range(1, 6):
    # I have created a for loop to avoid writing the same 5 inputs over and over.
    # This allowed me to validate if all inputs in under the variable the 'marks' repeated 5 times
    # is an integer, not a string as well valued between 0 and 100.
    marks = input("\nEnter a mark no. {}: ".format(i))
    while marks != int:
        try:
            # Validates if marks is between 0 and 100.
            marks = int(marks)
            while marks <= -1 or marks >= 101:
                if marks <= -1:
                    marks = input("\nMarks must be greater or equal than 0."
                                  "\nEnter a mark no. {}: ".format(i))
                    marks = int(marks)
                elif marks >= 101:
                    marks = input("\nMarks cannot be greater than 100."
                                  "\nEnter a mark no. {}: ".format(i))
                    marks = int(marks)
            break
        except ValueError:
            # Validates if marks is a number(int).
            marks = input("\nNot a number."
                          "\nEnter a mark no. {}: ".format(i))
    marksList.append(marks)

# print the array/list
print("\n{}".format(marksList))

# calculate the sum and average
sumOfMarks = sum(marksList)
averageOfMarks = sum(marksList) / 5

# display results
print("\nThe sum of your marks is: {}/500".format(sumOfMarks))
print("The average of your marks is: " + str(averageOfMarks))
print("")

averageOfMarks = int(averageOfMarks)

# grading system
print("------------------------------------------------")
if averageOfMarks == 0:
    print("Grade: F")
    print("What have you been doing?")
elif 1 <= averageOfMarks <= 50:
    print("Grade: E")
    print("You'll have to repeat the course again.")
elif 50 <= averageOfMarks <= 75:
    print("Grade: D")
    print("Doing  well, but you better try harder")
elif 75 <= averageOfMarks <= 85:
    print("Grade: C")
    print("Average mark doesn't mean you're bad. Don't let it discourage you.")
elif 85 <= averageOfMarks <= 95:
    print("Grade: B")
    print("Top range marks. Splendidly done.")
elif 95 <= averageOfMarks <= 99:
    print("Grade: A")
    print("Definitely Asian level my boi.")
elif averageOfMarks == 100:
    print("Grade: EXCEPTIONAL")
    print("You must be GOD.")
print("------------------------------------------------")
