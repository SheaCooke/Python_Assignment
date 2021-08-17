# inspired by https://exercism.io/tracks/javascript/exercises/etl/solutions/91f99a3cca9548cebe5975d7ebca6a85
import string

OLD_POINT_STRUCTURE = {
  1: ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'R', 'S', 'T'],
  2: ['D', 'G'],
  3: ['B', 'C', 'M', 'P'],
  4: ['F', 'H', 'V', 'W', 'Y'],
  5: ['K'],
  8: ['J', 'X'],
  10: ['Q', 'Z']
}

def old_scrabble_scorer(word):
    word = word.upper()
    letterPoints = ""

    for char in word:

        for point_value in OLD_POINT_STRUCTURE:

            if char in OLD_POINT_STRUCTURE[point_value]:
                letterPoints += 'Points for {char}: {point_value}\n'.format(char = char, point_value = point_value)

    return letterPoints

def simple_scorer(word):
    for i in word:
        if i not in string.ascii_letters:
            word = word.replace(i , '')

    return len(word)


def vowel_bonus_scorer(word):
    score = 0
    vowles = ['a','e','i','o','u']
    for i in word.lower():
        if i in vowles:
            score += 3
        elif i in string.ascii_letters:
            score += 1
    return score



# your job is to finish writing these functions and variables that we've named
# don't change the names or your program won't work as expected.

def initial_prompt():
   print("Let's play some Scrabble!\n")
   word = input("Enter a word: ")
   return word
   


# def simple_scorer():
#     return choice

# def vowel_bonus_scorer():
#     return 

def scrabble_scorer():
    return

scoring_algorithms = ( {'Name': 'Simple Score', 'Description': 'Each letter is worth 1 point.', 'Score Function':'A function with a parameter for user input that returns a score.'}, {'Name':'Bonus Vowels' , 'Description': 'Vowels are 3 pts, consonants are 1 pt.', 'Score Function':'A function that returns a score based on the number of vowels and consonants.'}, {'Name': 'Scrabble', 'Description': 'The traditional scoring algorithm.', 'Score Function':'Uses the old_scrabble_scorer() function to determine the score for a given word.'}      )

def scorer_prompt(word):
    choice = int(input("Select scoring algorithm:\n0-Simple\n1-Vowel bonus\n2-Scrabble Scorer"))
    if choice == 0:
        print()
    return scoring_algorithms[choice]

def transform():
    return

def run_program():
    word = initial_prompt()
    return scorer_prompt(word)
    # return old_scrabble_scorer(word)
