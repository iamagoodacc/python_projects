values = {
    'A': 1,
    'B': 2,
    'C': 3,
    'D': 4,
    'E': 5,
    'F': 6,
    'G': 7,
    'H': 8,
    'I': 9,
    'J': 10,
    'K': 11,
    'L': 12,
    'M': 13,
    'N': 14,
    'O': 15,
    'P': 16,
    'Q': 17,
    'R': 18,
    'S': 19,
    'T': 20,
    'U': 21,
    'V': 22,
    'W': 23,
    'X': 24,
    'Y': 25,
    'Z': 26,
}

reversed_values = {v: k for k, v in values.items()}

def calculate_word_score(word):
    score = 0
    for letter in word:
        score += ord(letter) - ord('A') + 1
    return score

def find_combos(wordlist, amount):
    arrayofwords = []
    dp = [float('inf')] * (amount + 1)

    dp[0] = 0
    for word in wordlist:
        word = calculate_word_score(wordlist)
        for i in range(word, amount + 1):
            #arrayofwords.append(dp[i - word] + 1)
            dp[i] = min(dp[i], dp[i - word] + 1)
            #dp[i].append(dp[i - word] + 1)

    # if dp[amount] != float('inf') :
    #     return dp[amount]
    return dp[amount]
    
print(find_combos(values, 5))