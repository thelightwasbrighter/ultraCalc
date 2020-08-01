from scipy.interpolate import interp1d
from scipy.misc import derivative
from functools import partial
import gpxpy
from gpxpy.gpx import mod_geo

with open('sample.gpx','r') as gpx_file:
    points = gpxpy.parse(gpx_file).walk()
points = list(map(lambda t: t[0],points))

segs = tuple(zip(points[:-1],points[1:]))

#elevation linear interpolation
acc = 0.0
x=[0.0]
y=[points[0].elevation]
for a,b in segs:
    dist = a.distance_2d(b)
    if dist>0:
        acc += dist
        x.append(acc)
        y.append(b.elevation)

f_elev = interp1d(x,y,bounds_error=False,fill_value='extrapolate',kind='cubic')
f_grad = partial(derivative,f_elev)
