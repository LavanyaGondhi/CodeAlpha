import random
words = ["mango", "apple", "python", "ravi", "lion"]
hidden_word = random.choice(words)
max_attempts = 6
wrong_attempts = 0
guessed_letter = []
while wrong_attempts < max_attempts:
    guessed_word = ""
    for i in hidden_word:
        if i in guessed_letter:
            guessed_word += i
        else:
            guessed_word += "_ "
    print("Word:", guessed_word)
    if "_" not in guessed_word:
        print("You Won!")
        break
    guess = input("Enter the letter you guess: ").lower()
    if len(guess) != 1 or not guess.isalpha():
        print("Enter only one alphabet letter.")
        continue
    if guess in guessed_letter:
        print("You already guessed that letter.")
        continue
    if guess in hidden_word:
        guessed_letter.append(guess)
    else:
        wrong_attempts += 1
        print("Wrong guess! Attempts left:", max_attempts - wrong_attempts)
if "_" in guessed_word:
    print("You Lost! The word was:", hidden_word)
