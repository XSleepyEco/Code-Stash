from sys import argv 
import time

start = time.time()

script, file1, file2, file3, file4, file5, outputPath = argv 

dict = {}
column = 0
i = 0
prev_prop_len = 0
curr_prop_len = 0
prop_len = 0
#For each file
#for fName in argv[1:6]:
#    f = open(fName)
#    lines = f.readlines()
#    f.close()

#For each file
for fName in argv[1:6]:
    #print("prev prop len ", prev_prop_len)
    #print("old prop len ", prop_len)
    prop_len += prev_prop_len
    #print("new prop len ", prop_len)
    print(fName)
    f = open(fName)
    header = f.readline()                   #Grab the headers
    curr_prop_len = len(header.split(',')) - 1   #Number of properties
    print(header)
    f.seek(0)
    lines = f.readlines()       #Read all the lines from the file
    data = ''                   #Set data to 'nothing'

    """
    #Skip the header line
    for line in lines[1:]:
        data += line            #Put all the lines into data excluding the headers
        i += 1
        print(i)
    
    table = data.split('\n')    #Split each line into elements in a list
    """ 

    #Remove \n from items in the list
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
        """
        if len(val) < curr_prop_len and id :
            val = [''] * prop_len
            print([''] * prop_len)
            print(val)
        """

        dict[id] = val + property   #Append the properties to the end of the list which is the v
        #dict[id] = dict[id] + property

    prev_prop_len = len(header.split(',')) - 1   #Number of properties
    
    #Add empty strings when key does not appear
    for key, val in dict.items():
        if len(dict[key]) < prop_len + curr_prop_len:
            #print(([''] * curr_prop_len) )
            dict[key] = val + ([''] * curr_prop_len) 
        #i += 1
        #print(i)

    #prop_len = len(header.split(',')) - 1   #Number of properties

    f.close()
    

#print(dict)
outputFile = open("outputLive.csv", "w+")
outputFile.write("ID,Property_1,Property_2,Property_3,Property_4,Property_5,Property_6,Property_7\n")
for key, val in dict.items():
    #print("key: ", key, " Values: ", val)

    #i += 1
    #print(i)

    outputFile.write(key + ',')   #Write the key value first
    #print(key)
    #Write in each property
    """
    for v in val:
        outputFile.write(',' + v)
        i += 1
        print(i)
    """
    #print(','.join(val))
    outputFile.write(','.join(val))     #Write in the property
    outputFile.write('\n')              #Write in the nextline

outputFile.close()


#print(outputPath)

end = time.time()
print("Execution time: ", end - start)