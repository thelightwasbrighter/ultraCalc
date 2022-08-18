import math

PBRAKE = 3000

class Cyclist():
    def __init__(self,mass,P,cda,crr,dte,vmax=50/3.6,vth=0):
        self.mass = mass
        self.P   = P
        self.base_cda = cda
        self.crr = crr
        self.dte = dte
        self.vmax = vmax
        self.vth = vth

    def Pbrake(self,v):
        #curve braking
        #p_crv = self.PbrakeMax*max(0,v)*max(0,abs(bend)-0.2)
        #max speed braking
        p_vmx = max(0,PBRAKE*(v-self.vmax))

        #return p_crv+p_vmx
        return p_vmx

        
    def cda(self,v_cyc,d_cyc,v_win,d_win,G):
        if G>0.03:
            return self.base_cda*1.2
        elif G<-0.03:
            return self.base_cda*0.9
        #wind direction
        a = d_cyc-d_win
        #apparent wind speed
        w = math.sqrt((v_cyc+v_win*math.cos(a))**2+(v_win*math.sin(a))**2)
        #apparent wind direction
        b = math.acos((v_cyc+(v_win*math.cos(a)))/w)
        v = w*math.cos(b)
        if v<15/3.6:
            return self.base_cda*1.2
        elif v<30/3.6:
            return self.base_cda
        else:
            return self.base_cda*0.9
        
    def power(self,G,v):
        a=0.05 #threshhold gradient
        b=0.25 #uphill power boost
        if G<-a:
            if v>self.vth:
                p=0
            else:
                p = self.P
        elif G<0:
            if v>self.vth:
                p=(G+a)/a*self.P
            else:
                p = self.P
        elif G<a:
            p=self.P*(1+G/a*b)
        else:
            p=self.P*(1+b)
        return self.dte*p

    def __str__(self):
        return "Cyclist: {}kg, {}W, cda{}, crr{}, dte{}, vmax{}m/s, vth{}m/s".format(round(self.mass,0),round(self.P,0),round(self.base_cda,2),round(self.crr,4),round(self.dte,2),round(self.vmax,2),round(self.vth,2))

