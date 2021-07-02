import glob
import pandas

#for name in glob.glob('landingpad/China/*.csv'):
name = 'landingpad/China/000001.SZ.csv'
df = pandas.read_csv(name)
col = []
for numentry in df['trade_date']:
    entry = str(numentry)
    y = entry[:4]
    m = entry[4:6]
    d = entry[6:]
    date = str(m)+ '-' + str(d) + '-' + str(y)
    col.append(date)
df.drop('trade_date')