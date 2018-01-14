#!/usr/local/lib/python3.6
import scipy.io
import numpy as np
import properties as pr
import matplotlib.pyplot as mp

# Raw data
data = scipy.io.loadmat('Data_BallGame_6pairs.mat.mat')
data = data["data_over_trials"]
print(data.shape) # (6,3) => 6 games with three columns, that are first player, second player, some information
#print(data)
# contains meta-information for all pairs in data
meta = scipy.io.loadmat('meta_info_6pairs.mat')
meta = meta["meta_info"]
print(meta.shape) # (6,2) => info for 6 games with two columns, that contain information about first player and second player

pair0 = meta[0]
pair1 = meta[1]
print("Info player 1: %s" % pair0[0])
print("Info player 2: %s" % pair0[1])

# extract data from game 0
game = 0
(p1, p2, pair) = data[game] #(32, 961, 140) (info, frame, trial)
print(p1.shape) #
print(p2.shape) # (21, 961, 140)
print(pair.shape) # (1,1)

#####################################################################STOP ab hier macht es keinen Sinn mehr, der code kann weg
# check who sees the obstacle in trial
# first transform variables

trial = 139
#good = p1[22][:][trial] #das 20tes property with
#obstacle = p1[30][:][trial]
#visible = p1[31][:][trial]

#for n in p1[1]

#print(max(obstacle))

#print("obstacle,visible for player,good play")
#for frame in range(0, obstacle.shape[0]):
#  print("%d,%d,%d" % (obstacle[frame], visible[frame], good[frame]))

#print(p1[])


for frameNr in range(0, len(p1[1])):
  x = p1[pr.X_POS][frameNr][trial]
  y = p1[pr.Y_POS][frameNr][trial]
  hit = p1[pr.OBSTACLE_HIT][frameNr][trial]
  print("x und y coordinate: %d %d and obstacle hit:%d" % (x,y, hit))

# x and y coordinates
mainline = plt.plot(results, 'r-', alpha=0.8)
plt.setp(mainline, color='red', linewidth=2.0)
