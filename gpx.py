import gpxpy
from gpxpy.gpx import mod_geo

with open('sample.gpx','r') as gpx_file:
    points = gpxpy.parse(gpx_file).walk()
points = list(map(lambda t: t[0],points))

segs = tuple(zip(points[:-1],points[1:]))
lens = tuple(map(mod_geo.length_2d,segs))






