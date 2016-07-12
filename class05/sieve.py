#!/usr/bin/python

# Re-write primesUnder(x)
# Use the Sieve of Eratosthenes, instead of math, to determine
#   if a number is prime.
# https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes

def sieveOut(lst, x):
  if (lst[x]):
    index = 2 * x
    while (index < len(lst)):
      lst[index] = False
      index += x
    #end while
  #end if
#end sieveOut()

def eratosthisList(lst):
  lst[0] = False
  lst[1] = False
  for i in xrange(2,len(lst)):
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

