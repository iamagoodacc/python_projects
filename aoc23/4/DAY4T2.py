def findCard(cardNum):
    with open('D:\Visual Studio\Python\ADVENTOFCODE23\DAY4MINI.txt') as file:
        document = [line.strip() for line in file]
    for card in document:
        if int(card.split(': ')[0].split('Card ')[1]) == cardNum:
            print(card)
            return card
        
def gamble(document, totalCards):
    possibilities = {}

    for card in document:
        winningNumberCount = 0

        cardNumber = int(card.split(': ')[0].split('Card ')[1])
        cardNumbers = card.split(': ')[1]
        winningNumbers = cardNumbers.split(' | ')[0].split(' ')
        inventoryNumbers = cardNumbers.split(' | ')[1].split(' ')

        for number in inventoryNumbers:
            if number.isdigit() and number in winningNumbers:
                winningNumberCount += 1

        possibilities[cardNumber] = winningNumberCount
    totalCards[0] += len(document)

    for card in possibilities: #second pass
        if possibilities[card] > 0:
            newPossibilities = []
            for i in range(1, possibilities[card]+1): #prep third pass
                newPossibilities.append(card+i)
            totalCards[0] += possibilities[card]

            noMoreCards = False
            while noMoreCards == False:
                tempdict = []
                if newPossibilities == []:
                    noMoreCards = True
                for card in newPossibilities:
                    for i in range(1, possibilities[card]+1):
                        tempdict.append(card+i)
                newPossibilities = tempdict.copy()
                totalCards[0] += len(newPossibilities)

    return totalCards[0]


with open('D:\Visual Studio\Python\ADVENTOFCODE23\DAY4.txt') as file:
    document = [line.strip() for line in file]

result = gamble(document, [0])
print(result)