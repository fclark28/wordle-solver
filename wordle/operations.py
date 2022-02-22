from guess_state import GuessState 

def pruneWordList(words, state: GuessState):
  updatedWords = []
  isoMap = state.getKnownLetters()

  for word in words:
    isValid = True

    for i in range(0, len(word)):
      isValid = state.possibleMatchAt(i, word[i])
      if not isValid:
        break
    
    if isValid and __containsAllKnownLetters(word, isoMap):
      updatedWords.append(word)
  
  return updatedWords

def __containsAllKnownLetters(word, knownMap):
  wordMap = __createLetterMap(word)

  for k in knownMap:
    if not k in wordMap:
      # Our word doesn't contain a letter we know we need
      return False
    elif wordMap[k] < knownMap[k]:
      # The word has the letter, but not enough of them
      return False
  
  return True

def __createLetterMap(word):
  lettermap = {}
  for i in range (0, len(word)):
    letter = word[i]
    if letter in lettermap:
      lettermap[letter] += 1
    else:
      lettermap[letter] = 1
  return lettermap