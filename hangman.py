import random
def ascii(k):
    asci = "qwertyuiopasdfghjklzxcvbnm"
    for i in asci:
        if i == k:
            return k if True else False
            break
choosen = list(random.choice(['python', 'java', 'kotlin', 'javascript']))
def play():
    hidden = list('-' * len(choosen))
    lives = 8
    check = list()
    while lives > 0 and choosen != hidden:
        print()
        print(''.join(hidden))
        guess = input('Input a letter: ')
        if guess in check or guess in hidden and guess != "-":
            print("You already typed this letter")
        elif guess in choosen:
            for i in range(len(choosen)):
                if choosen[i] == guess:
                    hidden[i] = guess          
        else:
            if guess not in check:
                if guess == "-":
                    print("It is not an ASCII lowercase letter")
                    
                elif guess.islower() == False and len(guess) == 1:
                    print("It is not an ASCII lowercase letter")
                    check.append(guess)
                elif len(guess) > 1 or guess == " " or guess == "":
                    print("You should input a single letter")
                else:
                    if guess in hidden:
                        print("You already typed this letter")
                    else:
                        print("No such letter in the word")
                    check.append(guess)
                    lives = lives - 1
        if lives == 0 and choosen != hidden:
            print("You are hanged!\n")
            break
        elif lives <= 8 and choosen == hidden:
            print("You guessed the word!")
            print("You survived!\n")
            break
    main()
def main():
    print('H A N G M A N')
    button = input(("Type \"play\" to play the game, \"exit\" to quit:"))
    if button == "play":
        play()
    elif button == "exit":
        pass
main()
