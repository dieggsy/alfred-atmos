'''atmos.py [options] [args]
Usage:
    atmos.py <query>
'''
import sys
from workflow import Workflow
import re
import os
import numpy as np
from math import exp,sqrt

def atmoslapse(h,g,gamma,R,L,hts,htp,rho0,P0,T0,*args):
    h=np.array(h)
    T=np.zeros(len(h))
    expon=np.zeros(len(h))
    if len(args)>1:
        return 'Too many args'

    if len(args)==1:
        H0=args[0]
    else:
        H0=0

    for i in range(len(h)-1,-1,-1):
        if h[i]>htp:
            h[i]=htp

        if h[i]<H0:
            h[i]=H0

        if h[i] > hts:
            T[i] = T0 - L*hts
            expon[i] = exp(g/(R*T[i])*(hts-h[i]))

        else:
            T[i]=T0-L*h[i]
            expon[i]=1.0

    a=(T*gamma*R)**(1/2.)
    theta=T/T0
    P=P0*theta**(g/(L*R))*expon
    rho=rho0*theta**((g/(L*R))-1.0)*expon
    return(T,a,P,rho)

def atmosisa(h):
    return atmoslapse([h],9.80665,1.4,287.0531,0.0065,11000.,20000.,
                      1.225,101325.,288.15)

def main(wf):
    from docopt import docopt
    args=docopt(__doc__,wf.args)
    query=args.get('<query>')
    try:
        if query[-2:]=='ft':
            vals=atmosisa(float(query[:-2])*.3048)
        elif query[-1:]=='f':
            vals=atmosisa(float(query[:-1]))
        else:
            vals=atmosisa(float(query))
    
        wf.add_item(str(vals[0][0]),icon='T.png')
        wf.add_item(str(vals[1][0]),icon='a.png')
        wf.add_item(str(vals[2][0]),icon='P.png')
        wf.add_item(str(+vals[3][0]),icon='rho.png')
    except:
        wf.add_item('Lol, wat?',icon='icon.png')
    wf.send_feedback()


if __name__==u"__main__":
    wf=Workflow()
    sys.exit(wf.run(main))
