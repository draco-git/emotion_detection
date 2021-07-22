import pandas as pd
import numpy as np
df=pd.read_excel('DATA.xlsx')
inp=df['input']
out=df['fear']
f=open('output.txt','w')
inpt=np.array(inp)
print(len(inp))
for i in range(7654):
    f.write(out[i])
    f.write('\n')

f.close()
print(inp.head(),out.head())
