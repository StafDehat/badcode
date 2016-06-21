#!/usr/bin/python

# Re-write primesUnder(x)
# Use the Sieve of Eratosthenes, instead of math, to determine
#   if a number is prime.
# https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes

def isPrime(num):
  # Use the Sieve lookup table
  return True
#end isPrime()

def primesUnder(x):
  for num in xrange(2,x):
    if isPrime(num):
      print num
  #end for
#end primesUnder()


# Generate the lookup table using the Sieve algorithm
# I suggest using a List of Booleans as your data structure.


print "primesUnder(10):"
primesUnder(10)

print "primesUnder(100):"
primesUnder(100)

print "primesUnder(1000):"
primesUnder(1000)
