import sys,re,html
from html.parser import HTMLParser
class P(HTMLParser):
    def __init__(s): super().__init__(); s.skip=0; s.o=[]
    def handle_starttag(s,t,a):
        if t in('script','style','svg'): s.skip+=1
    def handle_endtag(s,t):
        if t in('script','style','svg'): s.skip-=1
    def handle_data(s,d):
        if not s.skip and d.strip(): s.o.append(d.strip())
p=P(); p.feed(open(sys.argv[1],encoding='utf8').read())
out=[]
for x in p.o:
    if not out or out[-1]!=x: out.append(x)
print('\n'.join(out))
