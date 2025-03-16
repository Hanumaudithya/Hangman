import random
from hangman_words import word_list
from hangman_art import stages, logo

# Game settings
lives = 6
game_over = False
correct_letters = []

# Display logo
print("\n" + "=" * 40)
print(logo)
print("=" * 40 + "\n")

# Randomly choose a word
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

# Placeholder for the word
placeholder = "_" * word_length
print(f"\n🚀 Let's Play Hangman! 🚀\n")
print(f"🔍 Word to guess: {' '.join(placeholder)}\n")

while not game_over:
    print(f"\n{'*' * 30}  {lives}/6 ❤️ LIVES LEFT  {'*' * 30}\n")
    
    guess = input("🎯 Guess a letter: ").lower()

    # Check if the letter was already guessed
    if guess in correct_letters:
        print(f"\n⚠️ You've already guessed '{guess}'. Try another letter! ⚠️\n")
        continue

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print(f"\n🔍 Word to guess: {' '.join(display)}\n")

    if guess not in chosen_word:
        lives -= 1
        print(f"\n❌ Oops! '{guess}' is not in the word. You lost a life. ❌\n")
        print(stages[lives])  # Display hangman stage

        if lives == 0:
            game_over = True
            print("\n" + "=" * 60)
            print(f"💀 GAME OVER! The word was '{chosen_word.upper()}'. Better luck next time! 💀")
            print("=" * 60 + "\n")

    if "_" not in display:
        game_over = True
        print("\n" + "=" * 50)
        print("🎉🎉 CONGRATULATIONS! YOU WIN! 🎉🎉")
        print("=" * 50 + "\n")

print("🎮 Thanks for playing Hangman! 🎮\n")
