import random
import solver
from scipy.stats import sem

def assign_ans():
  with open('word_list','r') as f:
    wordlist = f.read().split()
  
  ans = random.choice(wordlist)  # Correct answer
  return ans

if __name__ == "__main__":

  with open('word_list', 'r') as f:
    wordlist = f.read().split()

  score = 0
  nwords = len(wordlist)

  for i in range(len(wordlist)):
    score += solver.solve(wordlist[i])

  print("Total solved puzzles:", score, "/", nwords)
  print("Win rate:", round(score / nwords * 100,2), "\b%")
  # Get sem for win rate?
  # ^Unnecessary if stat is on population and not sample
