# Pattern Matching Problem: Find all occurrences of a pattern in a string.
#      Input: Two strings, Pattern and Genome.
#      Output: All starting positions where Pattern appears as a substring of Genome.

def find_all_pattern_positions(genome, pattern):
    positions = []
    start = 0
    position = genome.find(pattern, start)
    while (position != -1):
        positions.append(position)
        start = position + 1
        position = genome.find(pattern, start)
    return positions


# Get input
print "Enter input filename:",
inFilename = raw_input()
inFile = open(inFilename, 'r')
pattern = inFile.readline().strip()
genome = inFile.readline().strip()
inFile.close()
print pattern
print genome

# Get the starting positions of the pattern within the genome
starting_positions = find_all_pattern_positions(genome, pattern)

# Print result
outFilename = "output.txt"
outFile = open(outFilename, 'w')
print ' '.join(map(str,starting_positions))
outFile.write(' '.join(map(str,starting_positions)))
outFile.close()