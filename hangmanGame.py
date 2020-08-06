import random
from words import countryList

def getWord():
    word = random.choice(countryList)
    return word.upper()

def play(word):
    #wordCompletion = "_" * len(word)
    blanks = '_' * len(word)
    guessed = False
    guessedLetters = []
    guessedWords = []
    tries = 7



    print("Let's play Hangman!")
    print(displayHangman(tries))
    print(blanks)
    print("\n")


    for i in range(len(word)):  # replace blanks with correctly guessed letters
        if word[i] in guessedLetters:
            blanks = blanks[:i] + word[i] + blanks[i + 1:]


    for letter in blanks:  # show the secret word with spaces in between each letter
        print(letter, end=' ')
    print()

    while not guessed and tries > 0:
        guess = input("Please guess a letter or the country: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessedLetters:
                print("You have already guessed this letter", guess)
            elif guess not in word:
                print(guess, "is not in the word.")
                tries -= 1
                print("you have ", tries, "attempts left" )
                guessedLetters.append(guess)
            else:
                print("Woo, ", guess, "is in the country")
                guessedLetters.append(guess)
                wordAsList = list(blanks)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    wordAsList[index] = guess
                blanks = "".join(wordAsList)
                if "_" not in blanks:
                    guessed = True

        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessedWords:
                print("You have already guessed this country", guess)
            elif guess != word:
                print(guess, "it is not the country.")
                tries -= 1
                guessedWords.append(guess)
            else:
                guessed = True
                blanks = word

        else:
            print("Sorry, not a valid guess.")

        print(displayHangman(tries))
        print(blanks)



    if guessed:
        print("Congrats, you guessed the country! You win!")
    else:
        print("Sorry, you ran out of tries. The country was " + word + ". Maybe next time!")

 

def displayHangman(tries):
    stages = [  # final state: head, torso, both arms, and both legs
            """
               --------
               |      |
               |      O
               |     \\|/
               |      |
               |     / \\
               -
            """,
            # head, torso, both arms, and one leg
            """
               --------
               |      |
               |      O
               |     \\|/
               |      |
               |     / 
               -
            """,
            # head, torso, and both arms
            """
               --------
               |      |
               |      O
               |     \\|/
               |      |
               |      
               -
            """,
            # head, torso, and one arm
            """
               --------
               |      |
               |      O
               |     \\|
               |      |
               |     
               -
            """,
            # head and torso
            """
               --------
               |      |
               |      O
               |      |
               |      |
               |     
               -
            """,
            # head
            """
               --------
               |      |
               |      O
               |    
               |      
               |     
               -
            """,
            #rope
            """
                       --------
                       |      |
                       |      
                       |    
                       |      
                       |     
                       -
            """,
            # initial empty state
            """
               --------
               |      
               |      
               |    
               |      
               |     
               -
            """
        ]
    return stages[tries]



def main():
    word = getWord()
    play(word)
    while input("Play Again? (Y/N) ").upper() == "Y":
        word = getWord()
        play(word)


if __name__ == "__main__":
    main()