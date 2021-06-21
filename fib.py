# You will have to figure out what parameters to include
# 🚨 All functions must use recursion 🚨

# This function returns the Nth number in the fibonacci sequence.
# https://en.wikipedia.org/wiki/Fibonacci_number
# For this function, the first two fibonacci numbers are 0 and 1

def fib(n):
  if n <= 0:
    return 0
  if n == 1 or n == 2:
    return 1
  else:
    return fib(n - 1) + fib(n - 2)

# print(f"fibonacci of 9: {fib(9)} ")
# print(f"fibonacci of 13: {fib(13)} ")

# print(fib(-1))
# => 0
# print(fib(0))
# => 0
# print(fib(1))
# => 1
# print(fib(2))
# => 1
print(fib(20))
# => 13



def han_fib(n):
    # base case
    if n <= 0:
        return 0
    if n == 1 or n == 2:
        return 1
    else:
        # recursive step
        return han_fib(n - 1) + han_fib(n - 2)

# 

print(han_fib(5))
print(han_fib(7))


# han_fib(4)            +                  han_fib(3)



