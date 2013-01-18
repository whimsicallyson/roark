from math import log

def g_1(ratio):
    choice = {1.000: 0.000,
              0.900: 0.098580346,
              0.800: 0.19478465,
              0.750: 0.2423283,
              0.700: 0.2897871,
              0.667: 0.3215349,
              0.600: 0.3858887,
              0.500: 0.487773,
              0.400: 0.605736,
              0.333: 0.704699,
              0.300: 0.765608,
              0.250: 0.881523,
              0.200: 1.049227,
              0.125: 1.547080,
              0.100: 1.882168,
              0.050: 3.588611}
    return choice[ratio]
def g_2(ratio):
    choice = {1.000: 0.000,
              0.900: 0.004828991,
              0.800: 0.01859406,
              0.750: 0.0284644,
              0.700: 0.0401146,
              0.667: 0.0487855,
              0.600: 0.0680514,
              0.500: 0.100857,
              0.400: 0.136697,
              0.333: 0.161188,
              0.300: 0.173321,
              0.250: 0.191053,
              0.200: 0.207811,
              0.125: 0.229848,
              0.100: 0.235987,
              0.050: 0.245630}
    return choice[ratio]
def g_3(ratio):
    choice = {1.000: 0.000,
              0.900: 0.000158070,
              0.800: 0.00119108,
              0.750: 0.0022506,
              0.700: 0.0037530,
              0.667: 0.0050194,
              0.600: 0.0082084,
              0.500: 0.014554,
              0.400: 0.022290,
              0.333: 0.027649,
              0.300: 0.030175,
              0.250: 0.033465,
              0.200: 0.035691,
              0.125: 0.035236,
              0.100: 0.033390,
              0.050: 0.025072}
    return choice[ratio]
def g_4(ratio):
    choice = {1.000: 1.000,
              0.900: 0.973888889,
              0.800: 0.95750000,
              0.750: 0.9541667,
              0.700: 0.9550000,
              0.667: 0.9583333,
              0.600: 0.9733333,
              0.500: 1.025000,
              0.400: 1.135000,
              0.333: 1.266667,
              0.300: 1.361667,
              0.250: 1.562500,
              0.200: 1.880000,
              0.125: 2.881250,
              0.100: 3.565000,
              0.050: 7.032500}
    return choice[ratio]
def g_5(ratio):
    choice = {1.000: 0.000,
              0.900: 0.095000000,
              0.800: 0.18000000,
              0.750: 0.2187500,
              0.700: 0.2550000,
              0.667: 0.2777778,
              0.600: 0.3200000,
              0.500: 0.375000,
              0.400: 0.420000,
              0.333: 0.444444,
              0.300: 0.455000,
              0.250: 0.468750,
              0.200: 0.480000,
              0.125: 0.492187,
              0.100: 0.495000,
              0.050: 0.498750}
    return choice[ratio]
def g_6(ratio):
    choice = {1.000: 0.000,
              0.900: 0.004662232,
              0.800: 0.01725742,
              0.750: 0.0258495,
              0.700: 0.0355862,
              0.667: 0.0425624,
              0.600: 0.0572477,
              0.500: 0.079537,
              0.400: 0.099258,
              0.333: 0.109028,
              0.300: 0.112346,
              0.250: 0.114693,
              0.200: 0.112944,
              0.125: 0.099203,
              0.100: 0.090379,
              0.050: 0.062425}
    return choice[ratio]
def g_7(ratio):
    choice = {1.000: 0.000,
              0.900: 0.096055556,
              0.800: 0.20475000,
              0.750: 0.2654167,
              0.700: 0.3315000,
              0.667: 0.3791667,
              0.600: 0.4853333,
              0.500: 0.682500,
              0.400: 0.955500,
              0.333: 1.213333,
              0.300: 1.380167,
              0.250: 1.706250,
              0.200: 2.184000,
              0.125: 3.583125,
              0.100: 4.504500,
              0.050: 9.077250}
    return choice[ratio]
def g_8(ratio):
    choice = {1.000: 1.000,
              0.900: 0.933500000,
              0.800: 0.8740000,
              0.750: 0.8468750,
              0.700: 0.8215000,
              0.667: 0.8055556,
              0.600: 0.7760000,
              0.500: 0.737500,
              0.400: 0.706000,
              0.333: 0.688889,
              0.300: 0.681500,
              0.250: 0.671875,
              0.200: 0.664000,
              0.125: 0.655469,
              0.100: 0.653500,
              0.050: 0.650875}
    return choice[ratio]
def g_9(ratio):
    choice = {1.000: 0.000,
              0.900: 0.091560902,
              0.800: 0.16643465,
              0.750: 0.1976669,
              0.700: 0.2247621,
              0.667: 0.2405164,
              0.600: 0.2664220,
              0.500: 0.290898,
              0.400: 0.297036,
              0.333: 0.289885,
              0.300: 0.282550,
              0.250: 0.266288,
              0.200: 0.242827,
              0.125: 0.190488,
              0.100: 0.166993,
              0.050: 0.106089}
    return choice[ratio]
def g_11(ratio):
    choice = {1.000: 0.000,
              0.900: 0.000003996,
              0.800: 0.00006104,
              0.750: 0.0001453,
              0.700: 0.0002935,
              0.667: 0.0004391,
              0.600: 0.0008752,
              0.500: 0.001999,
              0.400: 0.003833,
              0.333: 0.005499,
              0.300: 0.006463,
              0.250: 0.008057,
              0.200: 0.009792,
              0.125: 0.012489,
              0.100: 0.013350,
              0.050: 0.003872}
    return choice[ratio]
def g_12(ratio):
    choice = {1.000: 0.000,
              0.900: 0.000000805,
              0.800: 0.00001240,
              0.750: 0.0000297,
              0.700: 0.0000603,
              0.667: 0.0000905,
              0.600: 0.0001820,
              0.500: 0.000422,
              0.400: 0.000827,
              0.333: 0.001208,
              0.300: 0.001435,
              0.250: 0.001822,
              0.200: 0.002266,
              0.125: 0.003027,
              0.100: 0.003302,
              0.050: 0.003872}
    return choice[ratio]
def g_13(ratio):
    choice = {1.000: 0.000,
              0.900: 0.000000270,
              0.800: 0.00000418,
              0.750: 0.0000100,
              0.700: 0.0000205,
              0.667: 0.0000308,
              0.600: 0.0000623,
              0.500: 0.000146,
              0.400: 0.000289,
              0.333: 0.000427,
              0.300: 0.000510,
              0.250: 0.000654,
              0.200: 0.000822,
              0.125: 0.001121,
              0.100: 0.001233,
              0.050: 0.001474}
    return choice[ratio]
def g_14(ratio):
    choice = {1.000: 0.000,
              0.900: 0.000158246,
              0.800: 0.00119703,
              0.750: 0.0022693,
              0.700: 0.0038011,
              0.667: 0.0051026,
              0.600: 0.0084257,
              0.500: 0.015272,
              0.400: 0.024248,
              0.333: 0.031211,
              0.300: 0.034904,
              0.250: 0.040595,
              0.200: 0.046306,
              0.125: 0.054362,
              0.100: 0.056737,
              0.050: 0.060627}
    return choice[ratio]
def g_15(ratio):
    choice = {1.000: 0.000,
              0.900: 0.000039985,
              0.800: 0.00030618,
              0.750: 0.0005844,
              0.700: 0.0009861,
              0.667: 0.0013307,
              0.600: 0.0022227,
              0.500: 0.004111,
              0.400: 0.006691,
              0.333: 0.008790,
              0.300: 0.009945,
              0.250: 0.011798,
              0.200: 0.013777,
              0.125: 0.016917,
              0.100: 0.017991,
              0.050: 0.020139}
    return choice[ratio]
def g_16(ratio):
    choice = {1.000: 0.000,
              0.900: 0.000016107,
              0.800: 0.00012431,
              0.750: 0.0002383,
              0.700: 0.0004039,
              0.667: 0.0005468,
              0.600: 0.0009196,
              0.500: 0.001721,
              0.400: 0.002840,
              0.333: 0.003770,
              0.300: 0.004290,
              0.250: 0.005138,
              0.200: 0.006065,
              0.125: 0.007589,
              0.100: 0.008130,
              0.050: 0.009252}
    return choice[ratio]
def g_17(ratio):
    choice = {1.000: 0.000,
              0.900: 0.004718219,
              0.800: 0.01775614,
              0.750: 0.0268759,
              0.700: 0.0374539,
              0.667: 0.0452137,
              0.600: 0.0621534,
              0.500: 0.090166,
              0.400: 0.119723,
              0.333: 0.139340,
              0.300: 0.148888,
              0.250: 0.162637,
              0.200: 0.175397,
              0.125: 0.191795,
              0.100: 0.196271,
              0.050: 0.203191}
    return choice[ratio]
def g_18(ratio):
    choice = {1.000: 0.000,
              0.900: 0.001596148,
              0.800: 0.00610470,
              0.750: 0.0093209,
              0.700: 0.0131094,
              0.667: 0.0159275,
              0.600: 0.0221962,
              0.500: 0.032948,
              0.400: 0.044939,
              0.333: 0.053402,
              0.300: 0.057723,
              0.250: 0.064263,
              0.200: 0.070816,
              0.125: 0.080511,
              0.100: 0.083666,
              0.050: 0.089788}
    return choice[ratio]
def g_19(ratio):
    choice = {1.000: 0.000,
              0.900: 0.000805106,
              0.800: 0.00310827,
              0.750: 0.0047694,
              0.700: 0.0067426,
              0.667: 0.0082212,
              0.600: 0.0115422,
              0.500: 0.017341,
              0.400: 0.023971,
              0.333: 0.028769,
              0.300: 0.031261,
              0.250: 0.035098,
              0.200: 0.039031,
              0.125: 0.045057,
              0.100: 0.047086,
              0.050: 0.051154}
    return choice[ratio]

def f_1(v,b,r):
    x = (1+v)/2*(b/r)*log(r/b)
    y = (1-v)/4*(r/b-b/r)
    return x+y
def f_2(v,b,r):
    x = 1-(b/r)**2*(1+2*log(r/b))
    return .25*x
def f_3(v,b,r):
    x = ((b/r)**2+1)*log(r/b)
    y = (b/r)**2-1
    return b/(4*r)*(x+y)
def f_4(v,b,r):
    x = (1+v)*(b/r)
    y = (1-v)*(r/b)
    return .5*(x+y)
def f_5(v,b,r):
    x = 1-(b/r)**2
    return .5*x
def f_6(v,b,r):
    x = (b/r)**2-1+2*log(r/b)
    return b/(4*r)*x
def f_7(v,b,r):
    x = 1-v**2
    y = (r/b)-(b/r)
    return .5*x*y
def f_8(v,b,r):
    x = 1+v+(1-v)*(b/r)**2
    return .5*x
def f_9(v,b,r):
    x = (1+v)/2*log(r/b)
    y = (1-v)/4*(1-(b/r)**2)
    return b/r*(x+y)

def c_1(v,b,a):
    return f_1(v,b,a)
def c_2(v,b,a):
    return f_2(v,b,a)
def c_3(v,b,a):
    return f_3(v,b,a)
def c_4(v,b,a):
    return f_4(v,b,a)
def c_5(v,b,a):
    return f_5(v,b,a)
def c_6(v,b,a):
    return f_6(v,b,a)
def c_7(v,b,a):
    return f_7(v,b,a)
def c_8(v,b,a):
    return f_8(v,b,a)
def c_9(v,b,a):
    return f_9(v,b,a)

def l_1(v,r,a):
    x = (1+v)/2*(r/a)*log(r/a)
    y = (1-v)/4*(a/r-r/a)
    return x+y
def l_2(v,r,a):
    x = 1-(r/a)**2*(1+2*log(a/r))
    return .25*x
def l_3(v,r,a):
    x = ((r/a)**2+1)*log(a/r)
    y = (r/a)**2
    return r/(4*a)*(x+y-1)
def l_4(v,r,a):
    x = (1+v)*(r/a)
    y = (1-v)*(a/r)
    return .5*(x+y)
def l_5(v,r,a):
    x = 1-(r/a)**2
    return .5*x
def l_6(v,r,a):
    x = (r/a)**2-1+2*log(a/r)
    return r/(4*a)*x
def l_7(v,r,a):
    x = 1-v**2
    y = (a/r)-(r/a)
    return .5*x*y
def l_8(v,r,a):
    x = 1+v+(1-v)*(r/a)**2
    return .5*x
def l_9(v,r,a):
    x = (1+v)/2*log(a/r)
    y = (1-v)/4*(1-(r/a)**2)
    return r/a*(x+y)
def l_11(v,r,a):
    x = 4*(r/a)**2*(2+(r/a)**2)*log(a/r)
    y = 1+4*(r/a)**2-5*(r/a)**4-x
    return (1/64.0)*y
def l_12(v,r,a):
    x = 60*(r/a)**3*(3*(r/a)**2+10)*log(a/r)
    y = 64-225*(r/a)-100*(r/a)**3+261*(r/a)**5+x
    z = a/(14400*(a-r)**2)
    return z*y
def l_13(v,r,a):
    x = 60*(r/a)**4*(5+(r/a)**2)*log(a/r)
    y = 25-128*(r/a)+225*(r/a)**2-25*(r/a)**4-97*(r/a)**6-x
    z = a**2/(14400*(a-r)**2)
    return z*y
def l_14(v,r,a):
    x = 4*(r/a)**2*log(a/r)
    y = 1-(r/a)**4-x
    return (1/16.0)*y
def l_15(v,r,a):
    x = 20*(r/a)**3*(1+3*log(a/r))
    y = 16-45*(r/a)+9*(r/a)**5+x
    z = a/(720*(a-r))
    return z*y
def l_16(v,r,a):
    x = 5*(r/a)**4*(7+12*log(a/r))
    y = 15-64*(r/a)+90*(r/a)**2-6*(r/a)**6-x
    z = a**2/(1440*(a-r)**2)
    return z*y
def l_17(v,r,a):
    x = (1-v)/4*(1-(r/a)**4)
    y = (r/a)**2*(1+(1+v)*log(a/r))
    return 0.25*(1-x-y)
def l_18(v,r,a):
    x = (20*(r/a)**3+16)*(4+v)
    y = 45*(r/a)*(3+v)
    z = 9*(r/a)**5*(1-v)
    w = 60*(r/a)**3*(1+v)*log(a/r)
    f = a/(720*(a-r))
    return f*(x-y-z+w)
def l_19(v,r,a):
    x = 64*(r/a)*(4+v)
    y = 90*(r/a)**2*(3+v)
    z = 5*(r/a)**4*(19+7*v)
    w = 6*(r/a)**6*(1-v)
    u = 60*(r/a)**4*(1+v)*log(a/r)
    f = a**2/(1440*(a-r)**2)
    return f*(15*(5+v)-x+y-z+w-u)

def d_(v,e,t):
    x = e*t**3
    y = 12*(1-v**2)
    return x/y
