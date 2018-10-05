# This script removes the first row of every CSV file, no matter how many there are. 
# In order for this code to work, you need .CSV files in a folder.


import csv, os
os.makedirs('headerRemoved', exist_ok = True) # Creates a folder named 'headerReomved'

# Loop to go through every CSV file in the folder
for csvFile in os.listdir('.'): # Will open ALL the files in the folder. See next line to skip non - .csv files. 
    if not csvFile.endswith('.csv'):
        continue # Skips if the file is not a csv file

    print('Removing header from ' + csvFile + '..')

    # Read the CSV file (skip the first row AKA header)
    csvRows = []
    csvFileObj = open(csvFile) # Opens CSV file
    readerObj = csv.reader(csvFileObj) # Python reads it and assigns variable readerObj(ective)
    for row in readerObj: # And here we tell it to skip the first row
        if readerObj.line_num == 1:
            continue    # Skips the first line
        csvRows.append(row)     # Rewrites the lines in the csv as a list inside the csvRows
    csvFileObj.close()

    # Write/Output the CSV File
    csvFileObj = open(os.path.join('headerRemoved', 'new{}'.format(csvFile)), 'w', newline='') # Rewrites the CSV title with the "new" added in the title
    csvWriter = csv.writer(csvFileObj)
    for row in csvRows:
        csvWriter.writerow(row)
    csvFileObj.close()
