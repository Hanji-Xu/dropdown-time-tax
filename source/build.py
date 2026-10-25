# Rebuild the page: python3 build.py <series number> <output.html>
import csv, json, sys, datetime
ab = {'Alabama':'AL','Alaska':'AK','Arizona':'AZ','Arkansas':'AR','California':'CA','Colorado':'CO','Connecticut':'CT','Delaware':'DE','District of Columbia':'DC','Florida':'FL','Georgia':'GA','Hawaii':'HI','Idaho':'ID','Illinois':'IL','Indiana':'IN','Iowa':'IA','Kansas':'KS','Kentucky':'KY','Louisiana':'LA','Maine':'ME','Maryland':'MD','Massachusetts':'MA','Michigan':'MI','Minnesota':'MN','Mississippi':'MS','Missouri':'MO','Montana':'MT','Nebraska':'NE','Nevada':'NV','New Hampshire':'NH','New Jersey':'NJ','New Mexico':'NM','New York':'NY','North Carolina':'NC','North Dakota':'ND','Ohio':'OH','Oklahoma':'OK','Oregon':'OR','Pennsylvania':'PA','Rhode Island':'RI','South Carolina':'SC','South Dakota':'SD','Tennessee':'TN','Texas':'TX','Utah':'UT','Vermont':'VT','Virginia':'VA','Washington':'WA','West Virginia':'WV','Wisconsin':'WI','Wyoming':'WY'}
# dens.csv: name, 2020 resident population, density (Census 2020); Puerto Rico row is skipped
states = [[n, ab[n], int(p)] for n, p, d in csv.reader(open('dens.csv')) if n in ab]
assert len(states) == 51
cities = json.load(open('cities.json'))
iso = json.load(open('countries.json'))
codes = {c[1] for c in iso}
city = {k: v for k, v in cities['cities'].items() if k in codes}
t = open('template.html').read()
for k, v in {'__STATES__': json.dumps(states, separators=(',', ':')),
             '__COUNTRIES__': json.dumps(iso, ensure_ascii=False, separators=(',', ':')),
             '__CITIES__': json.dumps(city, ensure_ascii=False, separators=(',', ':')),
             '__GNC_VER__': cities['source'].split()[-1],
             '__NUM__': sys.argv[1],
             '__DATE__': datetime.date.today().strftime('%B %-d, %Y')}.items():
    t = t.replace(k, v)
open(sys.argv[2], 'w').write(t)
