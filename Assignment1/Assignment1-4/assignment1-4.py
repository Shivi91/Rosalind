# Clump Finding Problem: Find patterns forming clumps in a string.
#      Input: A string Genome, and integers k, L, and t.
#      Output: All distinct k-mers forming (L, t)-clumps in Genome.

# Finds all k-mers in the given genome
# Returns a mapping of k-mer to a list of indexes that it was found at
def find_kmers(genome, k):
    kmers = {}
    i = 0
    while i < len(genome) - (k - 1):
        kmer = genome[i:i+k]
        if kmer in kmers:
            kmers[kmer].append(i)
        else:
            kmers[kmer] = [i,]
        i += 1
    return kmers
        

def is_Lt_clump(positions, k, L, t):
    i = 0
    while len(positions) - i >= t:
        if positions[i+t-1] - positions[i] + k <= L:
            return True
        i += 1
    return False

# Get input
print "Enter input filename:",
inFilename = raw_input()
inFile = open(inFilename, 'r')
genome = inFile.readline().strip()
k, L, t = map(int, inFile.readline().strip().split())
inFile.close()
print genome
print k, L, t

# Find all k-mers and their locations
print "Finding all k-mers and their locations"
kmers = find_kmers(genome, k)

# For each k-mer, check if it forms an (L, t)-clump
print "Checking each k-mer for (L, t)-clumps"
clumpedKmers = []
for kmer, positions in kmers.items():
    if is_Lt_clump(positions, k, L, t):
        clumpedKmers.append(kmer)

# Print results
outFilename = "output.txt"
outFile = open(outFilename, 'w')
outFile.write(' '.join(clumpedKmers))
outFile.close()
print ' '.join(clumpedKmers)