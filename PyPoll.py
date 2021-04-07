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

# Initialize total vote counter (accumulator variable)
total_votes = 0

# Declare  new list
candidate_options = []

# Declare empty dictionary
candidate_votes = {}

# Declare winning cadidate with empty string varibale
winning_candidate = ""

# Declare winning count variable equal to zero
winning_count = 0

# Declare winning percentage variable equal to zero
winning_percentage = 0

# Open election results and read file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)

    # Print each row in CSV file
    for row in file_reader:
        # Add to total_votes count (increment by 1)
        total_votes = total_votes + 1

        # Print the candidates name from each row (third col but second index)
        candidate_name = row[2]

        # If the candidate does not match  any existing candidate
        if candidate_name not in candidate_options:
            # Add candidate name to candidate options list
            candidate_options.append(candidate_name)
            #Create candidates as key and set intial vote count to zero
            candidate_votes[candidate_name] = 0
        #Add a vote to candidates count (increment by 1)
        candidate_votes[candidate_name] += 1

    # Print candidate vote dictionary
    print(candidate_votes)

    #Iterate through candidate list
    for candidate_name in candidate_votes:
        # Retrieve number of votes from each candidate
        votes = candidate_votes[candidate_name]
        # Calculate percentage
        vote_percentage = float(votes) / float(total_votes) * 100
        # Print each candidates name, number of votes and percentage of votes
        print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Determine if votes and vote percentage are greater then winning count and winning percentage
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # If true set winning count and winning percentage equal to votes and vote percentage
            winning_count = votes
            winning_percentage = vote_percentage
            # Set winning candidate equal to candidate name
            winning_candidate = candidate_name

    # Print winning candidate, votes, and winning percentage
    winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)
    

# Assign a variable to SAVE a file from a path (indirect path to file)
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:

# Write three counties to the file.
    txt_file.write("Counties in the Election\n-----------------------\nArapahoe\nDenver\nJefferson")
