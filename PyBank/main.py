
# Author: Sandra Pastrana




# Modules
import os
import csv


# Set path for file, My file is located under the PYBank folder. 
csvpath = os.path.join("..", "PyBank", "budget_data.csv")

# Open the CSV
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
# first row as a header.
    csv_header = next(csvfile)
#Create containers for variables to be used. Use dictionaries to store greates increase and decrease  
    RowCounter=0
    NetLastRow=0
    NetAmount=0
    NetRunningTotal=0
    NetChange=0
    NetChangeRunningTotal=0
    GreatestIncrease={"Month":"","Amount":0}
    GreatestDecrease={"Month":"","Amount":0}
    # Loop through file
    for row in csvreader:
        #count the number of rows as each row is one month.
        RowCounter=RowCounter+1
        #NetAmount is column 2 in the file
        NetAmount=int(row[1])
        #Create a running total for net amount
        NetRunningTotal+=NetAmount
        #calculate Net change comparing to last month's value. Start from the second row.
        if NetLastRow==0:  
            NetChange=0
        else:
            NetChange=NetAmount-NetLastRow
        #store greatest increase/ decrease in dictionaries.
        if NetChange>GreatestIncrease["Amount"]:
            GreatestIncrease["Month"]=row[0]
            GreatestIncrease["Amount"]=int(NetChange)
        if NetChange<GreatestDecrease["Amount"]:
            GreatestDecrease["Month"]=row[0]
            GreatestDecrease["Amount"]=int(NetChange)
        #Create a running total for net change        
        NetChangeRunningTotal+=NetChange
        #store Net amount to be compared with next row execution.
        NetLastRow=NetAmount
    #calculate average change    
    averageChange=NetChangeRunningTotal/(RowCounter-1)
# create final report
    print("")
    print ("Financial Report")
    print("---------------------------------------------------------")
    print("Total Months:  %s" % RowCounter)
    print("Total: $%s" % NetRunningTotal)
    print ("Greatest Increase In Profits: "+ GreatestIncrease['Month'] +" ($"+ str(GreatestIncrease['Amount'])+")")
    print ("Greatest Decrease In Profits: "+ GreatestDecrease['Month'] +" ($"+ str(GreatestDecrease['Amount'])+")")
#export to a csv file

# Write it to PyBank folder
output_path = os.path.join("..", "PyBank", "PYBankReport.csv")

# Open the file, create variable for content
with open(output_path, 'w', newline='') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')

    # Write the first row
    csvwriter.writerow(['Financial Report'])

    # Report will have one column. write each row
    csvwriter.writerow(["Total Months:  %s" % RowCounter])
    csvwriter.writerow(["Total: $%s" % NetRunningTotal])
    csvwriter.writerow(["Greatest Increase In Profits: "+ GreatestIncrease['Month'] +" ($"+ str(GreatestIncrease['Amount'])+")"])
    csvwriter.writerow(["Greatest Decrease In Profits: "+ GreatestDecrease['Month'] +" ($"+ str(GreatestDecrease['Amount'])+")"])
