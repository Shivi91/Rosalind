# Approximate Pattern Matching Problem: Find all approximate occurrences of a pattern in a string.
#      Input: Two strings Pattern and Text along with an integer d.
#      Output: All positions where Pattern appears in Text with at most d mismatches.

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

# Get input
print "Enter input filename:",
inFilename = raw_input()
inFile = open(inFilename, 'r')
pattern = inFile.readline().strip()
text = inFile.readline().strip()
d = int(inFile.readline())
inFile.close()
print pattern
print text
print d

approxPatternPositions = find_approx_pattern_positions(pattern, text, d)

# Print results
outFilename = "output.txt"
outFile = open(outFilename, 'w')
resultString = ' '.join(map(str, approxPatternPositions))
outFile.write(resultString)
outFile.close()
print resultString
