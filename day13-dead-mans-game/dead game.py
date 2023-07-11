# WEEK 7
import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

print(f'Pssst, the solution is {chosen_word}.')

display = []  # WEEK 7
import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

print(f'Pssst, the solution is {chosen_word}.')

display = []
word_length = len(chosen_word)
for _ in range(word_length):
    display += "_"
lives = 6

end_of_game = False
while not end_of_game:

    guess = input("Guess a letter: ").lower()
    if guess in display:
        print("Already guessed")
    for position in range(word_length):
        # for position in 10
        letter = chosen_word[position]  # chosen_word[10]
        if letter == guess:  # if chosen_word[10]  ir vienāds ar minējumu burtu
            display[position] = letter  # display[pozīcija kaut kāda = replaco letter, chosen_word positionu kas ir _ ar burtu

        if "_" not in display:
            end_of_game = True
            print("You won")
    if guess not in chosen_word:
        print('Not in Word DUMB FUCK')
    print(*display)
    if guess not in chosen_word:
        lives -= 1

    print(stages[lives])
    if lives == 0:
        end_of_game = True
        print("You lose")
    coun = 0
    if guess in chosen_word:
        coun += 1
    if coun > 1:
        print("Already guessed")
        coun = 0

word_length = len(chosen_word)
for _ in range(word_length):
    display += "_"
lives = 6

end_of_game = False
while not end_of_game:
    guess = input("Guess a letter: ").lower()
    for position in range(word_length):
        # for position in 10
        letter = chosen_word[position]  # chosen_word[10]
        if letter == guess:  # if chosen_word[10]  ir vienāds ar minējumu burtu
            display[position] = letter  # display[pozīcija kaut kāda = replaco letter, chosen_word positionu kas ir _ ar burtu

        if "_" not in display:
            end_of_game = True
            print("You won")
    print(display)
    if guess not in chosen_word:
        lives -= 1
        print(stages[lives])
    if guess not in chosen_word:
        print('Not in Word')
    if lives == 0:
        end_of_game = True
        print("You lose")
