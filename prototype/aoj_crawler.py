import xml.etree.ElementTree
import urllib2
import sys
import time
import random

res = urllib2.urlopen('http://judge.u-aizu.ac.jp/onlinejudge/webservice/user_list?solved_min=2')
if res.code != 200:
    print 'Error!'
    sys.exit(-1)

user_tree = xml.etree.ElementTree.fromstring(unicode(res.read(), errors = 'ignore'))

for user in user_tree.iterfind('user'):
    user_id = user.findtext('id').replace(u'\n', u'')
    print user.findtext('name').replace(u'\n', u'').encode('utf-8', errors = 'ignore')
    print user_id.encode('utf-8', errors = 'ignore')
    
    res = urllib2.urlopen('http://judge.u-aizu.ac.jp/onlinejudge/webservice/solved_record?user_id={}'.format(user_id))
    if res.code != 200:
        print 'Error!'
        sys.exit(-1)
    
    solved_tree = xml.etree.ElementTree.fromstring(unicode(res.read(), errors = 'ignore'))
    for solved in solved_tree:
        print solved.findtext('problem_id').replace(u'\n', u'').encode('utf-8', errors = 'ignore'),
    print
    
    time.sleep(random.uniform(1, 2))
