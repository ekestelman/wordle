import matplotlib.pyplot as plt
import random
import solver
from scipy.stats import sem
from list_stats import get_word_scores, get_ltr_freq

def assign_ans():
  with open('word_list','r') as f:
    wordlist = f.read().split()
  
  ans = random.choice(wordlist)  # Correct answer
  return ans

if __name__ == "__main__":

  with open('word_list', 'r') as f:
    wordlist = f.read().split()

  ltr_freq = get_ltr_freq(wordlist)
  wordlist = get_word_scores(wordlist, ltr_freq, orderedlist=True)

  score = 0
  nwords = len(wordlist)

  for i in range(len(wordlist)):
    old_score = score
    score += solver.solve(wordlist[i], wordlist=wordlist, ordered=True)
    if 0 and old_score == score: # Print failed puzzles
      print(wordlist[i])

  print("Total solved puzzles:", score, "/", nwords)
  print("Win rate:", round(score / nwords * 100,2), "\b%")
  # Get sem for win rate?
  # ^Unnecessary if stat is on population and not sample
