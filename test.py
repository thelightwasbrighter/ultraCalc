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
gpx_files = ['sample.gpx']

cs = [Cyclist(85+24,
              175,
              0.40,
              0.003448,
              0.95,
              55/3.6,
              3000)
]

ws = [Wind(v/3.6,math.radians(d)) for v,d in [(15,160)]]

routes = map(gpx.Route,gpx_files)

experiments = tuple(itertools.product(cs,ws,routes))


    
y0 = [1e-99,0.0]
t0 = 0.0
tf = 10*24*3600.0
t_span = (t0,tf)
t_eval = np.linspace(t0,tf,num=int(tf))

def solve(arg):
    cyclist,wind,route = arg
    def remaining_dist(t,y):
        return route.x_end-y[1]
    remaining_dist.terminal = True
    return ode.solver(cyclist,wind,route)(t_span,y0,t_eval=t_eval,method='RK23',events=remaining_dist)

with Pool(CORES) as p:
    rs = p.map(solve, experiments)

for e,r in zip(experiments,rs):
    #speed over distance
    #plt.plot(list(map(lambda x:x/1000,r.y[1])),list(map(lambda x:x*3.6,r.y[0])),label=' | '.join(map(str,e)))
    #plt.plot(list(map(lambda x:x,r.t)),list(map(lambda y:y[0]*route.f_curve(y[1]),zip(*r.y))),label=' | '.join('curve*speed'))
    #speed over time
    #plt.plot(list(map(lambda t:t/3600,r.t)),list(map(lambda x:x*3.6,r.y[0])),label=' | '.join(map(str,e)))
    #distance over time
    plt.plot(list(map(lambda t:t/3600,r.t)),list(map(lambda x:x/1000,r.y[1])),label=' | '.join(map(str,e)))

#plt.plot(r.t,r.y[1])
#plt.plot(r[0].t,grad)
plt.legend(loc='best')
plt.show()
