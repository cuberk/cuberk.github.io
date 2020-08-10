from tkinter import *
from turtle import *
import turtle as t
import time

# 画方块
def draw_cube():
  t.color("blue")
  t.pensize(5)
  for i in range(4):
    t.penup()
    t.setpos(-120, i*80-120)
    t.pendown()
    t.forward(240)
    t.left(90)
    
    t.penup()
    t.setpos(i*80-120, -120)
    t.pendown()
    t.forward(240)
    t.right(90)

# 画箭头
def draw_arrow(start, end):
  # 根据具体情况缩短线段
  def tmp(m, n):
    if m == 0:
      if n > 0:
        return m + 10, n - 10
      else:
        return m - 10, n + 10
    if n == 0:
      if m > 0:
        return m - 10, n + 10
      else:
        return m + 10, n - 10
    ret_m = m - 10 if m > 0 else m + 10
    ret_n = n - 10 if n > 0 else n + 10
    return ret_m, ret_n
  # 辅助获取方向
  def tmp2(m, n):
    if m > n:
      return 2
    elif m < n:
      return 0
    return 1

  # 线段部分
  # 缩短线段以留白，避免线段连在一起
  if end[0] == start[0]:
    s0, e0 = start[0], end[0] 
    s1, e1 = tmp(start[1], end[1]) 
  elif end[1] == start[1]:
    s0, e0 = tmp(start[0], end[0]) 
    s1, e1 = start[1], end[1] 
  else:
    s0, e0 = tmp(start[0], end[0]) 
    s1, e1 = tmp(start[1], end[1]) 
  # 画线段
  t.penup()
  t.pensize(5)
  t.color("black")
  t.goto(s0, s1)
  t.down()
  t.goto(e0, e1)

  # 箭头部分
  # 先判断箭头方向
  res0 = tmp2(e0, s0)
  res1 = tmp2(e1, s1)
  angle = [
    [ 225, 180, 135],
    [ 270, 0, 90],
    [ 315, 0, 45]
  ]
  t.seth(angle[res0][res1])
  # 画箭头
  t.right(160)
  t.forward(10)
  t.goto(e0, e1)
  t.right(40)
  t.forward(10)

def draw(CE):
  C, E= CE[0], CE[1]
  lenC, lenE = len(C), len(E)
  if lenC % 2 == 0:
    for i in range(0, lenC, 2):
      draw_arrow(c[C[i]], c[C[i+1]])
      draw_arrow(c[C[i+1]], c[C[i]])
  elif lenC == 3:
    draw_arrow(c[C[0]], c[C[1]])
    draw_arrow(c[C[1]], c[C[2]])
    draw_arrow(c[C[2]], c[C[0]])

  if lenE % 2 == 0:
    for i in range(0, lenE, 2):
      draw_arrow(e[E[i]], e[E[i+1]]) 
      draw_arrow(e[E[i+1]], e[E[i]]) 
  elif lenE == 3:
    draw_arrow(e[E[0]], e[E[1]])
    draw_arrow(e[E[1]], e[E[2]])
    draw_arrow(e[E[2]], e[E[0]])

# edge画箭头用坐标
e = [
  [0, -80],
  [80, 0],
  [0, 80],
  [-80, 0]
]
# corner画箭头用坐标
c = [
  [-80, -80],
  [80, -80],
  [80, 80],
  [-80, 80]
]
# PLL具体情况，先角后棱
PLLs = {
  'H' : [[],[0,2,1,3]],
  'Z' : [[],[0,3,1,2]],
  'Ua' : [[],[3,0,1]],
  'Ub' : [[],[1,0,3]],
  'E' : [[0,3,1,2],[]],
  'Aa' : [[0,1,2],[]],
  'Ab' : [[1,0,2],[]],
  'V' : [[1,3],[1,2]],
  'Y' : [[1,3],[2,3]],
  'T' : [[1,2],[1,3]],
  'F' : [[1,2],[0,2]],
  'Ra' : [[2,3],[0,1]],
  'Rb' : [[2,3],[0,3]],
  'Ja' : [[1,2],[1,2]],
  'Jb' : [[1,2],[0,1]],
  'Ga' : [[0,3,2],[1,2,3]],
  'Gb' : [[0,1,3],[0,3,2]],
  'Gc' : [[0,1,3],[0,1,3]],
  'Gd' : [[0,3,2],[0,2,3]],
  'Na' : [[0,2],[1,3]],
  'Nb' : [[1,3],[1,3]],
}

for PLL in PLLs:
  draw_cube()
  draw(PLLs[PLL])
  t.hideturtle()
  ts = t.getscreen()
  ts.getcanvas().postscript(file = PLL + "_perm.eps")
  t.reset()
