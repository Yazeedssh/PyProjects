import random
word_list = ["ardvark", "baboon","camel"]

chosen_word = random.choice(word_list)
print(chosen_word)

wordlen = len(chosen_word)
blank_list = ["_"]*wordlen
print(blank_list)

lives = 6

end_of_game = False
while not end_of_game:
    guess = input("Guess a letter: ").lower()

    for position in range(wordlen):
        letter = chosen_word[position]
        if letter == guess:
            blank_list[position] = letter

    if guess not in chosen_word:
        print("That is not in the word")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose);")

    print(blank_list)

    if "_" not in blank_list:
        end_of_game = True
        print("You win!")