cards_input = []
cards = {'K': 13, 'Q': 12, 'J': 11, '10': 10, '9': 9, '8': 8, '7': 7, '6': 6, '5': 5, '4': 4, '3': 3, '2': 2, 'A': 1}

input = input()

for card in input.split(' '):
    cards_input.append(cards[card])

current_guess = "higher" if cards_input[0] <= 7 else "lower"
correct_guesses = 0

for card in cards_input[1:]:
    if current_guess == "higher" and card > cards_input[0]:
        correct_guesses += 1
    elif current_guess == "lower" and card < cards_input[0]:
        correct_guesses += 1
    else:
        break

    current_guess = "higher" if current_guess == "lower" else "lower"

if correct_guesses == 5:
    print('win')
else:
    print(correct_guesses)


