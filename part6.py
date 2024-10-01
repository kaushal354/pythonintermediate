#Create a dictionary to store information about a person

#(name, age, address).
mydict = {}
mydict.update({"name" : "kaushal"})
mydict.update({"age" : 22})
mydict.update({"adress" : "patna"})
print(mydict)

#Add a new key-value pair to an existing dictionary.

my_dict = {"name":"kaushal",
           "age": 23,
           "adress" : "patna"}
my_dict.update({"pocketmoney" : 2000})
print(my_dict)

#Create a set of unique numbers from a list of numbers..
list1 = [1,2,3,4,5,5,9,5,6,5,6]
uniquenos = set(list1)
print(uniquenos)

#Given two dictionaries, merge them into a single dictionary(for diff key).

my_dict1 = {"name" : "aarti",
           "age" : 93,
           "adress" : "patna"}

my_dict2 = {"fname" : "muskan",
           "fage" : 18,
           "fadress" : "patna"}
my_dict1.update(my_dict2)
print(my_dict1)

#Given two dictionaries, merge them into a single dictionary(for both diff and  same key)

my_dict1 = {"name" : "aarti",
           "age" : "93",
           "adress" : "banglore"}
my_dict2 = {"name" : ", muskan",
           "age" : ", 18",
           "adress" : ", patna"}
merge_dict = my_dict1.copy()
for key, value in my_dict2.items():
    if key in merge_dict:
        merge_dict[key] += (value)
    else:
        merge_dict[key] = value

print(merge_dict)

#write a program that finds the most frequent element in a list.

list4 = ["hello",1,2,3,5,"aryan","hello",2,3,4,"hello"]
my_dict6 = {}
a=0
for i in range(0,len(list4)):
    for j in range(0,len(list4)):
        if list4[i] == list4[j]:
            a = a + 1
        else:
            a = a + 0
    my_dict6.update({list4[i] : a})
    a = 0

max_key = max(my_dict6, key = my_dict6.get)
print("the most frequent element in a list:", max_key)
print("how much ",max_key, "is repeat:", my_dict6[max_key])

#Implement a program that removes a key-value pair from a dictionary.
#del method
my_dict = {'apple' : 2, "banana" : 3,"orange": 3}
del my_dict['banana']
print(my_dict)

#pop method
my_dict1 = {'apple' : 2, "banana" : 3,"orange": 3}
my_dict1.pop('banana')
print(my_dict)

#Create a program that checks if two sets have any element in common.
set1 = {1,2,3,4,5}
set2 = {5,6,7,8,9}
intersection = set1.intersection(set2)
print(intersection)


#Given a list of dictionaries, find the dictionary with the highest value for a specific key.
students = [
    {"name": "John", "age": 20, "major": "Computer Science"},
    {"name": "Alice", "age": 22, "major": "Mathematics"},
    {"name": "Bob", "age": 21, "major": "Physics"}
]
oldest_student = max(students, key=lambda x: x['age'])
print(oldest_student)


# # Write a Python program that counts the number of
# occurrences of each character in a given string using a
# dictionary.
students = {}
str1 = "hello world"
b = 0
for i in range(0,len(str1)):
    for j in range(0,len(str1)):
        if str1[i] == str1[j]:
            b = b + 1
        else:
            b = b + 0
    students.update({str1[i] : b})
    b = 0
print(students)



# Given two sets, find the union, intersection, and
# difference between them.

set1 = {1,2,3,4,5}
set2 = {5,6,7,8,9}
union = set1.union(set2)
intersection = set1.intersection(set2)
difference = set1.difference(set2)
print("union:",union)
print("intersection:",intersection)
print("difference:",difference)

#create a program that takes a list of dictionaries
#sorts them based on a specified key.
students = [
    {"name": "John", "age": 20, "major": "Computer Science"},
    {"name": "Alice", "age": 22, "major": "Mathematics"},
    {"name": "Bob", "age": 21, "major": "Physics"}
]
sort_dict = sorted(students, key=lambda x: x['age'])
print(sort_dict)

#write a program that finds the avg value of all element
#in a list of dictionaries
list_of_dicts = [
    {"a": 10, "b": 20},
    {"a": 30, "b": 40},
    {"a": 50, "b": 60}
]
key_to_average = "a"
values = [d[key_to_average] for d in list_of_dicts if key_to_average in d]
if values:
    average = sum(values) / len(values)
else:
    average = 0
print('The average value of key ',key_to_average, 'is',average)

#implement a program that takes a list of strings and return a set of 
#unique characters present in all strings
list_of_str = ["hello","kaushal","present","happy"]
for i in range(0,len(list_of_dicts) + 1):
    a = set(list_of_str[i])
    print(list_of_str[i],":",a)
    







    






