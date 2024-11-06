import random

def fill_the_gaps_game():
    word_list = ['ubuntu', 'windows','android', 'arch','java','python','ruby']
    word = random.choice(word_list) 
    word_as_list = list(word)  
    hidden_word = word_as_list[:]  
    list_3_car = random.sample(range(len(word)), 1)
    for i in list_3_car:
        hidden_word[i] = '_'
    print("Word to complete:", ' '.join(hidden_word))
    num_try = 6
    guessed_letters = set()

    for i in range (5) :
        print("\nUpdated word:", ' '.join(hidden_word))
        guess = input("Enter a letter to fill in the gaps: ").lower()
        guessed_letters.add(guess)
        if any(word_as_list[i] == guess for i in list_3_car):
            for i in list_3_car:
                if word_as_list[i] == guess:
                    hidden_word[i] = guess
            print(" The letter is in the word.")
        else:
            num_try -= 1
            print("Wrong guess.")

        if hidden_word == word_as_list:
            print("\nCongratulations! You've completed the word:", word)
            break

    if hidden_word != word_as_list:
        print("\nGame over! The correct word was:", word)

fill_the_gaps_game()
