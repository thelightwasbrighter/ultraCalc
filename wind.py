from math import degrees

class Wind():
    def __init__(self,v,d):
        self.v = v
        self.d = d

    def __str__(self):
        return 'Wind: {}m/s, {}deg'.format(round(self.v,1),round(degrees(self.d),0))

