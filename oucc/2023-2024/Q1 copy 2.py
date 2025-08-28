cards = {'K': 13, 'Q': 12, 'J': 11, '10': 10, '9': 9, '8': 8, '7': 7, '6': 6, '5': 5, '4': 4, '3': 3, '2': 2, 'A': 1}

cardlist = []
cardinput = input()

for card in cardinput.split(' '):
    cardlist.append(card)

cardsguessed = 0
currentvalue = 0
higher = False

for i, card in enumerate(cardlist):
    if i == 0 and int(card) > 7:
        cardsguessed += 1
    elif i == 0 and int(card) <= 7:
        print(cardsguessed)
    else:
        if higher == False:
            if int(card) < 7:
                cardsguessed += 1
            elif int(card) >= 7:
                print(cardsguessed)
            higher = not higher
        else:
            if int(card) > 7:
                cardsguessed += 1
            elif int(card) <= 7:
                print(cardsguessed)
            higher = not higher
            

