# Computing GC Content

# Calculates the percentage of the DNA string that is 'G' or 'C'
def calculateGC(dnaString):
    if len(dnaString) == 0:
        return 0
    gcCount = dnaString.count("G") + dnaString.count("C")
    print gcCount, len(dnaString), float(gcCount) / len(dnaString)
    return float(gcCount) / len(dnaString)


inputFile = open("rosalind_gc.txt")

highestGC = 0
highestID = ""
currentGC = 0
currentID = ""
currentDNA = ""
line = ""
for line in inputFile:
    line = line.strip()
    if line.startswith(">"):
        print "\n" + currentID
        currentGC = calculateGC(currentDNA)
        if currentGC > highestGC:
            highestGC = currentGC
            highestID = currentID
        currentID = line[1:]
        currentDNA = ""
    else:
        currentDNA += line

print "\n" + currentID
currentGC = calculateGC(currentDNA)
if currentGC > highestGC:
    highestGC = currentGC
    highestID = currentID

print
print highestID
print highestGC * 100
        
inputFile.close()