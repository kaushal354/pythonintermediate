# #given a list of numbers, find the sum and avg using
# #built-in functions.
# import numpy as np
# list9 = [2,4,6,8,9,10,12,14,15,16,17]
# sum2 = sum(list9)
# avg2 =np.mean(list9)
# print("sum of list:",sum2,"average of list:",round(avg2,2))

# #create a list of fruits and add a new fruit to the list
# list6 = ["banana","apple","orange","mousmbi"]
# list6.append("kiwi")
# print(list6)

# #Access elements in a tuple using indexing
# tuple2 = ("apple","mango","hello")
# i = 0
# a = tuple2[i]
# print(a)

# #given a two lists of numbers, concatenate them into a single list.
# list1 = [1,2,3,4,5,6]
# list2 = [1,2,3,4,5,6]
# list3 = list1 + list2
# print(list3)

# #write a program that finds the largest and smallest
# #element in a list
# list33 = [25,36,85,18,24,16,99,45,101,22,3]
# list33.sort()
# print("min:",list33[0],"max:",list33[len(list33) - 1])

# #implement a program that takes lists of numbers and
# #return a new list with the squared values.
# list25 = []
# for i in range(0,4):
#     list25.append(int(input("enter a numbers:"))**2)
# print(list25)

# #create a program that finds the common elements
# #between two lists and stores them in a new lists
# list63 = []
# list61 = [1,2,3,4,5]
# list62 = [2,3,4,5,6]
# for i in range(0,len(list61)):
#     for j in range(0,len(list62)):
#         if list61[i] == list62[j]:
#             list63.append(list61[i])
# print(list63)

# #given a list of words, find the word with the
# #maximum length and its length.
# list26 = ["komal","kaushal","aryan","airtel"]
# b = 0
# for i in range(0,len(list26)):
#     if b <= len(list26[i]):
#         b = len(list26[i])
#         c = list26[i]

# print("the word with max len is",c,"length:",b)

# #write a python program to count the occurances of
# #each element in a given list

# my_list = [1,2,2,3,3,3,4]
# b = list(set(my_list))
# c = 0
# for i in range(0,len(b)):
#     for j in range(0,len(my_list)):
#         if b[i] == my_list[j]:
#             c = 0 + 1
#     print("",b[i],":", c,end=",")
#     c = 0

# #given a lists of names, remove all duplicate names
# #and print the unique names.
# list25 = ["kaushal","abhishek","aryan","kaushal","akash","aditya","kaushal","aryan"]
# b = list(set(list25))
# print(b)

# #write a program that checks if a given list is sorted
# #in ascending order
# list25 = [1,2,3,4,5,6]
# b = list25[0:len(list25)]
# b.sort()
# c = 0
# for i in range(0,len(list25)):
#     if list25[i] == b[i]:
#         c = c + 1
#     else:
#         c = c + 0
# if c == len(list25):
#     print("it is sorted")
# else:
#     print("it is not sorted")

# #write a program that takes a list
# #of strings and return the list
# #sorted by the length of the strings.
# list26 = ["mayur","vikash","rajan","aniket","vipul","kaushal"] #5,6,5,6,5,7 
# lengof = len(list26)
# list27 = []
# j = 0
# i = 0
# while len(list27) < lengof - 1 :
#     if len(list26[0]) < len(list26[1]):
#         list27.append(list26[0])
#         list26.pop(0)
#     elif len(list26[0]) == len(list26[1]):
#         if len(list26[1]) < len(list26[2]):
#             list27.append(list26[1])
#             list26.pop(1)
#         else:
#             list27.append(list26[2])
#             list26.pop(2)
#     else:
#         list27.append(list26[1])
#         list26.pop(1)
#     j += 1
# list27.append(list26[0])
# print(list27)

# #implement a function that takes
# #two lists and return their union
# #(all unique elements from both lists)

# list1 = ["hello","aryan","lotion","bag"]
# list2 = ["hello","aryan","kaushal","abhinay"]
# a = set(list1)
# b = set(list2)
# c = set.union(a,b)
# d = list(c)
# print(d)











