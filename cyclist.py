class Cyclist():
    def __init__(self,mass,P,cda,crr,dte,vmax=50/3.6,PbrakeMax=2000):
        self.mass = mass
        self.P   = P
        self.cda = cda
        self.crr = crr
        self.dte = dte
        self.vmax = vmax
        self.PbrakeMax = PbrakeMax

    def Pbrake(self,v):
        #curve braking
        #p_crv = self.PbrakeMax*max(0,v)*max(0,abs(bend)-0.2)
        #max speed braking
        p_vmx = max(0,self.PbrakeMax*(v-self.vmax))

        #return p_crv+p_vmx
        return p_vmx

        
    def v_cda(self,v):
        if v<15/3.6:
            return self.cda*1.1
        elif v<30/3.6:
            return self.cda
        else:
            return self.cda*0.9
        
    def power(self,G):
        a=0.05 #threshhold gradient
        b=0.25 #uphill power boost
        if G<-a:
            p=0
        elif G<0:
            p=(G+a)/a*self.P
        elif G<a:
            p=self.P*(1+G/a*b)
        else:
            p=self.P*(1+b)
        return self.dte*p

    def __str__(self):
        return "Cyclist: {}kg, {}W, cda{}, crr{}, dte{}, vmax{}m/s, Pbrake{}W".format(round(self.mass,0),round(self.P,0),round(self.cda,2),round(self.crr,4),round(self.dte,2),round(self.vmax,2),round(self.PbrakeMax,0))

