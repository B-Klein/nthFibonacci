#!/usr/bin/python -tt
# Benjamin Klein June 2017

"""A small Python program to find the nth Fibonacci number. The code implements the fast
matrix exponential algorithm, using the expressions:
  F(2n) = ( 2 * F(n-1) - F(n) ) * F(n)
  F(2n-1) = Fn^2 + F(n-1)^2
see : https://en.wikipedia.org/wiki/Fibonacci_number#Matrix_form
and https://www.nayuki.io/page/fast-fibonacci-algorithms
(Example for VAT IT)
"""

import sys
import math

def nthFibonacci(n):
  """ Function to find the nth Fibonacci number
  """

  # Run some basic error checking
  try:
    n = int(n)
  except: # if this fails not a number inputed
    sys.stderr.write('Incorrect data input\n')
    return None
  if n < 0:
    sys.stderr.write('Only positive integers allowed\n')
    return None
  
  # since the error checking slows down the recursion we run it as a seperate function
  [Fnm,Fn] = fastrecursivefibonacci(n)
  return Fnm

def fastrecursivefibonacci(n):
  """ Recursively solves the fast fibonacci series using the fast matrix form 
  """
  # Needs a termination point, this is done @ n = 0
  if n == 0:
    return 0,1
  else: # now we can recursively solve this
    if n % 2 == 0: # even case
      [Fn, Fnm] = fastrecursivefibonacci(n/2)
    else: 
      [Fn, Fnm] = fastrecursivefibonacci((n-1)/2)
          
    # Solve the fast matrix form
    Fn2 = ( 2 * Fnm - Fn ) * Fn  
    Fn2m = pow(Fn,2) + pow(Fnm,2)

    # This must be returned in the form n, n+1
    if n % 2 == 0:
      return Fn2, Fn2m
    else:
      return Fn2m, Fn2m+Fn2

# reads in exactly one input, n, and prints out the nth Fibonacci number
def main():
  if len(sys.argv) == 2:
    n = sys.argv[1]
  else:
    print 'usage: nthFibonacci n'
    sys.exit(1)

  Fn = nthFibonacci(n)
  print Fn

# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()
