#This is Ralph Miller's Homework #2A for Programming for Absolute Beginners with Mark Lassoff, completed March 25, 2014

testScores = list() 
n = int(input('How many test scores do you want to enter? ')) 
for i in range(n): 
    testScore = input('Enter your test score: ') 
    testScores.append(testScore) 
average = sum(testScores)/n
print 'The average of your test scores is:' , average
if average >= 90:
    grade = 'A'
elif average >= 80:
    grade = 'B'
elif average >= 70:
    grade = 'C'
elif average >= 60:
    grade = 'D'
elif average < 60:
    grade = 'F'
print 'Your grade is a' , grade