word = "nazmul"
chances = 6
guessword = []
done = False

while not done:
    for letter in word:
        if letter.lower() in guessword:
            print(letter, end = " ")
        else:
            print(" ", end = " ")
    guess = input(f"your chances is {chances}, guess the letter: ")
    guessword.append(guess.lower())
    if guess.lower() not in word.lower():
        chances -= 1
        if chances == 0:
            break
    done = True  
    for letter in word:
      if letter.lower() not in guessword:
          done = False
if done:
    print(f"yes, you win the game. The word is {word}")
else:
    print(f"you lose the game. The word was {word}")