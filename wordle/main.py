#!/usr/bin/python

import constants
import random
import os
from dictionary import LiveDictionary
from game_master import GameMaster
from guess_state import GuessState

def readDictionary(filename):
  with open(filename) as file:
    return [line.strip() for line in file]

def main():

  script_dir = os.path.dirname(__file__)
  relative_fp = "../resources/five_letter_dictionary.txt"
  wordFile = os.path.join(script_dir, relative_fp)
  words = readDictionary(wordFile)

  print("Dictionary has " + str(len(words)) + " words")
  winWord = "sugar" #random.choice(words)
  print("Winword: " + winWord)
  print("Verifying size: " + str(len(words)))

  dictionary = LiveDictionary(words, 5)
  state = GuessState(5)
  gm = GameMaster(winWord)

  for i in range(0, 6):
    guess = random.choice(words)
    print("Guess " + str(i + 1) + " is: " + guess)

    result = gm.acceptGuess(guess)
    if result == constants.WIN_RESULT:
      print("WINNER!")
      break
    else:
      print("Result is " + result)

    state.update(guess, result)
    words = dictionary.prune(state)

    print("There are " + str(len(words)) + " left")


if __name__ == "__main__":
    main()
