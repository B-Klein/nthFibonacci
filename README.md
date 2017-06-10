Finds the nth Fibonacci number, starting at n = 0,

Usage: 
  nthFibonacci n 

Example: 
  $python nthFibonacci 100 
  $./nthFibonacci 100 

Requires:
  Python 2.7 and the Python math library.

Algorithm:
  The code uses the matrix exponential algorithm detailed here:
  https://en.wikipedia.org/wiki/Fibonacci_number#Matrix_form and,
  https://www.nayuki.io/page/fast-fibonacci-algorithms

Testing:
  The code is tested using the script testnthFibonacci.py run with:
  $ python testnthFibonacci.py 

Approach:
  There are several ways to solve this, I looked at 3.

  a. Simple recursion 
    fibonacci(n):
      if n == 0:
        return 0
      elif n == 1:
        return 1
      return fibonacci(n-1)+fibonacci(n-2)

    This is neat but will be O(x^n) complex and use O(n) in memory space.

  b. Use the Binet formula:
    
    Fn = round(phi^n/sqrt(5))

    Tried this first. It is a single calculation, so is independant of n for speed and
    memory. Unfortunately it runs into resolution errors for n > 70. This could be
    improved using packages like bigfloat, but these are not custom in Python.

  c. The matrix exponential algorithm, using the expressions:
      F(2n) = ( 2 * F(n-1) - F(n) ) * F(n)
      F(2n-1) = Fn^2 + F(n-1)^2 
    see : https://en.wikipedia.org/wiki/Fibonacci_number#Matrix_form
    and https://www.nayuki.io/page/fast-fibonacci-algorithms

    It recursively halves the stack, so grows by O(log2(n)) in both time and memory.
