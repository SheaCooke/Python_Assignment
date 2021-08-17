import string

def vowel_bonus_scorer(word):
    score = 0
    vowles = ['a','e','i','o','u']
    for i in word.lower():
        if i in vowles:
            score += 3
        elif i in string.ascii_letters:
            score += 1
    return score


print(vowel_bonus_scorer('tE 7st'))