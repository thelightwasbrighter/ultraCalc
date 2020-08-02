from scipy.interpolate import interp1d
from scipy.misc import derivative
from numpy import unwrap
from functools import partial
import gpxpy
from gpxpy.gpx import mod_geo
import math

with open('sample.gpx','r') as gpx_file:
#with open('minisample.gpx','r') as gpx_file:
    points = gpxpy.parse(gpx_file).walk()
points = list(map(lambda t: t[0],points))

segs = tuple(zip(points[:-1],points[1:]))

courses = map(lambda s: math.radians(s[0].course_between(s[1])),segs)

#elevation linear interpolation
acc = 0.0
x=[0.0]
elev=[points[0].elevation]
course = []
for a,b in segs:
    dist = a.distance_2d(b)
    if dist>0:
        acc += dist
        x.append(acc)
        elev.append(b.elevation)
        course.append(math.radians(a.course_between(b)))

course = unwrap(course)

f_elev = interp1d(x,elev,bounds_error=False,fill_value='extrapolate',kind='cubic',assume_sorted=True)
f_grad = partial(derivative,f_elev)
f_course = interp1d(x[:-1],course,bounds_error=False,fill_value='extrapolate',kind='previous',assume_sorted=True)
f_curve = partial(derivative,f_course)
