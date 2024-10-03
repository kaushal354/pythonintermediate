revision of file i/o
f = open("kaushal354's Commits.csv","r")
data = f.read(5)
print(data)
print(type(data))
f.close()

f = open("kaushal354's Commits.csv","r")
dataline = f.readlines()
print(dataline)
f.close()


#Write a program that reads a text file and prints its contents.

f = open("file.txt","r")
data1 = f.read()
print(data1)
f.close()



#Create a new text file and write some content into it.
f = open("hello.txt","x")
f.write("hello")
f.close()



#write a python program to copy the contents of one text file into another
f = open("file.txt","r")
a = f.read()
f1 = open("hello.txt","w")
f1.write(a)
f.close()
f1.close()


#implement a program that reads a text file and count
#the number of words in it.
f = open("file.txt","r")
a = f.read()
b = len(a.split(" "))
print(b)


#read a CSV file and process its data.
import pandas as pd
import numpy as np
df = pd.read_csv("kaushal354's Commits.csv")
print(df.head())
a = np.sum(df["Commits"])
print(a)

#given a csv file with student names and scores,
#find the student with the highest scores.
import pandas as pd
import numpy as np
df = pd.read_csv("students1.csv")
a = np.max(df["Scores"])
max_score_row = df[df["Scores"] == a]
print(max_score_row['Students name'].values[0],"is a highest score of:",a)



#create a function that takes a list of sentences
#and writes them to a new text file, each on a new
#line
list1 = ["hello how are you?","happy birthday.","Happy new year","laptop is getting shut down"]
def listofsent():
    global list1
    f = open("listinsert.txt","a")
    for i in range(0,len(list1)):
        f.writelines(list1[i] + "\n")

listofsent()


#Given a CSV file with employee details (name, age,
# salary), calculate the average salary of all employees.
import pandas as pd
import numpy as np
df = pd.read_csv("employeedetailes.csv")
a = np.average(df["salary"].str.replace(',', '').astype(float))
print("the avg salary of all the employees is:",a)


# Write a program that reads a CSV file and finds the total
# #to find the sum of all the product and their sum
import pandas as pd
import numpy as np
import pandas as pd



df = pd.read_csv('salesstore.csv')

product_sales_sum = df.groupby('Product_Name')['Sales'].sum()

print(product_sales_sum)

#to find for specific ones
import pandas as pd
import numpy as np
import pandas as pd

product_name = "i470"

df = pd.read_csv('salesstore.csv')

product_sales_sum = df[df['Product_Name'] == product_name]['Sales'].sum()

print(product_sales_sum)





#  Given a text file with a list of numbers, write a function
# that finds the sum of all numbers in the file
def extract_numbers_simple(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        
        # Split the content by spaces and line breaks
        words = content.split()
        
        # Filter out and convert only the numbers
        numbers = [int(word) for word in words if word.isdigit()]
        
        return numbers
    
    except FileNotFoundError:
        return "The file was not found."

# Example usage
file_path = 'listofnum.txt'
print(f"Extracted numbers: {extract_numbers_simple(file_path)}")



#Implement a program that reads a CSV file and generates
# a bar chart to represent the data using Matplotlib
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("employeedetailes.csv")
x = df['age']
y = df['salary']
plt.bar(x,y)
plt.show()


# Given a CSV file with temperature data for each day of
# the week, find the average temperature for each day.
import pandas as pd
import numpy as np
df = pd.read_csv("tempraturedata.csv")
temp_avg = df.groupby("days")["temprature"].mean()
temp_avg = round(temp_avg,2)
print(temp_avg)








