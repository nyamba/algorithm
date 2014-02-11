from sys import stdin
import math

a, b, alpha = (float(i) for i in stdin.read().split())

k = (a-b)/2.0
alpha = 90 - alpha
alpha = (alpha*3.14)/180
h = k / math.tan(alpha)

print round(h*(a+b)/2, 1)
