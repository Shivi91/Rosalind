# Peptide Encoding Problem: Find substrings of a genome encoding a given amino acid sequence.
#      Input: A DNA string Text and an amino acid string Peptide.
#      Output: All substrings of Text encoding Peptide (if any such substrings exist).

import string

# Find the reverse complement of dna
def reverse_complement(dna):
    reversedDna = dna[::-1]
    translationTable = string.maketrans("ACGT", "TGCA")
    reverseComplement = reversedDna.translate(translationTable)
    return reverseComplement

def translate_dna_to_rna(dna):
    return dna.replace("T", "U")
    
def load_rna_codon_table(rnaCodonTableFilename):
    # Open, read, close file
    rnaCodonTableFile = open(rnaCodonTableFilename, 'r')
    lines = rnaCodonTableFile.readlines()
    rnaCodonTableFile.close()
    
    # Parse lines
    rnaCodonTable = {}
    for line in lines:
        splitLine =line.strip().split()
        codon = splitLine[0]
        if len(splitLine) > 1:
            aminoAcid = splitLine[1]
        else:
            aminoAcid = ""
        rnaCodonTable[codon] = aminoAcid
    
    return rnaCodonTable

def translate_rna_to_amino_acids(rnaString, rnaCodonTable):
    aminoAcidString = ""
    for i in range(0, len(rnaString), 3):
        if rnaString[i:i+3] in rnaCodonTable:
            aminoAcidString += rnaCodonTable[rnaString[i:i+3]]
    return aminoAcidString

def find_dna_substrings_encoding_peptide(dna, peptide, rnaCodonTable):
    print "Found first one at:", dna.find("AAGGAAGTATTTGAGCCTCATTATTAC")
    # Get reverse complement
    rcDna = reverse_complement(dna)
    
    # Translate dna to rna
    rna = translate_dna_to_rna(dna)
    print "Found first one (RNA) at:", rna.find("AAGGAAGUAUUUGAGCCUCAUUAUUAC")
    rcRna = translate_dna_to_rna(rcDna)
    
    dnaLength = len(dna)
    peptideLength = len(peptide)
    dnaSubstrings = []
    for i in range(3):
        aminoAcids = translate_rna_to_amino_acids(rna[i:], rnaCodonTable)
        print "Amino acids, len=", len(aminoAcids), "at i=", i, ":", aminoAcids
        print "Found first one (AA) at:", aminoAcids.find("KEVFEPHYY")
        rcAminoAcids = translate_rna_to_amino_acids(rcRna[i:], rnaCodonTable)
        for j in range(len(aminoAcids) - peptideLength + 1):
            if aminoAcids[j:j+peptideLength] == peptide:
                startIndex = j*3 + i
                endIndex = startIndex + (peptideLength * 3)
                dnaSubstrings.append(dna[startIndex:endIndex])
            elif rcAminoAcids[j:j+peptideLength] == peptide:
                startIndex = dnaLength - (peptideLength*3) - (j*3) - i
                endIndex = startIndex + (peptideLength * 3)
                dnaSubstrings.append(dna[startIndex:endIndex])
    
    return dnaSubstrings
        
    
# Get input
print "Enter input filename:",
inputFilename = raw_input()
inputFile = open(inputFilename, 'r')
dna = inputFile.readline().strip()
peptide = inputFile.readline().strip()
inputFile.close()
print dna
print "dna len=", len(dna)
print peptide

# Load rna codon table
rnaCodonTable = load_rna_codon_table("RNA_codon_table_1.txt")

# Search dna and its reverse complement for substrings encoding peptide
substringsEncodingPeptide = find_dna_substrings_encoding_peptide(dna, peptide, rnaCodonTable)

# Print results
outputFilename = "output.txt"
outputFile = open(outputFilename, 'w')
resultStr = '\n'.join(substringsEncodingPeptide)
outputFile.write(resultStr)
outputFile.close()
print resultStr