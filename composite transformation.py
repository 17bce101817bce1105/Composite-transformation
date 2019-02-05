import PIL.ImageDraw as ID, PIL.Image as Image, PIL.ImageShow as IS
from math import *
im = Image.new("RGB", (640,480))
draw = ID.Draw(im)
val=pi/180
t1=int(input("Enter value for t1:"))
t2=int(input("Enter value for t2:"))
s1=int(input("Enter value for s1:"))
s2=int(input("Enter value for s2:"))
a=int(input("Enter value for a:"))
hx=int(input("Enter value for hx:"))


t=[[1,0,t1],[0,1,t2],[0,0,1]]
s=[[s1,0,0],[0,s2,0],[0,0,1]]
r=[[cos(a*val),-sin(a*val),0],[sin(a*val),cos(a*val),0],[0,0,1]]
shr=[[1,hx,0],[0,1,0],[0,0,1]]
ref=[[-1,0,0],[0,1,0],[0,0,1]]

def multiply(a,b):
   c=list()
   for i in range(0,3):
      temp = []
      for j in range(0,3):
         sumVal = 0
         for k in range(0,3):
            sumVal = sumVal + a[i][k] * b[k][j]
         temp.append(sumVal)
      c.append(temp)
   return c
f=multiply(t,s)
f=multiply(f,r)
f=multiply(f,shr)
f=multiply(f,ref)

p=[[160,134],[160,200],[120,174],[120,155]]
def ref(f,a,b):
   temp=[]
   xref=f[0][0]*a + f[0][1]*b + f[0][2]*1 + 320 
   yref=f[1][0]*a + f[1][1]*b + f[1][2]*1 
   temp.append((int(xref),int(yref)))
   return temp
new=[]
for i in p:
   b=ref(f,i[0],i[1])
   new.append(b)
   
print(new)
draw.polygon(((160+320,134),(160+320,200),(120+320,174),(120+320,155)),fill=0,outline=255)
draw.polygon((new[0][0],new[1][0],new[2][0],new[3][0]),fill=0,outline=255)
print(f)


im.show()
