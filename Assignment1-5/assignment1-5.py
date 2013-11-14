# Minimum Skew Problem: Find a position in a genome minimizing the skew.
#      Input: A DNA string Genome.
#      Output: All integer(s) i minimizing Skew(Prefixi (Text)) among all values of i (from 0 to |Genome|)

def calculate_skews(genome):
    skews = [0,]
    for i, base in enumerate(genome):
        if base == 'C':
            skews.append(skews[i] - 1)
        elif base == 'G':
            skews.append(skews[i] + 1)
        else:
            skews.append(skews[i])
    return skews

def find_minimums_in_list(list):
    minimum = list[0]
    minimumIndexes = []
    for i, element in enumerate(list):
        if element < minimum:
            minimum = element
            minimumIndexes = [i,]
        elif element == minimum:
            minimumIndexes.append(i)
    return minimumIndexes

def find_minimum_skews(genome):
    # Calculate skew for all positions in genome
    skews = calculate_skews(genome)
    
    # Find all indexes with minimum skew
    minSkewIndexes = find_minimums_in_list(skews)
    
    return minSkewIndexes

#Get input
print "Enter input filename:",
inFilename = raw_input()
inFile = open(inFilename, 'r')
genome = inFile.readline().strip()
inFile.close()
print genome

# Find all indexes with minimum skew
minSkewIndexes = find_minimum_skews(genome)

# Print results
outFilename = "output.txt"
outFile = open(outFilename, 'w')
resultString = ' '.join(map(str, minSkewIndexes))
outFile.write(resultString)
outFile.close()
print resultString