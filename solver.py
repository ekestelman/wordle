import random

def solve(ans, show=False):
  
  with open('word_list','r') as f:
    wordlist = f.read().split()

  #ans = random.choice(wordlist)  # Correct answer

  i = 0
  tries = 1
  
  guess = wordlist[i]
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
    for j in range(5):
      if guess[j] == ans[j]:
        green[guess[j]] = j
      elif guess[j] in ans:
        orange[guess[j]] = j
      else:
        grey[guess[j]] = None
  
    #print(green);print(orange);print(grey)
  
    good = False    # Good guess
    while not good:
      breakout = False  # True if a loop is broken
      i += 1
      guess = wordlist[i]
      for elem in green:
        if guess[green[elem]] != elem:
          breakout = True
          break
      if breakout:
        continue
      for j in range(5):
        if guess[j] in grey:
          breakout = True
          break
        elif guess[j] in orange and orange[guess[j]] == j:
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
    return 1
  else:
    return 0

