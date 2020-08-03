#!/usr/bin/env python3
from multiprocessing import Pool
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import math
import itertools

from physics import *
import gpx,ode
from cyclist import Cyclist
from wind import Wind

CORES = 4
gpx_file = 'brocken.gpx'

cs = [Cyclist(88+14,
              120,
              0.39,
              0.0045,
              0.95),
      Cyclist(89+14,
              120,
              0.39,
              0.0045,
              0.95),
      Cyclist(88+14,
              130,
              0.39,
              0.0045,
              0.95),
]

ws = [Wind(v/3.6,math.radians(140)) for v in [10,15,20]]
      
experiments = tuple(itertools.product(cs,ws))

route = gpx.Route(gpx_file)

def remaining_dist(t,y):
    return route.x_end-y[1]
remaining_dist.terminal = True
    
y0 = [1e-99,0.0]
t0 = 0.0
tf = 365*24*3600.0
t_span = (t0,tf)
t_eval = np.linspace(t0,tf,num=int(tf))

def solve(arg):
    cyclist,wind = arg
    return ode.solver(cyclist,wind,route)(t_span,y0,t_eval=t_eval,method='RK23',events=remaining_dist)

with Pool(CORES) as p:
    rs = p.map(solve, experiments)

for e,r in zip(experiments,rs):
    #plt.plot(list(map(lambda t:t/3600,r.t)),list(map(lambda v:v*3.6,r.y[0])))
    plt.plot(list(map(lambda t:t/3600,r.t)),list(map(lambda x:x/1000,r.y[1])),label=' | '.join(map(str,e)))

#plt.plot(r.t,r.y[1])
#plt.plot(r[0].t,grad)
plt.legend(loc='best')
plt.show()
