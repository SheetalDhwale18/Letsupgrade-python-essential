#python assignment | day 2

#que 1[list and its default methods ]

#Append list2 into list1:

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)

#output :['a', 'b', 'c', 1, 2, 3]

#Make a copy of a list with the copy() method:

thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

#output:['apple', 'banana', 'cherry']


#The clear() method empties the list:

thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

#output:[]


#Insert an item as the second position:

thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)
#output:['apple', 'orange', 'banana', 'cherry']

#The remove() method removes the specified item:

thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

#output:['apple', 'cherry']


# que 2 [dictionary and its default functions]




#Create and print a dictionary:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)


#Accessing items
#Change the "year" to 2018:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2018





#Removing Items

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)



#The popitem() method 

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
print(thisdict)



thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]
print(thisdict)



thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict





#The clear() method empties the dictionary:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()
print(thisdict)


#Copy a Dictionary
#Make a copy of a dictionary with the copy() method:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)



#que 3[sets and its default functions]



#Create a Set:

thisset = {"apple", "banana", "cherry"}
print(thisset)


#Access Items

thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)


#Check if "banana" is present in the set:

thisset = {"apple", "banana", "cherry"}

print("banana" in thisset)




#Add Items



thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)



#Add multiple items to a set, using the update() method:

thisset = {"apple", "banana", "cherry"}

thisset.update(["orange", "mango", "grapes"])

print(thisset)



#Get the number of items in a set:

thisset = {"apple", "banana", "cherry"}

print(len(thisset))


#Remove Item


thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset)



#Remove "banana" by using the discard() method:

thisset = {"apple", "banana", "cherry"}

thisset.discard("banana")

print(thisset)



#Remove the last item by using the pop() method:

thisset = {"apple", "banana", "cherry"}

x = thisset.pop()

print(x)

print(thisset)



#The clear() method empties the set:

thisset = {"apple", "banana", "cherry"}

thisset.clear()

print(thisset)


#The del keyword will delete the set completely:

thisset = {"apple", "banana", "cherry"}

del thisset





#Join Two Sets
#The union() method returns a new set with all items from both sets:

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)



#The update() method inserts the items in set2 into set1:

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)




#que 4[tuple and explore default method]

#Create a Tuple:

thistuple = ("apple", "banana", "cherry")
print(thistuple)

#Print the second item in the tuple:

thistuple = ("apple", "banana", "cherry")
print(thistuple[1])


#Print the last item of the tuple:

thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])


#The del keyword can delete the tuple completely:

thistuple = ("apple", "banana", "cherry")
del thistuple
 #this will raise an error because the tuple no longer exists


#Join two tuples:

tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)



#que 5[string and explore default methods ]


#Get the characters from position 2 to position 5 (not included):

b = "Hello, World!"
print(b[2:5])


#The len() function returns the length of a string:

a = "Hello, World!"
print(len(a))



#The strip() method removes any whitespace from the beginning or the end:

a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"




#The lower() method returns the string in lower case:

a = "Hello, World!"
print(a.lower())




#The upper() method returns the string in upper case:

a = "Hello, World!"
print(a.upper())


#The replace() method replaces a string with another string:

a = "Hello, World!"
print(a.replace("H", "J"))



#The split() method splits the string into substrings if it finds instances of the separator:

a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']







#output of  entire program 



['a', 'b', 'c', 1, 2, 3]
['apple', 'banana', 'cherry']
[]
['apple', 'orange', 'banana', 'cherry']
['apple', 'cherry']
{'brand': 'Ford', 'model': 'Mustang', 'year': 1964}
{'brand': 'Ford', 'year': 1964}
{'brand': 'Ford', 'model': 'Mustang'}
{'brand': 'Ford', 'year': 1964}
{}
{'brand': 'Ford', 'model': 'Mustang', 'year': 1964}
{'cherry', 'banana', 'apple'}
cherry
banana
apple
True
{'orange', 'cherry', 'banana', 'apple'}
{'banana', 'grapes', 'orange', 'mango', 'apple', 'cherry'}
3
{'cherry', 'apple'}
{'cherry', 'apple'}
cherry
{'banana', 'apple'}
set()
{'c', 1, 2, 3, 'a', 'b'}
{'c', 1, 2, 3, 'a', 'b'}
('apple', 'banana', 'cherry')
banana
cherry
('a', 'b', 'c', 1, 2, 3)
llo
13
Hello, World!
hello, world!
HELLO, WORLD!
Jello, World!
['Hello', ' World!']


