# ls = [5,7,2,34,5,67,7]
# Importance function of List
# 1. len() - returns the no of elements present in the list
# 2. count() - returns the no. of occurrences of specified item
# 3. index() - return the index of first occurremce of the specified item
# 4. append() - to add item at the end of the list
# 5. insert() - to insert item at specified index position
# 6. extend() - to add all items of one list to another list
# 7. remove() - to remove specified item from the list
# 8. pop() - it removes and returns the last element of the list

# print(len(ls))
# print(ls.count(67))
# print(ls.index(34))
# ls.append(88)
# print(ls)
# ls.append(45)
# print(ls)
# ls.insert(3,'Hello')
# print(ls)
# ls2 = ['a','b','c']
# ls2.extend(ls)
# print(ls2)
# print(ls)
# ls.remove(5)
# print(ls)
# deletedValue = ls.pop()
# print(ls)
# print("deleted",deletedValue)


# ls= [64,72,4,9,27,95,0,34,28,47,28,42,37]
# to display only even numbers from this list

from classAndObjects import Factorial

fact = Factorial()
fact.fact()
fact.display()