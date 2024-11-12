import matplotlib.pyplot as plt
import random
import solver
import json
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
  guesses_list = [0 for _ in range(7)]  # 1-6 possible guesses + failing

  for i in range(len(wordlist)):
    guesses = solver.solve(wordlist[i], wordlist=wordlist, ordered=True)
    #old_score = score
    #score += solver.solve(wordlist[i], wordlist=wordlist, ordered=True)
    if guesses:  # solver returns 0 if failed
      score += 1
    guesses_list[guesses] += 1
    if 0 and guesses==0: # Print failed puzzles
      print(wordlist[i])

  print("Total solved puzzles:", score, "/", nwords)
  print("Win rate:", round(score / nwords * 100,2), "\b%")
  results_summary = {
                     "win rate" : str(score) + "/" + str(nwords),
                     "win rate" : str(round(score / nwords * 100, 2)) + '%',
                     "avg guesses" : round( (sum(i * guesses_list[i] \
                     for i in range(1,7)) + guesses_list[0] * 6) / score, 2)
                     }
  with open("results_summary.json", 'w') as f:
    json.dump(results_summary, f, indent=2)
  # Get sem for win rate?
  # ^Unnecessary if stat is on population and not sample
  if 1:
    label=list(range(1,7)) + ["Fail"]
    plt.bar(range(7), guesses_list[1:] + guesses_list[0:1], tick_label=label)
    #plt.xticks = ([1,2,3,4,5,6,7], ['1','2','3','4','5','6',"Fail"])
    plt.show()
