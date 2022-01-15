"""
Student Name : Yagnik Poshiya
Student ID   : 20CE114
Github Repository Link :
Charusat University -> Chandubhai S. Patel Institute Of Technology

Index :
1. Checking given key is present in dictionary or not
2. Merging two dictionaries
    i.  Defining user defined function
    ii. Using update() method
3. Sum all items in dictionary
4. add new key & value to dictionary
    i. Using update() method
    ii. Using Assignment Operator
5. concatenation of dictionaries
"""

"""Section 1. Checking given key is present in dictionary or not"""
# defining one dictionary "DictionaryExample" which contains students' id as key and their names as value.
DictionaryExample = {'20ce114': 'Yagnik Poshiya', '20ce115': 'Divya Prajapati', '20ce116': 'Mayan Prajapati',
                     '20ce117': 'Dhruv Puvar', '20ce118': 'Khushi Ranpariya', '20ce119': 'Deep Rupapara'}


# defining function "checkingKeyIsValidOrNot"
def checkingKeyIsValidOrNot(DictionaryName,
                            Key):  # Passing DictionaryExample and Key to the function "checkingKeyIsValidOrNot"
    if Key in DictionaryName.keys():  # checking if key in present in DictionaryExample which is name as "DictionaryName" then print "Key is present" and its "value".
        print('Key : ', Key, ' is present')
        print('Value :', DictionaryName[Key])
    else:  # if key is not present then print "Key is not present"
        print('Key : ', Key, ' is not present')


checkingKeyIsValidOrNot(DictionaryExample, '20ce121')  # calling the function for checking Key is present or not.

"""Section 2. Merging two dictionaries"""
# defining two dictionaries "DictionaryExample_One" and "DictionaryExample_Two"
DictionaryExample_One = {'20ce114': 'Yagnik Poshiya', '20ce115': 'Divya Prajapati', '20ce116': 'Mayan Prajapati',
                         '20ce117': 'Dhruv Puvar', '20ce118': 'Khushi Ranpariya', '20ce119': 'Deep Rupapara'}
DictionaryExample_Two = {'Ritesh Patel': 'CSPIT', 'Amit Ganatra': 'Depstar', 'Mrugendra Rahevar': 'CSPIT',
                         'Nikita Bhatt': 'CSPIT'}


# 2(i). Defining user defined function
# defining function "dictionaryMerger" and passing two dictionaries to it and at last returning merged dictionary
def dictionaryMerger(Dictionary_One, Dictionary_Two):
    MergedDictionary = Dictionary_One or Dictionary_Two
    return MergedDictionary


UniversalDictionary = dictionaryMerger(DictionaryExample_One,
                                       DictionaryExample_Two)  # calling function and save returned dictionary into "UniversalDictionary"
print(UniversalDictionary)  # printing "UniversalDictionary"

# 2(ii). Using update() method
DictionaryExample_One.update(DictionaryExample_Two)  # updating "DictionaryExample_One"
print(DictionaryExample_One)  # printing updated "DictionaryExample_One"

"""Section 3. Sum all items (Keys as well as Values) in dictionary"""
DigitDictionary = {1: 12, 2: 29, 3: 123, 4: 3476, 5: 8964, 6: 90, 7: 1, 8: 34, 9: 123}
DigitDictionary_Values = DigitDictionary.values()  # storing all values of dictionary into "DigitDictionary_Values"
SumOfDigitDictionaryValues = sum(DigitDictionary_Values)  # sum of those all values
print(SumOfDigitDictionaryValues)  # printing sum of all those values : Expected value = 12852

DigitDictionary_Keys = DigitDictionary.keys()  # storing all keys of dictionary into "DigitDictionary_Keys"
SumOfDigitDictionaryKeys = sum(DigitDictionary_Keys)  # sum of those all keys
print(SumOfDigitDictionaryKeys)  # printing sum of all those keys : Expected value = 45

"""Section 4. add new key to dictionary"""
# Here we are using previously declared dictionary "DictionaryExample" and we are going to add new "student id" as well as "student name"
# 4(i). Using update() method
print(DictionaryExample)  # printing whole dictionary before updating
DictionaryExample.update({'20ce120': 'Achyut Krishna Sai'})
print(DictionaryExample)  # printing whole dictionary after updating

# 4(ii). Using Assignment Operator
print(DictionaryExample)  # printing whole dictionary before updating
DictionaryExample['20ce121'] = 'Dhruv Shah'
DictionaryExample['20ce122'] = 'Jay Shah'
print(DictionaryExample)  # printing whole dictionary after updating

"""Section 5. concatenation of dictionaries"""
DictionaryExample_Three = {'Arijit Singh': 'Naina', 'Neha Kakkar': 'Mile Ho Tum Hamko', 'Hariharan': 'Tu hi re',
                           'Himesh Reshmiya': 'Tere Naam'}  # defining "DictionaryExample_Three"
DictionaryExample_Four = {'Akshay Kumar': 'Mission Mangal', 'Salman Khan': 'Bajrangi Bhaijaan',
                          'Sharukh Khan': 'Chak De India',
                          'Surjeet Singh': 'Surma'}  # defining "DictionaryExample_Four"
ConcatenatedDictionary = DictionaryExample_Three  # assigning "DictionaryExample_Three" to the "ConcatenatedDictionary"
ConcatenatedDictionary.update(DictionaryExample_Four)  # updating "ConcatenatedDictionary"
print(ConcatenatedDictionary)  # printing "ConcatenatedDictionary"
