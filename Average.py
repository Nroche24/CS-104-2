#Initialize all variables to 0
numberofscores = 0
total = 0
score = 0
scorecount = 0
average = 0.0

#Accept the numbrer of scores to average
numberofscores = int (input ("please enter the number of scores you want to average: "))

#Add a loop to make this code repeat until scorecount = numberofscores
score = int (input("please enter a score:"))
total = total + score
scorecount = scorecount + 1



average = total / numberofscores
print (average)  
