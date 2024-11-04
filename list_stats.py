import string

with open("word_list", 'r') as f:
  wordlist = f.read().split()

ltr_freq = {ltr : 0 for ltr in string.ascii_lowercase}

for word in wordlist:
  for ltr in set(word):  # set() takes out duplicate letters
    ltr_freq[ltr] += 1

print(ltr_freq)

ordered_freq = sorted(ltr_freq, key=ltr_freq.get, reverse=True)
ordered_freq = {ltr : ltr_freq[ltr] for ltr in ordered_freq}

print(ordered_freq)

# Consider not only the letters that appear in the most words, but whether
# some letters frequently show up in the same words. We may learn more by
# guessing letters that both occur frequently but in different words.

# Ways to assess goodness of a guess:
# - sum of frequencies
# - sum of distinct frequencies (each letter key's value should be a list
# of words?)

# TODO give each word a score, print top 10 words

word_scores = {word : 0 for word in wordlist}

for word in wordlist:
  for ltr in set(word):     # set() removes duplicate letters
                            # Consider how to handle score when a letter is
                            # known and we wish to test a duplicate
    word_scores[word] += ltr_freq[ltr]

ordered_scores = sorted(word_scores, key=word_scores.get, reverse=True)
#ordered_scores_dict = {word : word_scores[word] for word in ordered_scores}
print({word : word_scores[word] for word in ordered_scores[:10]})
