import xml.etree.ElementTree
import urllib2
import sys
import time
import math

def jaccard(v1, v2):
    numerator = sum([c in v2 for c in v1])
    denominator = len(v1) + len(v2) - numerator
    return float(numerator) / denominator if denominator != 0 else 0

user = {}

count = 0
for line in sys.stdin:
    line = line.strip()
    count += 1
    if count == 2:
        id = line
    if count == 3:
        problem = set(line.split())
        user[id] = problem
        count = 0

for u1, p1 in user.iteritems():
    temp = []
    for u2, p2 in user.iteritems():
        if p1.issubset(p2) or p1.issuperset(p2):
            continue
        sim = jaccard(p1, p2)
        if sim != 1.0:
            temp.append((sim, u1, u2))
    temp.sort()
    for t in temp[-10:]:
        print t