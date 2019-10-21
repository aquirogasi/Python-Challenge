
import os
import csv
import statistics

# Path to collect data from the Resources folder
paybank_csv = os.path.join('..', 'python-challenge', 'budget_data.csv')

# Read in the CSV file
with open(paybank_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Skeep the header
    header = next(csvreader)
    
    # Initialize net_total variable to zero
    net_total = 0
    
    # Initialize empty lists 
    changes_list = []
    changes_pair_list = []
    merged_list =[]
    
    
    # Create a list of tuples from csvreader using list comprehension
    # This list is composed of pair values: (month, profit_losses)
    pair_list = [tuple(row) for row in csvreader]
    
    # Find the total number of months by calculating the lengh of the created list of tuples
    total_months = len(pair_list)
    
    # Loop through the list of tuples 
    for pair in pair_list:
        
        # Find the net total amount of "Profit_Losses"
        # 2nd position's values in tuples are transformed to integer to allow arichmetic operation (+) 
        net_total += int(pair[1])
                
    # Loop through the list in a the range 1 to lengh of list               
    for i in range(1,len(pair_list)):
        
        # Find the changes in "Proffit_Losses" by moving through the list by elements (i),
        # but only pointing the 2nd position value in each of the tupples (index 1) 
        changes = int(pair_list[i][1]) - int(pair_list[i-1][1])
        
        # Find the corresponding pair of each change, this time pointing the frist position value in the tuples (index 0) 
        changes_pair = str(pair_list[i][0])
            
        # Create a list of changes
        changes_list.append(changes)
        
        # Create a list of changes's pairs
        changes_pair_list.append(changes_pair)
            
            
    # Find the average of changes during the entire period using mean function from statistics library
    # Result is transformed to float 
    average_changes = float(statistics.mean(changes_list))
    
    # Create a new list of tuples by zipping the two previous lists 
    # This new list is composed of pairs: (months, corresponding changes's values)
    merged_list = zip(changes_pair_list,changes_list)
    
    # Initialize two empty tuples
    greatest_increase_pair = (0,0)
    greatest_decrease_pair = (0,0)
    
    # Loop through list of tuples "merged_list"
    for merged_pair in merged_list:
        
        # Conditional statement to set greatest increase - pair / tuple 
        if merged_pair[1] > greatest_increase_pair[1]:
            
            greatest_increase_pair = merged_pair
        
        # Conditional statement to set greatest decrease - pair / tuple 
        if merged_pair[1] < greatest_decrease_pair[1]:
        
            greatest_decrease_pair = merged_pair

# Open a text file with w+ which indicates write and create a file if it does not exist in library
file = open("pay_bank.txt","w+")

# Write results in the text file
file.write('Financial Analysis \n')
file.write('------------------------\n')
file.write(f"Total Months: {total_months} \n")
file.write(f"Total: {'${}'.format(net_total)} \n")
file.write(f"Total: {'${:0.2f}'.format(average_changes)} \n")
file.write(f"Greatest Increase in Profits: {greatest_increase_pair[0]} ({'${}'.format(greatest_increase_pair[1])}) \n")
file.write(f"Greatest Decrease in Profits: {greatest_decrease_pair[0]} ({'${}'.format(greatest_decrease_pair[1])}) \n")
        
# Print all the results to the terminal 
print("Financial Analysis")
print("-----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: {'${}'.format(net_total)}")
print(f"Total: {'${:0.2f}'.format(average_changes)}")
print(f"Greatest Increase in Profits: {greatest_increase_pair[0]} ({'${}'.format(greatest_increase_pair[1])})")
print(f"Greatest Decrease in Profits: {greatest_decrease_pair[0]} ({'${}'.format(greatest_decrease_pair[1])})")

# Closing the file      
file.close()





