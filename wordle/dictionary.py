import os

def readDictionary(filename):
  with open(filename) as file:
    return [line.strip() for line in file]


def getFiveLetterWords():
  script_dir = os.path.dirname(__file__)
  relative_fp = "../resources/five_letter_dictionary.txt"
  wordFile = os.path.join(script_dir, relative_fp)
  return readDictionary(wordFile)

