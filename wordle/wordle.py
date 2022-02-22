#!/usr/bin/python

import sys, getopt, os
import constants
import random
import dictionary
import operations
from game_master import GameMaster
from guess_state import GuessState

def main(argv):
  try:
    opts, args = getopt.getopt(argv, "hm:",["mode="])
  except getopt.GetoptError:
    print('wordle.py -m <game mode>')
    sys.exit(2)

  mode = ''
  for opt, arg in opts:
    if opt == '-h':
      print('wordle.py -m <bot | helper>')
      sys.exit()
    elif opt in ('-m', '--mode'):
      mode = arg.lower()
  
  if mode not in ["bot", "helper"]:
    print("Game modes are: bot, helper")
    sys.exit()
  
  if mode == "bot":
    bot()
  elif mode == "helper":
    helper()
  else:
    print("No idea what happened. Can't use mode " + mode)
    sys.exit()

def helper():
  words = dictionary.getFiveLetterWords()

  state = GuessState(5)

  while len(words) > 2:
    res = input("What was the result [guess] [result]: ")
    guess, result = res.split()
    state.update(guess, result)
    words = operations.pruneWordList(words, state)

    print(words)


def bot():

  words = dictionary.getFiveLetterWords()

  winWord = random.choice(words)
  print("Winword: " + winWord)

  state = GuessState(5)
  gm = GameMaster(winWord)

  for i in range(0, 6):
    guess = random.choice(words)
    print("Guess " + str(i + 1) + " is: " + guess)

    result = gm.acceptGuess(guess)
    if result == constants.WIN_RESULT:
      print("WINNER!")
      sys.exit()

    state.update(guess, result)
    words = operations.pruneWordList(words, state)

    print("    There are " + str(len(words)) + " left")

  print("LOSER!")

if __name__ == "__main__":
    main(sys.argv[1:])
