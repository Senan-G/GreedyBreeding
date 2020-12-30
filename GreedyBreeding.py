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
bestValue = [[0, 0, 0, 0, 0]]

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

                avgVal1 = (data.at[data.index[R1], data.columns[C1]] + data.at[data.index[R2], data.columns[C2]]) / 2
                avgVal2 = (data.at[data.index[R1], data.columns[C2]] + data.at[data.index[R2], data.columns[C1]]) / 2
                valDifference = abs(avgVal1 - avgVal2)
                print('New Best Value at', R1, C1, R2, C2, '   ', valDifference, 'coins')

                if valDifference > bestValue[0][4]:
                    bestValue = [[R1, C1, R2, C2, valDifference]]
                    print('New Best Value at', R1, C1, R2, C2, '   ', valDifference, 'coins')
                elif valDifference == bestValue[0][4]:
                    bestValue.append([R1, C1, R2, C2, valDifference])

                C2 += 1
                count += 1

            R2 += 1

print()
print(count, 'breeding pairs evaluated\nBest Value: +' + str(bestValue[0][4]), '\n')

print('All +' + str(bestValue[0][4]), 'coin pairings\n-------------------------------------------')
for breedingPair in bestValue:

    pair1 = data.at[data.index[breedingPair[0]], data.columns[breedingPair[1]]] + data.at[data.index[breedingPair[2]], data.columns[breedingPair[3]]]
    pair2 = data.at[data.index[breedingPair[0]], data.columns[breedingPair[3]]] + data.at[data.index[breedingPair[2]], data.columns[breedingPair[1]]]

    if pair1 < pair2:
        print(data.index[breedingPair[0]], data.columns[breedingPair[1]], breedName, '+', data.index[breedingPair[2]], data.columns[breedingPair[3]], breedName)
    elif pair2 < pair1:
        print(data.index[breedingPair[0]], data.columns[breedingPair[3]], breedName, '+', data.index[breedingPair[2]], data.columns[breedingPair[1]], breedName)