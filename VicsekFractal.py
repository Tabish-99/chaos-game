from matplotlib.patches import RegularPolygon
import matplotlib.pyplot as plt
import random as rd
import numpy as np


fg,ax=plt.subplots()
sqr = RegularPolygon(xy=(5,4),
                     numVertices=4,
                     radius=20,
                     edgecolor='k', fill=False)
vrt=sqr.get_verts()[:sqr.numvertices]
x=np.linspace(vrt.min(0)[0],vrt.max(0)[0],100)
y=np.linspace(vrt.min(0)[1],vrt.max(0)[1],100)
vrt = np.append(vrt, [sqr.xy], axis=0)

rx, ry = 5, 4
while sqr.contains_point((rx, ry), 0):
    rx = rd.choice(x)
    ry = rd.choice(y)


l = [*range(0, sqr.numvertices+1)]

n=int(input("Enter iteration(min 2000): "))
for i in range(0, n):
    pix = rd.choice(l)
    cx, cy = vrt[pix]
    rx = (2*cx + rx)/3
    ry = (2*cy + ry)/3
    ax.scatter(rx, ry, s=0.25, c='b')
    print('\t\t', ['|', '/', '-', '\\'][i % 4], end='\r')

ax.add_patch(sqr)
ax.set_title("Vicsek Fractal")
ax.axes.axis('equal')
ax.axes.axis('off')
plt.show()