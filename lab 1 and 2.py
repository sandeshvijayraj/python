import pandas as pd
import numpy as np
data =pd.DataFrame(pd.read_csv("book2.csv"))
concept=np.array(data.iloc[:,:-1])
target=np.array(data.iloc[:,-1:])
specific_h=['?' for i in range(len(concept[0]))]

general_h=[['?' for i in range(len(concept[0]))] for i in range(len(concept[0]))]
print(specific_h)
print(general_h)

for i in range(len(concept)):
    if target[i]=='yes':
        specific_h=concept[i]
        break
for i in range(len(concept)):
    if target[i]=='yes':
        for j in range(len(concept[i])):
            if specific_h[j]!=concept[i][j] and specific_h[j]!='?':
                specific_h[j]='?'
        for l in range(len(concept[i])):
            if general_h[l][l]!=specific_h[l]:
                general_h[l][l]='?'
    else:
        for k in range(len(concept[i])):
            if specific_h[k]!=concept[i][k]:
                general_h[k][k]=specific_h[k]
            else:
                general_h[k][k]='?'
    print('specific',specific_h)
    print('general',general_h)
while True:
    try:
        general_h.remove(['?','?','?','?','?','?'])
    except ValueError:
        break
print("optimized general",general_h)
