# You will have to figure out what parameters to include
# 🚨 All functions must use recursion 🚨`

# This function returns an array of all possible outcomes from flipping a coin N times.
# Input type: Integer 
# H stands for Heads and T stands for tails
# Represent the two outcomes of each flip as "H" or "T"

def coin_flips(n):
  if n <= 0:
    return []
  if n == 1:
    return ['H', 'T']
  combos = coin_flips(n - 1)
  return [x + 'H' for x in combos] + [x + 'T' for x in combos]