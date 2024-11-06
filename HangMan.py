import random

words_list = [
    "apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew",
    "kiwi", "lemon", "mango", "nectarine", "orange", "papaya", "quince", "raspberry",
    "strawberry", "tangerine", "vanilla"
]

def get_word_with_letter(letter):
    filtered_words = [word for word in words_list if letter in word]
    if not filtered_words:
        return None
    return random.choice(filtered_words)

def display_word_with_gaps(word, letter):
    return ''.join([char if char == letter else '_' for char in word])

print("Give a letter of a word:")
letter = input().strip().lower()

word = get_word_with_letter(letter)

if word:
    print("Guess the word: ", display_word_with_gaps(word, letter))
    user_guess = input("Your guess: ").strip().lower()
    if user_guess == word:
        print("Correct!")
    else:
        print(f"Wrong! The correct word was: {word}")
else:
    print("No word contains the given letter.")