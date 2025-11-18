import random

word_list = ["apple", "tiger", "chair", "house", "snake"]

secret_word = random.choice(word_list)
display = ["_"] * len(secret_word)

max_attempts = 6
wrong_attempts = 0

print("=== Welcome to Hangman Game ===")

while wrong_attempts < max_attempts and "_" in display:
    print("\nWord:", " ".join(display))
    print("Wrong attempts left:", max_attempts - wrong_attempts)

    guess = input("Guess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one alphabet letter.")
        continue

    if guess in secret_word:
        print("Good guess!")
        for i in range(len(secret_word)):
            if secret_word[i] == guess:
                display[i] = guess
    else:
        print("Wrong guess!")
        wrong_attempts += 1

if "_" not in display:
    print("\n🎉 Congratulations! You won!")
    print("The word was:", secret_word)
else:
    print("\n❌ You lost!")
    print("The correct word was:", secret_word)