
import os
import csv
import pandas as pd

# Path to collect data from the Resources folder
payboss_csv = os.path.join('..', 'python-challenge', 'employee_data.csv')

# Use Pandas to read data
employee_data_file_pd = pd.read_csv(payboss_csv)


# Split Name column into separate First Name and Last Name columns
# Using split function with space delimeter 
new_column = employee_data_file_pd["Name"].str.split(" ", n = 1, expand = True)

# Add new columns with the corresponding string values
employee_data_file_pd["First Name"] = new_column[0]
employee_data_file_pd["Last Name"] = new_column[1]

# Dropping old Name columns 
employee_data_file_pd.drop(columns =["Name"], inplace = True) 

# Convert DOB string to datetime format 
employee_data_file_pd['DOB'] = pd.to_datetime(employee_data_file_pd.DOB)

# Change DOB datatime format to MM/DD/YYYY format
employee_data_file_pd['DOB'] = employee_data_file_pd['DOB'].dt.strftime('%m/%d/%Y')

# Hide the first 5 numbers of SSN by replacing the first 6 characters for ***-**
employee_data_file_pd["SSN"] = employee_data_file_pd["SSN"].apply(lambda x: "***-**" + x[6:])


# Convert State values to their corresponding 2 letter abreviation using replace
employee_data_file_pd['State'] = employee_data_file_pd['State'].replace(
    {'Alabama': 'AL','Alaska': 'AK','Arizona': 'AZ','Arkansas': 'AR','California': 'CA','Colorado': 'CO','Connecticut': 'CT','Delaware': 'DE','Florida': 'FL',
     'Georgia': 'GA','Hawaii': 'HI','Idaho': 'ID','Illinois': 'IL','Indiana': 'IN','Iowa': 'IA','Kansas': 'KS','Kentucky': 'KY','Louisiana': 'LA','Maine': 'ME',
     'Maryland': 'MD','Massachusetts': 'MA','Michigan': 'MI','Minnesota': 'MN','Mississippi': 'MS','Missouri': 'MO','Montana': 'MT','Nebraska': 'NE','Nevada': 'NV',
     'New Hampshire': 'NH','New Jersey': 'NJ','New Mexico': 'NM','New York': 'NY','North Carolina': 'NC','North Dakota': 'ND','Ohio': 'OH','Oklahoma': 'OK',
     'Oregon': 'OR','Pennsylvania': 'PA','Rhode Island': 'RI','South Carolina': 'SC','South Dakota': 'SD','Tennessee': 'TN','Texas': 'TX','Utah': 'UT',
     'Vermont': 'VT','Virginia': 'VA','Washington': 'WA','West Virginia': 'WV','Wisconsin': 'WI','Wyoming': 'WY'})



employee_data_file_pd.head(10)




