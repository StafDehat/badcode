#!/usr/bin/env python

def isPrime(x):
  for i in xrange(2,x):
    if ( x%i == 0 ):
      return False
    #end if
  #end for
  return True
#end isPrime()

def primesUnder(x):
  for num in xrange(2,x):
    if isPrime(num):
      print num
  #end for
#end primesUnder()

primesUnder(1000)

