# Learning CSV files
''' Benefits of CSV files:
1. simplicity
2. everything is a string
3. don't have multiple sheets
4. don't have heights and widths
5. don't have merged cells
6. can't have images or graphs
'''

import csv
# 1. Reading data from a CSV file
def reader_objects():
    exampleFile = open('example.csv')   # Reads csv file
    exampleReader = csv.reader(exampleFile)
    exampleData = list(exampleReader)
    print(exampleData)          # Returns a list of lists         
    print(exampleData[0][0])    # Returns cell A1
    print(exampleData[0][1])    # Returns cell B1
    print(exampleData[1][0])    # Returns cell A2
   
reader_objects()                # Calls the function

# 2. Reading data from large CSV file
def reader_objects_for_loop():
    exampleFile = open('example.csv')
    exampleReader = csv.reader(exampleFile)
    for row in exampleReader:
        print('Row #' + str(exampleReader.line_num) + ' ' + str(row))

reader_objects_for_loop()

# 3. Write data to a CSV file
def writer_objects():
    outputFile = open('output.csv', 'w', newline='')    # Creates a new .csv file
    outputWriter = csv.writer(outputFile)
    outputWriter.writerow(['spam', 'cats', 'dogs', 'joe'])
    outputWriter.writerow(['Hello World', 'cats', 'dogs', 'joe'])
    outputWriter.writerow(['1', '2', '3', '4'])
    outputFile.close()

writer_objects()
