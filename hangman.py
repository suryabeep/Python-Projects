# things to do:
# 1) set a target word 2) convert to a list of lists (letter, guessed) 3) ask user for input
# 4) check if user input is in the list of tuples, increment strikes if not
# 5) if user runs out of strikes, end game with sys.exit

import sys
import random
MAX_STRIKES = 5


def game():
    target_word = get_target()
    letter_set = get_target_set(target_word)
    guess_set = get_guess_set(letter_set)
    strikes = 0
    over = False
    while not over:
        guess = input("guess a letter")
        guess_set, strikes = check_guess(guess, letter_set, guess_set, strikes)
        done = check_done(guess_set, strikes)
        if done == "complete":
            print("You won! The word was {0}".format(target_word))
            over = True
        elif done == "strike out":
            print("You lost! The word was {0}".format(target_word))
            over = True


def get_target():
    choices = ["linux", "kernel", "gnu", "ubuntu", "windows", "apple"]
    return choices[random.randint(0, len(choices) - 1)]


def get_target_set(word):
    letters = []
    for i in range(len(word)):
        temp = [word[int(i): int(i+1)], False]
        letters.append(temp)
    return letters;


def get_guess_set(letters):
    guess_set = [];
    for i in range(len(letters)):
        guess_set.append("_")
    return guess_set;


def check_guess(guess, letter_set, guess_set, strikes):
    if guess == "QQQ":
        sys.exit("Good Bye!")
    bad_guess = True
    for i in range(len(letter_set)):
        if guess == letter_set[i][0] and letter_set[i][1] == False:
            guess_set[i] = guess
            bad_guess = False
            print("Good guess! Word is now: " + create_word(guess_set))
    if bad_guess:
        print("bad guess!")
        strikes += 1
    return guess_set, strikes


def check_done(guess_set, strikes):
    done = ""
    if "_" not in guess_set:
        done = "complete"
    if strikes >= 6:  # max num of strikes
        done = "strike out"
    return done


def create_word(guess_set):
    word = ""
    for i in guess_set:
        word += i
    return word


# start of gameplay
print("welcome to hangman! Enter QQQ at any point to quit immediately")
playing = True
while playing:
    game()
    again = input("Play again? y/n")
    if again == "y" or again == "Y":
        game()
    elif again == "n" or again == "N":
        print("Good Bye!")
        playing = False
        sys.exit("Game ended")
    else:
        print("invalid input, game over")
        playing = False
