# Rabbits and Recurrence Relations

def calculateRabbitPairs(n, k, solutionTable):
    if (solutionTable[n-1] == 0):
        solutionTable[n-1] = calculateRabbitPairs(n-1, k, solutionTable)
        solutionTable[n-1] += solutionTable[n-2-1] * k
    return solutionTable[n-1]


# Get input
n, k = raw_input().split(" ")
n = int(n)
k = int(k)

# Start a solution table (Dynamic Programming)
solutionTable = [0]*n
if (n == 1):
    solutionTable.append(0)
solutionTable[0] = 1
solutionTable[1] = 1

print calculateRabbitPairs(n, k, solutionTable)