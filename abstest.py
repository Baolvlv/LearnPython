#!/usr/bin/env python3
#def my_abs(x):
#    if not isinstance(x,(int,float)):
#       raise TypeError('bad opear type')
#  if(x>=0):
#       return x
#   else:
#       return -x
import math
def quadratic(a,b,c):
    t = b*b-4*a*c
    if(t< 0):
        return 'no solution'
    else:
        return (-b+math.sqrt(t))/(2*a),(-b-math.sqrt(t))/(2*a)

