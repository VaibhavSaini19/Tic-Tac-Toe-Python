# TIC-TAC-TOE
import turtle as pt
#pt=turtle.Turtle()
pt.speed(speed=0)

def cross(pt):     #create cross
  pt.pu()
  pt.lt(45)
  pt.fd(56.5685)
  pt.pd()
  pt.bk(113.1370)
  pt.pu()
  pt.lt(45)
  pt.fd(80)
  pt.rt(135)
  pt.pd()
  pt.fd(113.1370)

matrix=[[0 for x in range(3)]for y in range(3)]      #marks positions

index={1:[0,0],2:[0,1],3:[0,2],4:[1,0],5:[1,1],6:[1,2],7:[2,0],8:[2,1],9:[2,2]}

pos=0
j=0
flag=0

def mat(pos,j): #update matrix
  a=index[pos][0]
  b=index[pos][1]
  global matrix
  global flag
  if matrix[a][b]==0:
    if j%2==0:
        matrix[a][b]=1
    else:
        matrix[a][b]=2
    flag=1
  return matrix

strikeh={0:[-150,100],1:[-150,0],2:[-150,-100]}
strikev={0:[-100,150],1:[0,150],2:[100,150]}
striked={1:[-150,150],2:[150,150]}

def won():       # check victory
  global matrix
  mx=matrix
  pt.pensize(8)
  for k in range(3):
    if all(x==1 for x in mx[k]):
      pt.pu()
      pt.goto(strikeh[k])
      pt.seth(0)
      pt.pd()
      pt.fd(300)
      print('P1 WON')
      return True
    elif all(x[k]==1 for x in mx):
      pt.pu()
      pt.goto(strikev[k])
      pt.seth(270)
      pt.pd()
      pt.fd(300)
      print('P1 WON')
      return  True
    elif all(x==2 for x in mx[k]):
      pt.pu()
      pt.goto(strikeh[k])
      pt.seth(0)
      pt.pd()
      pt.fd(300)
      print('P2 WON')
      return True
    elif all(x[k]==2 for x in mx):
      pt.pu()
      pt.goto(strikev[k])
      pt.seth(270)
      pt.pd()
      pt.fd(300)
      print('P2 WON')
      return True
    elif (mx[0][0]==1 and mx[1][1]==1 and mx[2][2]==1):
      pt.pu()
      pt.goto(striked[1])
      pt.seth(315)
      pt.pd()
      pt.fd(424.264)
      print('P1 WON')
      return True
    elif (mx[0][2]==1 and mx[1][1]==1 and mx[2][0]==1):
      pt.pu()
      pt.goto(striked[2])
      pt.seth(225)
      pt.pd()
      pt.fd(424.264)
      print('P1 WON')
      return True
    elif (mx[0][0]==2 and mx[1][1]==2 and mx[2][2]==2):
      pt.pu()
      pt.goto(striked[1])
      pt.seth(315)
      pt.pd()
      pt.fd(424.264)
      print('P2 WON')
      return True
    elif (mx[0][2]==2 and mx[1][1]==2 and mx[2][0]==2):
      pt.pu()
      pt.goto(striked[2])
      pt.seth(225)
      pt.pd()
      pt.fd(424.264)
      print('P2 WON')
      return True
  return False

for i in range(4):    #create board
  pt.pu()
  pt.fd(50)
  pt.lt(90)
  pt.fd(150)
  pt.rt(180)
  pt.pd()
  pt.fd(300)
  pt.pu()
  pt.goto(0,0)
  pt.seth(0)
  rot=(i+1)*90
  pt.lt(rot)
pt.pu()

circoord={1:[-100,60],2:[0,60],3:[100,60],4:[-100,-40],5:[0,-40],6:[100,-40],7:[-100,-140],8:[0,-140],9:[100,-140]}          # coordinates for circle
crocoord={1:[-100,100],2:[0,100],3:[100,100],4:[-100,0],5:[0,0],6:[100,0],7:[-100,-100],8:[0,-100],9:[100,-100]}         # coordinates for cross


def get(a,b):
  pt.pensize(3)
  global pos,matrix,j
  if b>50:
    if a<-50:
        pos=1
    elif a>-50 and a<50:
        pos=2
    else:
        pos=3
  elif b<50 and b>-50:
    if a<-50:
        pos=4
    elif a>-50 and a<50:
        pos=5
    else:
        pos=6
  else:
    if a<-50:
        pos=7
    elif a>-50 and a<50:
        pos=8
    else:
        pos=9


  pt.pu()
  pt.goto(0,0)
  pt.seth(0)

  matrix=mat(pos,j)

  global flag
  if flag==1:
    if j%2==0:
        x=circoord[pos][0]
        y=circoord[pos][1]
        pt.pencolor("blue")
        pt.goto(x,y)
        pt.pd()
        pt.circle(40)
    else:
        x=crocoord[pos][0]
        y=crocoord[pos][1]
        pt.pencolor('#74f442')
        pt.goto(x,y)
        pt.pd()
        cross(pt)

    j=j+1
    flag=0

  if won():
      pt.exitonclick()


def main():
    pt.onscreenclick(get)
    pt.mainloop()
  
if __name__ == "__main__":
	main()
