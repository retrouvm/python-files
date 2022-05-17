#set is is similar to list
#set contains distinct items, no two items can be the same
#set is unorderd, there is no predefined order for traversing or printing
#values in a set cannot be indexed since there is no ordering
#it's really fast to find the union/intersection/difference of two sets
# this is because set internally uses hashing for comparisons and operations
################################################################################################################
s1={10,20,30} #sets use curly braces
print(s1)
s2=set([40,20,30]) #set() function can take a list/tuple and create/return a set with the values within
print(s2)
s3={} #empty braces is a dictionary
print(type(s3))
s4=set() #for empty set you have to use set()
print(type(s4))
print(s4,"\n")
################################################################################################################

################################################################################################################
#add, update

s={10,20}
s.add(30) #adds value into end of set
print(s)
s.add(30) #cannot add duplicate values
print(s) #set does not change, since no two items can be the same

s.update ([40,50]) #using the update function we can add items from other collections such as lists/tuples
print(s) #the order in which the items are inserted into the set does not follow a certain pattern, it is unpredictables

s.update({60,70},[80,90]) #you can insert items from different types of collections at the same time
print(s,"\n")
################################################################################################################

################################################################################################################
#discard, remove, clear, delete

s={10,30,20,40}
s.discard(30) #if value exists within set, it is removed, otherwise nothing happens and set remains as is
print(s)
s.remove(20) #similar to discard but with remove if value does not exist within set, then error is raised
print(s)
s.clear() #everything is removed and you're left with an empty set, set(), not {}
print(s,"\n")
s.add(50) #adds value (50) to previously empty set 
del s #completely removes object, meaning it cannot be referenced anymore, you cannot add to it 
################################################################################################################

################################################################################################################
#length, existence

s={10,30,20,40}
print(len(s)) #returns size of set, num of elements
print(20 in s) #returns T/F if value exists within set
print(50 in s, "\n") #returns T/F if value exists within set
################################################################################################################

################################################################################################################
