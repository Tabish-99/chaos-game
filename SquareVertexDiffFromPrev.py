from matplotlib.patches import RegularPolygon
import matplotlib.pyplot as plt
import random as rd
import numpy as np


fg,ax=plt.subplots()
sqr = RegularPolygon(xy=(5,4),
                     numVertices=4,
                     edgecolor='k', fill=False)
vrt=sqr.get_verts()[:sqr.numvertices]
x=np.linspace(vrt.min(0)[0],vrt.max(0)[0],100)
y=np.linspace(vrt.min(0)[1],vrt.max(0)[1],100)
rx, ry = 5, 4
while sqr.contains_point((rx, ry), 0):
    rx = rd.choice(x)
    ry = rd.choice(y)


pix = rd.choice(range(0, sqr.numvertices))
n=int(input("Enter iteration(min 1000): "))
for i in range(0, n):
    l = [*range(0, sqr.numvertices)]
    l.remove(pix)
    pix = rd.choice(l)
    cx, cy = vrt[pix]
    rx = (rx+cx)/2
    ry = (ry+cy)/2
    ax.scatter(rx, ry, s=0.25, c='b')
    print('\t\t', ['|', '/', '-', '\\'][i % 4], end='\r')

ax.add_patch(sqr)
ax.set_title("Square: vertex different from previous")
ax.axes.axis('equal')
ax.axes.axis('off')
plt.show()