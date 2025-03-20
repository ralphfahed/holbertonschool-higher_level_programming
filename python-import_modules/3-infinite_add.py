#!/usr/bin/python3
import sys
'''
mna3mol var esma numbers = array ta nhot bi alba []
men 7awel arg la int => int(arg)
for loop mnobrom bel sys.arg[1:] men doun esem lfile
sum () is a built in function 
'''
if __name__ == "__main__":
    numbers = [int(arg) for arg in sys.argv[1:]]
    total = sum(numbers)
    print(total)
