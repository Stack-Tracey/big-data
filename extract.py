#!/usr/local/lib/python3.6
import scipy.io
import numpy as np
import matplotlib.pyplot as plt

import subject as sb
import properties as pr
from anime import runAnimation


# Raw data
data = scipy.io.loadmat('Data/Data_BallGame_6pairs.mat.mat')
data = data["data_over_trials"]
meta = scipy.io.loadmat('Data/meta_info_6pairs.mat')

game = 1
player = 0

# extract data from game 0
(p1, p2, pair_meta) = data[game] #(info, frame, trial)
fem_age = []
male_age = []

# prints the number of subjects and gender distribution among them
def gender_distribution(card_sub, card_fem , card_male):
  x = card_fem
  y = card_male
  card_game = 0
  while card_game < len(data):
    gender = sb.Subject(card_sub , card_game).sex()
    if gender == 'f':
      x = x + 1
      age = sb.Subject(card_sub , card_game).age()
      fem_age.append(age)
    else:
      y = y + 1
      age = sb.Subject(card_sub, card_game).age()
      male_age.append(age)
    card_game = card_game + 1
  card_sub = card_sub + 1
  if card_sub < 2:
    gender_distribution(card_sub, x, y)
  else:
    print(len(data)*2, "subjects did attend \n")
    print("%d are female \n" % x + "%d are male \n" % y)
  return x, y, fem_age, male_age


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


ages = gender_distribution(0, 0, 0)
x, y, x_age, y_age = ages

# returns age classification based on given gender a = {<20}, b = {20-30}, c = {>30}
def age_and_gender_cor(gender):
  a = 0
  b = 0
  c = 0
  for item in gender:
    if item < 20:
      a = a + 1
    elif item < 31:
      b = b + 1
    else:
      c = c + 1

  return a, b, c


#plots the age and gender distribution
female = age_and_gender_cor(x_age) #number of females in each group
male = age_and_gender_cor(y_age) #number of males in each group

plt.rcdefaults()

objects = ('<20', '20-30', '>30')
y_pos = np.arange(len(objects))
bar_width = 0.35
opacity = 0.4
fig, ax = plt.subplots()
error_config = {'ecolor': '0.3'}
rects1 = plt.bar(y_pos, male, bar_width,
                alpha=opacity, color='b',
                error_kw=error_config,
                label='Men')

rects2 = plt.bar(y_pos + bar_width, female, bar_width,
                alpha=opacity, color='r',
                error_kw=error_config,
                label='Women')

plt.xticks(y_pos, objects)
plt.ylabel('subjects')
plt.xlabel('age')
plt.title('age and gender distribution')
ax.legend()





#returns x and y coordinates of ball and hits by obstacles
hits = []
targethits = []
positions = []
trial = 120
for frameNr in range(0, len(p1[1])):
  x = p1[pr.X_POS_BALL][frameNr][trial]
  y = p1[pr.Y_POS_BALL][frameNr][trial]
  hit = p1[pr.OBSTACLE_HIT][frameNr][trial]
  target = p1[pr.TARGET_HIT_COL][frameNr][trial]
  hits.append(hit)
  targethits.append(target)
  positions.append((x, y))
 # print("x und y coordinate: %d %d and obstacle hit:%d" % (x,y, hit))

age_distribution(0, 0, 0, 0)
#runAnimation(positions, hits, targethits)
plt.show()

