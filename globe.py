""" Globe """

import math
import random

_RADIUS = 6371000


def distance(lat1, lon1, lat2, lon2):
    lat1, lon1 = latlon2sc(lat1, lon1)
    lat2, lon2 = latlon2sc(lat2, lon2)

    dlon = lon2 - lon1
    c_lat1 = math.cos(lat1)
    c_lat2 = math.cos(lat2)
    s_lat1 = math.sin(lat1)
    s_lat2 = math.sin(lat2)
    s_dlon = math.sin(dlon)
    c_dlon = math.cos(dlon)

    t1 = c_lat2 * s_dlon
    t2 = c_lat1 * s_lat2
    t3 = s_lat1 * c_lat2 * c_dlon
    t4 = s_lat1 * s_lat2
    t5 = c_lat1 * c_lat2 * c_dlon

    n = (t1 ** 2 + (t2 - t3) ** 2) ** 0.5
    d = t4 + t5

    return _RADIUS * math.atan2(n, d)


def average(lat1, lon1, lat2, lon2):
    t1, p1 = latlon2sc(lat1, lon1)
    t2, p2 = latlon2sc(lat2, lon2)
    
    x1 = math.sin(t1) * math.cos(p1)
    y1 = math.sin(t1) * math.sin(p1)
    z1 = math.cos(t1)

    x2 = math.sin(t2) * math.cos(p2)
    y2 = math.sin(t2) * math.sin(p2)
    z2 = math.cos(t2)

    x = (x1 + x2) / 2.0
    y = (y1 + y2) / 2.0
    z = (z1 + z2) / 2.0

    r = (x ** 2 + y ** 2 + z ** 2) ** 0.5
    t = math.acos(z / r)
    p = math.atan2(y, x)

    (lat, lon) = sc2latlon(t, p)
    
    return (lat, lon)
    

def latlon2sc(lat, lon):
    return (math.pi * (-lat + 90.0) / 180.0, math.pi * lon / 180.0)


def sc2latlon(t, p):
    return (90 - t * 180 / math.pi, p * 180 / math.pi)


def is_lat_valid(lat):
    return isinstance(lat, (float, int)) and -90.0 <= lat <= 90.0


def is_lon_valid(lon):
    return isinstance(lon, (float, int)) and -180.0 <= lon <= 180.0
        

def teleport(latitude, longitude, distance=None, seed=None):
    
    return (latitude, longitude)  # STUB
    
