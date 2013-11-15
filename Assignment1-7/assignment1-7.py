# Frequent Words with Mismatches Problem: Find the most frequent k-mers with mismatches in a string.
#      Input: A string Text as well as integers k and d. (You may assume k <= 12 and d <= 3.)
#      Output: All most frequent k-mers with up to d mismatches in Text.

DNA_BASES = ['A', 'C', 'G', 'T']

def find_most_frequent_kmers_with_mismatches(text, k, d):
    
                

# Get input
print "Enter input filename:",
inFilename = raw_input()
inFile = open(inFilename, 'r')
line = map(str, inFile.readline().split())
inFile.close()
text = line[0]
k = int(line[1])
d = int(line[2])
print text
print k
print d

mostFrequentKmers = find_most_frequent_kmers_with_mismatches(text, k, d)

# Print results
outFilename = "output.txt"
outFile = open(outputFilename, 'w')
resultStr = ' '.join(mostFrequentKmers)
outFile.write(resultStr)
outFile.close()
print resultStr
