# wordle

![Dynamic JSON Badge](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fgithub.com%2Fekestelman%2Fwordle%2Fraw%2Frefs%2Fheads%2Fmain%2Fresults_summary.json&query=%24.win%20rate&label=Win%20Rate&color=brightgreen)
![Dynamic JSON Badge](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fgithub.com%2Fekestelman%2Fwordle%2Fraw%2Frefs%2Fheads%2Fmain%2Fresults_summary.json&query=%24.avg%20guesses&style=flat&label=Avg%20Guesses&color=blue)


Wordle puzzle solver.

`solver` module takes steps to solve a puzzle for a given solution.

`tester` module tests the win rate for the `solver`.

`word_list` is the list of possible solutions.

`list_stats` provides information about the `word_list` (such as what words contain the most common letters).

## Analysis

Below we see each letter in order of greatest to least frequency. "Frequency" refers to the number of possible solutions that contain each letter (duplicate letters in a single word are not counted).

![](https://github.com/ekestelman/wordle/blob/main/letter_bar_graph.svg)

We can attempt to give each word a rating based on how much we learn by guessing that word. A simple rating method is to add up the frequencies of each letter for a given word while omitting duplicate letters. Then the word "weary" would have a rating of $194+1056+909+837+417=3413$. There are 272 words on the solution list with higher ratings.

With this method, the five top rated words are alert, alter, later, irate, and arose.

Currently the program is solving puzzles with the distribution below.

![](https://github.com/ekestelman/wordle/blob/main/guesses_bar_graph.svg)

This shows the number of guesses taken to solve each of the 2315 puzzles. If the puzzle is not solved within 6 guesses, it is failed. Note that exactly one puzzle is solved in one guess.
