import random
#shouldmake option for user to guess the full word 
word_list = [
    "apple", "book", "chair", "table", "water", "sun", "moon", "star", "tree", "leaf",
    "bird", "cat", "dog", "fish", "house", "car", "road", "sky", "grass", "stone",
    "cloud", "river", "mountain", "flower", "bread", "milk", "shoe", "door", "window", "clock",
    "train", "ball", "light", "rain", "wind", "snow", "fire", "sand", "beach", "music",
    "happy", "smile", "sleep", "walk", "run", "play", "jump", "sing", "read", "write"
]

chosen_word = random.choice(word_list)
print(chosen_word)
 
user_guess = input("Guess the letter in the word = ").lower()
for word in chosen_word: # You can loop through Strings the same way you can loop through Lists(no need to change into list first!)
    #string is a set of word strung together like list(or we call it in sequence)!
    if user_guess == word:
        print("Right")
    else:
        print("Wrong")
