import random as rd
import numpy as np
from matplotlib.patches import RegularPolygon,Circle
import matplotlib.pyplot as plt

def mxang(rd,ds):
    return np.arcsin(rd/ds)

def dist(p1,p2):
    p1=np.array(p1)
    p2=np.array(p2)
    return round(np.linalg.norm(p2-p1),3)

def ang(rp,vrt,cnt):
    rp=np.array(rp)
    vrt=np.array(vrt)
    cnt=np.array(cnt)
    rv=vrt-rp
    rc=cnt-rp
    csx=rv.dot(rc)/np.linalg.norm(rv)/np.linalg.norm(rc)
    return np.arccos(csx)
    
fg,ax=plt.subplots(figsize=(10,10))
sq=RegularPolygon((5,4),4,5,edgecolor='k',fill=False,orientation=np.pi/4)
cr=Circle((5,4),1,edgecolor='r',fill=False)
pnt=sq.get_verts()[:4]

x=np.linspace(pnt.min(0)[0],pnt.max(0)[0],100)
y=np.linspace(pnt.min(0)[1],pnt.max(0)[1],100)

rx,ry=5,4
while not cr.contains_point((rx,ry),0):
    rx=rd.choice(x)
    ry=rd.choice(y)

sx=-2;ix=-1

i=0
inp = int(input("Enter no. of iterations(min 1000):"))
while i<inp:
    ix=rd.choice(range(0,4))
    if ix==sx  :
        continue
    sx=ix
    cx,cy=pnt[sx]
    mx=(rx+cx)/2
    my=(ry+cy)/2
   
    if ang((rx,ry),(cx,cy),cr.center)<mxang(cr.radius,dist((rx,ry),cr.center)):
        continue
    
    rx=mx
    ry=my
    ax.scatter(rx,ry,s=1,c='b')
    i+=1
    print('\t\t',['|', '/', '-', '\\'][i % 4], end='\r')



ax.add_patch(sq)
ax.add_patch(cr)

ax.axes.axis('equal')
ax.axes.axis('off')
plt.show()
