#Step 3

import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

#TODO-1: - Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.

#Angela Solution
end_of_game = False

while not end_of_game:

# a = 1

# while a > 0: 
    guess = input("Guess a letter: ").lower()
    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter
            
    
    print(display)
    
    # for blank in display:
    #     if blank == "_":
    #         a = 1
    #     elif blank != "_":
    #         a = 0
    #     print("You Win!")
    #Angela Solution
    if "_" not in display:
        end_of_game = True
        print("You Win.")