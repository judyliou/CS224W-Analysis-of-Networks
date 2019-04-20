import snap
import numpy as np
import matplotlib.pyplot as plt


wiki = snap.LoadEdgeList(snap.PNGraph, "wiki-Vote.txt", 0, 1, '\t')

degree = []
cnt = []
CntV = snap.TIntPr64V()

snap.GetOutDegCnt(wiki, CntV)
for i in CntV:
    if i.GetVal1() != 0 and i.GetVal2() != 0:
        degree.append(i.GetVal1())
        cnt.append(i.GetVal2())
degree = np.array(degree)
cnt = np.array(cnt)
    
    
fig = plt.figure()
plt.figure(figsize=(12,8)) 
ax = plt.gca()
ax.scatter(degree, cnt, c='red', alpha=0.5, edgecolors='none', s=80)
ax.set_yscale('log')
ax.set_xscale('log')
ax.set_xlim([degree.min(), degree.max()])
ax.set_title('Out-degree Distribution', fontsize=30)
ax.set_xlabel('Degree (log)', fontsize=24)
ax.set_ylabel('Count (log)', fontsize=24)
plt.savefig('hw0_2.1.png')

degree = np.log10(degree)
cnt = np.log10(cnt)

a, b = np.polyfit(degree, cnt, 1)
print('a =', a)
print('b =', b)

# Make theoretical line to plot
x = np.array([degree.min(), degree.max()])
y = a * x + b

plt.figure(figsize=(12,8))
plt.plot(degree, cnt, 'ro')
plt.plot(x, y, 'b', linewidth=3)
plt.xlabel('Degree (log)', fontsize=20)
plt.ylabel('Count (log)', fontsize=20)
plt.title('Out-degree Distribution', fontsize=30)

plt.savefig('hw0_2.2.png')
