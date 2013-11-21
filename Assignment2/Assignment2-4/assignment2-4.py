# CODE CHALLENGE: Implement CYCLOPEPTIDESEQUENCING (pseudocode reproduced below).
# 
# Note: After the failure of the first brute-force algorithm we considered, you may be hesitant to implement this algorithm for fear that its runtime will be prohibitive. The potential problem with CYCLOPEPTIDESEQUENCING is that it may generate incorrect k-mers at intermediate stages (i.e., k-mers that are not subpeptides of a correct solution). You may wish to wait to implement CYCLOPEPTIDESEQUENCING until after the next section, where we will analyze this algorithm.
# 
# CYCLOPEPTIDESEQUENCING(Spectrum)
#     List <- {0-peptide}
#     while List is nonempty
#         List <- Expand(List)
#         for each peptide Peptide in List
#             if Cyclospectrum(Peptide) = Spectrum
#                 output Peptide
#                 remove Peptide from List
#             else if Peptide is not consistent with Spectrum
#                 remove Peptide from List

def expandList(list):
    newList = []
    for peptide in list:
        for aminoAcidMass in aminoAcidMasses:
            newPeptide = peptide + [aminoAcidMass,]
            newList.append(newPeptide)
    return newList

def cyclo_peptide_sequencing(experimentalSpectrum):
    list = [0,]
    while list:
        list = expandList(list)
        for peptide in list:
            if cyclo_spectrum(peptide) == experimentalSpectrum:
                peptides.append(peptide)
                

# Get input
print "Enter input filename:",
inputFilename = raw_input()
inputFile = open(inputFilename, 'r')
experimentalSpectrum = map(int, inputFile.readline().strip().split())
inputFile.close()
print experimentalSpectrum

peptides = cyclo_peptide_sequencing(experimentalSpectrum)

# Print results
outputFilename = "output.txt"
outputFile = open(outputFilename, 'w')
resultStr = ''
outputFile.write(resultStr)
print resultStr
outputFile.close()
