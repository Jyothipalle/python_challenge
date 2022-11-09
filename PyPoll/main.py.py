#Week3 - Challenge 2
#Pypoll - Election results
#Author: Jyothi Palle
# Calcualte Total votes
# Calcuate each candidate name, votes polled and percentage of votes polled
# Find the winner
# Write the output in terminal and text file

# Import dependencies
import os
import csv

# assign variable to load file from path
csvfile_path=os.path.join("Resources","election_data.csv")
#Define candidate options list
candidate_options=[]
#Define candidate votes dictionary
candidate_votes={}
# Initialise total votes counter
total_votes=0

# Open the csv file and read the file
with open(csvfile_path,'r',encoding="utf") as csvfile:
    #Reading 
    csvreader=csv.reader(csvfile,delimiter=",")
    #Read header row
    header=next(csvreader)
    # Reading each row in the file
    for row in csvreader:
        # Add to the total votes
        total_votes = total_votes+1
        #Read candidate name for each row
        candidate_name=row[2]
        # Check if the candidate name does not match in existing candidate name in candidate options
        if candidate_name not in candidate_options:
           # Add candidate name to the candidate options
           candidate_options.append(candidate_name)
           #Start counting the votes for that candidate
           candidate_votes[candidate_name]=0
        
        # Increment the votes for that candidate
        candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1

#Declare winner name and winner count
winner_name=""
winner_count=0

#assign variable to the output text file path
txtfile_path=os.path.join("pypoll_output.txt")

#Open the text file and print the results
with open(txtfile_path,"w") as txtfile:
    #Print the output header and total votes     
    txt_output1= (
        f"Election Results \n"
        f"------------------------------------------------------------\n\n"
        f"Total Votes: {total_votes}\n\n"
        f"------------------------------------------------------------\n")
    #Print to the terminal
    print(txt_output1)
    # Write output to the text file
    txtfile.write(txt_output1)

    #Loop candidate votes dictionary to get votes and calculate votes percentage
    for candidate_name in candidate_votes:
        # Get the vote counts for the candidate
        votes=candidate_votes[candidate_name]
        # Calcualte percentage votes polled
        votes_perc=float(votes) / float(total_votes) * 100
        #Write candiate name, percentage votes polled and votes polled to a variable
        results = (f"{candidate_name}: {votes_perc:.3f}% ({votes:,})\n")
        #print the results variable to terminal for each candidate
        print(results)
        #Write the results to text file 
        txtfile.write(results)
   
        #Find the winner who got the highest votes
        if (votes > winner_count):
            #Assign the winner name count and name
            winner_count=votes
            winner_name=candidate_name
   # Write the winner name output as required to a variable
    winner_results=(
        f"------------------------------------------------------------\n\n"
        f"Winner : {winner_name}\n\n"
        f"------------------------------------------------------------\n\n")
    #Print winner results to terminal
    print(winner_results)
    #Write winner results to text file
    txtfile.write(winner_results)




        