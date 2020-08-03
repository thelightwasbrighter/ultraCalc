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
        a = Fres(cyclist.grad_power(G),
                 cyclist.crr,
                 cyclist.v_cda(v),
                 G,
                 cyclist.mass,
                 rho,
                 v,
                 route.f_course(x),
                 wind.v,
                 wind.d,
                 cyclist.Pbrake(route.f_curve(x),v)) / cyclist.mass
        return a
        
    def fun(t,y):
        return (dvdt(*y),dxdt(*y))

    return partial(solve_ivp,fun)
    
