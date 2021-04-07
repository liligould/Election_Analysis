# Add our dependencies.
import csv
import os

# Assign a variable to LOAD a file from a path (indirect path to file)
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to SAVE the file to a path (indirect path to file)
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize total vote counter (accumulator variable)
total_votes = 0
# Declare new list
candidate_options = []
# Declare empty dictionary
candidate_votes = {}
# Declare winning candidate with empty string variable. Declare winning count and winning % variables equal to zero.
winning_candidate = ""
winning_count = 0
winning_percentage = 0
# Open the election results and read the file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    # Read the header row
    headers = next(file_reader)
    # Print each row in the CSV file
    for row in file_reader:
        # Add to the total vote count (increment by 1)
        total_votes += 1
        # Print candidates name from each row (third col but second index)
        candidate_name = row[2]
        # If candidate does not match any existing candidate, add 
        # the candidate list
        if candidate_name not in candidate_options:
            # Add candidate name to the candidate options list
            candidate_options.append(candidate_name)
            # Create candidate as key and set initial vote count to zero
            candidate_votes[candidate_name] = 0
        # Add a vote to candidates count (increment by 1)
        candidate_votes[candidate_name] += 1

# Save results to text file
with open(file_to_save, "w") as txt_file:
    # Print final vote count to terminal
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    # Save final vote count to text file
    txt_file.write(election_results)
    for candidate_name in candidate_votes:
        # Retrieve vote count from each candidate
        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each candidates name, number of votes, and % of votes
        print(candidate_results)
        #  Save candidate results to text file
        txt_file.write(candidate_results)
        # Determine winning vote count, winning percentage, and winning candidate
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage
    # Print winning candidates results to the terminal
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    # Save the winning candidate's results to the text file
    txt_file.write(winning_candidate_summary)
