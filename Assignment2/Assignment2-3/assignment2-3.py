# Generating Theoretical Spectrum Problem: Generate the theoretical spectrum of a cyclic peptide.
#      Input: An amino acid string Peptide.
#      Output: Cyclospectrum(Peptide).

def load_amino_acid_integer_mass_table(filename):
    aminoAcidIntegerMassTable = {}
    
    # Read lines from file
    inputFile = open(filename, 'r')
    lines = inputFile.readlines()
    inputFile.close()
    
    # Process lines into table
    for line in lines:
        aminoAcid, mass = line.strip().split()
        mass = int(mass)
        aminoAcidIntegerMassTable[aminoAcid] = mass
    
    return aminoAcidIntegerMassTable

def calculate_mass(peptide, aminoAcidIntegerMassTable):
    totalMass = 0
    for x in peptide:
        totalMass += aminoAcidIntegerMassTable[x]
    return totalMass

def find_cyclo_spectrum(peptide, aminoAcidIntegerMassTable):
    peptideLength = len(peptide)
    
    # Add 0 to the spectrum
    cycloSpectrum = [0,]
    
    # For each length of amino acids (except 0 and total length)
    for subpeptideLength in range(1, peptideLength):
        # For each subpeptide of the given length
        for i in range(peptideLength):
            mass = 0
            if (i+subpeptideLength > peptideLength):
                mass = calculate_mass(peptide[i:], aminoAcidIntegerMassTable)
                mass += calculate_mass(peptide[0:(subpeptideLength+i) % peptideLength], aminoAcidIntegerMassTable)
            else:
                mass = calculate_mass(peptide[i:subpeptideLength+i], aminoAcidIntegerMassTable)
            
            cycloSpectrum.append(mass)
    
    # Add total peptide mass to the spectrum
    totalPeptideMass = calculate_mass(peptide, aminoAcidIntegerMassTable)
    cycloSpectrum.append(totalPeptideMass)
    
    return cycloSpectrum

# Get input
print "Enter input filename:",
inputFilename = raw_input()
inputFile = open(inputFilename, 'r')
peptide = inputFile.readline().strip()
inputFile.close()
print peptide

# Load amino acid integer mass table
aminoAcidIntegerMassTable = load_amino_acid_integer_mass_table("integer_mass_table.txt")

cycloSpectrum = find_cyclo_spectrum(peptide, aminoAcidIntegerMassTable)
cycloSpectrum.sort()

# Print results
outputFilename = "output.txt"
outputFile = open(outputFilename, 'w')
resultStr = ' '.join(map(str,cycloSpectrum))
outputFile.write(resultStr)
print resultStr
outputFile.close()
