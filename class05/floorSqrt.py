#!/usr/bin/python

import math
import time

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

x = 1234567890123456789012345678901234567890

start = time.time()
xme = floorSqrt(x)
stop = time.time()
print "floorSqrt: " + str(stop - start)
print "sqrt(" + str(x) + ") = " + str(xme)

start = time.time()
xmath = math.floor(math.sqrt(x))
stop = time.time()
print "math.sqrt: " + str(stop - start)
print "sqrt(" + str(x) + ") = " + str(xmath)

