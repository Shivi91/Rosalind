# Frequent Words Problem: Find the most frequent k-mers in a string.
# Input: A string Text and an integer k.
# Output: All most frequent k-mers in Text.

def most_frequent_kmers(dna, k):
    # Count the frequency of all the k-mers
    kmers = {}
    highestFrequency = 0
    i = 0
    while i < len(dna) - (k-1):
        kmer = dna[i:i+k]
        if kmer in kmers:
            kmers[kmer] += 1
        else:
            kmers[kmer] = 1
        if kmers[kmer] > highestFrequency:
            highestFrequency = kmers[kmer]
        
        i += 1
    
    # Find all the k-mers that have the highest frequency
    mostFrequentKmers = []
    for kmer, freq in kmers.iteritems():
        if freq == highestFrequency:
            mostFrequentKmers.append(kmer)
    
    return mostFrequentKmers 


# Get input
dna = raw_input()
k = input()

# Find most frequent k-mers
kmers = most_frequent_kmers(dna, k)

# Print result
for kmer in kmers:
    print kmer,