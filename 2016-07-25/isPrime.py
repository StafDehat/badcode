#!/usr/bin/python

# Re-write primesUnder(x)
# Use the Sieve of Eratosthenes, instead of math, to determine
#   if a number is prime.
# https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes

# Homebrew math.floor(math.sqrt(x)) function
def floorSqrt(x):
  low = 1
  hi = 2
  while True:
    if (hi**2 > x):
      break
    #end if
    low = hi
    hi = hi << 1
  #end while
  while True:
    span = hi - low
    if ( span < 2 ):
      return low
    mid = low + (span>>1)
    mid2 = mid**2
    if ( x < mid2 ):
      hi = mid
    elif ( x > mid2 ):
      low = mid
    #end if
  #end while
#end floorSqrt()

def sieveOut(lst, x):
  if (x == 2):
    increment = x
  else:
    # x is odd.  Skip the evens.
    increment = 2 * x
  #end if
  index = x + increment
  while (index < len(lst)):
    lst[index] = False
    index += increment
  #end while
#end sieveOut()

def growSieve(lst, upTo):
  lst[0] = False
  lst[1] = False
  oldLen = len(lst)
  # Tack on True's to get to length upTo
  newSlots = upTo + 1 - oldLen
  lst.extend([True] * newSlots)
  sieveStop = floorSqrt(len(lst))
  for i in xrange(2,sieveStop):
    if (lst[i]):
      sieveOut(lst,i)
    #end if
  #end for
#end growSieve()

def isPrime(num):
  # If our primeList is big enough to lookup 'num', cool.
  # If not though, extend the primeList as necessary:
  if (len(primeList) < num):
    growSieve(primeList, num)
  #end if
  return primeList[num]
#end isPrime()

# Initialize a list of primes
#  primeList[0] = False
#  primeList[1] = False
#  primeList[2] = True
primeList = [False, False, True]

# Test a bunch of numbers to see if they're prime
testThese = [1384743,
             1315,
             579321,
             11833,
             17383881]
for testNum in testThese:
  print str(testNum) + ": " + str(isPrime(testNum))

