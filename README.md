# wordle

Wordle puzzle solver.

`solver` module takes steps to solve a puzzle for a given solution.

`tester` module tests the win rate for the `solver`.

`word_list` is the list of possible solutions.

`list_stats` provides information about the `word_list` (such as what words contain the most common letters).

## Analysis

Below we see each letter in order of greatest to least frequency. "Frequency" refers to the number of possible solutions that contain each letter (duplicate letters in a single word are not counted).

![](https://raw.githubusercontent.com/ekestelman/wordle/eca85689eca314d560f10c6777a4e66aa8fd8b79/letter_bar_graph.svg)

We can attempt to give each word a rating based on how much we learn by guessing that word. A simple rating method is to simply add up the frequencies of each letter for a given word while omitting duplicate letters. Then the word "weary" would have a rating of $194+1056+909+837+417=3413$. There are 273 words on the solution list with higher ratings.

The five top rated words are alert, alter, later, irate, and arose.
