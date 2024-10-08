with open ("new.txt") as fp:
     data1= fp.read()
with open("new1.txt") as fp:
    data2= fp.read()
    
data1+="\n"
data1+=data2 
print("Merging two files")
with open ("Mergedfile.txt","w") as fp:
    fp.write(data1)


outputFile=open("updatedFile.txt","w")
inputFile=open("Mergedfile.txt","r")
linesSeenSoFar=set()
print("Eliminating dublicate lines")
for line in inputFile:
    if line not in linesSeenSoFar:
        outputFile.write(line)
        linesSeenSoFar.add(line)
inputFile.close()
outputFile.close()