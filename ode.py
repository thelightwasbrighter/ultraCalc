from physics import *

import numpy as np
from cyclist import peter
from scipy.integrate import solve_ivp

# dv/dt = Fres / m
# dx/dt = v

def dvdt(v,x):
    return Fres(peter.p,peter.crr,peter.cda,0,peter.mass,1.225,v) / peter.mass

def dxdt(v,x):
    return v

def fun(t,y):
    v = y[0]
    x = y[1]
    return (dvdt(v,x),dxdt(v,x))


