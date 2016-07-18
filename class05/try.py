import sys
try:
  untrusted.execute()
except: # catch *all* exceptions
# except ZeroDivisionError as e:
  e = sys.exc_info()[0]
  write_to_page( "<p>Error: %s</p>" % e )
