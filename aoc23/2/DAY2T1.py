conditions = {
    'green': 13,
    'red': 12,
    'blue': 14
}

def cubeconundrum(document):
    idsum = 0

    for game in document:
        gamenumber = game.split(': ')[0].split('Game ')[1]
        gamesubsets = game.split(': ')[1].split('; ')

        validgame = True

        for gamesubset in gamesubsets:
            total = {
                'green': 0,
                'red': 0,
                'blue': 0
            }
            for cubes in gamesubset.split(', '):
                cube = cubes.split(' ')
                if cube[1] in total:
                    total[cube[1]] += int(cube[0])
            
            for value in total:
                if total[value] > conditions[value]:
                    validgame = False
        
        if validgame == True:
            idsum += int(gamenumber)

    return idsum


with open('D:\Visual Studio\Python\ADVENTOFCODE23\DAY2.txt') as file:
    document = [line.strip() for line in file]

result = cubeconundrum(document)
print(result)