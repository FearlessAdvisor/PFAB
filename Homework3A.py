#This is Ralph Miller's Homework #3A for Programming for Absolute Beginners with Mark Lassoff, completed March 29, 2014

#2 - create a list of names
bradys = ["Mike" , "Carol" , "Marsha" , "Jan" , "Cindy" , "Greg" , "Peter" , "Bobby" , "Alice"]
#3 -output the length of the list
print len (bradys)
#4
numBradys = len(bradys)
    
#5 - we'll use a variable to help us count and output each member of the list on a separate line.
i = 0
while i < numBradys:
      print bradys[i]
      i += 1
    
#6
bradys.sort()
#Sorted
#7
print "Let's print a sorted list"
i = 0
while i < numBradys:
      print bradys[i]
      i += 1
      
#7-8 For...In Loop
print "Let's print the list again using a for loop"
for x in bradys:
    print x

