import random
#shouldmake option for user to guess the full word 

stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
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

lives = 6

word_list = [
    "apple", "book", "chair", "table", "water", "sun", "moon", "star", "tree", "leaf",
    "bird", "cat", "dog", "fish", "house", "car", "road", "sky", "grass", "stone",
    "cloud", "river", "mountain", "flower", "bread", "milk", "shoe", "door", "window", "clock",
    "train", "ball", "light", "rain", "wind", "snow", "fire", "sand", "beach", "music",
    "happy", "smile", "sleep", "walk", "run", "play", "jump", "sing", "read", "write"
]
useranswer = ""

chosen_word = random.choice(word_list)
#print(chosen_word)

letters = len(chosen_word)
#changing the word into underscores
for count in range(letters):
    useranswer += "_"
print(useranswer)

correctanswer = []

while "_"  in useranswer: #using "_" and 'in' to stop the loop when user completed the guess(when false exit the loop)
    user_guess = input("Guess the letter in the word = ").lower()
    useranswer = "" #deleting the data in useranswer so that when loop the answer will not continue from the prev answer
    for letter in chosen_word: # You can loop through Strings the same way you can loop through Lists(no need to change into list first!)
        #string is a set of word strung together like list(or we call it in sequence)!
        
        #for answer
        if user_guess == letter:
            useranswer += letter
            correctanswer.append(user_guess)
        elif letter in correctanswer: #take the letter from chosen word and check if have in correctanswer if have then add the letter into the answer
            useranswer += letter
        else:
            useranswer += "_"
    
    #for lives
    if user_guess not in chosen_word:
        lives -= 1
    print(stages[lives])
    if lives == 0 :
        print("Game Over!!")
        break
    
    print(useranswer)
    if "_"  not in useranswer:
        print("You win!!")
