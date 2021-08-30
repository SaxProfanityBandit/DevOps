#Constants
intro_python = "Avklarat"
exercises = 3
points_per_exercise = 5
point_total = 100

#Calculation of the points, using += to shorten the line.
point_total += (exercises * points_per_exercise)

#Adding the comment line in Swedish that is part of the exercise:
#Fast det är ju lite osant, med tanke på att jag inte får några poäng av läraren.

#Printing and formatting the result.
print("I got " + str(point_total) + " points!")
