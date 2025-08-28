def cubeconundrum(document):
    idsumpower = 0

    for game in document:
        gamesubsets = game.split(': ')[1].split('; ')

        mins = {
            'green': 0,
            'red': 0,
            'blue': 0
        }

        for gamesubset in gamesubsets:
            for cubes in gamesubset.split(', '):
                cube = cubes.split(' ')
                if cube[1] in mins:
                    if int(cube[0]) > mins[cube[1]]:
                        mins[cube[1]] = int(cube[0])
        
        power = 1
        for value in mins:
            power *= mins[value]

        idsumpower += power

    return idsumpower


with open('D:\Visual Studio\Python\ADVENTOFCODE23\DAY2.txt') as file:
    document = [line.strip() for line in file]

result = cubeconundrum(document)
print(result)