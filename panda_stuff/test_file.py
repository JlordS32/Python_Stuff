# Importing pandas library
import pandas as pd
import json

# Creating and initializing a nested list
name = ["Jaylou", "John", "Cena", "Ice", "Flame", "Gold", "Luffy", "Mary"]
age = [19, 22, 34, 24, 23, 55, 21, 12]
gender = ["Male", "Male", "Male", "Male", "Male", "Male", "Male", "Female"]

data = []
for i in zip(name, age, gender):
       data.append(i)
# Creating a pandas dataframe
df = pd.DataFrame(data, columns=['Name', 'Marks', 'Gender'])

# Printing dataframe
print(df)