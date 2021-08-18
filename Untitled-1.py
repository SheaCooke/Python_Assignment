import string

# def vowel_bonus_scorer(word):
#     score = 0
#     vowles = ['a','e','i','o','u']
#     for i in word.lower():
#         if i in vowles:
#             score += 3
#         elif i in string.ascii_letters:
#             score += 1
#     return score


# print(vowel_bonus_scorer('tE 7st'))

OLD_POINT_STRUCTURE = {
  1: ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'R', 'S', 'T'],
  2: ['D', 'G'],
  3: ['B', 'C', 'M', 'P'],
  4: ['F', 'H', 'V', 'W', 'Y'],
  5: ['K'],
  8: ['J', 'X'],
  10: ['Q', 'Z']
}

def transform(dict):
    new_point_structure = {}
    for k,v in dict.items():
        for letters in v:
            new_point_structure[letters.lower()] = k
    new_point_structure[' '] = 0


    return new_point_structure


print(transform(OLD_POINT_STRUCTURE))