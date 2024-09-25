#create a program that checks if a given string is a palindrome
string1 = input("enter a string: ")
lengof = len(string1) - 1
loop = lengof / 2
no = int(loop)
string2 = string1
j = 0
for i in range(0,no):
    if string1[i] == string2[lengof - i]:
        j = j + 1
    else:
        j = j + 0
if j == no:
    print("it is palindrome")
else:
    print("it is not a palindrome")

#write a function to count the no of vowels
# in a given string

string3 = "microsoft azure"
vowel = "aeiouAEIOU"
num = 0
for i in range(0,10):
    num = string3.count(vowel[i]) + num
print(num)

#given a list of words , concatenate them into a single string seprated
#by spaces.
list1 = ["kaushal","aditya","komal","aryan"]
result = " ".join(list1)
print(result)

#create a function to reverse a given string
def reversestr():
    str3 = input("enter a string: ")
    length3 = len(str3) - 1
    for i in range(0,length3 + 1):
        print(str3[length3 - i],end= "")
reversestr()

#write a program that takes a sentence as input
#counts the number of words in it.
sentence = input("enter a sentence:")
words = sentence.split()
print(len(words))

#implement a function that checks if a given string
#a pangram(contain all letter of alphabet)
import string
str6 = "the quick brown fox jumps over the lazy dog"
alphabet = set(string.ascii_lowercase)
input_set = set(str6.lower())
if alphabet <= input_set:
    print("string is a pangram")
else:
    print("string is not a pangram")

#given a string, write a function to remove all
#vowels from it and return the modified string
string9 = "kaushal"
vowel = "aeiouAEIOU"
str9 = list(string9)
len9 = len(str9)
for i in range(0,len9):
    for j in range(0,10):
        if string9[i] == vowel[j]:
            a = string9[i]
            str9.remove(a)
        else:
            pass
print("".join(str9))

#write a python program to find the length of the 
#longest word in a sentence
string22 = "buy anti cavity mouthwash now"
words = string22.split()
a = len(words)
b = len(words[0])
for i in range(1,a):
    if b <= len(words[i]):
        b = len(words[i])
    else:
        pass
print(b)

#create a program that takes a sentence as input
#and returns the sentence in reverse order.
sentence = input("enter a sentence:-")
length6 = len(sentence) - 1
for i in range(0,length6 + 1):
    print(sentence[length6 - i],end = "")

# given a list of names, count the number of names
# that start with a vowel
list6 = ["komal","kaushal","aryan","abhishek","om","eliza"]
listrg = len(list6)
a = 0
vowel = ['a','i','e','o','u','A','E','I','O','U']
for i in range(0,listrg):
    b = list6[i]
    for j in range(0,10):
        if b[0] == vowel[j]:
            a = a + 1
        else:
            a = a + 0
print(a)

#write a program to remove all duplicate characters
#from a given string
from ordered_set import OrderedSet
str99 = "kaushal"
b = OrderedSet(str99)
a = "".join(b)
print(a)

#implement a program that takes a sentence and 
#a word as input and checks if the word
#is present in the sentence.
sentence6 = input("enter a sentence :")
words = input("enter a words:")
a = sentence6.count(words)
if a > 0:
    print(words,"found")
else:
    print(words,"not found")








