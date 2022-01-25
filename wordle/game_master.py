import constants

class GameMaster:

  def __init__(self, winWord):
    self.winWord = winWord

  def acceptGuess(self, guess):
    if len(guess) != len(self.winWord):
      raise("Invalid number of charactesr in " + guess + ". Require " + str(self.winWord))
    
    if guess == self.winWord:
      return constants.WIN_RESULT

    result = ""
    for i in range(0, len(guess)):
      c = guess[i]
      winc = self.winWord[i]
      if c == winc:
        result += constants.CORRECT_LETTER
      elif c in self.winWord:
        result += constants.WRONG_PLACE
      else:
        result += constants.WRONG_LETTER
    
    return result