import constants

class GuessState:

  def __init__(self, letterCount):
    self.numLetters = letterCount
    self.iso = {}
    self.__initMask(letterCount)

  def update(self, guess, result):
    isoMap = {}
    for i in range(0, self.numLetters):
      if result[i] == constants.WRONG_LETTER:
        self.__removeLetter(guess[i])
      elif result[i] == constants.WRONG_PLACE:
        self.mask[i].discard(guess[i])
        if guess[i] in isoMap: isoMap[guess[i]] += 1
        else: isoMap[guess[i]] = 1
      else:
        if guess[i] in self.iso:
          c = self.iso[guess[i]]
          if c == 1: del self.iso[guess[i]]
          else: self.iso[c] = c - 1

        self.mask[i] = set(guess[i]) # This was a match. It's the only letter in this pos
   
    self.__updateISOMap(isoMap)


  def possibleMatchAt(self, i, letter):
    return letter in self.mask[i]

  def searchingFor(self, letter):
    return letter in self.iso

  def getKnownLetters(self):
    return self.iso

  def __removeLetter(self, letter):
    for i in range (0, len(self.mask)):
      self.mask[i].discard(letter)

  def __initMask(self, num):
    self.mask = []
    for i in range(0, num):
      self.mask.append(constants.ALPHABET.copy())

  def __updateISOMap(self, updateMap):
    for k in updateMap:
      if not k in self.iso:
        self.iso[k] = 1
      elif updateMap[k] > self.iso[k]:
        self.iso[k] = updateMap[k] # We now know we need more of this letter