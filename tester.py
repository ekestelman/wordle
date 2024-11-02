import random
import solver
from scipy.stats import sem

def assign_ans():
  with open('word_list','r') as f:
    wordlist = f.read().split()
  
  ans = random.choice(wordlist)  # Correct answer
  return ans

if __name__ == "__main__":
  score = 0
  for i in range(1000):
    score += solver.solve(assign_ans())
  print(score/10)
  # TODO get sem for win rate
