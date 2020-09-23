from matplotlib.patches import RegularPolygon
import matplotlib.pyplot as plt
import random as rd
import numpy as np

fg,ax=plt.subplots()
tr=RegularPolygon((5,4),3,0.3,edgecolor='k',fill=False)
vrt=tr.get_verts()[:3]
x=np.linspace(vrt.min(0)[0],vrt.max(0)[0],100)
y=np.linspace(vrt.min(0)[1],vrt.max(0)[1],100)
rx,ry=5,4
while tr.contains_point((rx,ry),0):
    rx=rd.choice(x)
    ry=rd.choice(y)


n=int(input("Enter iteration(min 1000): "))
for i in range(0,n):
    cx,cy=vrt[rd.choice(range(0,3))]
    rx=(rx+cx)/2
    ry=(ry+cy)/2
    ax.scatter(rx,ry,s=0.5,c='b')
    print('\t\t',['|', '/', '-', '\\'][i % 4], end='\r')

ax.add_patch(tr)
ax.set_title("Serpenski Triangle")
ax.axes.axis('equal')
ax.axes.axis('off')
plt.show()