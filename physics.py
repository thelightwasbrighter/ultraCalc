import math

g   = 9.81
rho = 1.275

def Cda(Cd,A):
    return Cd*A

def Frr(Crr,G,m):
    return Crr*math.cos(math.atan(G))*m*g

def Fgrav(G,m):
    return math.sin(math.atan(G))*m*g

def Fbrake(Pbrake,v):
    return min(1e5,abs(Pbrake/v))

def Fda(Cda,rho,v_cyc,d_cyc,v_win,d_win):
    #wind direction
    a = d_cyc-d_win
    #apparent wind speed
    w = math.sqrt((v_cyc+v_win*math.cos(a))**2+(v_win*math.sin(a))**2)
    #apparent wind direction
    b = math.acos((v_cyc+(v_win*math.cos(a)))/w)
    return 0.5*Cda*rho*w**2*math.cos(b)

def Fbwd(Crr,Cda,G,m,rho,v_cyc,d_cyc,v_win,d_win,Pbrake):
    return Frr(Crr,G,m) + Fgrav(G,m) + Fda(Cda,rho,v_cyc,d_cyc,v_win,d_win) + Fbrake(Pbrake,v_cyc)

def Ffwd(Pfwd,v):
    return min(1e5,abs(Pfwd/v))

def Fres(Pfwd,Crr,Cda,G,m,rho,v_cyc,d_cyc,v_win,d_win,Pbrake):
    return Ffwd(Pfwd,v_cyc)-Fbwd(Crr,Cda,G,m,rho,v_cyc,d_cyc,v_win,d_win,Pbrake)


    
