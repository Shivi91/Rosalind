# Given a nucleotide p, we denote its complementary nucleotide as p.
# The reverse complement of a string Pattern = p1..pn is the string Pattern = pn .. p1 formed by taking the complement of each nucleotide in Pattern, then reversing the resulting string.
# We will need the solution to the following problem throughout the book:
# 
# Reverse Complement Problem: Reverse complement a nucleotide pattern.
#      Input: A DNA string Pattern.
#      Output: Pattern, the reverse complement of Pattern.

import string

# Find the reverse complement of dna
def reverse_complement(dna):
    reversedDna = dna[::-1]
    translationTable = string.maketrans("ACGT", "TGCA")
    reverseComplement = reversedDna.translate(translationTable)
    return reverseComplement


# Get input
f = open('dataset_3_2.txt', 'r')
dna = f.readline()
#dna = raw_input()

# Get reverse complement
reverseComplement = reverse_complement(dna)

# Print result
outF = open("output.txt", "w")
outF.write(reverseComplement)
#print reverseComplement