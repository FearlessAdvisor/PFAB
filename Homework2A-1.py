#This is Ralph Miller's Homework #2 (for reals, yo) for Programming for Absolute Beginners with Mark Lassoff, completed March 25, 2014

import sys

#I think is what you actually wanted.
test1 = int(sys.argv[1])
test2 = int(sys.argv[2])
test3 = int(sys.argv[3])
test4 = int(sys.argv[4])

average= (test1 + test2 + test3 + test4) / 4
print average
#now let's determine the grade
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