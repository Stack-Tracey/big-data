#!/usr/local/opt python3
import scipy.io
m = scipy.io.loadmat('meta_info_6pairs.mat')
m = m["meta_info"]

# contains information for all pairs
print(m.shape)
pair0 = m[0]
print("Info player 1: %s" % pair0[0])
print("Info player 2: %s" % pair0[1])

# Raw data
data = scipy.io.loadmat('Data_BallGame_6pairs.mat.mat')

data = data["data_over_trials"]
print(data.shape) # (6,3) => 6 games with three columns, that are first player, second player, some information

game = 0
# extract data from game 0
(p1, p2, pair) = data[game]
print(p1.shape) # (32, 961, 140) (info, frame, trial)
print(p2.shape) # (21, 961, 140)
print(pair.shape) # (1,1)

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
