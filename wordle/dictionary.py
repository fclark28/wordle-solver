from guess_state import GuessState 


class LiveDictionary:

  def __init__(self, words, worldLength):
    self.wordLength = worldLength
    self.activeWords = words

  def prune(self, state: GuessState):
    updatedWords = []
    isoMap = state.getKnownLetters()

    #isoMap = self.__createLetterMap(known)

    for word in self.activeWords:
      isValid = True

      for i in range(0, self.wordLength):
        isValid = state.possibleMatchAt(i, word[i])
        if not isValid:
          break
      
      if isValid and self.__containsAllKnownLetters(word, isoMap):
        updatedWords.append(word)
    
    self.activeWords = updatedWords
    return self.activeWords


  def __containsAllKnownLetters(self, word, knownMap):
    wordMap = self.__createLetterMap(word)

    for k in knownMap:
      if not k in wordMap:
        # Our word doesn't contain a letter we know we need
        return False
      elif wordMap[k] < knownMap[k]:
        # The word has the letter, but not enough of them
        return False
    
    return True

  def __createLetterMap(self, word):
    lettermap = {}
    for i in range (0, len(word)):
      letter = word[i]
      if letter in lettermap:
        lettermap[letter] += 1
      else:
        lettermap[letter] = 1
    return lettermap
