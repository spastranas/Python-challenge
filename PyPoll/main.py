# Modules
import os
import csv


# Set path for file, My file is located under the PYBank folder. 
csvpath = os.path.join("..", "PyPoll", "election_data.csv")

# Open the CSV
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
# first row as a header.
    csv_header = next(csvfile)

#look at the file for general findings: total voters and candidates    
#Create list of distinct candidates
    CandidateList = []
    TotalVoters=0
    for row in csvreader:
        TotalVoters+=1

        if row[2] not in CandidateList:
            CandidateList.append(row[2])
    #print (CandidateList)
    NumberOfCandidates=len(CandidateList)
    
    #With the candidate names stored in the list, create one dictionary per candidate.
    MasterDictonary={}
    MaxPercentageVote=00
    n = NumberOfCandidates
    while n > 0:
            DictionaryName=(CandidateList[n-1])
            Dictionary={"Name":DictionaryName, "VoteCount":0}
            
            #After creating the dictionay, loop through the file to tally counts for the candidate and update the dictionary.
            #have to open the file each time
            with open(csvpath, newline="") as csvfile:
                csvreader = csv.reader(csvfile, delimiter=",")
                csv_header = next(csvfile)
                # loop through the file with a list comprenhention for improved performance
                VoterList=[rows[0] for rows in csvreader if rows[2]==CandidateList[n-1]]
                VoterCount=len(VoterList)
                PercentageVotes= VoterCount/TotalVoters    
                #update voter count on the dictionary
                Dictionary["VoterCount"]=VoterCount 
                Dictionary["Percentage Votes"]=int(PercentageVotes*100)
                if PercentageVotes>MaxPercentageVote:
                    Winner=Dictionary["Name"]  
                    MaxPercentageVote=PercentageVotes        
                #print (Dictionary)
                #append dictionaries into a master dictinary for reporting
                MasterDictonary[n]=Dictionary
               
            n -= 1
# print results            
    print ("")
    print ("Election Results")
    print ("---------------------------------------------------------")
    print ("Total Votes %s" % TotalVoters)
    print ("---------------------------------------------------------")

#make it dynamic
NumberOfCandidates=len(CandidateList)
n = NumberOfCandidates
while n > 0:
    print (MasterDictonary[n]['Name']+ ": " + str(MasterDictonary[n]['Percentage Votes'])+".000% ("+ str(MasterDictonary[n]['VoterCount'])+")" )
    n -= 1

print ("---------------------------------------------------------")
print ("Winner: " +(Winner))
print ("---------------------------------------------------------")


#export to a csv file

# Write it to PyBank folder
output_path = os.path.join("..", "PyPoll", "ElectionsReport.csv")

# Open the file, create variable for content
with open(output_path, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')
    #write row 1
    csvwriter.writerow(['Elections Report'])

    # Report will have one column. write each row
    #make it dynamic
    NumberOfCandidates=len(CandidateList)
    n = NumberOfCandidates
    while n > 0:

        csvwriter.writerow([MasterDictonary[n]['Name']+ ": " + str(MasterDictonary[n]['Percentage Votes'])+".000% ("+ str(MasterDictonary[n]['VoterCount'])+")" ])
        n -= 1
    csvwriter.writerow([("Winner: " +(Winner))])    
    
    
