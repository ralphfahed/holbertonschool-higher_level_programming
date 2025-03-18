#!/usr/bin/python3

# Using only one print function and string format
print("".join("{}".format(chr(x)) 
      for x in range(97, 123) 
      if chr(x) != 'q' and chr(x) != 'e'), end="")
