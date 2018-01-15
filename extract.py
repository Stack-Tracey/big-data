#!/usr/local/lib/python3.6
import scipy.io
import numpy as np
import properties as pr
import matplotlib.pyplot as plt
import subject as sb

from gpanel import *

#AnimEx1.py

from gpanel import *
import time

makeGPanel(-6, 6, -220, 70)
setColor("red")
enableRepaint(False)

g = 9.81
dt= 0.05

t = 0; y = 0
v = 25

while t < 10:
  v = v - g * dt
  y = y + v * dt
  t = t + dt
  drawGrid(-5, 5, -200, 50, "gray")
  pos(0, y)
  fillCircle(0.3)
  repaint()
  time.sleep(dt)
  clear()
keep()







# Raw data
data = scipy.io.loadmat('Data/Data_BallGame_6pairs.mat.mat')
data = data["data_over_trials"]
meta = scipy.io.loadmat('Data/meta_info_6pairs.mat')

game = 0
player = 0

# extract data from game 0
(p1, p2, pair_meta) = data[game] #(info, frame, trial)

# prints the number of subjects and gender distribution among them
def gender_distribution(card_sub, card_fem , card_male):
  x = card_fem
  y = card_male
  card_game = 0
  while card_game < len(data):
    gender = sb.Subject(card_sub , card_game).sex()
    if gender == 'f':
      x = x + 1
    else:
      y = y + 1
    card_game = card_game + 1
  card_sub = card_sub + 1
  if card_sub < 2:
    gender_distribution(card_sub, x, y)
  else:
    print(len(data)*2, "subjects did attend \n")
    print("%d are female \n" % x + "%d are male \n" % y)

gender_distribution(0, 0, 0)


# categorizes subjects into 3 age intervalls and prints tem out
def age_distribution(card_sub, teen , twen, old):
  x = teen
  y = twen
  z = old
  card_game = 0
  while card_game < len(data):
    age = sb.Subject(card_sub , card_game).age()
    if age <= 20:
      x = x + 1
    elif 21 <= age <= 30:
      y = y + 1
    else:
      z = z + 1
    card_game = card_game + 1
  card_sub = card_sub + 1
  if card_sub < 2:
    age_distribution(card_sub, x, y, z)
  else:
    print("%d are younger that 20" % x)
    print("%d are between 20 and 30" % y)
    print("%d is older than 30 \n" % z)

age_distribution(0, 0, 0, 0)



#pair = p1[pr.START_PAIR : pr.END_PAIR]
#print("Proximitry to obstacle", pair)
#print(pair_meta)


#returns x and y coordinates of ball and hits by obstacles
hits = []
trial = 120
for frameNr in range(0, len(p1[1])):
  x = p1[pr.X_POS_BALL][frameNr][trial]
  y = p1[pr.Y_POS_BALL][frameNr][trial]
  hit = p1[pr.OBSTACLE_HIT][frameNr][trial]
  hits.append(hit)
 # print("x und y coordinate: %d %d and obstacle hit:%d" % (x,y, hit))

# hits
mainline = plt.plot(hits, 'r-', alpha=0.8) #der eigentlich plot
plt.setp(mainline, color='red', linewidth=2.0)# einstellung zeichnung

plt.ylabel('hits')
plt.show()






