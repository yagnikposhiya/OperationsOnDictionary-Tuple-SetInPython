"""
Student Name : Yagnik Poshiya
Student ID   : 20CE114
Github Repository Link :
Charusat University -> Chandubhai S. Patel Institute Of Technology

Index :
1. To add member(s) into set and clear set
2. To remove an item from a set
    i. Using discard() method
    ii. Using remove() method
3. To create intersection, union and difference of set
4. convert tuple to string
    i. Using join() method
    ii. Using for loop
5. To find most common element from list, tuple, dictionary
"""

"""Section 1. To add member(s) into set and clear set"""
# defining one set variable "SetExample"
SetExample = {134, 2452, 39452, 7724614, 0.8985}
print(SetExample)  # printing whole set before updating
SetExample.add(83996)  # add element
print(SetExample)  # printing whole set after updating
SetExample.add('Yagnik Poshiya')  # You can add string as an element in set
print(SetExample)
SetExample.add((1, 2, 3, 4))  # You can also add tuple as an element of set
print(SetExample)
# Attention : You can not add multiple elements at a time into set. and You can not add List as well as Dictionary as an element into set

"""Section 2. To remove an item from a set"""
# 2(i). Using discard() method
# Here we are using SetExample variable
print(SetExample)  # printing set before updating
SetExample.discard(134)  # discarding element-134 from set
print(SetExample)  # printing set after updating

# 2(ii). Using remove() method
# Here we are using SetExample variable
print(SetExample)  # printing set before updating
SetExample.remove('Yagnik Poshiya')  # removing element-'Yagnik Poshiya' from set
print(SetExample)  # printing set after updating

"""Section 3. To create intersection, union and difference os sets"""
# defining "SetExample_One" and "SetExample_Two"
SetExample_One = {1, 2, 3, 4, 5, 6}
SetExample_Two = {5, 6, 7, 8, 9, 10, 11, 12}
SetIntersection = set.intersection(SetExample_One, SetExample_Two)  # storing intersection of sets
print(SetIntersection)  # printing
SetUnion = set.union(SetExample_One, SetExample_Two)  # storing union of sets
print(SetUnion)  # printing
SetDifference = set.difference(SetExample_One, SetExample_Two)  # storing difference of sets
# Here in output it will give {1,2,3,4} because here i have written SetExample_One, SetExample_Two so that it will give only those elements which are in set "SetExample_One" but not in set "SetExample_Two".
# for more information refer given link : https://byjus.com/maths/difference-of-sets/
print(SetDifference)  # printing

"""Section 4. To find maximum and minimum values in set"""
# Here we are referring "SetExample_One" and "SetExample_Two"
SetMaximumValue_One = max(SetExample_One)  # finding maximum value from set "SetExample_One"
SetMaximumValue_Two = max(SetExample_Two)  # finding maximum value from set "SetExample_Two"
print(SetMaximumValue_One)
print(SetMaximumValue_Two)
SetMinimumValue_One = min(SetExample_One)
SetMinimumValue_Two = min(SetExample_Two)
print(SetMinimumValue_One)  # finding minimum value from set "SetExample_One"
print(SetMinimumValue_Two)  # finding minimum value from set "SetExample_Two"

"""Section 5. To find most common element from list, tuple, dictionary"""


# defining function to find most common element in list
def mostCommonInList(ListName):
    COUNTERINLIST = 0
    NUMBERINLIST = 0

    for iterationVariable in ListName:
        currentFrequency = ListName.count(iterationVariable)
        if currentFrequency > COUNTERINLIST:
            COUNTERINLIST = currentFrequency
            NUMBERINLIST = iterationVariable

    return NUMBERINLIST


# defining string list
ListExample = ['Yagnik', 'Yagnik', 'Yagnik', 'Poshiya', 'Poshiya', 'CSPIT', 'List', 'Tuple', 'Tuple', 'Tuple', 'Tuple']
MostCommonElementInList = mostCommonInList(ListExample)
print(MostCommonElementInList)


# defining function to find most common element in list
def mostCommonInTuple(TupleName):
    COUNTERINTUPLE = 0
    NUMBERINTUPLE = 0

    for iterationVariable in TupleName:
        currentFrequency = TupleName.count(iterationVariable)
        if currentFrequency > COUNTERINTUPLE:
            COUNTERINTUPLE = currentFrequency
            NUMBERINTUPLE = iterationVariable

    return NUMBERINTUPLE


# defining string tuple
TupleExample = (1, 2, 3, 4, 5, 61, 1, 1, 1, 12, 2, 22, 2, 234, 5, 6, 6, 6, 6, 6,)
MostCommonElementInTuple = mostCommonInTuple(TupleExample)
print(MostCommonElementInTuple)


# defining function to find most common element in list
def mostCommonInDictionary(DictionaryName):
    COUNTERINDICTIONARY = 0  # set counter to zero
    NUMBERINDICTIONARY = 0  # set number to zero

    DictionaryValues = DictionaryName.values()  # store all values of dictionary into "DictionaryValues"
    currentFrequency = 0  # set currentFrequency to zero
    for iterationVariable in DictionaryValues:
        for iterationVariable2 in DictionaryValues:
            if iterationVariable == iterationVariable2:
                currentFrequency = currentFrequency + 1
        if currentFrequency > COUNTERINDICTIONARY:
            COUNTERINDICTIONARY = currentFrequency
            NUMBERINDICTIONARY = iterationVariable
        currentFrequency = 0
    return NUMBERINDICTIONARY


# defining dictionary
DictionaryExample = {'20ce114': 10, '20ce115': 10, '20ce116': 12, '20ce117': 12, '20ce118': 10, '20ce119': 1}
MostCommonElementInDictionary = mostCommonInDictionary(DictionaryExample)  # calling function "mostCommonInDictionary"
print(MostCommonElementInDictionary)
