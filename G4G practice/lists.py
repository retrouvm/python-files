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
print("after removing 20", l)
