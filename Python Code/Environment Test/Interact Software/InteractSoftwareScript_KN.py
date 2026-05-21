from sys import argv 
import time

start = time.time()

script, file1, file2, file3, file4, file5, outputPath = argv 

dict = {}
prev_prop_len = 0
curr_prop_len = 0
prop_len = 0

#For each file
for fName in argv[1:6]:
    prop_len += prev_prop_len                       #Total number of properties processed so far
    f = open(fName)                                 #Open the file
    header = f.readline()                           #Grab the headers
    curr_prop_len = len(header.split(',')) - 1      #Number of properties in the currrent file
    f.seek(0)                                       #Reset to the start of the file
    lines = f.readlines()                           #Read all the lines from the file
    data = ''                                       #Set data to 'nothing'

    #Remove \n from items in the list (cleaning the data)
    for i in range(1, len(lines)):
        lines[i] = lines[i].replace("\n", "")

    #ignore header
    table = lines[1:]

    #For each line in the table
    for row in table:
        #i += 1
        #print(i)
        element = row.split(',')    #Split into elements
        id = element[0]

        property = element[1:]      #All properties past the Id column
        
        val = dict.get(id, [])      #Value of the key 

        dict[id] = val + property   #Append the properties to the end of the list which is the v

    prev_prop_len = len(header.split(',')) - 1   #Number of properties
    
    #Add empty strings when key does not appear
    for key, val in dict.items():
        if len(dict[key]) < prop_len + curr_prop_len:
            dict[key] = val + ([''] * curr_prop_len) 

    f.close()

print(outputPath + "\outputLive.csv")
outputFile = open(outputPath + "outputLive.csv", "w+")                                                               
outputFile.write("ID,Property_1,Property_2,Property_3,Property_4,Property_5,Property_6,Property_7\n") #Write in the headers

for key, val in dict.items():
    outputFile.write(key + ',')         #Write the key value first
    outputFile.write(','.join(val))     #Write in the property
    outputFile.write('\n')              #Write in the nextline

outputFile.close()

end = time.time()
print("Execution time: ", end - start)