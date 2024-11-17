import random
from list_stats import get_word_scores, get_ltr_freq

def solve(ans, wordlist=None, ordered=False, show=False):
  
  # TODO for more interactive program, try having user input string
  # representing orange/green/grey after each guess.

  if not wordlist:
    with open('word_list','r') as f:
      wordlist = f.read().split()

  # If wordlist is given but it's not ordered we still need to order it.
  if not ordered:
    # These function are much slower than the repeat file reading.
    ltr_freq = get_ltr_freq(wordlist)
    wordlist = get_word_scores(wordlist, ltr_freq, orderedlist=True)
  #ans = random.choice(wordlist)  # Correct answer

  i = -1
  tries = 1

  first = "irate"#wordlist[i+1]
  # TODO keep track of guessed words with dict
  
  guess = first
  if show:
    print(guess)
  
  grey = {}         # Letters known to not be in ans
  orange = {}       # Letters known to be in ans but placement unknown
  green = {}        # Letters in ans with known placement
  
  while guess != ans:
  
    # FIXME anticipate bug in case of repeat letters
    # I think simply this will work as if the game gives orange to
    # non repeat letter repeated in a guess.
    # TODO needs to come after guess to better update "show"
    # make function to come immediately after first guess, or second
    # guess won't be good.
    # TODO "move" guess from orange to green when position becomes known? then
    # we can rule out repeat letters as we would in real game
    # TODO dict assigner function, this is useful in other modules.
    for j in range(5):
      if guess[j] == ans[j]:
        green[guess[j]] = green.get(guess[j],set()) | {j}
      elif guess[j] in ans:
        orange[guess[j]] = orange.get(guess[j],set()) | {j}
        # FIXME overwrites previously known wrong position.
        # Values for green and orange should be lists containing each
        # known position.
      else:
        grey[guess[j]] = None
  
    #print(green);print(orange);print(grey)
  
    good = False    # Good guess
    while not good:
      breakout = False  # True if a loop is broken
      i += 1
      guess = wordlist[i]
      # TODO better way to track used words if non alpha
      # Current method: preorder the words (con: can't adjust based on new info
      # Also: no need to track used words if we determine that we learn nothing
      if guess == first:  # Allows you to choose any starting word even if it's
        continue          # not the first in the word order. Skip this word.
      # TODO Alernative that allows flexibility with greens but checks if
      # remaining missing letters are already known.
      # Maybe special set of criteria for elimination guesses, or even guess
      # could be elimination (try both?)
      for ltr in green:   # Letter
        for pos in green[ltr]:   # Known positions
          if guess[pos] != ltr:
            breakout = True
            break
        if breakout:   # TODO beneficial for performance?
          break
      if breakout:
        continue
      for ltr in orange:
        # TODO way to handle duplicates
        if ltr not in guess:  # or guess[orange[elem]] = elem
          breakout = True
      if breakout:
        continue
      for j in range(5):
        if guess[j] in grey:
          breakout = True
          break
        elif guess[j] in orange and j in orange[guess[j]]:
          breakout = True
          break
        # The following is the converse of what we want
        #elif guess[j] in green and green[guess[j]] != j:
        # ^Wrong, eliminates answers with green in an unknown spot, instead
        # of answers without green in correct spot (i.e., fails to find any
        # answer with a repeat letter and will exhaust the word list.
        #elif guess[j] in green and guess[green[guess[j]]] != guess[j]:
        # ^Better, but only checks green if it's already in the guess.
          #breakout = True
          #break
      #print(i,breakout,good)
      # TODO better way to "show work"
      if breakout:
        continue
      good = True    # This is just another break
    
    if show:
      correct = ""
      for j in range(5):
        if guess[j] == ans[j]:
          correct += guess[j]
        else:
          correct += "_"
      print(guess, correct, [x for x in orange])
    tries += 1
    if tries == 6:
      break
  
  if show:
    print(ans)
  if guess == ans:
    return tries
  else:
    return 0

