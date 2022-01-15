"""
Student Name : Yagnik Poshiya
Student ID   : 20CE114
Github Repository Link :
Charusat University -> Chandubhai S. Patel Institute Of Technology

Index :
1. Create tuple with different data types
2. Create tuple with numbers of only and accessing any one of them
3. add an item into tuple
    i. Using + operator
    ii. Using list
4. convert tuple to string
    i. Using join() method
    ii. Using for loop
5. to find length of tuple
"""

"""Section 1. Create tuple with different data types"""
# defining variable TupleExample of type tuple
# tuple type variable can contains various types of element of different data types like: "string","number(float + integer)","List","Dictionary","set(number + string)"
TupleExample = (
    'Yagnik Poshiya', 12, [12, 373, '20CE114', 1222.121], 93863.363, {'20ce114': 'Yagnik Poshiya'},
    {365, 8746, 365, 24154},
    {'Yagnik', 'Github', 'Microsoft'})

print(TupleExample)  # printing TupleExample

"""Section 2. Create tuple with numbers of only and accessing any one of them"""
# defining TupleExample_One with only numbers
TupleExample_One = (12, 23, 34, 45, 56, 67, 78, 89, 90)
print(TupleExample_One[0])  # accessing first element
# you can access any element of tuple using indexing method
# tuple supports indexing method same as list
print(TupleExample_One[8])  # accessing last element
print(
    TupleExample_One)  # to print whole tuple do not give any index number just write name of tuple variable inside "print"

"""Section 3. add an item into tuple"""
# 3(i). Using + operator
# Here we are using TupleExample_One
TupleExample_One = TupleExample_One + (
    112.8938,)  # Here we are adding element that is 112.8938 into tuple but remember that always write "comma(,)" after element you want to add
print(TupleExample_One)  # printing whole tuple after updating

# 3(ii). Using list
# to add element into tuple using list : you have to first convert tuple into list and append element into list and then convert list into tuple. In short,
# 1-> Convert Tuple Into List
# 2-> Append Element Into List
# 3-> Convert List Into Tuple
TupleExample_One_List = list(TupleExample_One)  # converting tuple to list
TupleExample_One_List.append('Yagnik Poshiya')  # appending element "Yagnik Poshiya" to list
TupleExample_One = tuple(TupleExample_One_List)  # converting list to tuple
print(TupleExample_One)  # printing again whole tuple

"""Section 4. convert tuple to string"""
# 4(i). Using join() method
# defining TupleExample_Two
TupleExample_Two = (
    'Yagnik Poshiya', ' is', ' studying', ' in', ' Chandubhai S Patel', ' Institute Of Technology', ' in',
    ' Charusat University.')
TupleExample_Two_String = ''.join(TupleExample_Two)
print(TupleExample_Two_String)

# 4(ii). Using for loop
# declaring string variable to store string of all tuple elements
StringVariable = ''  # declaring empty string variable
for iterationVariable in TupleExample_Two:  # running for loop using iterationVariable iterator
    StringVariable = StringVariable + iterationVariable  # storing all element into string variable
print(StringVariable)  # print string stored into "StringVariable"

"""Section 5. to find length of tuple"""
# Here we are using TupleExample_Two tuple type variable
print('Length of TupleExample_Two :', len(TupleExample_Two))