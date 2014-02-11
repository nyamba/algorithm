from sys import stdin
import math

x, y, z = (float(i) for i in stdin.read().split())

a = round(2*math.cos(x-3.14/6)/(0.5 + math.sin(y)**2), 3)
b = round(1+ z**2/(3+(z**2)/5))
print "%.3f %.3f" % (a, b)
