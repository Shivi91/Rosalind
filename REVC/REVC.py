# Complementing a Strand of DNA
import string
dnaString = raw_input()
reversedString = dnaString[::-1]
translationTable = string.maketrans("ACGT", "TGCA")
complementString = reversedString.translate(translationTable)
print complementString