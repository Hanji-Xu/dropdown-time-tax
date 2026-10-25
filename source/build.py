import csv,json,sys
ab={'Alabama':'AL','Alaska':'AK','Arizona':'AZ','Arkansas':'AR','California':'CA','Colorado':'CO','Connecticut':'CT','Delaware':'DE','District of Columbia':'DC','Florida':'FL','Georgia':'GA','Hawaii':'HI','Idaho':'ID','Illinois':'IL','Indiana':'IN','Iowa':'IA','Kansas':'KS','Kentucky':'KY','Louisiana':'LA','Maine':'ME','Maryland':'MD','Massachusetts':'MA','Michigan':'MI','Minnesota':'MN','Mississippi':'MS','Missouri':'MO','Montana':'MT','Nebraska':'NE','Nevada':'NV','New Hampshire':'NH','New Jersey':'NJ','New Mexico':'NM','New York':'NY','North Carolina':'NC','North Dakota':'ND','Ohio':'OH','Oklahoma':'OK','Oregon':'OR','Pennsylvania':'PA','Rhode Island':'RI','South Carolina':'SC','South Dakota':'SD','Tennessee':'TN','Texas':'TX','Utah':'UT','Vermont':'VT','Virginia':'VA','Washington':'WA','West Virginia':'WV','Wisconsin':'WI','Wyoming':'WY','Puerto Rico':'PR'}
comm={r[0]:float(r[1])/2 for r in csv.reader(open('comm.csv'))}
rows=[]
for n,p,d in csv.reader(open('dens.csv')):
    row=[n,ab[n],int(p),float(d),round(comm[n],1)]
    if n=='Puerto Rico': row.append(1)
    rows.append(row)
assert len(rows)==52 and len(comm)==52 and set(comm)==set(ab)
t=open('template.html').read()
t=t.replace('__STATES__',json.dumps(rows,separators=(',',':'))).replace('__COUNTRIES__',json.dumps(json.load(open('countries.json')),ensure_ascii=False,separators=(',',':'))).replace('__NUM__',sys.argv[1])
open(sys.argv[2],'w').write(t)
