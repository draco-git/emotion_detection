f=open('output.txt','r')
import pandas as pd
import matplotlib.pyplot as plt
l=[]

for k in f:
    l.append(k.strip())
x=pd.Series(l)
print(x.head(),x.value_counts(),x.describe())
colors=['green']
x.hist(bins=25,histtype='bar',color=colors)
plt.show()
