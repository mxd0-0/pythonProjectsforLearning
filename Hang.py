import random

words_list = ['ubuntu', 'windows', 'android', 'arch', 'java', 'python', 'ruby']

def choose_word():
    return random.choice(words_list)

def display_word(word, guessed_letters):
    return ' '.join([char if char in guessed_letters else '_' for char in word])

def hangman():
    word = choose_word()
    guessed_letters = set()
    attempts = 6

    print("Welcome to Hangman!")
    print(display_word(word, guessed_letters))

    while attempts > 0 and set(word) != guessed_letters:
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter.")
        elif guess in word:
            guessed_letters.add(guess)
            print("Correct!")
        else:
            attempts -= 1
            print(f"Wrong! You have {attempts} attempts left.")

        print(display_word(word, guessed_letters))

    if set(word) == guessed_letters:
        print(f"Congratulations! You guessed the word: {word}")
    else:
        print(f"Game over! The correct word was: {word}")

hangman()