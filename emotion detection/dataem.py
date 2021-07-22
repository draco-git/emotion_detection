import pandas as pd
import numpy as np
s=[]
f=open('output.txt','r')
for line in f:
    kl=line.strip()
    s.append(kl)
f.close()
out=np.array(pd.get_dummies(s))
print(out[1:5])