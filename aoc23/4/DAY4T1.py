print('\033[2J\033[H')

def gamble(document):
    totalWorth = 0
    for card in document:
        winningNumberCount = 0
        cardWorth = 0

        cardNumbers = card.split(': ')[1]
        winningNumbers = cardNumbers.split(' | ')[0].split(' ')
        inventoryNumbers = cardNumbers.split(' | ')[1].split(' ')
        for number in inventoryNumbers:
            if number.isdigit() and number in winningNumbers:
                winningNumberCount += 1
        
        if winningNumberCount > 0:
            cardWorth += 1
            for i in range(winningNumberCount-1):
                cardWorth *= 2
        totalWorth += cardWorth
    return totalWorth


with open('D:\Visual Studio\Python\ADVENTOFCODE23\DAY4MINI.txt') as file:
    document = [line.strip() for line in file]

result = gamble(document)
print(result)