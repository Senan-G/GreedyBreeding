import pandas

while True:
    breedName = input('Enter breed to evaluate: ')
    fileName = 'venv/src/' + breedName + '.csv'

    try:
        data = pandas.read_csv(fileName, index_col='Unnamed: 0')
        print()
        break
    except:
        print('Breed not in database')
# print(data)

count = 0
bestPairs = [[0, 0, 0, 0, 0]]

# topleft = data.at[data.index[R1], data.columns[C1]]
# topright = data.at[data.index[R1], data.columns[C2]]
# botleft = data.at[data.index[R2], data.columns[C1]]
# botright = data.at[data.index[R2], data.columns[C2]]


for R1 in range(23):

    for C1 in range(16):

        R2 = R1 + 1

        while R2 < 23:

            C2 = C1 + 1

            while C2 < 16:

                mainDiagonal = data.at[data.index[R1], data.columns[C1]] + data.at[data.index[R2], data.columns[C2]]
                counterDiagonal = data.at[data.index[R1], data.columns[C2]] + data.at[data.index[R2], data.columns[C1]]
                avgProfit = 0

                if mainDiagonal < counterDiagonal:
                    avgProfit = ((mainDiagonal + counterDiagonal) / 4) - int(mainDiagonal / 4)
                else:
                    avgProfit = ((mainDiagonal + counterDiagonal) / 4) - int(counterDiagonal / 4)


                if avgProfit > bestPairs[0][4]:
                    bestPairs = [[R1, C1, R2, C2, avgProfit]]
                    print('New Best Average Profit at', R1, C1, R2, C2, '   ', avgProfit, 'coins')
                elif avgProfit == bestPairs[0][4]:
                    bestPairs.append([R1, C1, R2, C2, avgProfit])

                C2 += 1
                count += 1

            R2 += 1

print()
print(count, 'breeding pairs evaluated\nBest Average Profit: ' + str(bestPairs[0][4]), 'coins\n')

print('All', str(bestPairs[0][4]), 'coin Profit Pairings\n-------------------------------------------')
for breedingPair in bestPairs:

    pair1 = data.at[data.index[breedingPair[0]], data.columns[breedingPair[1]]] + data.at[data.index[breedingPair[2]], data.columns[breedingPair[3]]]
    pair2 = data.at[data.index[breedingPair[0]], data.columns[breedingPair[3]]] + data.at[data.index[breedingPair[2]], data.columns[breedingPair[1]]]

    if pair1 < pair2:
        print(data.index[breedingPair[0]], data.columns[breedingPair[1]], breedName, '+', data.index[breedingPair[2]], data.columns[breedingPair[3]], breedName, "\nCost to breed:", int(pair1 / 4))
    elif pair2 < pair1:
        print(data.index[breedingPair[0]], data.columns[breedingPair[3]], breedName, '+', data.index[breedingPair[2]], data.columns[breedingPair[1]], breedName, "\nCost to breed:", int(pair2 / 4))