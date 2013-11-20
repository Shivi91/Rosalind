# Spectral Convolution Problem: Compute the convolution of a spectrum.
#      Input: A collection of integers Spectrum.
#      Output: The list of elements in the convolution of Spectrum. If an element has multiplicity k, it should
#      appear exactly k times; you may return the elements in any order.

def find_spectral_convolution(spectrum):
    convolution = {}
    for i in range(1, len(spectrum)):
        for j in range(i):
            mass = spectrum[i] - spectrum[j]
            if mass > 0:
                if mass in convolution:
                    convolution[mass] += 1
                else:
                    convolution[mass] = 1
    return convolution

# Get input
print "Enter input filename:",
inputFilename = raw_input()
inputFile = open(inputFilename, 'r')
spectrum = map(int, inputFile.readline().strip().split())
inputFile.close()
print spectrum

spectrum.sort()
print spectrum
convolution = find_spectral_convolution(spectrum)
print convolution

# Print results
resultsStr = ""
for mass, k in convolution.items():
    resultsStr += (str(mass) + ' ') * k
resultsStr.strip()
print resultsStr
outputFilename = "output.txt"
outputFile = open(outputFilename, 'w')
outputFile.write(resultsStr)
outputFile.close()
