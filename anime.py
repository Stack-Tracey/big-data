import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation

ball = None
obstacle = None
ax = None
pos = []
hits = []
tarhits = []


def init():
    ball.center = (0, 0)
    obstacle.center = (-15, 0)
    target.center = (-15, 0)
    ax.add_patch(ball)
    ax.add_patch(obstacle)
    ax.add_patch(target)
    return []

def animate_ball(i):
    ball.center = pos[i]
    return ball,

def animate_obstacle(i):
    if(hits[i]==1):
        obstacle.center = pos[i]
    return obstacle,

def animate_target(i):
    if(tarhits[i]==1):
        target.center = pos[i]
        print("is")
    return target,

def animateAll(i):
    animate_ball(i)
    animate_obstacle(i)
    animate_target(i)
    return []


def runAnimation(positions, hitsarray, targethits):
    global ball, obstacle, target, ax, pos, hits, tarhits
    pos = positions
    hits = hitsarray
    tarhits = targethits

    fig = plt.figure()
    fig.set_dpi(100)
    fig.set_size_inches(7, 6.5)
    ax = plt.axes(xlim=(0, 1000), ylim=(0, 1000))

    ball = plt.Circle((5, -5), 20, fc='black')
    obstacle = plt.Circle((5, -5), 20, fc='r')
    target = plt.Circle((5, -5), 20, fc='g')

    anim = animation.FuncAnimation(fig, animateAll,
                                   init_func=init,
                                   frames=len(positions),
                                   interval=20,
                                   blit=True)

    plt.show()
