#tuples are similer to lists in that they are ordered, indexed and can have different value types
#tuples are different to lists in that they are immutable, you cannot add, remove or change items within tuples once it is created
#tuples are also different to lists in that they are faster, this is convenient in softwares that requires sollections that do not change, if tuples are used, the software can run faster
################################################################################################################
t=(10,20,"geek")
print(t) #prints tuples created above
t=() #creates empty tuple
print(type(t)) #prints tuple type
print(t) #prints empty tuple
t=(10) #creates integer variable not tuple
print(type(t)) #confirms t is integer type not tuple
t=(10,) #created single item tuple
print(type(t),"\n") #confirms t is type tuple
################################################################################################################

################################################################################################################
t=10,20,30,40,10 #brackets are optional in tuples with mutiple values
print(t[2]) #index at 2
print(t[-1]) #index at -1, from the right side
print(t[1:3]) #indexing from 1 to 3 minus 1
print(len(t)) #length of tuple
print(t.count(10)) #returns num of occurences for value (10)
print(t.index(10)) #returns index of value (10)
################################################################################################################
