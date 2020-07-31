#!/usr/bin/env python3

import numpy as np

from physics import *
import gpx,ode

y0 = [0.01,0]
t0 = 0.0
tf = 100.0
t_span = (t0,tf)
t_eval = np.linspace(t0,tf,num=10)

r = ode.solve_ivp(ode.fun,t_span,y0,t_eval=t_eval,method='RK23')

