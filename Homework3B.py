#This is Ralph Miller's Homework #3B for Programming for Absolute Beginners with Mark Lassoff, completed April 3, 2014

#Question 10 - Let's create a dictionary
gpas = {'Lassoff': 3.12 , 'Johnson': 2.22 , 'Reich': 3.59 , 'Honeychurch': 2.98 , 'Maini': 3.11 , 'Levin': 2.88 , 'Marcus': 2.77 , 'Banks': 3.71};





#Question 11 - Build a sorted list from the dictionary
sortedList = gpas.items()
#Then we'll sort it and output the values
sortedList.sort()
for k, v in sortedList:
    print k, v

#Question 12 - Build a List of gpa values from the dictionary
gpaList = gpas.values() 
#print the average of the gpas
print sum(gpaList)/len(gpaList)

#Question 13 - Class rankings
#let's try creating the dictionary in a different way
gpasNew = [{'lastName': 'Lassoff', 'gpa': 3.12}, {'lastName': 'Johnson' , 'gpa': 2.22}, {'lastName': 'Reich' , 'gpa': 3.59 }, {'lastName': 'Honeychurch' , 'gpa': 2.98}, {'lastName': 'Maini', 'gpa':3.11} , {'lastName': 'Levin', 'gpa':2.88} , {'lastName': 'Marcus', 'gpa': 2.77 }, {'lastName': 'Banks', 'gpa': 3.71}]
print "Last Name:" , gpasNew['lastName'] , "GPA:" , gpasNew['gpa'];


sortedList = sorted(gpasNew , key=lambda elem: "%02d %s" % (elem['lastName'], elem['gpa']))
for k, v in sortedList:
    print "Last Name:" , dict['name'] , "GPA:" , dict['age'];
    
#and...I give up...