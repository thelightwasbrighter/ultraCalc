import math
from functools import partial

from physics import *
from scipy.integrate import solve_ivp


# dx/dt = v
def dxdt(v,x):
    return v

def solver(cyclist,wind,route):
    # dv/dt = Fres / m
    def dvdt(v,x):
        G = route.f_grad(x)
        d_cyc = route.f_course(x)
        a = Fres(cyclist.power(G,v),
                 cyclist.crr,
                 cyclist.cda(v,d_cyc,wind.v,wind.d,G),
                 G,
                 cyclist.mass,
                 rho,
                 v,
                 d_cyc,
                 wind.v,
                 wind.d,
                 cyclist.Pbrake(v)) / cyclist.mass
        return a
        
    def fun(t,y):
        return (dvdt(*y),dxdt(*y))

    return partial(solve_ivp,fun)
    
