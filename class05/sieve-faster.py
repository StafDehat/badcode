#!/usr/bin/python

import math

# Re-write primesUnder(x)
# Use the Sieve of Eratosthenes, instead of math, to determine
#   if a number is prime.
# https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes

def sieveOut(lst, x):
  if (x == 2):
    increment = x
  else:
    # x is odd.  Skip the evens.
    increment = 2 * x
  #end if
  if (lst[x]):
    index = x + increment
    while (index < len(lst)):
      lst[index] = False
      index += increment
    #end while
  #end if
#end sieveOut()

def eratosthisList(lst):
  lst[0] = False
  lst[1] = False
  maxFactor = int(math.sqrt(len(lst)))
  for i in xrange(2,maxFactor):
    if (lst[i]):
      sieveOut(lst,i)
  #end for
#end sieveThisList()

def isPrime(num):
  return sieve[num]
#end isPrime()

def primesUnder(x):
  for num in xrange(2,x):
    if isPrime(num):
      print num
  #end for
#end primesUnder()

# Generate the lookup table using the Sieve algorithm
# I suggest using a List of Booleans as your data structure.
sieve = [True] * 100000
eratosthisList(sieve)

primesUnder(100000)

