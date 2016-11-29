'''for i in range(0,10):
	prct = input('enter your grade: ')
	if prct <= 69:
		print 'Score: ' + str(prct) + '; Your grade is - D'
	elif 70 <= prct <= 79:
		print 'Score: ' + str(prct) + '; Your grade is - C'
	elif 80 <= prct <= 89:
		print 'Score: ' + str(prct) + '; Your grade is - B'
	elif 90 <= prct <= 100:
		print 'Score: ' + str(prct) + '; Your grade is - A'
		'''
from random import randint

print "Scores and Grades"
for i in range(0,10):
	score = randint(60, 100)
	if(score < 70):
		grade = "D"
	elif(score <=80):
		grade = "C"
	elif(score <=90):
		grade = "B"
	elif(score <=100):
		grade = "A"

	print "Score: %d; Your grade is %s" %(score, grade)
print "End of program. Bye!"