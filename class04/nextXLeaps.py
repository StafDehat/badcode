#!/usr/bin/python

import datetime

def isLeap(year):
  if (year%400 == 0):
    return True
  elif ( (year%4 == 0) and
         (year%100 != 0) ):
    return True
  # end if
  return False
#end isLeap()

def xLeapsAfter(numLeaps, year):
  counter = 0
  while (counter < numLeaps):
    if ( isLeap(year) ):
      print year
      counter += 1
    #end if
    year += 1
  #end while
#end xLeapsAfter()

def nextXLeaps(numLeaps):
  return xLeapsAfter(numLeaps, datetime.datetime.now().year)
#end nextXLeaps()

def next20Leaps():
  nextXLeaps(20)
#end next20Leaps()

print "Next 20 leap years:"
next20Leaps()

print "Next 100 leap years:"
nextXLeaps(100)

print "First 100 leap years (AD):"
xLeapsAfter(100,0)

