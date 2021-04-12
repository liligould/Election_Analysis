# Election Analysis

## Purpose
With the help of Python, VS Code a report highlighting total votes, candidates and percentage of votes each candidate received. This information in turn can tell us who won the election.Based on the previous work completed, the purpose of this election analysis audit was to provide the commission with further information. We had to show them the voter turnout for each county, the percentage of votes from each county out of the total count as well as the county with the highest turnout. All this information could be found by looking at the reported total votes, candidates and percentage of votes each candidate received. For loops and conditional statements were used to provide this information.

## Findings
Below is a list of the important information gathered and how the results were found.

- How many votes were cast in this congressional election?
  * By first initializing a total vote count equal to zero, votes counted for each candidate in each county were then added together to get the total vote count of 369,711.
  *![Total Vote=0](https://user-images.githubusercontent.com/80358062/114328957-c9561080-9b03-11eb-99a2-0a8b584fef95.png)

- Provide a breakdown of the number of votes and the percentage of total votes for each county in the precinct.
  * To collect the total vote count and to collect individual information for each candidate a breakdown of number of votes per county and percentage of votes per county were necessary for further analysis. To do this a dictionary first had to be initialized. This allowed us to then track the number of votes per county
  * Insert screen shot (4c and 5). 
  * When the numbers for each county were collected we are then able to track the voting percentage per county.
  *  (6c).

- Which county had the largest number of votes?
  * After creating the county results we were able to determine the largest county turnout based on total number of votes and total voter percentage which was Denver with 82.8% of total votes or 306,055 total votes out of 369,711.

  * Insert screenshot (6c and 6f)

- Provide a breakdown of the number of votes and the percentage of the total votes each candidate received.
  * With the data we were given in blank file we were able to extract the candidate names from each row (row[2]) by first setting winning candidate to an empty set, and winning count and percentage starting at zero. (line 24). Using the information we gathered from the total votes we are able to determine the number of votes each candidate received as well as the percent of votes they held. (line 132)

- Which candidate won the election, what was their vote count, and what was their percentage of the total votes?
  * Based on the information gathered we were able to determine that Diana DeGette won the election with a winning vote count of 272,892 votes and winning percentage of 73.8%. (winning candidate summary)

Summary
There is a statement to the election commission that explores how this script can be used for any election, with two examples for modifying the script. 


