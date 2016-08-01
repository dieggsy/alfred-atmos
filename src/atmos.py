#!/usr/bin/env python
# encoding: utf-8
#
# Copyright © 2016 Diego A. Mundo <diegoamundo@gmail.com>
#
# MIT Licence. See http://opensource.org/licenses/MIT
#
# Created on 2016-07-29
#

"""
Output temperature, speed of sound, pressure, and density according to ISA.
"""
import sys
from workflow import Workflow
import re
import numpy as np
from math import exp


def atmoslapse(h, g, gamma, R, L, hts, htp, rho0, P0, T0, *args):
    h = np.array(h)
    T = np.zeros(len(h))
    expon = np.zeros(len(h))
    if len(args) > 1:
        return 'Too many args'

    if len(args) == 1:
        H0 = args[0]
    else:
        H0 = 0

    for i in range(len(h)-1, -1, -1):
        if h[i] > htp:
            h[i] = htp

        if h[i] < H0:
            h[i] = H0

        if h[i] > hts:
            T[i] = T0 - L*hts
            expon[i] = exp(g/(R*T[i])*(hts-h[i]))

        else:
            T[i] = T0-L*h[i]
            expon[i] = 1.0

    a = (T*gamma*R)**(1/2.)
    theta = T/T0
    P = P0*theta**(g/(L*R))*expon
    rho = rho0*theta**((g/(L*R))-1.0)*expon
    return(T, a, P, rho)


def atmosisa(h):
    return atmoslapse([h], 9.80665, 1.4, 287.0531, 0.0065, 11000., 20000.,
                      1.225, 101325., 288.15)


def main(wf):
    query = wf.args[0]
    try:
        if re.search('ft$|f$', query, flags = re.I):
            query = re.sub('[^\d.]', '', query, flags=re.I)
            vals = atmosisa(float(query)*.3048)
        else:
            query = re.sub('[^\d.]', '', query, flags=re.I)
            vals = atmosisa(float(query))

        wf.add_item(str(vals[0][0])+' K', icon='T.png',
                    arg=str(vals[0][0]), valid=True)
        wf.add_item(str(vals[1][0])+' m/s', icon='a.png',
                    arg=str(vals[1][0]), valid=True)
        wf.add_item(str(vals[2][0])+' Pa', icon='P.png',
                    arg=str(vals[2][0]), valid=True)
        wf.add_item(str(+vals[3][0])+' kg/m^3', icon='rho.png',
                    arg=str(vals[3][0]), valid=True)
    except:
        wf.add_item('Incorrect input', icon='icon.png')
    wf.send_feedback()


if __name__ == "__main__":
    wf = Workflow()
    sys.exit(wf.run(main))
