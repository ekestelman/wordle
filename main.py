import random
import solver

def assign_ans():
  with open('word_list','r') as f:
    wordlist = f.read().split()
  
  ans = random.choice(wordlist)  # Correct answer
  return ans

if __name__ == "__main__":
  ans = input("Choose answer (skip for random) > ") or assign_ans()
  default_first = 'irate'
  first = input(f"Choose starting word (skip for '{default_first}') > ") \
          or default_first
  solver.solve(ans, first=first, show=True)
