# Protein Translation Problem: Translate an RNA string into an amino acid string.
#      Input: An RNA string Pattern.
#      Output: The translation of Pattern into an amino acid string Peptide.

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
        aminoAcidString += rnaCodonTable[rnaString[i:i+3]]
    return aminoAcidString
        

# Load RNA codon table
rnaCodonTable = load_rna_codon_table("RNA_codon_table_1.txt")

# Get input
print "Enter input filename:",
inputFilename = raw_input()
inputFile = open(inputFilename, 'r')
rnaString = inputFile.readline().strip()
inputFile.close()
print rnaString

# Translate RNA -> amino acids
aminoAcidString = translate_rna_to_amino_acids(rnaString, rnaCodonTable)

# Print results
outputFilename = "output.txt"
outputFile = open(outputFilename, 'w')
outputFile.write(aminoAcidString)
outputFile.close()
print aminoAcidString
