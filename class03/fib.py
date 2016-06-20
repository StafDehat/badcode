#!/usr/bin/python

def fib(x):
  previous = 0
  current = 1
  tempSum = 0 #(ie: next)
  counter = 0
  while (counter < x):
    print current
    tempSum = previous + current
    previous = current
    current = tempSum
    counter += 1
  #end while
#end fib()

fib(10)
