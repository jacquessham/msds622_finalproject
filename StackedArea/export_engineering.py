import pandas as pd

f = open('../Data/export_raw.tsv','r',encoding='utf-8-sig')
raw = f.read()
rows = raw.split('\n')
header = rows[0].split('\t')
df = []
for i in range(1, len(rows)):
    row = rows[i].split('\t')
    for j in range(1, len(header)):
        if row[0]=='UNITED KINGDOM':
            df.append(['United Kingdom', header[j], row[j]])
        else:
            df.append([row[0].capitalize(), header[j], row[j]])
df = pd.DataFrame(df,columns=['country','year','volume'])
df.to_csv('../Data/export.csv',index=False)