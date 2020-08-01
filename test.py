#!/usr/bin/env python3

import numpy as np
import matplotlib
import matplotlib.pyplot as plt

from physics import *
import gpx,ode
from cyclist import Cyclist

cs = [Cyclist(86+18,
              180,
              0.4,
              0.003448,
              0.95),
      Cyclist(86+18,
              180,
              0.4,
              0.007,
              0.95),
      Cyclist(86+18,
              180,
              0.42,
              0.007,
              0.95)
]

x = 0.0
for a,b in gpx.segs:
    dist = a.distance_2d(b)

def remaining_dist(t,y):
    return gpx.x[-1]-y[1]
remaining_dist.terminal = True
    
y0 = [1e-99,0.0]
t0 = 0.0
tf = 365*24*3600.0
t_span = (t0,tf)
t_eval = np.linspace(t0,tf,num=int(tf))
rs = map(lambda c: ode.cyclist_solver(c)(t_span,y0,t_eval=t_eval,method='RK23',events=remaining_dist), cs)

#grad=[gpx.f_grad(x)*100 for x in r[0].y[1]]

for r in rs:
    #plt.plot(list(map(lambda t:t/3600,r.t)),list(map(lambda v:v*3.6,r.y[0])))
    plt.plot(list(map(lambda t:t/3600,r.t)),list(map(lambda x:x/1000,r.y[1])))

#plt.plot(r.t,r.y[1])
#plt.plot(r[0].t,grad)
plt.show()
