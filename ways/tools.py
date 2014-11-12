# -*- coding: utf-8 -*-
from __future__ import print_function, division
from time import clock
import zlib
'General tools'

DB_DIRNAME = 'db/'


def set_db_for_test():
    global DB_DIRNAME
    DB_DIRNAME = '../db/'

'This is arbitrary, and will change in the tests'
SEED = 0x23587643

def dhash(*data):
    'Generates a random-looking deterministic hash'
    return abs(zlib.adler32(str(data)*100) * SEED % 0xffffffff)


def dbopen(fname, *args, **kwargs):
    'make sure we are in the correct directory'
    if not fname.startswith(DB_DIRNAME):
        fname = DB_DIRNAME + fname
    return open(fname, *args, **kwargs)


'DMS := Degrees, Minutes, Seconds'
def float2dms(decimal_degrees):
    degrees = int(decimal_degrees)
    minutes = int(60 * (decimal_degrees - degrees))
    seconds = int(3600 * (decimal_degrees - degrees - minutes / 60))
    return (degrees, minutes, seconds)


def dms2float(degrees, minutes, seconds=0):
    return degrees + minutes / 60 + seconds / 3600


def compute_distance(lat1, lon1, lat2, lon2):
    '''computes distance in KM'''
    # for better performance, move the import outside: 
    from math import sin, cos, acos, radians, pi
    '''
    This code was borrowed from 
    http://www.johndcook.com/python_longitude_latitude.html
    '''
    if (lat1, lon1) == (lat2, lon2):
        return 0.0
    if max(abs(lat1 - lat2), abs(lon1 - lon2)) < 0.00001:
        return 0.001

    phi1 = radians(90 - lat1)
    phi2 = radians(90 - lat2)
    
    meter_units_factor = 40000 / (2 * pi)
    arc = acos(sin(phi1) * sin(phi2) * cos(radians(lon1) - radians(lon2))
             + cos(phi1) * cos(phi2))
    return arc * meter_units_factor


class Everything(object):
    '(Lousy) complement for the empty set'
    def __contains__(self, val):
        return True


def timed(f):
    '''decorator for printing the timing of functions
    usage: 
    @timed
    def some_funcion(args...):'''
    
    def wrap(*x, **d):
        start = clock()
        res = f(*x, **d)
        print(f.__name__, ':', clock() - start)
        return res
    return wrap


if __name__ == '__main__':
    for i in range(100):
        print(dhash(i))
