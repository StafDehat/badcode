#!/usr/bin/python

import datetime

def next20Leaps():
  now = datetime.datetime.now()
  year = now.year + 1
  foundLeaps = 0
  while (foundLeaps < 20):
    if ( year%100 == 0 ):
      if ( year%400 == 0 ):
        print year
        foundLeaps += 1
    elif ( year%4 == 0 ):
      print year
      foundLeaps += 1
    year += 1
  #end while
#end next20Leaps

next20Leaps()

