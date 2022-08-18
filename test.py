#!/usr/bin/env python3
from multiprocessing import Pool
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import math
from itertools import product

from physics import *
import gpx,ode
from cyclist import Cyclist
from wind import Wind

CORES = 4
gpx_files = ['routes/taw2021.gpx']

cs = [Cyclist(86+14,
              175,
              0.39,
              0.003,
              0.95,
              40/3.6,
              35/3.6)]
      
ws = [Wind(v/3.6,math.radians(d)) for v,d in [(10,270),(15,270),(20,270)]]

routes = tuple(map(gpx.Route,gpx_files))

experiments = tuple(product(cs,ws,routes))
    
y0 = [0.1,0.0]
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
    #plt.plot(list(map(lambda x:x/1000,rs[0].y[1])),list(map(lambda x:100.0*routes[0].f_grad(x),rs[0].y[1])),label='gradient')
    #plt.plot(list(map(lambda x:x,r.t)),list(map(lambda y:y[0]*route.f_curve(y[1]),zip(*r.y))),label=' | '.join('curve*speed'))
    #speed over time
    #plt.plot(list(map(lambda t:t/3600,r.t)),list(map(lambda x:x*3.6,r.y[0])),label=' | '.join(map(str,e)))
    #distance over time
    plt.plot(list(map(lambda t:t/3600,r.t)),list(map(lambda x:x/1000,r.y[1])),label=' | '.join(map(str,e)))

#plt.plot(r.t,r.y[1])
#plt.plot(r[0].t,grad)
plt.legend(loc='best')
plt.show()
