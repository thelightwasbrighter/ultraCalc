from scipy.interpolate import interp1d
from scipy.misc import derivative
from numpy import unwrap
from functools import partial
import gpxpy
from gpxpy.gpx import mod_geo
import math


class Route():
    def __init__(self,gpx_file):
        with open(gpx_file,'r') as fh:
            points_ = gpxpy.parse(fh).walk()

        self.points = list(map(lambda t: t[0],points_))

        #point to point connections
        self.segs = tuple(zip(self.points[:-1],self.points[1:]))

        #correlate distance with other data
        acc = 0.0
        x=[0.0]
        elev=[self.points[0].elevation]
        course = []
        for a,b in self.segs:
            dist = a.distance_2d(b)
            if dist>0:
                acc += dist
                x.append(acc)
                elev.append(b.elevation)
                course.append(math.radians(a.course_between(b)))

        #unwrap course for interpolation (modulo 2pi)
        course = unwrap(course)

        self.f_elev = interp1d(x,elev,bounds_error=False,fill_value='extrapolate',kind='cubic',assume_sorted=True)
        self.f_grad = partial(derivative,self.f_elev)
        self.f_course = interp1d(x[:-1],course,bounds_error=False,fill_value='extrapolate',kind='previous',assume_sorted=True)
        self.f_curve = partial(derivative,self.f_course)

        self.x_end = x[-1]
    
