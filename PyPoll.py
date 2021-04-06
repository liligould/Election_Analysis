# The data we need to retrieve
# 1. The total number of votes cast
# 2. A complete list of candidates who recieved votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote

# Add our dependencies
import csv
import os

# Assign a variable to LOAD a file from a path (indirect path to file)
file_to_load = os.path.join("Resources", "election_results.csv")

# Open election results and read file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    
     # Print the header row.
    headers = next(file_reader)
    print(headers)

# Assign a variable to SAVE a file from a path (indirect path to file)
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:

# Write three counties to the file.
    txt_file.write("Counties in the Election\n-----------------------\nArapahoe\nDenver\nJefferson")
