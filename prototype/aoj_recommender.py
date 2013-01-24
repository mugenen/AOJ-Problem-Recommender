import xml.etree.ElementTree
import urllib2
import sys
import time
import math

def cos(v1, v2):
    numerator = sum([v1[c] * v2[c] for c in v1 if c in v2])
    square = lambda x: x * x
    denominator =  math.sqrt(sum(map(square, v1.values())) * sum(map(square, v2.values())))
    return float(numerator) / denominator if denominator != 0 else 0


user = {}

count = 0
for line in sys.stdin:
    line = line.strip()
    count += 1
    if count == 2:
        id = line
    if count == 3:
        problem = dict(map(lambda x: (x, 1), line.split()))
        user[id] = problem
        count = 0

for u1, p1 in user.iteritems():
    temp = []
    for u2, p2 in user.iteritems():
        if u1 == u2:
            continue
        sim = cos(p1, p2)
        if sim != 1.0:
            temp.append((sim, u1, u2))
    temp.sort()
    for t in temp[-10:]:
        print t