#!/usr/local/opt python3
import scipy.io

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
(p1, p2, pair) = data[game]
print(p1.shape) # (32, 961, 140) (info, frame, trial)
print(p2.shape) # (21, 961, 140)
print(pair.shape) # (1,1)
#####################################################################STOP
# check who sees the obstacle in trial
# first transform variables
trial = 100
good = p1[20][:][trial]
obstacle = p1[30][:][trial]
visible = p1[31][:][trial]

print(max(obstacle))

print("obstacle,visible for player,good play")
for frame in range(0, obstacle.shape[0]):
  print("%d,%d,%d" % (obstacle[frame], visible[frame], good[frame]))
