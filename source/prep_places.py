# Build places.json from the Countries States Cities Database (dr5hn, ODbL 1.0).
# Inputs (from the repo's csv/ folder and its latest release): states.csv, countries.csv,
# csv-cities.csv, csv-counties.csv in the directory given as argv[1].
import csv, json, sys, collections, os
d = sys.argv[1]
rd = lambda f: list(csv.DictReader(open(os.path.join(d, f), encoding='utf-8')))
countries, states, cities, counties = rd('countries.csv'), rd('states.csv'), rd('csv-cities.csv'), rd('csv-counties.csv')
# city types the dataset documents as not being settlements (TYPE_FIELD.md)
NOT_SETTLEMENT = {'county','regency','prefecture','parish','banner','province','abandoned','area','historical','oblast'}
by_state = collections.defaultdict(set)
for c in cities:
    if c['type'] in NOT_SETTLEMENT: continue
    by_state[c['state_id']].add(c['name'].strip())
st_by_country = collections.defaultdict(list)
for s in states: st_by_country[s['country_code']].append(s)
# China: province -> prefecture-level city (counties level 2) -> district/county (counties level 3)
cn_l2 = collections.defaultdict(list); cn_l3 = collections.defaultdict(set)
for k in counties:
    if k['country_code'] != 'CN': continue
    if k['level'] == '2': cn_l2[k['state_id']].append(k)
    elif k['level'] == '3' and k['parent_id']: cn_l3[k['parent_id']].add(k['name'].strip())
out = []
for co in countries:
    cc = co['iso2']; regs = []
    types = collections.Counter(s['type'] for s in st_by_country[cc])
    for s in st_by_country[cc]:
        if cc == 'CN':
            kids = [[k['name'].strip(), sorted(cn_l3[k['id']])] for k in cn_l2[s['id']]]
            regs.append([s['name'].strip(), kids])
        else:
            regs.append([s['name'].strip(), sorted(by_state[s['id']])])
    top, n = (types.most_common(1)[0] if types else ('', 0))
    label = top.title() if n >= 0.6 * max(1, len(st_by_country[cc])) else 'State / province / region'
    label = {'Land': 'State (Land)', '': 'State / province / region'}.get(label, label)
    out.append([co['name'].strip(), cc, label, regs])
json.dump(out, open('places.json', 'w'), ensure_ascii=False, separators=(',', ':'))
print(len(out), 'countries', sum(len(c[3]) for c in out), 'regions', os.path.getsize('places.json'))
