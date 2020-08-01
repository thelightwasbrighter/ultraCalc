import math
from functools import partial

from physics import *
from scipy.integrate import solve_ivp
from gpx import f_grad

VMAX = 40/3.6

# dv/dt = Fres / m
# dx/dt = v

# dt/dv = m/Fres
# d^2t/dx^2 = m/Fres*d/dx
# dt/dx = 1/v

def dxdt(v,x):
    return v

def cyclist_solver(cyclist):
    def dvdt(v,x):
        G = f_grad(x)
        a = Fres(cyclist.grad_power(G),
                 cyclist.crr,
                 cyclist.v_cda(v),
                 G,
                 cyclist.mass,
                 rho,
                 v) / cyclist.mass
        if v>VMAX:
            return min(0,a)
        else:
            return a
        
    def fun(t,y):
        return (dvdt(*y),dxdt(*y))

    return partial(solve_ivp,fun)
    
