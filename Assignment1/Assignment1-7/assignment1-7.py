# Frequent Words with Mismatches Problem: Find the most frequent k-mers with mismatches in a string.
#      Input: A string Text as well as integers k and d. (You may assume k <= 12 and d <= 3.)
#      Output: All most frequent k-mers with up to d mismatches in Text.

import itertools

def is_approx_match(str1, str2, d):
    numMismatches = 0 
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            numMismatches += 1
    if numMismatches <= d:
        return True
    return False
    
def find_approx_pattern_positions(pattern, text, d):
    approxPatternPositions = []
    for i in range(len(text) - len(pattern) + 1):
        if (is_approx_match(pattern, text[i:i+len(pattern)], d)):
            approxPatternPositions.append(i)
    return approxPatternPositions


def find_most_frequent_kmers_with_mismatches(text, k, d):
    kmerFrequencies = {}
    mostFrequent = 0
    mostFrequentKmers = []
    for i in range(len(text) - k + 1):
        kmer = text[i:i+k]
        for j in range(d+1):
            for indexesToReplace in itertools.combinations(range(k), j):
                for basesToReplaceWith in itertools.product('ACGT', repeat=j):
                    # Avoid any duplicate counting by skipping k-mers with any of the same bases as the original
                    shouldContinue = False
                    for jIndex in range(j):
                        if kmer[indexesToReplace[jIndex]] == basesToReplaceWith[jIndex]:
                            shouldContinue = True
                            break
                    if shouldContinue:
                        continue
                    
                    # Do mismatch replacing
                    newKmer = ''
                    startIndex = 0
                    for jIndex in range(j):
                        newKmer += kmer[startIndex:indexesToReplace[jIndex]] + basesToReplaceWith[jIndex]
                        startIndex = indexesToReplace[jIndex]+1
                    if (startIndex < k):
                        newKmer += kmer[startIndex:]
                    
                    # Adjust frequency of this k-mer, and track most frequent
                    if newKmer in kmerFrequencies:
                        kmerFrequencies[newKmer] += 1
                    else:
                        kmerFrequencies[newKmer] = 1
                    if kmerFrequencies[newKmer] == mostFrequent:
                        mostFrequentKmers.append(newKmer)
                    elif kmerFrequencies[newKmer] > mostFrequent:
                        mostFrequentKmers = [newKmer,]
                        mostFrequent = kmerFrequencies[newKmer]
    return mostFrequentKmers

# Get input
print "Enter input filename:",
inFilename = raw_input()
inFile = open(inFilename, 'r')
line = map(str, inFile.readline().split())
print line
text = line[0]
k = int(line[1])
d = int(line[2])
print text
print k
print d
inFile.close()

mostFrequentKmers = find_most_frequent_kmers_with_mismatches(text, k, d)

# Print results
outFilename = "output.txt"
outFile = open(outFilename, 'w')
for kmer in mostFrequentKmers:
    outFile.write(kmer + " ")
outFile.close()
for kmer in mostFrequentKmers:
    print kmer,
