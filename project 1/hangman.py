import random

WORDS = [
    "python",
    "programming",
    "computer",
    "developer",
    "algorithm"
]


def play_hangman():
    word = random.choice(WORDS)
    guessed_letters = set()
    attempts = 6

    print("================================")
    print("       HANGMAN GAME")
    print("================================")
    print("Guess the word one letter at a time!")

    while attempts > 0:
        display_word = " ".join(
            letter if letter in guessed_letters else "_"
            for letter in word
        )

        print("\nWord:", display_word)
        print("Attempts remaining:", attempts)

        if all(letter in guessed_letters for letter in word):
            print("\nCongratulations!")
            print("You guessed the word:", word)
            return

        guess = input("Enter a letter: ").strip().lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter exactly one letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print("Correct guess!")
        else:
            attempts -= 1
            print("Wrong guess!")

    print("\nGame Over!")
    print("The correct word was:", word)


if __name__ == "__main__":
    play_hangman()