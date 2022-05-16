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
print(s4)
################################################################################################################

################################################################################################################
