# Rebuild the page: python3 build.py <series number> <output.html>
# places.json comes from prep_places.py; the speed-test list is in testwords.py.
import json, sys, datetime
from testwords import FOODS, WORDS
words = FOODS + WORDS
assert len(words) == len(set(words)) == 250
places = json.load(open('places.json'))
t = open('template.html').read()
for k, v in {'__TESTWORDS__': json.dumps(words, ensure_ascii=False),
             '__PLACES__': json.dumps(places, ensure_ascii=False, separators=(',', ':')),
             '__NFOODS__': str(len(FOODS)), '__NWORDS__': str(len(WORDS)),
             '__NUM__': sys.argv[1],
             '__DATE__': datetime.date.today().strftime('%B %-d, %Y')}.items():
    t = t.replace(k, v)
open(sys.argv[2], 'w').write(t)
