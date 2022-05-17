#list introduction

################################################################################################################
#access element by indexing
#elements increment by 0,1,2,3,4
#you can also access elements from the end starting at -1,-2,-3,-4,-5
l=[10,20,30,40,50]
print(l)
print(l[3])
print(l[-1])
print(l[-2],"\n")
################################################################################################################

################################################################################################################
#append, insert, check, count, index
l=[10,20,30,40,50]
print(l)
l.append(30) #appends->adds 30 to the end of the list
print(l)

l.insert(1,15) #inserts value (15) at index (1)
print(l)

print(15 in l) #returns true/false if value (15) exists in list (l)

print(l.count(30)) #counts number of occurences for vaue (30)

print(l.index(30,),"\n") #returns index of the first occurence of value (30)
################################################################################################################

################################################################################################################
#removing a value
l=[10,20,30,40,50,60,70,80]
print(l)

l.remove(20) #removes value (20) from list (l)
print(l)

l.pop() #pops off->removes value at the end of the list
print(l)

l.pop(2) #pops off->removes value at index 2 from the list
print(l)

del l[1] #delete value at index 1
print(l)

del l[0:2] #delete values from indexes 0 to 2 minus 1
#another example would be, del l[0:0]
print(l, "\n")
################################################################################################################

################################################################################################################
#general purpose functions
l=[10,40,20,50]
print(l)

print(max(l)) #maximum value in list

print(min(l)) #minimum value in list

print(sum(l)) #summation of values within list
l.reverse() #reverse list
print(l)
l.sort() #sort list in ascending order
print(l,"\n") 
################################################################################################################