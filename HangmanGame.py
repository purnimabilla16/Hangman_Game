import random

wordlist = ["apple","paris","book","car","coding","blue"]
word = random.choice(wordlist)
print("Welcome to hangman game!!")
lives = 6
guess = []
for i in word :
    guess.append("_")
while lives > 0 :
    print(f"you are left with {lives} lives.")
    print(f"the word is :\n{guess}")
    letter = input("guess the letter : ")
    if letter in word :
        print(f"the letter you have guessed {letter} is present in the word.")
        for i in range(len(word)) :
            if word[i] == letter :
                guess[i] = letter
        if "_" not in guess :
            print("Congratulations! You win!!")
            print(f"the word is \n{guess}")
            break
    else :
        print(f"the letter you have guessed {letter} is not present in the word")
        lives -= 1
        if lives == 5 :
            print(" +---+\n |   |\n 0   |\n     |\n     |\n     |")
        elif lives == 4 :
            print(" +---+\n |   |\n 0   |\n |   |\n     |\n     |")
        elif lives == 3 :
            print(" +---+\n |   |\n 0   |\n\|   |\n     |\n     |")
        elif lives == 2 :
            print(" +---+\n |   |\n 0   |\n\|/  |\n     |\n     |")
        elif lives == 1 :
            print(" +---+\n |   |\n 0   |\n\|/  |\n/    |\n     |")
        elif lives == 0 :
            print(" +---+\n |   |\n 0   |\n\|/  |\n/ \  |\n     |")
            print("You have lost the game...")
            print("The word is",word)