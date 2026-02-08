marks = [94.5, 87.5, 95.6, 45.6]
print(marks)
print(type(marks))
print(marks[0])
print(marks[1])
print(len(marks))

# we can store elements of different data types together in the same list
student = ["Tanvi", 95, 22, "Nagpur"]
print(student)

# strings are immutable in python while lists are mutable
str = "hello"
print(str[0])
# str[0] = "y"   this is not possible

student[0] = "Ankit" #this is allowed
print(student)

# slicing is also possible = sublist
scores = [85, 94, 95, 96, 97, 98]
print(scores[0:2])
print(scores[:4]) 
print(scores[2:])
print(scores[-3:-1])

# lists methods
list = [3, 1, 2]

list.append(4)
print(list)
list.sort() # if we try to print this directly it will return None for all meths in lists
print(list)
list.sort(reverse = True)
print(list)
list.reverse()
print(list)
list.insert(4,5) # index , element
print(list)

# remove and pop method
list.remove(1)
print(list)
list.pop(2)
print(list)
# copy and count
# copy to copy list into another 
# count to count the occurance of a particular element

# Tuples in Python
# immutable sequences of values

tup = (2,3,4,5,2,6)
print(type(tup))
print(tup[0])
print(tup[1])
# tup[0] = 5  this is not allowed

tup2 = ()
print(tup2)
print(type(tup2))

# in case of a single element we have to add a comma 
# if we dont add a comma it will be treated as an integer
tuple = (1,)
print(tuple)
print(type(tuple))

# slicing in tuple
print(tup[1:3])

# methods in tuple
print(tup.index(2))
print(tup.count(2))