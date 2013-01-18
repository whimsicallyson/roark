from  annularPlateEqs import *
from datetime import datetime

def promptFile1():
    #User Input Section for Intermediate Load

    load = None #w
    while load is None:
        try:
            load = float(raw_input("Annular Line Load (lb/in): "))
        except ValueError:
            print "Non-Numerical Input.  Try Again."
          
    length = None #r
    while length is None:
        try:
            length = float(raw_input("Location of Unit Line Load from Plate Center(in): "))
        except ValueError:
            print "Non-Numerical Input.  Try Again."

    radOut = None #a
    while radOut is None:
        try:
            radOut = float(raw_input("Outer Radius of Plate (in): "))
        except ValueError:
            print "Non-Numerical Input.  Try Again."

    radIn = None #b
    while radIn is None:
        try:
            radIn = float(raw_input("Inner Radius of Plate (in): "))
        except ValueError:
            print "Non-Numerical Input.  Try Again."

    poisson = None #v
    while poisson is None:
        try:
            poisson = float(raw_input("Poisson's Ratio of Material: "))
        except ValueError:
            print "Non-Numerical Input.  Try Again."

    modOfElas = None #E
    while modOfElas is None:
        try:
            modOfElas = float(raw_input("Modulus of Elasticity of Material (lb/in2): "))
        except ValueError:
            print "Non-Numerical Input.  Try Again."

    thick = None #t
    while thick is None:
        try:
            thick = float(raw_input("Thickness of Plate (in): "))
        except ValueError:
            print "Non-Numerical Input.  Try Again."

    return (load, length, radOut, radIn, poisson, modOfElas, thick)

def promptFile2():
    #User Input Section for Uniformly Distributed Pressure

    load = None #q
    while load is None:
        try:
            load = float(raw_input("Uniformly Distributed Pressure (lb/in): "))
        except ValueError:
            print "Non-Numerical Input.  Try Again."
          
    length = None #r
    while length is None:
        try:
            length = float(raw_input("Location of Start of Pressure Distribution from Plate Center(in): "))
        except ValueError:
            print "Non-Numerical Input.  Try Again."

    radOut = None #a
    while radOut is None:
        try:
            radOut = float(raw_input("Outer Radius of Plate (in): "))
        except ValueError:
            print "Non-Numerical Input.  Try Again."

    radIn = None #b
    while radIn is None:
        try:
            radIn = float(raw_input("Inner Radius of Plate (in): "))
        except ValueError:
            print "Non-Numerical Input.  Try Again."

    poisson = None #v
    while poisson is None:
        try:
            poisson = float(raw_input("Poisson's Ratio of Material: "))
        except ValueError:
            print "Non-Numerical Input.  Try Again."

    modOfElas = None #E
    while modOfElas is None:
        try:
            modOfElas = float(raw_input("Modulus of Elasticity of Material (lb/in2): "))
        except ValueError:
            print "Non-Numerical Input.  Try Again."

    thick = None #t
    while thick is None:
        try:
            thick = float(raw_input("Thickness of Plate (in): "))
        except ValueError:
            print "Non-Numerical Input.  Try Again."

    return (load, length, radOut, radIn, poisson, modOfElas, thick)


def promptFile3():
    #User Input Section for Uniformly Distributed Pressure

    load = None #q
    while load is None:
        try:
            load = float(raw_input("Maximum Distributed Pressure Load (lb/in): "))
        except ValueError:
            print "Non-Numerical Input.  Try Again."
          
    length = None #r
    while length is None:
        try:
            length = float(raw_input("Location of Start of Pressure Distribution from Plate Center(in): "))
        except ValueError:
            print "Non-Numerical Input.  Try Again."

    radOut = None #a
    while radOut is None:
        try:
            radOut = float(raw_input("Outer Radius of Plate (in): "))
        except ValueError:
            print "Non-Numerical Input.  Try Again."

    radIn = None #b
    while radIn is None:
        try:
            radIn = float(raw_input("Inner Radius of Plate (in): "))
        except ValueError:
            print "Non-Numerical Input.  Try Again."

    poisson = None #v
    while poisson is None:
        try:
            poisson = float(raw_input("Poisson's Ratio of Material: "))
        except ValueError:
            print "Non-Numerical Input.  Try Again."

    modOfElas = None #E
    while modOfElas is None:
        try:
            modOfElas = float(raw_input("Modulus of Elasticity of Material (lb/in2): "))
        except ValueError:
            print "Non-Numerical Input.  Try Again."

    thick = None #t
    while thick is None:
        try:
            thick = float(raw_input("Thickness of Plate (in): "))
        except ValueError:
            print "Non-Numerical Input.  Try Again."

    return (load, length, radOut, radIn, poisson, modOfElas, thick)


def promptFile4():
    #User Input Section for Parabolically Distributed Pressure

    load = None #q
    while load is None:
        try:
            load = float(raw_input("Maximum Distributed Pressure Load (lb/in): "))
        except ValueError:
            print "Non-Numerical Input.  Try Again."
          
    length = None #r
    while length is None:
        try:
            length = float(raw_input("Location of Start of Pressure Distribution from Plate Center(in): "))
        except ValueError:
            print "Non-Numerical Input.  Try Again."

    radOut = None #a
    while radOut is None:
        try:
            radOut = float(raw_input("Outer Radius of Plate (in): "))
        except ValueError:
            print "Non-Numerical Input.  Try Again."

    radIn = None #b
    while radIn is None:
        try:
            radIn = float(raw_input("Inner Radius of Plate (in): "))
        except ValueError:
            print "Non-Numerical Input.  Try Again."

    poisson = None #v
    while poisson is None:
        try:
            poisson = float(raw_input("Poisson's Ratio of Material: "))
        except ValueError:
            print "Non-Numerical Input.  Try Again."

    modOfElas = None #E
    while modOfElas is None:
        try:
            modOfElas = float(raw_input("Modulus of Elasticity of Material (lb/in2): "))
        except ValueError:
            print "Non-Numerical Input.  Try Again."

    thick = None #t
    while thick is None:
        try:
            thick = float(raw_input("Thickness of Plate (in): "))
        except ValueError:
            print "Non-Numerical Input.  Try Again."

    return (load, length, radOut, radIn, poisson, modOfElas, thick)

def promptFile5():
    #User Input Section for Uniform Line Moment

    moment = None #m
    while moment is None:
        try:
            moment = float(raw_input("Applied Moment (in-lb): "))
        except ValueError:
            print "Non-Numerical Input.  Try Again."
          
    length = None #r
    while length is None:
        try:
            length = float(raw_input("Distance to Applied Moment from Plate Center(in): "))
        except ValueError:
            print "Non-Numerical Input.  Try Again."

    radOut = None #a
    while radOut is None:
        try:
            radOut = float(raw_input("Outer Radius of Plate (in): "))
        except ValueError:
            print "Non-Numerical Input.  Try Again."

    radIn = None #b
    while radIn is None:
        try:
            radIn = float(raw_input("Inner Radius of Plate (in): "))
        except ValueError:
            print "Non-Numerical Input.  Try Again."

    poisson = None #v
    while poisson is None:
        try:
            poisson = float(raw_input("Poisson's Ratio of Material: "))
        except ValueError:
            print "Non-Numerical Input.  Try Again."

    modOfElas = None #E
    while modOfElas is None:
        try:
            modOfElas = float(raw_input("Modulus of Elasticity of Material (lb/in2): "))
        except ValueError:
            print "Non-Numerical Input.  Try Again."

    thick = None #t
    while thick is None:
        try:
            thick = float(raw_input("Thickness of Plate (in): "))
        except ValueError:
            print "Non-Numerical Input.  Try Again."

    return (moment, length, radOut, radIn, poisson, modOfElas, thick)


def promptFile6():
    #User Input Section for Externally Applied Slope Change

    theta = None #theta
    while theta is None:
        try:
            theta = float(raw_input("Applied Slope Change (rad): "))
        except ValueError:
            print "Non-Numerical Input.  Try Again."
          
    length = None #r
    while length is None:
        try:
            length = float(raw_input("Distance to Applied Slope Change from Plate Center(in): "))
        except ValueError:
            print "Non-Numerical Input.  Try Again."

    radOut = None #a
    while radOut is None:
        try:
            radOut = float(raw_input("Outer Radius of Plate (in): "))
        except ValueError:
            print "Non-Numerical Input.  Try Again."

    radIn = None #b
    while radIn is None:
        try:
            radIn = float(raw_input("Inner Radius of Plate (in): "))
        except ValueError:
            print "Non-Numerical Input.  Try Again."

    poisson = None #v
    while poisson is None:
        try:
            poisson = float(raw_input("Poisson's Ratio of Material: "))
        except ValueError:
            print "Non-Numerical Input.  Try Again."

    modOfElas = None #E
    while modOfElas is None:
        try:
            modOfElas = float(raw_input("Modulus of Elasticity of Material (lb/in2): "))
        except ValueError:
            print "Non-Numerical Input.  Try Again."

    thick = None #t
    while thick is None:
        try:
            thick = float(raw_input("Thickness of Plate (in): "))
        except ValueError:
            print "Non-Numerical Input.  Try Again."

    return (theta, length, radOut, radIn, poisson, modOfElas, thick)

def promptFile7():
    #User Input Section for Externally Applied Vertical Deformation

    delta = None #y
    while delta is None:
        try:
            delta = float(raw_input("Applied Vertical Deformation (in): "))
        except ValueError:
            print "Non-Numerical Input.  Try Again."
          
    length = None #r
    while length is None:
        try:
            length = float(raw_input("Distance to Applied Deformation from Plate Center(in): "))
        except ValueError:
            print "Non-Numerical Input.  Try Again."

    radOut = None #a
    while radOut is None:
        try:
            radOut = float(raw_input("Outer Radius of Plate (in): "))
        except ValueError:
            print "Non-Numerical Input.  Try Again."

    radIn = None #b
    while radIn is None:
        try:
            radIn = float(raw_input("Inner Radius of Plate (in): "))
        except ValueError:
            print "Non-Numerical Input.  Try Again."

    poisson = None #v
    while poisson is None:
        try:
            poisson = float(raw_input("Poisson's Ratio of Material: "))
        except ValueError:
            print "Non-Numerical Input.  Try Again."

    modOfElas = None #E
    while modOfElas is None:
        try:
            modOfElas = float(raw_input("Modulus of Elasticity of Material (lb/in2): "))
        except ValueError:
            print "Non-Numerical Input.  Try Again."

    thick = None #t
    while thick is None:
        try:
            thick = float(raw_input("Thickness of Plate (in): "))
        except ValueError:
            print "Non-Numerical Input.  Try Again."

    return (delta, length, radOut, radIn, poisson, modOfElas, thick)

def promptFile8():
    #User Input Section for Externally Applied Temperature Differential

    temp = None #delta-t
    while temp is None:
        try:
            temp = float(raw_input("Applied Temperature Differential (degF): "))
        except ValueError:
            print "Non-Numerical Input.  Try Again."
          
    gamma = None #gamma
    while gamma is None:
        try:
            gamma = float(raw_input("Temperature Coefficient of Expansion (in/in/degF): "))
        except ValueError:
            print "Non-Numerical Input.  Try Again."

    length = None #r
    while length is None:
        try:
            length = float(raw_input("Distance to Applied Temperature Differential from Plate Center(in): "))
        except ValueError:
            print "Non-Numerical Input.  Try Again."

    radOut = None #a
    while radOut is None:
        try:
            radOut = float(raw_input("Outer Radius of Plate (in): "))
        except ValueError:
            print "Non-Numerical Input.  Try Again."

    radIn = None #b
    while radIn is None:
        try:
            radIn = float(raw_input("Inner Radius of Plate (in): "))
        except ValueError:
            print "Non-Numerical Input.  Try Again."

    poisson = None #v
    while poisson is None:
        try:
            poisson = float(raw_input("Poisson's Ratio of Material: "))
        except ValueError:
            print "Non-Numerical Input.  Try Again."

    modOfElas = None #E
    while modOfElas is None:
        try:
            modOfElas = float(raw_input("Modulus of Elasticity of Material (lb/in2): "))
        except ValueError:
            print "Non-Numerical Input.  Try Again."

    thick = None #t
    while thick is None:
        try:
            thick = float(raw_input("Thickness of Plate (in): "))
        except ValueError:
            print "Non-Numerical Input.  Try Again."

    return (temp, gamma, length, radOut, radIn, poisson, modOfElas, thick)


def annularPlate1A():
    #Annular Plate with Uniform Annular Line Load
    #Outer Edge Simply Supported, Inner Edge Free
    load, length, radOut, radIn, poisson, modOfElas, thick = promptFile1()

    c1 = c_1(poisson, radIn, radOut)
    c4 = c_4(poisson, radIn, radOut)
    c7 = c_7(poisson, radIn, radOut)
    l3 = l_3(poisson, length, radOut)
    l6 = l_6(poisson, length, radOut)
    l9 = l_9(poisson, length, radOut)
    d =  d_(poisson, modOfElas, thick)

    mrb = 0
    qb = 0
    ya = 0
    mra = 0
    yb = -load*radOut**3/d*((c1*l9/c7)-l3)
    thetab = load*radOut**2/(d*c7)*l9
    thetaa = load*radOut**2/d*((c4*l9/c7)-l6)
    qa = -load*(length/radOut)

    writeFile1(load, length, radOut, radIn, poisson, modOfElas, thick, ya, yb, thetaa, thetab, qa, qb, mra, mrb)
    
def annularPlate1B():
    #Annular Plate with Uniform Annular Line Load
    #Outer Edge Simply Supported, Inner Edge Guided
    load, length, radOut, radIn, poisson, modOfElas, thick = promptFile1()

    c2 = c_2(poisson, radIn, radOut)
    c5 = c_5(poisson, radIn, radOut)
    c8 = c_8(poisson, radIn, radOut)
    l3 = l_3(poisson, length, radOut)
    l6 = l_6(poisson, length, radOut)
    l9 = l_9(poisson, length, radOut)
    d =  d_(poisson, modOfElas, thick)

    thetab = 0
    qb = 0
    ya = 0
    mra = 0
    yb = -load*radOut**3/d*((c2*l9/c8)-l3)
    mrb = load*radOut/c8*l9
    thetaa = load*radOut**2/d*((c5*l9/c8)-l6)
    qa = -load*(length/radOut)

    writeFile1(load, length, radOut, radIn, poisson, modOfElas, thick, ya, yb, thetaa, thetab, qa, qb, mra, mrb)

def annularPlate1C():
    #Annular Plate with Uniform Annular Line Load
    #Outer Edge Simply Supported, Inner Edge Simply Supported
    load, length, radOut, radIn, poisson, modOfElas, thick = promptFile1()

    c1 = c_1(poisson, radIn, radOut)
    c3 = c_3(poisson, radIn, radOut)
    c4 = c_4(poisson, radIn, radOut)
    c6 = c_6(poisson, radIn, radOut)
    c7 = c_7(poisson, radIn, radOut)
    c9 = c_9(poisson, radIn, radOut)
    l3 = l_3(poisson, length, radOut)
    l6 = l_6(poisson, length, radOut)
    l9 = l_9(poisson, length, radOut)
    d =  d_(poisson, modOfElas, thick)

    yb = 0
    mrb = 0
    ya = 0
    mra = 0
    thetab = (-load*radOut**2/d)*((c3*l9-c9*l3)/(c1*c9-c3*c7))
    qb = load*((c1*l9-c7*l3)/(c1*c9-c3*c7))
    thetaa = thetab*c4+(qb*(radOut**2/d)*c6)-(load*radOut**2/d*l6)
    qa = qb*(radIn/radOut)-((load*length)/radOut)

    writeFile1(load, length, radOut, radIn, poisson, modOfElas, thick, ya, yb, thetaa, thetab, qa, qb, mra, mrb)

def annularPlate1D():
    #Annular Plate with Uniform Annular Line Load
    #Outer Edge Simply Supported, Inner Edge Fixed
    load, length, radOut, radIn, poisson, modOfElas, thick = promptFile1()

    c2 = c_2(poisson, radIn, radOut)
    c3 = c_3(poisson, radIn, radOut)
    c5 = c_5(poisson, radIn, radOut)
    c6 = c_6(poisson, radIn, radOut)
    c8 = c_8(poisson, radIn, radOut)
    c9 = c_9(poisson, radIn, radOut)
    l3 = l_3(poisson, length, radOut)
    l6 = l_6(poisson, length, radOut)
    l9 = l_9(poisson, length, radOut)
    d =  d_(poisson, modOfElas, thick)

    yb = 0
    thetab = 0
    ya = 0
    mra = 0
    mrb = -load*radOut*((c3*l9-c9*l3)/(c2*c9-c3*c8))
    qb = load*((c2*l9-c8*l3)/(c2*c9-c3*c8))
    thetaa = mrb*(radOut/d)*c5+qb*(radOut**2/d)*c6-(load*radOut**2/d)*l6
    qa = qb*(radIn/radOut)-(load*length/radOut)

    writeFile1(load, length, radOut, radIn, poisson, modOfElas, thick, ya, yb, thetaa, thetab, qa, qb, mra, mrb)

def annularPlate1E():
    #Annular Plate with Uniform Annular Line Load
    #Outer Edge Fixed, Inner Edge Free
    load, length, radOut, radIn, poisson, modOfElas, thick = promptFile1()

    c1 = c_1(poisson, radIn, radOut)
    c4 = c_4(poisson, radIn, radOut)
    c7 = c_7(poisson, radIn, radOut)
    l3 = l_3(poisson, length, radOut)
    l6 = l_6(poisson, length, radOut)
    l9 = l_9(poisson, length, radOut)
    d =  d_(poisson, modOfElas, thick)

    mrb = 0
    qb = 0
    ya = 0
    thetaa = 0
    yb = -load*radOut**3/d*((c1*l6/c4)-l3)
    thetab = (load*radOut**2/(d*c4))*l6
    mra = -load*radOut*(l9-(c7*l6/c4))
    qa = -load*length/radOut

    writeFile1(load, length, radOut, radIn, poisson, modOfElas, thick, ya, yb, thetaa, thetab, qa, qb, mra, mrb)

def annularPlate1F():
    #Annular Plate with Uniform Annular Line Load
    #Outer Edge Fixed, Inner Edge Guided
    load, length, radOut, radIn, poisson, modOfElas, thick = promptFile1()

    c2 = c_2(poisson, radIn, radOut)
    c5 = c_5(poisson, radIn, radOut)
    c8 = c_8(poisson, radIn, radOut)
    l3 = l_3(poisson, length, radOut)
    l6 = l_6(poisson, length, radOut)
    l9 = l_9(poisson, length, radOut)
    d =  d_(poisson, modOfElas, thick)

    thetab = 0
    qb = 0
    ya = 0
    thetaa = 0
    yb = -load*radOut**3/d*((c2*l6/c5)-l3)
    mrb = (load*radOut/c5)*l6
    mra = -load*radOut*(l9-(c8*l6/c5))
    qa = -load*length/radOut

    writeFile1(load, length, radOut, radIn, poisson, modOfElas, thick, ya, yb, thetaa, thetab, qa, qb, mra, mrb)

def annularPlate1G():
    #Annular Plate with Uniform Annular Line Load
    #Outer Edge Fixed, Inner Edge Simply Supported
    load, length, radOut, radIn, poisson, modOfElas, thick = promptFile1()

    c1 = c_1(poisson, radIn, radOut)
    c3 = c_3(poisson, radIn, radOut)
    c4 = c_4(poisson, radIn, radOut)
    c6 = c_6(poisson, radIn, radOut)
    c7 = c_7(poisson, radIn, radOut)
    c9 = c_9(poisson, radIn, radOut)
    l3 = l_3(poisson, length, radOut)
    l6 = l_6(poisson, length, radOut)
    l9 = l_9(poisson, length, radOut)
    d =  d_(poisson, modOfElas, thick)

    yb = 0
    mrb = 0
    ya = 0
    thetaa = 0
    thetab = (-load*radOut**2/d)*((c3*l6-c6*l3)/(c1*c6-c3*c4))
    qb = load*((c1*l6-c4*l3)/(c1*c6-c3*c4))
    mra = thetab*(d/radOut)*c7+(qb*radOut*c9)-(load*radOut*l9)
    qa = qb*(radIn/radOut)-(load*length/radOut)

    writeFile1(load, length, radOut, radIn, poisson, modOfElas, thick, ya, yb, thetaa, thetab, qa, qb, mra, mrb)

def annularPlate1H():
    #Annular Plate with Uniform Annular Line Load
    #Outer Edge Fixed, Inner Edge Fixed
    load, length, radOut, radIn, poisson, modOfElas, thick = promptFile1()

    c2 = c_2(poisson, radIn, radOut)
    c3 = c_3(poisson, radIn, radOut)
    c5 = c_5(poisson, radIn, radOut)
    c6 = c_6(poisson, radIn, radOut)
    c8 = c_8(poisson, radIn, radOut)
    c9 = c_9(poisson, radIn, radOut)
    l3 = l_3(poisson, length, radOut)
    l6 = l_6(poisson, length, radOut)
    l9 = l_9(poisson, length, radOut)
    d =  d_(poisson, modOfElas, thick)

    yb = 0
    thetab = 0
    ya = 0
    thetaa = 0
    mrb = -load*radOut*((c3*l6-c6*l3)/(c2*c6-c3*c5))
    qb = load*((c2*l6-c5*l3)/(c2*c6-c3*c5))
    mra = mrb*c8+qb*radOut*c9-load*radOut*l9
    qa = qb*(radIn/radOut)-(load*length/radOut)

    writeFile1(load, length, radOut, radIn, poisson, modOfElas, thick, ya, yb, thetaa, thetab, qa, qb, mra, mrb)

def annularPlate1I():
    #Annular Plate with Uniform Annular Line Load
    #Outer Edge Guided, Inner Edge Simply Supported
    load, length, radOut, radIn, poisson, modOfElas, thick = promptFile1()

    c1 = c_1(poisson, radIn, radOut)
    c3 = c_3(poisson, radIn, radOut)
    c4 = c_4(poisson, radIn, radOut)
    c6 = c_6(poisson, radIn, radOut)
    c7 = c_7(poisson, radIn, radOut)
    c9 = c_9(poisson, radIn, radOut)
    l3 = l_3(poisson, length, radOut)
    l6 = l_6(poisson, length, radOut)
    l9 = l_9(poisson, length, radOut)
    d =  d_(poisson, modOfElas, thick)

    yb = 0
    mrb = 0
    thetaa = 0
    qa = 0
    thetab = -load*radOut**2/(d*c4)*((length*c6/radIn)-l6)
    qb = load*length/radIn
    ya = -load*radOut**3/d*((c1/c4)*((length*c6/radIn)-l6)-(length*c3/radIn)+l3)
    mra = load*radOut*((c7/c4)*(l6-(length*c6/radIn))+(length*c9/radIn)-l9)

    writeFile1(load, length, radOut, radIn, poisson, modOfElas, thick, ya, yb, thetaa, thetab, qa, qb, mra, mrb)

def annularPlate1J():
    #Annular Plate with Uniform Annular Line Load
    #Outer Edge Guided, Inner Edge Fixed
    load, length, radOut, radIn, poisson, modOfElas, thick = promptFile1()

    c2 = c_2(poisson, radIn, radOut)
    c3 = c_3(poisson, radIn, radOut)
    c5 = c_5(poisson, radIn, radOut)
    c6 = c_6(poisson, radIn, radOut)
    c8 = c_8(poisson, radIn, radOut)
    c9 = c_9(poisson, radIn, radOut)
    l3 = l_3(poisson, length, radOut)
    l6 = l_6(poisson, length, radOut)
    l9 = l_9(poisson, length, radOut)
    d =  d_(poisson, modOfElas, thick)

    yb = 0
    thetab = 0
    thetaa = 0
    qa = 0
    mrb = -load*radOut/c5*((length*c6/radIn)-l6)
    qb = load*length/radIn
    ya = -load*radOut**3/d*((c2/c5)*((length*c6/radIn)-l6)-(length*c3/radIn)+l3)
    mra = load*radOut*((c8/c5)*(l6-(length*c6/radIn))+(length*c9/radIn)-l9)

    writeFile1(load, length, radOut, radIn, poisson, modOfElas, thick, ya, yb, thetaa, thetab, qa, qb, mra, mrb)

def annularPlate1K():
    #Annular Plate with Uniform Annular Line Load
    #Outer Edge Free, Inner Edge Simply Supported
    load, length, radOut, radIn, poisson, modOfElas, thick = promptFile1()

    c1 = c_1(poisson, radIn, radOut)
    c3 = c_3(poisson, radIn, radOut)
    c4 = c_4(poisson, radIn, radOut)
    c6 = c_6(poisson, radIn, radOut)
    c7 = c_7(poisson, radIn, radOut)
    c9 = c_9(poisson, radIn, radOut)
    l3 = l_3(poisson, length, radOut)
    l6 = l_6(poisson, length, radOut)
    l9 = l_9(poisson, length, radOut)
    d =  d_(poisson, modOfElas, thick)

    yb = 0
    mrb = 0
    mra = 0
    qa = 0
    thetab = -load*radOut**2/(d*c7)*((length*c9/radIn)-l9)
    qb = load*length/radIn
    ya = (-load*radOut**3/d)*((c1/c7)*((length*c9/radIn)-l9)-(length*c3/radIn)+l3)
    thetaa = -load*radOut**2/d*((c4/c7)*((length*c9/radIn)-l9)-(length*c6/radIn)+l6)

    writeFile1(load, length, radOut, radIn, poisson, modOfElas, thick, ya, yb, thetaa, thetab, qa, qb, mra, mrb)

def annularPlate1L():
    #Annular Plate with Uniform Annular Line Load
    #Outer Edge Free, Inner Edge Fixed
    load, length, radOut, radIn, poisson, modOfElas, thick = promptFile1()

    c2 = c_2(poisson, radIn, radOut)
    c3 = c_3(poisson, radIn, radOut)
    c5 = c_5(poisson, radIn, radOut)
    c6 = c_6(poisson, radIn, radOut)
    c8 = c_8(poisson, radIn, radOut)
    c9 = c_9(poisson, radIn, radOut)
    l3 = l_3(poisson, length, radOut)
    l6 = l_6(poisson, length, radOut)
    l9 = l_9(poisson, length, radOut)
    d =  d_(poisson, modOfElas, thick)

    yb = 0
    thetab = 0
    mra = 0
    qa = 0
    mrb = -load*radOut/c8*((length*c9/radIn)-l9)
    qb = load*length/radIn
    ya = -load*radOut**3/d*((c2/c8)*((length*c9/radIn)-l9)-(length*c3/radIn)+l3)
    thetaa = -load*radOut**2/d*((c5/c8)*((length*c9/radIn)-l9)-(length*c6/radIn)+l6)

    writeFile1(load, length, radOut, radIn, poisson, modOfElas, thick, ya, yb, thetaa, thetab, qa, qb, mra, mrb)

def annularPlate2A():
    #Annular Plate with Uniform Distributed Pressure
    #Outer Edge Simply Supported, Inner Edge Free
    load, length, radOut, radIn, poisson, modOfElas, thick = promptFile2()

    c1 = c_1(poisson, radIn, radOut)
    c4 = c_4(poisson, radIn, radOut)
    c7 = c_7(poisson, radIn, radOut)
    l11 = l_11(poisson, length, radOut)
    l14 = l_14(poisson, length, radOut)
    l17 = l_17(poisson, length, radOut)
    d =  d_(poisson, modOfElas, thick)

    mrb = 0
    qb = 0
    ya = 0
    mra = 0
    yb = -load*radOut**4/d*((c1*l17/c7)-l11)
    thetab = load*radOut**3/(d*c7)*l17
    thetaa = load*radOut**3/d*((c4*l17/c7)-l14)
    qa = -load/(2*radOut)*(radOut**2-length**2)

    writeFile2(load, length, radOut, radIn, poisson, modOfElas, thick, ya, yb, thetaa, thetab, qa, qb, mra, mrb)

def annularPlate2B():
    #Annular Plate with Uniform Distributed Pressure
    #Outer Edge Simply Supported, Inner Edge Guided
    load, length, radOut, radIn, poisson, modOfElas, thick = promptFile2()

    c2 = c_2(poisson, radIn, radOut)
    c5 = c_5(poisson, radIn, radOut)
    c8 = c_8(poisson, radIn, radOut)
    l11 = l_11(poisson, length, radOut)
    l14 = l_14(poisson, length, radOut)
    l17 = l_17(poisson, length, radOut)
    d =  d_(poisson, modOfElas, thick)

    thetab = 0
    qb = 0
    ya = 0
    mra = 0
    yb = -load*radOut**4/d*((c2*l17/c8)-l11)
    mrb = load*radOut**2/c8*l17
    thetaa = load*radOut**3/d*((c5*l17/c8)-l14)
    qa = -load/(2*radOut)*(radOut**2-length**2)

    writeFile2(load, length, radOut, radIn, poisson, modOfElas, thick, ya, yb, thetaa, thetab, qa, qb, mra, mrb)

def annularPlate2C():
    #Annular Plate with Uniform Distributed Pressure
    #Outer Edge Simply Supported, Inner Edge Simply Supported
    load, length, radOut, radIn, poisson, modOfElas, thick = promptFile2()

    c1 = c_1(poisson, radIn, radOut)
    c3 = c_3(poisson, radIn, radOut)
    c4 = c_4(poisson, radIn, radOut)
    c6 = c_6(poisson, radIn, radOut)
    c7 = c_7(poisson, radIn, radOut)
    c9 = c_9(poisson, radIn, radOut)
    l11 = l_11(poisson, length, radOut)
    l14 = l_14(poisson, length, radOut)
    l17 = l_17(poisson, length, radOut)
    d =  d_(poisson, modOfElas, thick)

    yb = 0
    mrb = 0
    ya = 0
    mra = 0
    thetab = -load*radOut**3/d*((c3*l17-c9*l11)/(c1*c9-c3*c7))
    qb = load*radOut*((c1*l17-c7*l11)/(c1*c9-c3*c7))
    thetaa = thetab*c4+qb*(radOut**2/d)*c6-load*radOut**3/d*l14
    qa = qb*(radIn/radOut)-load/(2*radOut)*(radOut**2-length**2)

    writeFile2(load, length, radOut, radIn, poisson, modOfElas, thick, ya, yb, thetaa, thetab, qa, qb, mra, mrb)

def annularPlate2D():
    #Annular Plate with Uniform Distributed Pressure
    #Outer Edge Simply Supported, Inner Edge Free
    load, length, radOut, radIn, poisson, modOfElas, thick = promptFile2()

    c2 = c_2(poisson, radIn, radOut)
    c3 = c_3(poisson, radIn, radOut)
    c4 = c_4(poisson, radIn, radOut)
    c5 = c_5(poisson, radIn, radOut)
    c6 = c_6(poisson, radIn, radOut)
    c8 = c_8(poisson, radIn, radOut)
    c9 = c_9(poisson, radIn, radOut)
    l11 = l_11(poisson, length, radOut)
    l14 = l_14(poisson, length, radOut)
    l17 = l_17(poisson, length, radOut)
    d =  d_(poisson, modOfElas, thick)

    yb = 0
    thetab = 0
    ya = 0
    mra = 0
    mrb = -load*radOut**2*((c3*l17-c9*l11)/(c2*c9-c3*c8))
    qb = load*radOut*((c2*l17-c8*l11)/(c2*c9-c3*c8))
    thetaa = thetab*c4+qb*(radOut**2/d)*c6-load*radOut**3/d*l14
    qa = qb*(radIn/radOut)-load*(2*radOut)*(radOut**2-length**2)

    writeFile2(load, length, radOut, radIn, poisson, modOfElas, thick, ya, yb, thetaa, thetab, qa, qb, mra, mrb)

def annularPlate2E():
    #Annular Plate with Uniform Distributed Pressure
    #Outer Edge Fixed, Inner Edge Free
    load, length, radOut, radIn, poisson, modOfElas, thick = promptFile2()

    c1 = c_1(poisson, radIn, radOut)
    c4 = c_4(poisson, radIn, radOut)
    c7 = c_7(poisson, radIn, radOut)
    l11 = l_11(poisson, length, radOut)
    l14 = l_14(poisson, length, radOut)
    l17 = l_17(poisson, length, radOut)
    d =  d_(poisson, modOfElas, thick)

    mrb = 0
    qb = 0
    ya = 0
    thetaa = 0
    yb = -load*radOut**4/d*((c1*l14/c4)-l11)
    thetab = load*radOut**3*l14/(d*c4)
    mra = -load*radOut**2*(l17-(c7/c4)*l14)
    qa = -load/(2*radOut)*(radOut**2-length**2)

    writeFile2(load, length, radOut, radIn, poisson, modOfElas, thick, ya, yb, thetaa, thetab, qa, qb, mra, mrb)

def annularPlate2F():
    #Annular Plate with Uniform Distributed Pressure
    #Outer Edge Fixed, Inner Edge Guided
    load, length, radOut, radIn, poisson, modOfElas, thick = promptFile2()

    c2 = c_2(poisson, radIn, radOut)
    c5 = c_5(poisson, radIn, radOut)
    c8 = c_8(poisson, radIn, radOut)
    l11 = l_11(poisson, length, radOut)
    l14 = l_14(poisson, length, radOut)
    l17 = l_17(poisson, length, radOut)
    d =  d_(poisson, modOfElas, thick)

    thetab = 0
    qb = 0
    ya = 0
    thetaa = 0
    yb = -load*radOut**4/d*((c2*l14/c2)-l11)
    mrb = load*radOut**2*l14/c5
    mra = -load*radOut**2*(l17-(c8/c5)*l14)
    qa = -load/(2*radOut)*(radOut**2-length**2)

    writeFile2(load, length, radOut, radIn, poisson, modOfElas, thick, ya, yb, thetaa, thetab, qa, qb, mra, mrb)

def annularPlate2G():
    #Annular Plate with Uniform Distributed Pressure
    #Outer Edge Simply Supported, Inner Edge Free
    load, length, radOut, radIn, poisson, modOfElas, thick = promptFile2()

    c1 = c_1(poisson, radIn, radOut)
    c3 = c_3(poisson, radIn, radOut)
    c4 = c_4(poisson, radIn, radOut)
    c6 = c_6(poisson, radIn, radOut)
    c7 = c_7(poisson, radIn, radOut)
    c9 = c_9(poisson, radIn, radOut)
    l11 = l_11(poisson, length, radOut)
    l14 = l_14(poisson, length, radOut)
    l17 = l_17(poisson, length, radOut)
    d =  d_(poisson, modOfElas, thick)

    yb = 0
    mrb = 0
    ya = 0
    thetaa = 0
    thetab = -load*radOut**3/d*((c3*l14-c6*l11)/(c1*c6-c3*c4))
    qb = load*radOut*((c1*l14-c4*l11)/(c1*c6-c3*c4))
    mra = thetab*(d/radOut)*c7+qb*radOut*c9-load*radOut**2*l17
    qa = qb*(radIn/radOut)-load/(2*radOut)*(radOut**2-length**2)

    writeFile2(load, length, radOut, radIn, poisson, modOfElas, thick, ya, yb, thetaa, thetab, qa, qb, mra, mrb)

def annularPlate2H():
    #Annular Plate with Uniform Distributed Pressure
    #Outer Edge Fixed, Inner Edge Fixed
    load, length, radOut, radIn, poisson, modOfElas, thick = promptFile2()

    c2 = c_2(poisson, radIn, radOut)
    c3 = c_3(poisson, radIn, radOut)
    c5 = c_5(poisson, radIn, radOut)
    c6 = c_6(poisson, radIn, radOut)
    c8 = c_8(poisson, radIn, radOut)
    c9 = c_9(poisson, radIn, radOut)
    l11 = l_11(poisson, length, radOut)
    l14 = l_14(poisson, length, radOut)
    l17 = l_17(poisson, length, radOut)
    d =  d_(poisson, modOfElas, thick)

    yb = 0
    thetab = 0
    ya = 0
    thetaa = 0
    mrb = -load*radOut**2*((c3*l14-c6*l11)/(c2*c6-c3*c5))
    qb = load*radOut*((c2*l14-c5*l11)/(c2*c6-c3*c5))
    mra = mrb*c8+qb*radOut*c9-load*radOut**2*l17
    qa = qb*(radIn/radOut)-load/(2*radOut)*(radOut**2-length**2)

    writeFile2(load, length, radOut, radIn, poisson, modOfElas, thick, ya, yb, thetaa, thetab, qa, qb, mra, mrb)

def annularPlate2I():
    #Annular Plate with Uniform Distributed Pressure
    #Outer Edge Guided, Inner Edge Simply Supported
    load, length, radOut, radIn, poisson, modOfElas, thick = promptFile2()

    c1 = c_1(poisson, radIn, radOut)
    c3 = c_3(poisson, radIn, radOut)
    c4 = c_4(poisson, radIn, radOut)
    c6 = c_6(poisson, radIn, radOut)
    c7 = c_7(poisson, radIn, radOut)
    c9 = c_9(poisson, radIn, radOut)
    l11 = l_11(poisson, length, radOut)
    l14 = l_14(poisson, length, radOut)
    l17 = l_17(poisson, length, radOut)
    d =  d_(poisson, modOfElas, thick)

    yb = 0
    mrb = 0
    thetaa = 0
    qa = 0
    thetab = -load*radOut**3/(d*c4)*(c6/(2*radOut*radIn)*(radOut**2-length**2)-l14)
    qb = load/(2*radIn)*(radOut**2-length**2)
    ya = thetab*radOut*c1+qb*(radOut**3/d)*c3-load*radOut**4/d*l11
    mra = thetab*(d/radOut)*c7+qb*radOut*c9-load*radOut**2*l17

    writeFile2(load, length, radOut, radIn, poisson, modOfElas, thick, ya, yb, thetaa, thetab, qa, qb, mra, mrb)

def annularPlate2J():
    #Annular Plate with Uniform Distributed Pressure
    #Outer Edge Guided, Inner Edge Fixed
    load, length, radOut, radIn, poisson, modOfElas, thick = promptFile2()

    c2 = c_2(poisson, radIn, radOut)
    c3 = c_3(poisson, radIn, radOut)
    c5 = c_5(poisson, radIn, radOut)
    c6 = c_6(poisson, radIn, radOut)
    c8 = c_8(poisson, radIn, radOut)
    c9 = c_9(poisson, radIn, radOut)
    l11 = l_11(poisson, length, radOut)
    l14 = l_14(poisson, length, radOut)
    l17 = l_17(poisson, length, radOut)
    d =  d_(poisson, modOfElas, thick)

    yb = 0
    thetab = 0
    thetaa = 0
    qa = 0
    mrb = -load*radOut**2/c5*(c6/(2*radOut*radIn)*(radOut**2-length**2)-l14)
    qb = load/(2*radIn)*(radOut**2-length**2)
    ya = mrb*(radOut**2/d)*c2+qb*(radOut**3/d)*c3-(load*radOut**4/d)*l11
    mra = mrb*c8+qb*radOut*c9-load*radOut**2*l17

    writeFile2(load, length, radOut, radIn, poisson, modOfElas, thick, ya, yb, thetaa, thetab, qa, qb, mra, mrb)

def annularPlate2K():
    #Annular Plate with Uniform Distributed Pressure
    #Outer Edge Free, Inner Edge Simply Supported
    load, length, radOut, radIn, poisson, modOfElas, thick = promptFile2()

    c1 = c_1(poisson, radIn, radOut)
    c3 = c_3(poisson, radIn, radOut)
    c4 = c_4(poisson, radIn, radOut)
    c6 = c_6(poisson, radIn, radOut)
    c7 = c_7(poisson, radIn, radOut)
    c9 = c_9(poisson, radIn, radOut)
    l11 = l_11(poisson, length, radOut)
    l14 = l_14(poisson, length, radOut)
    l17 = l_17(poisson, length, radOut)
    d =  d_(poisson, modOfElas, thick)

    yb = 0
    mrb = 0
    mra = 0
    qa = 0
    thetab = -load*radOut**3/(d*c7)*(c9/(2*radOut*radIn)*(radOut**2-length**2)-l17)
    qb = load/(2*radIn)*(radOut**2-length**2)
    ya = thetab*radOut*c1+qb*(radOut**3/d)*c3-(load*radOut**4/d)*l11
    thetaa = thetab*c4+qb*(radOut**2/d)*c6-(load*radOut**3/d)*l14

    writeFile2(load, length, radOut, radIn, poisson, modOfElas, thick, ya, yb, thetaa, thetab, qa, qb, mra, mrb)

def annularPlate2L():
    #Annular Plate with Uniform Distributed Pressure
    #Outer Edge Free, Inner Edge Fixed
    load, length, radOut, radIn, poisson, modOfElas, thick = promptFile2()

    c2 = c_2(poisson, radIn, radOut)
    c3 = c_3(poisson, radIn, radOut)
    c5 = c_5(poisson, radIn, radOut)
    c6 = c_6(poisson, radIn, radOut)
    c8 = c_8(poisson, radIn, radOut)
    c9 = c_9(poisson, radIn, radOut)
    l11 = l_11(poisson, length, radOut)
    l14 = l_14(poisson, length, radOut)
    l17 = l_17(poisson, length, radOut)
    d =  d_(poisson, modOfElas, thick)

    yb = 0
    thetab = 0
    mra = 0
    qa = 0
    mrb = -load*radOut**2/c8*(c9/(2*radOut*radIn)*(radOut**2-length**2)-l17)
    qb = load/(2*radIn)*(radOut**2-length**2)
    ya = mrb*(radOut**2/d)*c2+qb*(radOut**3/d)*c3-(load*radOut**4/d)*l11
    thetaa = mrb*(radOut/d)*c5+qb*(radOut**2/d)*c6-(load*radOut**3/d)*l14

    writeFile2(load, length, radOut, radIn, poisson, modOfElas, thick, ya, yb, thetaa, thetab, qa, qb, mra, mrb)

def annularPlate3A():
    #Annular Plate with Linearly Increasing Distributed Pressure
    #Outer Edge Simply Supported, Inner Edge Free
    load, length, radOut, radIn, poisson, modOfElas, thick = promptFile3()

    c1 = c_1(poisson, radIn, radOut)
    c4 = c_4(poisson, radIn, radOut)
    c7 = c_7(poisson, radIn, radOut)
    l12 = l_12(poisson, length, radOut)
    l15 = l_15(poisson, length, radOut)
    l18 = l_18(poisson, length, radOut)
    d =  d_(poisson, modOfElas, thick)

    mrb = 0
    qb = 0
    ya = 0
    mra = 0
    yb = -load*radOut**4/d*((c1*l18/c7)-l12)
    thetab = load*radOut**3/(d*c7)*l18
    thetaa = load*radOut**3/d*((c4*l18/c7)-l15)
    qa = -load/(6*radOut)*(2*radOut**2-length*radOut-length**2)

    writeFile3(load, length, radOut, radIn, poisson, modOfElas, thick, ya, yb, thetaa, thetab, qa, qb, mra, mrb)

def annularPlate3B():
    #Annular Plate with Linearly Increasing Distributed Pressure
    #Outer Edge Simply Supported, Inner Edge Guided
    load, length, radOut, radIn, poisson, modOfElas, thick = promptFile3()

    c2 = c_2(poisson, radIn, radOut)
    c5 = c_5(poisson, radIn, radOut)
    c8 = c_8(poisson, radIn, radOut)
    l12 = l_12(poisson, length, radOut)
    l15 = l_15(poisson, length, radOut)
    l18 = l_18(poisson, length, radOut)
    d =  d_(poisson, modOfElas, thick)

    thetab = 0
    qb = 0
    ya = 0
    mra = 0
    yb = -load*radOut**4/d*((c2*l18/c8)-l12)
    mrb = load*radOut**2*l18/c8
    thetaa = load*radOut**3/d*((c5*l18/c8)-l15)
    qa = -load/(6*radOut)*(2*radOut**2-length*radOut-length**2)

    writeFile3(load, length, radOut, radIn, poisson, modOfElas, thick, ya, yb, thetaa, thetab, qa, qb, mra, mrb)

def annularPlate3C():
    #Annular Plate with Linearly Increasing Distributed Pressure
    #Outer Edge Simply Supported, Inner Edge Simply Supported
    load, length, radOut, radIn, poisson, modOfElas, thick = promptFile3()

    c1 = c_1(poisson, radIn, radOut)
    c3 = c_3(poisson, radIn, radOut)
    c4 = c_4(poisson, radIn, radOut)
    c6 = c_6(poisson, radIn, radOut)
    c7 = c_7(poisson, radIn, radOut)
    c9 = c_9(poisson, radIn, radOut)
    l12 = l_12(poisson, length, radOut)
    l15 = l_15(poisson, length, radOut)
    l18 = l_18(poisson, length, radOut)
    d =  d_(poisson, modOfElas, thick)

    yb = 0
    mrb = 0
    ya = 0
    mra = 0
    thetab = (-load*radOut**3/d)*((c3*l18-c9*l12)/(c1*c9-c3*c7))
    qb = load*radOut*((c1*l18-c7*l12)/(c1*c9-c3*c7))
    thetaa = thetab*c4+qb*(radOut**2/d)*c6-(load*radOut**3/d)*l15
    qa = qb*(radIn/radOut)-(load/(6*radOut))*(2*radOut**2-length*radOut-length**2)

    writeFile3(load, length, radOut, radIn, poisson, modOfElas, thick, ya, yb, thetaa, thetab, qa, qb, mra, mrb)

def annularPlate3D():
    #Annular Plate with Linearly Increasing Distributed Pressure
    #Outer Edge Simply Supported, Inner Edge Fixed
    load, length, radOut, radIn, poisson, modOfElas, thick = promptFile3()

    c2 = c_2(poisson, radIn, radOut)
    c3 = c_3(poisson, radIn, radOut)
    c5 = c_5(poisson, radIn, radOut)
    c6 = c_6(poisson, radIn, radOut)
    c8 = c_8(poisson, radIn, radOut)
    c9 = c_9(poisson, radIn, radOut)
    l12 = l_12(poisson, length, radOut)
    l15 = l_15(poisson, length, radOut)
    l18 = l_18(poisson, length, radOut)
    d =  d_(poisson, modOfElas, thick)

    yb = 0
    thetab = 0
    ya = 0
    mra = 0
    mrb = -load*radOut**2*((c3*l18-c9*l12)/(c2*c9-c3*c8))
    qb = load*radOut*((c2*l18-c8*l12)/(c2*c9-c3*c8))
    thetaa = mrb*(radOut/d)*c5+qb*(radOut**2/d)*c6-(load*radOut**3/d)*l15
    qa = qb*(radIn/radOut)-load/(6*radOut)*(2*radOut**2-length*radOut-length**2)

    writeFile3(load, length, radOut, radIn, poisson, modOfElas, thick, ya, yb, thetaa, thetab, qa, qb, mra, mrb)

def annularPlate3E():
    #Annular Plate with Linearly Increasing Distributed Pressure
    #Outer Edge Fixed, Inner Edge Free
    load, length, radOut, radIn, poisson, modOfElas, thick = promptFile3()

    c1 = c_1(poisson, radIn, radOut)
    c4 = c_4(poisson, radIn, radOut)
    c7 = c_7(poisson, radIn, radOut)
    l12 = l_12(poisson, length, radOut)
    l15 = l_15(poisson, length, radOut)
    l18 = l_18(poisson, length, radOut)
    d =  d_(poisson, modOfElas, thick)

    mrb = 0
    qb = 0
    ya = 0
    thetaa = 0
    yb = -load*radOut**4/d*((c1*l15/c4)-l12)
    thetab = load*radOut**3*l15/(d*c4)
    mra = -load*radOut**2*(l18-(c7/c4)*l15)
    qa = -load/(6*radOut)*(2*radOut**2-length*radOut-length**2)

    writeFile3(load, length, radOut, radIn, poisson, modOfElas, thick, ya, yb, thetaa, thetab, qa, qb, mra, mrb)

def annularPlate3F():
    #Annular Plate with Linearly Increasing Distributed Pressure
    #Outer Edge Fixed, Inner Edge Guided
    load, length, radOut, radIn, poisson, modOfElas, thick = promptFile3()

    c2 = c_2(poisson, radIn, radOut)
    c5 = c_5(poisson, radIn, radOut)
    c8 = c_8(poisson, radIn, radOut)
    l12 = l_12(poisson, length, radOut)
    l15 = l_15(poisson, length, radOut)
    l18 = l_18(poisson, length, radOut)
    d =  d_(poisson, modOfElas, thick)

    thetab = 0
    qb = 0
    ya = 0
    thetaa = 0
    yb = -load*radOut**4/d*((c2*l15/c5)-l12)
    mrb = load*radOut**2*l15/c5
    mra = -load*radOut**2*(l18-(c8/c5)*l15)
    qa = -load/(6*radOut)*(2*radOut**2-length*radOut-length**2)

    writeFile3(load, length, radOut, radIn, poisson, modOfElas, thick, ya, yb, thetaa, thetab, qa, qb, mra, mrb)

def annularPlate3G():
    #Annular Plate with Linearly Increasing Distributed Pressure
    #Outer Edge Fixed, Inner Edge Simply Supported
    load, length, radOut, radIn, poisson, modOfElas, thick = promptFile3()

    c1 = c_1(poisson, radIn, radOut)
    c3 = c_3(poisson, radIn, radOut)
    c4 = c_4(poisson, radIn, radOut)
    c6 = c_6(poisson, radIn, radOut)
    c7 = c_7(poisson, radIn, radOut)
    c9 = c_9(poisson, radIn, radOut)
    l12 = l_12(poisson, length, radOut)
    l15 = l_15(poisson, length, radOut)
    l18 = l_18(poisson, length, radOut)
    d =  d_(poisson, modOfElas, thick)

    yb = 0
    mrb = 0
    ya = 0
    thetaa = 0
    thetab = -load*radOut**3/d*((c3*l15-c6*l12)/(c1*c6-c3*c4))
    qb = load*radOut*((c1*l15-c4*l12)/(c1*c6-c3*c4))
    mra = thetab*(d/radOut)*c7+qb*radOut*c9-load*radOut**2*l18
    qa = qb*(radIn/radOut)-load/(6*radOut)*(2*radOut**2-length*radOut-length**2)

    writeFile3(load, length, radOut, radIn, poisson, modOfElas, thick, ya, yb, thetaa, thetab, qa, qb, mra, mrb)

def annularPlate3H():
    #Annular Plate with Linearly Increasing Distributed Pressure
    #Outer Edge Fixed, Inner Edge Fixed
    load, length, radOut, radIn, poisson, modOfElas, thick = promptFile3()

    c2 = c_2(poisson, radIn, radOut)
    c3 = c_3(poisson, radIn, radOut)
    c5 = c_5(poisson, radIn, radOut)
    c6 = c_6(poisson, radIn, radOut)
    c8 = c_8(poisson, radIn, radOut)
    c9 = c_9(poisson, radIn, radOut)
    l12 = l_12(poisson, length, radOut)
    l15 = l_15(poisson, length, radOut)
    l18 = l_18(poisson, length, radOut)
    d =  d_(poisson, modOfElas, thick)

    yb = 0
    thetab = 0
    ya = 0
    thetaa = 0
    mrb = -load*radOut**2*((c3*l15-c6*l12)/(c2*c6-c3*c5))
    qb = load*radOut*((c2*l15-c5*l12)/(c2*c6-c3*c5))
    mra = mrb*c8+qb*radOut*c9-load*radOut**2*l18
    qa = qb*(radIn/radOut)-load/(6*radOut)*(2*radOut**2-length*radOut-length**2)

    writeFile3(load, length, radOut, radIn, poisson, modOfElas, thick, ya, yb, thetaa, thetab, qa, qb, mra, mrb)

def annularPlate3I():
    #Annular Plate with Linearly Increasing Distributed Pressure
    #Outer Edge Simply Supported, Inner Edge Free
    load, length, radOut, radIn, poisson, modOfElas, thick = promptFile3()

    c1 = c_1(poisson, radIn, radOut)
    c3 = c_3(poisson, radIn, radOut)
    c4 = c_4(poisson, radIn, radOut)
    c6 = c_6(poisson, radIn, radOut)
    c7 = c_7(poisson, radIn, radOut)
    c9 = c_9(poisson, radIn, radOut)
    l12 = l_12(poisson, length, radOut)
    l15 = l_15(poisson, length, radOut)
    l18 = l_18(poisson, length, radOut)
    d =  d_(poisson, modOfElas, thick)

    yb = 0
    mrb = 0
    thetaa = 0
    qa = 0
    thetab = -load*radOut**3/(d*c4)*(c6/(6*radOut*radIn)*(2*radOut**2-length*radOut-length**2)-l15)
    qb = load/(6*radIn)*(2*radOut**2-length*radOut-length**2)
    ya = thetab*radOut*c1+qb*(radOut**3/d)*c3-(load*radOut**4/d)*l12
    mra = thetab*(d/radOut)*c7+qb*radOut*c9-load*radOut**2*l18

    writeFile3(load, length, radOut, radIn, poisson, modOfElas, thick, ya, yb, thetaa, thetab, qa, qb, mra, mrb)

def annularPlate3J():
    #Annular Plate with Linearly Increasing Distributed Pressure
    #Outer Edge Guided, Inner Edge Fixed
    load, length, radOut, radIn, poisson, modOfElas, thick = promptFile3()

    c2 = c_2(poisson, radIn, radOut)
    c3 = c_3(poisson, radIn, radOut)
    c5 = c_5(poisson, radIn, radOut)
    c6 = c_6(poisson, radIn, radOut)
    c8 = c_8(poisson, radIn, radOut)
    c9 = c_9(poisson, radIn, radOut)
    l12 = l_12(poisson, length, radOut)
    l15 = l_15(poisson, length, radOut)
    l18 = l_18(poisson, length, radOut)
    d =  d_(poisson, modOfElas, thick)

    yb = 0
    thetab = 0
    thetaa = 0
    qa = 0
    mrb = -load*radOut**2/c5*(c6/(6*radOut*radIn)*(2*radOut**2-length*radOut-length**2)-l15)
    qb = load/(6*radIn)*(2*radOut**2-length*radOut-length**2)
    ya = mrb*(radOut**2/d)*c2+qb*(radOut**3/d)*c3-(load*radOut**4/d)*l12
    mra = mrb*c8+qb*radOut*c9-load*radOut**2*l18

    writeFile3(load, length, radOut, radIn, poisson, modOfElas, thick, ya, yb, thetaa, thetab, qa, qb, mra, mrb)

def annularPlate3K():
    #Annular Plate with Linearly Increasing Distributed Pressure
    #Outer Edge Free, Inner Edge Simply Supported
    load, length, radOut, radIn, poisson, modOfElas, thick = promptFile3()

    c1 = c_1(poisson, radIn, radOut)
    c3 = c_3(poisson, radIn, radOut)
    c4 = c_4(poisson, radIn, radOut)
    c6 = c_6(poisson, radIn, radOut)
    c7 = c_7(poisson, radIn, radOut)
    c9 = c_9(poisson, radIn, radOut)
    l12 = l_12(poisson, length, radOut)
    l15 = l_15(poisson, length, radOut)
    l18 = l_18(poisson, length, radOut)
    d =  d_(poisson, modOfElas, thick)

    yb = 0
    mrb = 0
    mra = 0
    qa = 0
    thetab = -load*radOut**3/(d*c7)*(c9/(6*radOut*radIn)*(2*radOut**2-length*radOut-length**2)-l15)
    qb = load/(6*radIn)*(2*radOut**2-length*radOut-length**2)
    ya = thetab*radOut*c1+qb*(radOut**3/d)*c3-(load*radOut**4/d)*l12
    thetaa = thetab*c4+qb*(radOut**2/d)*c6-(load*radOut**3/d)*l15

    writeFile3(load, length, radOut, radIn, poisson, modOfElas, thick, ya, yb, thetaa, thetab, qa, qb, mra, mrb)

def annularPlate3L():
    #Annular Plate with Linearly Increasing Distributed Pressure
    #Outer Edge Free, Inner Edge Fixed
    load, length, radOut, radIn, poisson, modOfElas, thick = promptFile3()

    c2 = c_2(poisson, radIn, radOut)
    c3 = c_3(poisson, radIn, radOut)
    c5 = c_5(poisson, radIn, radOut)
    c6 = c_6(poisson, radIn, radOut)
    c8 = c_8(poisson, radIn, radOut)
    c9 = c_9(poisson, radIn, radOut)
    l12 = l_12(poisson, length, radOut)
    l15 = l_15(poisson, length, radOut)
    l18 = l_18(poisson, length, radOut)
    d =  d_(poisson, modOfElas, thick)

    yb = 0
    thetab = 0
    mra = 0
    qa = 0
    mrb = -load*radOut**2/c8*(c9/(6*radOut*radIn)*(2*radOut**2-length*radOut-length**2)-l15)
    qb = load/(6*radIn)*(2*radOut**2-length*radOut-length**2)
    ya = mrb*(radOut**2/d)*c2+qb*(radOut**3/d)*c3-(load*radOut**4/d)*l12
    thetaa = mrb*(radOut/d)*c5+qb*(radOut**2/d)*c6-(load*radOut**3/d)*l15

    writeFile3(load, length, radOut, radIn, poisson, modOfElas, thick, ya, yb, thetaa, thetab, qa, qb, mra, mrb)

def annularPlate4A():
    #Annular Plate with Parabolically Increasing Distributed Pressure
    #Outer Edge Simply Supported, Inner Edge Free
    load, length, radOut, radIn, poisson, modOfElas, thick = promptFile4()

    c1 = c_1(poisson, radIn, radOut)
    c4 = c_4(poisson, radIn, radOut)
    c7 = c_7(poisson, radIn, radOut)
    l13 = l_13(poisson, length, radOut)
    l16 = l_16(poisson, length, radOut)
    l19 = l_19(poisson, length, radOut)
    d =  d_(poisson, modOfElas, thick)

    mrb = 0
    qb = 0
    ya = 0
    mra = 0
    yb = -load*radOut**4/d*((c1*l19/c7)-l13)
    thetab = load*radOut**3/(d*c7)*l19
    thetaa = load*radOut**3/d*((c4*l19/c7)-l16)
    qa = -load/(12*radOut)*(3*radOut**2-2*radOut*length-length**2)

    writeFile4(load, length, radOut, radIn, poisson, modOfElas, thick, ya, yb, thetaa, thetab, qa, qb, mra, mrb)

def annularPlate4B():
    #Annular Plate with Parabolically Increasing Distributed Pressure
    #Outer Edge Simply Supported, Inner Edge Guided
    load, length, radOut, radIn, poisson, modOfElas, thick = promptFile4()

    c2 = c_2(poisson, radIn, radOut)
    c5 = c_5(poisson, radIn, radOut)
    c8 = c_8(poisson, radIn, radOut)
    l13 = l_13(poisson, length, radOut)
    l16 = l_16(poisson, length, radOut)
    l19 = l_19(poisson, length, radOut)
    d =  d_(poisson, modOfElas, thick)

    thetab = 0
    qb = 0
    ya = 0
    mra = 0
    yb = -load*radOut**4/d*((c2*l19/c8)-l13)
    mrb = load*radOut**2*l19/c8
    thetaa = load*radOut**3/d*((c5*l19/c8)-l16)
    qa = -load/(12*radOut)*(3*radOut**2-2*radOut*length-length**2)

    writeFile4(load, length, radOut, radIn, poisson, modOfElas, thick, ya, yb, thetaa, thetab, qa, qb, mra, mrb)

def annularPlate4C():
    #Annular Plate with Parabolically Increasing Distributed Pressure
    #Outer Edge Simply Supported, Inner Edge Simply Supported
    load, length, radOut, radIn, poisson, modOfElas, thick = promptFile4()

    c1 = c_1(poisson, radIn, radOut)
    c3 = c_3(poisson, radIn, radOut)
    c4 = c_4(poisson, radIn, radOut)
    c6 = c_6(poisson, radIn, radOut)
    c7 = c_7(poisson, radIn, radOut)
    c9 = c_9(poisson, radIn, radOut)
    l13 = l_13(poisson, length, radOut)
    l16 = l_16(poisson, length, radOut)
    l19 = l_19(poisson, length, radOut)
    d =  d_(poisson, modOfElas, thick)

    yb = 0
    mrb = 0
    ya = 0
    mra = 0
    thetab = -load*radOut**3/d*((c3*l19-c9*l13)/(c1*c9-c3*c7))
    qb = load*radOut*((c1*l19-c7*l13)/(c1*c9-c3*c7))
    thetaa = thetab*c4+qb*(radOut**2/d)*c6-(load*radOut**3/d)*l16
    qa = qb*(radIn/radOut)-load/(12*radOut)*(3*radOut**2-2*radOut*length-length**2)

    writeFile4(load, length, radOut, radIn, poisson, modOfElas, thick, ya, yb, thetaa, thetab, qa, qb, mra, mrb)

def annularPlate4D():
    #Annular Plate with Parabolically Increasing Distributed Pressure
    #Outer Edge Simply Supported, Inner Edge Fixed
    load, length, radOut, radIn, poisson, modOfElas, thick = promptFile4()

    c2 = c_2(poisson, radIn, radOut)
    c3 = c_3(poisson, radIn, radOut)
    c5 = c_5(poisson, radIn, radOut)
    c6 = c_6(poisson, radIn, radOut)
    c8 = c_8(poisson, radIn, radOut)
    c9 = c_9(poisson, radIn, radOut)
    l13 = l_13(poisson, length, radOut)
    l16 = l_16(poisson, length, radOut)
    l19 = l_19(poisson, length, radOut)
    d =  d_(poisson, modOfElas, thick)

    yb = 0
    thetab = 0
    ya = 0
    mra = 0
    mrb = -load*radOut**2*((c3*l19-c9*l13)/(c2*c9-c3*c8))
    qb = load*radOut*((c2*l19-c8*l13)/(c2*c9-c3*c8))
    thetaa = mrb*(radOut/d)*c5+qb*(radOut**2/d)*c6-(load*radOut**3/d)*l16
    qa = qb*(radIn/radOut)-load/(12*radOut)*(3*radOut**2-2*radOut*length-length**2)

    writeFile4(load, length, radOut, radIn, poisson, modOfElas, thick, ya, yb, thetaa, thetab, qa, qb, mra, mrb)

def annularPlate4E():
    #Annular Plate with Parabolically Increasing Distributed Pressure
    #Outer Edge Fixed, Inner Edge Free
    load, length, radOut, radIn, poisson, modOfElas, thick = promptFile4()

    c1 = c_1(poisson, radIn, radOut)
    c4 = c_4(poisson, radIn, radOut)
    c7 = c_7(poisson, radIn, radOut)
    l13 = l_13(poisson, length, radOut)
    l16 = l_16(poisson, length, radOut)
    l19 = l_19(poisson, length, radOut)
    d =  d_(poisson, modOfElas, thick)

    mrb = 0
    qb = 0
    ya = 0
    thetaa = 0
    yb = -load*radOut**4/d*((c1*l16/c4)-l13)
    thetab = load*radOut**3*l16/(d*c4)
    mra = -load*radOut**2*(l19-(c7/c4)*l16)
    qa = -load/(12*radOut)*(3*radOut**2-2*radOut*length-length**2)

    writeFile4(load, length, radOut, radIn, poisson, modOfElas, thick, ya, yb, thetaa, thetab, qa, qb, mra, mrb)

def annularPlate4F():
    #Annular Plate with Parabolically Increasing Distributed Pressure
    #Outer Edge Fixed, Inner Edge Guided
    load, length, radOut, radIn, poisson, modOfElas, thick = promptFile4()

    c2 = c_2(poisson, radIn, radOut)
    c5 = c_5(poisson, radIn, radOut)
    c8 = c_8(poisson, radIn, radOut)
    l13 = l_13(poisson, length, radOut)
    l16 = l_16(poisson, length, radOut)
    l19 = l_19(poisson, length, radOut)
    d =  d_(poisson, modOfElas, thick)

    thetab = 0
    qb = 0
    ya = 0
    thetaa = 0
    yb = -load*radOut**4/d*((c2*l16/c5)-l13)
    mrb = load*radOut**2*l16/c5
    mra = -load*radOut**2*(l19-(c8/c5)*l16)
    qa = -load/(12*radOut)*(3*radOut**2-2*radOut*length-length**2)

    writeFile4(load, length, radOut, radIn, poisson, modOfElas, thick, ya, yb, thetaa, thetab, qa, qb, mra, mrb)

def annularPlate4G():
    #Annular Plate with Parabolically Increasing Distributed Pressure
    #Outer Edge Fixed, Inner Edge Simply Supported
    load, length, radOut, radIn, poisson, modOfElas, thick = promptFile4()

    c1 = c_1(poisson, radIn, radOut)
    c3 = c_3(poisson, radIn, radOut)
    c4 = c_4(poisson, radIn, radOut)
    c6 = c_6(poisson, radIn, radOut)
    c7 = c_7(poisson, radIn, radOut)
    c9 = c_9(poisson, radIn, radOut)
    l13 = l_13(poisson, length, radOut)
    l16 = l_16(poisson, length, radOut)
    l19 = l_19(poisson, length, radOut)
    d =  d_(poisson, modOfElas, thick)

    yb = 0
    mrb = 0
    ya = 0
    thetaa = 0
    thetab = -load*radOut**3/d*((c3*l16-c6*l13)/(c1*c6-c3*c4))
    qb = load*radOut*((c1*l16-c4*l13)/(c1*c6-c3*c4))
    mra = thetab*(d/radOut)*c7+qb*radOut*c9-load*radOut**2*l19
    qa = qb*(radIn/radOut)-load/(12*radOut)*(3*radOut**2-2*radOut*length-length**2)

    writeFile4(load, length, radOut, radIn, poisson, modOfElas, thick, ya, yb, thetaa, thetab, qa, qb, mra, mrb)

def annularPlate4H():
    #Annular Plate with Parabolically Increasing Distributed Pressure
    #Outer Edge Fixed, Inner Edge Fixed
    load, length, radOut, radIn, poisson, modOfElas, thick = promptFile4()

    c2 = c_2(poisson, radIn, radOut)
    c3 = c_3(poisson, radIn, radOut)
    c5 = c_5(poisson, radIn, radOut)
    c6 = c_6(poisson, radIn, radOut)
    c8 = c_8(poisson, radIn, radOut)
    c9 = c_9(poisson, radIn, radOut)
    l13 = l_13(poisson, length, radOut)
    l16 = l_16(poisson, length, radOut)
    l19 = l_19(poisson, length, radOut)
    d =  d_(poisson, modOfElas, thick)

    yb = 0
    thetab = 0
    ya = 0
    thetaa = 0
    mrb = -load*radOut**2*((c3*l16-c6*l13)/(c2*c6-c3*c5))
    qb = load*radOut*((c2*l16-c5*l13)/(c2*c6-c3*c5))
    mra = mrb*c8+qb*radOut*c9-load*radOut**2*l19
    qa = qb*(radIn/radOut)-load/(12*radOut)*(3*radOut**2-2*radOut*length-length**2)

    writeFile4(load, length, radOut, radIn, poisson, modOfElas, thick, ya, yb, thetaa, thetab, qa, qb, mra, mrb)

def annularPlate4I():
    #Annular Plate with Parabolically Increasing Distributed Pressure
    #Outer Edge Guided, Inner Edge Simply Supported
    load, length, radOut, radIn, poisson, modOfElas, thick = promptFile4()

    c1 = c_1(poisson, radIn, radOut)
    c3 = c_3(poisson, radIn, radOut)
    c4 = c_4(poisson, radIn, radOut)
    c6 = c_6(poisson, radIn, radOut)
    c7 = c_7(poisson, radIn, radOut)
    c9 = c_9(poisson, radIn, radOut)
    l13 = l_13(poisson, length, radOut)
    l16 = l_16(poisson, length, radOut)
    l19 = l_19(poisson, length, radOut)
    d =  d_(poisson, modOfElas, thick)

    yb = 0
    mrb = 0
    thetaa = 0
    qa = 0
    thetab = -load*radOut**3/(d*c4)*(c6/(12*radOut*radIn)*(3*radOut**2-2*radOut*length-length**2)-l16)
    qb = load/(12*radIn)*(3*radOut**2-2*radOut*length-length**2)
    ya = thetab*radOut*c1+qb*(radOut**3/d)*c3-(load*radOut**4/d)*l13
    mra = thetab*(d/radOut)*c7+qb*radOut*c9-load*radOut**2*l19

    writeFile4(load, length, radOut, radIn, poisson, modOfElas, thick, ya, yb, thetaa, thetab, qa, qb, mra, mrb)

def annularPlate4J():
    #Annular Plate with Parabolically Increasing Distributed Pressure
    #Outer Edge Guided, Inner Edge Fixed
    load, length, radOut, radIn, poisson, modOfElas, thick = promptFile4()

    c2 = c_2(poisson, radIn, radOut)
    c3 = c_3(poisson, radIn, radOut)
    c5 = c_5(poisson, radIn, radOut)
    c6 = c_6(poisson, radIn, radOut)
    c8 = c_8(poisson, radIn, radOut)
    c9 = c_9(poisson, radIn, radOut)
    l13 = l_13(poisson, length, radOut)
    l16 = l_16(poisson, length, radOut)
    l19 = l_19(poisson, length, radOut)
    d =  d_(poisson, modOfElas, thick)

    yb = 0
    thetab = 0
    thetaa = 0
    qa = 0
    mrb = -load*radOut**2/c5*(c6/(12*radOut*radIn)*(3*radOut**2-2*radOut*length-length**2)-l16)
    qb = load/(12*radIn)*(3*radOut**2-2*radOut*length-length**2)
    ya = mrb*(radOut**2/d)*c2+qb*(radOut**3/d)*c3-(load*radOut**4/d)*l13
    mra = mrb*c8+qb*radOut*c9-load*radOut**2*l19

    writeFile4(load, length, radOut, radIn, poisson, modOfElas, thick, ya, yb, thetaa, thetab, qa, qb, mra, mrb)

def annularPlate4K():
    #Annular Plate with Parabolically Increasing Distributed Pressure
    #Outer Edge Free, Inner Edge Simply Supported
    load, length, radOut, radIn, poisson, modOfElas, thick = promptFile4()

    c1 = c_1(poisson, radIn, radOut)
    c3 = c_3(poisson, radIn, radOut)
    c4 = c_4(poisson, radIn, radOut)
    c6 = c_6(poisson, radIn, radOut)
    c7 = c_7(poisson, radIn, radOut)
    c9 = c_9(poisson, radIn, radOut)
    l13 = l_13(poisson, length, radOut)
    l16 = l_16(poisson, length, radOut)
    l19 = l_19(poisson, length, radOut)
    d =  d_(poisson, modOfElas, thick)

    yb = 0
    mrb = 0
    mra = 0
    qa = 0
    thetab = -load*radOut**3/(d*c7)*(c9/(12*radOut*radIn)*(3*radOut**2-2*radOut*length-length**2)-l19)
    qb = load/(12*radIn)*(3*radOut**2-2*radOut*length-length**2)
    ya = thetab*radOut*c1+qb*(radOut**3/d)*c3-(load*radOut**4/d)*l13
    thetaa = thetab*c4+qb*(radOut**2/d)*c6-(load*radOut**3/d)*l16

    writeFile4(load, length, radOut, radIn, poisson, modOfElas, thick, ya, yb, thetaa, thetab, qa, qb, mra, mrb)

def annularPlate4L():
    #Annular Plate with Parabolically Increasing Distributed Pressure
    #Outer Edge Free, Inner Edge Fixed
    load, length, radOut, radIn, poisson, modOfElas, thick = promptFile4()

    c2 = c_2(poisson, radIn, radOut)
    c3 = c_3(poisson, radIn, radOut)
    c5 = c_5(poisson, radIn, radOut)
    c6 = c_6(poisson, radIn, radOut)
    c8 = c_8(poisson, radIn, radOut)
    c9 = c_9(poisson, radIn, radOut)
    l13 = l_13(poisson, length, radOut)
    l16 = l_16(poisson, length, radOut)
    l19 = l_19(poisson, length, radOut)
    d =  d_(poisson, modOfElas, thick)

    yb = 0
    thetab = 0
    mra = 0
    qa = 0
    mrb = -load*radOut**2/c8*(c9/(12*radOut*radIn)*(3*radOut**2-2*radOut*length-length**2)-l19)
    qb = load/(12*radIn)*(3*radOut**2-2*radOut*length-length**2)
    ya = mrb*(radOut**2/d)*c2+qb*(radOut**3/d)*c3-(load*radOut**4/d)*l13
    thetaa = mrb*(radOut/d)*c5+qb*(radOut**2/d)*c6-(load*radOut**3/d)*l16

    writeFile4(load, length, radOut, radIn, poisson, modOfElas, thick, ya, yb, thetaa, thetab, qa, qb, mra, mrb)

def annularPlate5A():
    #Annular Plate with Uniform Line Moment
    #Outer Edge Simply Supported, Inner Edge Free
    moment, length, radOut, radIn, poisson, modOfElas, thick = promptFile5()

    c1 = c_1(poisson, radIn, radOut)
    c4 = c_4(poisson, radIn, radOut)
    c7 = c_7(poisson, radIn, radOut)
    l2 = l_2(poisson, length, radOut)
    l5 = l_5(poisson, length, radOut)
    l8 = l_8(poisson, length, radOut)
    d =  d_(poisson, modOfElas, thick)

    mrb = 0
    qb = 0
    ya = 0
    mra = 0
    yb = moment*radOut**2/d*((c1*l8/c7)-l2)
    thetab = -moment*radOut/(d*c7)*l8
    thetaa = -moment*radOut/d*((c4*l8/c7)-l5)
    qa = 0

    writeFile5(moment, length, radOut, radIn, poisson, modOfElas, thick, ya, yb, thetaa, thetab, qa, qb, mra, mrb)

def annularPlate5B():
    #Annular Plate with Uniform Line Moment
    #Outer Edge Simply Supported, Inner Edge Free
    moment, length, radOut, radIn, poisson, modOfElas, thick = promptFile5()

    c2 = c_2(poisson, radIn, radOut)
    c5 = c_5(poisson, radIn, radOut)
    c8 = c_8(poisson, radIn, radOut)
    l2 = l_2(poisson, length, radOut)
    l5 = l_5(poisson, length, radOut)
    l8 = l_8(poisson, length, radOut)
    l18 = l_18(poisson, length, radOut)
    d =  d_(poisson, modOfElas, thick)

    thetab = 0
    qb = 0
    ya = 0
    mra = 0
    yb = moment*radOut**2/d*((c2*l8/c8)-l2)
    mrb = -moment*l18/c8
    thetaa = -moment*radOut/d*((c5*l8/c8)-l5)
    qa = 0

    writeFile5(moment, length, radOut, radIn, poisson, modOfElas, thick, ya, yb, thetaa, thetab, qa, qb, mra, mrb)

def annularPlate5C():
    #Annular Plate with Uniform Line Moment
    #Outer Edge Simply Supported, Inner Edge Simply Supported
    moment, length, radOut, radIn, poisson, modOfElas, thick = promptFile5()

    c1 = c_1(poisson, radIn, radOut)
    c3 = c_3(poisson, radIn, radOut)
    c4 = c_4(poisson, radIn, radOut)
    c6 = c_6(poisson, radIn, radOut)
    c7 = c_7(poisson, radIn, radOut)
    c9 = c_9(poisson, radIn, radOut)
    l2 = l_2(poisson, length, radOut)
    l5 = l_5(poisson, length, radOut)
    l8 = l_8(poisson, length, radOut)
    d =  d_(poisson, modOfElas, thick)

    yb = 0
    mrb = 0
    ya = 0
    mra = 0
    thetab = moment*radOut/d*((c3*l8-c9*l2)/(c1*c9-c3*c7))
    qb = -moment/radOut*((c1*l8-c7*l2)/(c1*c9-c3*c7))
    thetaa = thetab*c4+qb*(radOut**2/d)*c6+(moment*radOut/d)*l5
    qa = qb*(radIn/radOut)

    writeFile5(moment, length, radOut, radIn, poisson, modOfElas, thick, ya, yb, thetaa, thetab, qa, qb, mra, mrb)

def annularPlate5D():
    #Annular Plate with Uniform Line Moment
    #Outer Edge Simply Supported, Inner Edge Fixed
    moment, length, radOut, radIn, poisson, modOfElas, thick = promptFile5()

    c2 = c_2(poisson, radIn, radOut)
    c3 = c_3(poisson, radIn, radOut)
    c5 = c_5(poisson, radIn, radOut)
    c6 = c_6(poisson, radIn, radOut)
    c8 = c_8(poisson, radIn, radOut)
    c9 = c_9(poisson, radIn, radOut)
    l2 = l_2(poisson, length, radOut)
    l5 = l_5(poisson, length, radOut)
    l8 = l_8(poisson, length, radOut)
    d =  d_(poisson, modOfElas, thick)

    yb = 0
    thetab = 0
    ya = 0
    mra = 0
    mrb = moment*((c3*l8-c9*l2)/(c2*c9-c3*c8))
    qb = -moment/radOut*((c2*l8-c8*l2)/(c2*c9-c3*c8))
    thetaa = mrb*(radOut/d)*c5+qb*(radOut**2/d)*c6+(moment*radOut/d)*l5
    qa = qb*(radIn/radOut)

    writeFile5(moment, length, radOut, radIn, poisson, modOfElas, thick, ya, yb, thetaa, thetab, qa, qb, mra, mrb)

def annularPlate5E():
    #Annular Plate with Uniform Line Moment
    #Outer Edge Fixed, Inner Edge Free
    moment, length, radOut, radIn, poisson, modOfElas, thick = promptFile5()

    c1 = c_1(poisson, radIn, radOut)
    c4 = c_4(poisson, radIn, radOut)
    c7 = c_7(poisson, radIn, radOut)
    l2 = l_2(poisson, length, radOut)
    l5 = l_5(poisson, length, radOut)
    l8 = l_8(poisson, length, radOut)
    d =  d_(poisson, modOfElas, thick)

    mrb = 0
    qb = 0
    ya = 0
    thetaa = 0
    yb = moment*radOut**2/d*((c1*l5/c4)-l2)
    thetab = -moment*radOut/(d*c4)*l5
    mra = moment*(l8-(c7/c4)*l5)
    qa = 0

    writeFile5(moment, length, radOut, radIn, poisson, modOfElas, thick, ya, yb, thetaa, thetab, qa, qb, mra, mrb)

def annularPlate5F():
    #Annular Plate with Uniform Line Moment
    #Outer Edge Fixed, Inner Edge Guided
    moment, length, radOut, radIn, poisson, modOfElas, thick = promptFile5()

    c2 = c_2(poisson, radIn, radOut)
    c5 = c_5(poisson, radIn, radOut)
    c8 = c_8(poisson, radIn, radOut)
    l2 = l_2(poisson, length, radOut)
    l5 = l_5(poisson, length, radOut)
    l8 = l_8(poisson, length, radOut)
    d =  d_(poisson, modOfElas, thick)

    thetab = 0
    qb = 0
    ya = 0
    thetaa = 0
    yb = moment*radOut**2/d*((c2*l5/c5)-l2)
    mrb = -moment/c5*l5
    mra = moment*(l8-(c8/c5)*l5)
    qa = 0

    writeFile5(moment, length, radOut, radIn, poisson, modOfElas, thick, ya, yb, thetaa, thetab, qa, qb, mra, mrb)

def annularPlate5G():
    #Annular Plate with Uniform Line Moment
    #Outer Edge Fixed, Inner Edge Simply Supported
    moment, length, radOut, radIn, poisson, modOfElas, thick = promptFile5()

    c1 = c_1(poisson, radIn, radOut)
    c3 = c_3(poisson, radIn, radOut)
    c4 = c_4(poisson, radIn, radOut)
    c6 = c_6(poisson, radIn, radOut)
    c7 = c_7(poisson, radIn, radOut)
    c9 = c_9(poisson, radIn, radOut)
    l2 = l_2(poisson, length, radOut)
    l5 = l_5(poisson, length, radOut)
    l8 = l_8(poisson, length, radOut)
    d =  d_(poisson, modOfElas, thick)

    yb = 0
    mrb = 0
    ya = 0
    thetaa = 0
    thetab = moment*radOut/d*((c3*l5-c6*l2)/(c1*c6-c3*c4))
    qb = -moment/radOut*((c1*l5-c4*l2)/(c1*c6-c3*c4))
    mra = thetab*(d/radOut)*c7+qb*radOut*c9+moment*l8
    qa = qb*(radIn/radOut)

    writeFile5(moment, length, radOut, radIn, poisson, modOfElas, thick, ya, yb, thetaa, thetab, qa, qb, mra, mrb)

def annularPlate5H():
    #Annular Plate with Uniform Line Moment
    #Outer Edge Fixed, Inner Edge Fixed
    moment, length, radOut, radIn, poisson, modOfElas, thick = promptFile5()

    c2 = c_2(poisson, radIn, radOut)
    c3 = c_3(poisson, radIn, radOut)
    c5 = c_5(poisson, radIn, radOut)
    c6 = c_6(poisson, radIn, radOut)
    c8 = c_8(poisson, radIn, radOut)
    c9 = c_9(poisson, radIn, radOut)
    l2 = l_2(poisson, length, radOut)
    l5 = l_5(poisson, length, radOut)
    l8 = l_8(poisson, length, radOut)
    d =  d_(poisson, modOfElas, thick)

    yb = 0
    thetab = 0
    ya = 0
    thetaa = 0
    mrb = moment*((c3*l5-c6*l2)/(c2*c6-c3*c5))
    qb = -moment/radOut*((c2*l5-c5*l2)/(c2*c6-c3*c5))
    mra = mrb*c8+qb*radOut*c9+moment*l8
    qa = qb*(radIn/radOut)

    writeFile5(moment, length, radOut, radIn, poisson, modOfElas, thick, ya, yb, thetaa, thetab, qa, qb, mra, mrb)

def annularPlate5I():
    print "Sorry!  Roark doesn't give equations for this load combination.\n"
def annularPlate5J():
    print "Sorry!  Roark doesn't give equations for this load combination.\n"
def annularPlate5K():
    print "Sorry!  Roark doesn't give equations for this load combination.\n"
def annularPlate5L():
    print "Sorry!  Roark doesn't give equations for this load combination.\n"

def annularPlate6A():
    #Annular Plate with Externally Applied Slope Change
    #Outer Edge Simply Supported, Inner Edge Free
    theta, length, radOut, radIn, poisson, modOfElas, thick = promptFile6()

    c1 = c_1(poisson, radIn, radOut)
    c4 = c_4(poisson, radIn, radOut)
    c7 = c_7(poisson, radIn, radOut)
    l1 = l_1(poisson, length, radOut)
    l4 = l_4(poisson, length, radOut)
    l7 = l_7(poisson, length, radOut)
    d =  d_(poisson, modOfElas, thick)

    mrb = 0
    qb = 0
    ya = 0
    mra = 0
    yb = theta*radOut*((c1*l7/c7)-l1)
    thetab = -theta/c7*l7
    thetaa = -theta*((c4*l7/c7)-l4)
    qa = 0

    writeFile6(theta, length, radOut, radIn, poisson, modOfElas, thick, ya, yb, thetaa, thetab, qa, qb, mra, mrb)

def annularPlate6B():
    #Annular Plate with Externally Applied Slope Change
    #Outer Edge Simply Supported, Inner Edge Guided
    theta, length, radOut, radIn, poisson, modOfElas, thick = promptFile6()

    c2 = c_2(poisson, radIn, radOut)
    c5 = c_5(poisson, radIn, radOut)
    c8 = c_8(poisson, radIn, radOut)
    l1 = l_1(poisson, length, radOut)
    l4 = l_4(poisson, length, radOut)
    l7 = l_7(poisson, length, radOut)
    d =  d_(poisson, modOfElas, thick)

    thetab = 0
    qb = 0
    ya = 0
    mra = 0
    yb = theta*radOut*((c2*l7/c8)-l1)
    mrb = -theta*d*l7/(radOut*c8)
    thetaa = -theta*((c5*l7/c8)-l4)
    qa = 0

    writeFile6(theta, length, radOut, radIn, poisson, modOfElas, thick, ya, yb, thetaa, thetab, qa, qb, mra, mrb)

def annularPlate6C():
    #Annular Plate with Externally Applied Slope Change
    #Outer Edge Simply Supported, Inner Edge Simply Supported
    theta, length, radOut, radIn, poisson, modOfElas, thick = promptFile6()

    c1 = c_1(poisson, radIn, radOut)
    c3 = c_3(poisson, radIn, radOut)
    c4 = c_4(poisson, radIn, radOut)
    c6 = c_6(poisson, radIn, radOut)
    c7 = c_7(poisson, radIn, radOut)
    c9 = c_9(poisson, radIn, radOut)
    l1 = l_1(poisson, length, radOut)
    l4 = l_4(poisson, length, radOut)
    l7 = l_7(poisson, length, radOut)
    d =  d_(poisson, modOfElas, thick)

    yb = 0
    mrb = 0
    ya = 0
    mra = 0
    thetab = theta*((c3*l7-c9*l1)/(c1*c9-c3*c7))
    qb = -theta*d/radOut**2*((c1*l7-c7*l1)/(c1*c9-c3*c7))
    thetaa = thetab*c4+qb*(radOut**2/d)*c6+theta*l4
    qa = qb*(radIn/radOut)

    writeFile6(theta, length, radOut, radIn, poisson, modOfElas, thick, ya, yb, thetaa, thetab, qa, qb, mra, mrb)

def annularPlate6D():
    #Annular Plate with Externally Applied Slope Change
    #Outer Edge Simply Supported, Inner Edge Fixed
    theta, length, radOut, radIn, poisson, modOfElas, thick = promptFile6()

    c2 = c_2(poisson, radIn, radOut)
    c3 = c_3(poisson, radIn, radOut)
    c5 = c_5(poisson, radIn, radOut)
    c6 = c_6(poisson, radIn, radOut)
    c8 = c_8(poisson, radIn, radOut)
    c9 = c_9(poisson, radIn, radOut)
    l1 = l_1(poisson, length, radOut)
    l4 = l_4(poisson, length, radOut)
    l7 = l_7(poisson, length, radOut)
    d =  d_(poisson, modOfElas, thick)

    yb = 0
    thetab = 0
    ya = 0
    mra = 0
    mrb = theta*d/radOut*((c3*l7-c9*l1)/(c2*c9-c3*c8))
    qb = -theta*d/radOut**2*((c2*l7-c8*l1)/(c2*c9-c3*c8))
    thetaa = mrb*(radOut/d)*c5+qb*(radOut**2/d)*c6+theta*l4
    qa = qb*(radIn/radOut)

    writeFile6(theta, length, radOut, radIn, poisson, modOfElas, thick, ya, yb, thetaa, thetab, qa, qb, mra, mrb)

def annularPlate6E():
    #Annular Plate with Externally Applied Slope Change
    #Outer Edge Fixed, Inner Edge Free
    theta, length, radOut, radIn, poisson, modOfElas, thick = promptFile6()

    c1 = c_1(poisson, radIn, radOut)
    c4 = c_4(poisson, radIn, radOut)
    c7 = c_7(poisson, radIn, radOut)
    l1 = l_1(poisson, length, radOut)
    l4 = l_4(poisson, length, radOut)
    l7 = l_7(poisson, length, radOut)
    d =  d_(poisson, modOfElas, thick)

    mrb = 0
    qb = 0
    ya = 0
    thetaa = 0
    yb = theta*radOut*((c1*l4/c4)-l1)
    thetab = -theta*l4/c4
    mra = theta*d/radOut*(l7-(c7/c4)*l4)
    qa = 0

    writeFile6(theta, length, radOut, radIn, poisson, modOfElas, thick, ya, yb, thetaa, thetab, qa, qb, mra, mrb)

def annularPlate6F():
    #Annular Plate with Externally Applied Slope Change
    #Outer Edge Fixed, Inner Edge Guided
    theta, length, radOut, radIn, poisson, modOfElas, thick = promptFile6()

    c2 = c_2(poisson, radIn, radOut)
    c5 = c_5(poisson, radIn, radOut)
    c8 = c_8(poisson, radIn, radOut)
    l1 = l_1(poisson, length, radOut)
    l4 = l_4(poisson, length, radOut)
    l7 = l_7(poisson, length, radOut)
    d =  d_(poisson, modOfElas, thick)

    thetab = 0
    qb = 0
    ya = 0
    thetaa = 0
    yb = theta*radOut*((c2*l4/c5)-l1)
    mrb = -theta*d*l4/(radOut*c5)
    mra = theta*d/radOut*(l7-(c8/c5)*l4)
    qa = 0

    writeFile6(theta, length, radOut, radIn, poisson, modOfElas, thick, ya, yb, thetaa, thetab, qa, qb, mra, mrb)

def annularPlate6G():
    #Annular Plate with Externally Applied Slope Change
    #Outer Edge Fixed, Inner Edge Simply Supported
    theta, length, radOut, radIn, poisson, modOfElas, thick = promptFile6()

    c1 = c_1(poisson, radIn, radOut)
    c3 = c_3(poisson, radIn, radOut)
    c4 = c_4(poisson, radIn, radOut)
    c6 = c_6(poisson, radIn, radOut)
    c7 = c_7(poisson, radIn, radOut)
    c9 = c_9(poisson, radIn, radOut)
    l1 = l_1(poisson, length, radOut)
    l4 = l_4(poisson, length, radOut)
    l7 = l_7(poisson, length, radOut)
    d =  d_(poisson, modOfElas, thick)

    yb = 0
    mrb = 0
    ya = 0
    thetaa = 0
    thetab = theta*((c3*l4-c6*l1)/(c1*c6-c3*c4))
    qb = -theta*d/radOut**2*((c1*l4-c4*l1)/(c1*c6-c3*c4))
    mra = thetab*(d/radOut)*c7+qb*radOut*c9+(theta*d/radOut)*l7
    qa = qb*(radIn/radOut)

    writeFile6(theta, length, radOut, radIn, poisson, modOfElas, thick, ya, yb, thetaa, thetab, qa, qb, mra, mrb)

def annularPlate6H():
    #Annular Plate with Externally Applied Slope Change
    #Outer Edge Fixed, Inner Edge Fixed
    theta, length, radOut, radIn, poisson, modOfElas, thick = promptFile6()

    c2 = c_2(poisson, radIn, radOut)
    c3 = c_3(poisson, radIn, radOut)
    c5 = c_5(poisson, radIn, radOut)
    c6 = c_6(poisson, radIn, radOut)
    c8 = c_8(poisson, radIn, radOut)
    c9 = c_9(poisson, radIn, radOut)
    l1 = l_1(poisson, length, radOut)
    l4 = l_4(poisson, length, radOut)
    l7 = l_7(poisson, length, radOut)
    d =  d_(poisson, modOfElas, thick)

    yb = 0
    thetab = 0
    ya = 0
    thetaa = 0
    mrb = theta*d/radOut*((c3*l4-c6*l1)/(c2*c6-c3*c5))
    qb = -theta*d/radOut**2*((c2*l4-c5*l1)/(c2*c6-c3*c5))
    mra = mrb*c8+qb*radOut*c9+theta*(d/radOut)*l7
    qa = qb*(radIn/radOut)

    writeFile6(theta, length, radOut, radIn, poisson, modOfElas, thick, ya, yb, thetaa, thetab, qa, qb, mra, mrb)

def annularPlate6I():
    print "Sorry!  Roark doesn't give equations for this load combination.\n"
def annularPlate6J():
    print "Sorry!  Roark doesn't give equations for this load combination.\n"
def annularPlate6K():
    print "Sorry!  Roark doesn't give equations for this load combination.\n"
def annularPlate6L():
    print "Sorry!  Roark doesn't give equations for this load combination.\n"

def annularPlate7A():
    print "Sorry!  Roark doesn't give equations for this load combination.\n"
def annularPlate7B():
    print "Sorry!  Roark doesn't give equations for this load combination.\n"
def annularPlate7C():
    #Annular Plate with Externally Applied Vertical Deformation
    #Outer Edge Simply Supported, Inner Edge Simply Supported
    delta, length, radOut, radIn, poisson, modOfElas, thick = promptFile7()

    c1 = c_1(poisson, radIn, radOut)
    c3 = c_3(poisson, radIn, radOut)
    c4 = c_4(poisson, radIn, radOut)
    c6 = c_6(poisson, radIn, radOut)
    c7 = c_7(poisson, radIn, radOut)
    c9 = c_9(poisson, radIn, radOut)
    d =  d_(poisson, modOfElas, thick)

    yb = 0
    mrb = 0
    ya = 0
    mra = 0
    thetab = -delta*c9/(radOut*(c1*c9-c3*c7))
    qb = delta*d*c7/(radOut**3*(c1*c9-c3*c7))
    thetaa = delta/radOut*((c7*c6-c9*c4)/(c1*c9-c3*c7))
    qa = qb*(radIn/radOut)

    writeFile7(delta, length, radOut, radIn, poisson, modOfElas, thick, ya, yb, thetaa, thetab, qa, qb, mra, mrb)

def annularPlate7D():
    #Annular Plate with Externally Applied Vertical Deformation
    #Outer Edge Simply Supported, Inner Edge Fixed
    delta, length, radOut, radIn, poisson, modOfElas, thick = promptFile7()

    c2 = c_2(poisson, radIn, radOut)
    c3 = c_3(poisson, radIn, radOut)
    c5 = c_5(poisson, radIn, radOut)
    c6 = c_6(poisson, radIn, radOut)
    c8 = c_8(poisson, radIn, radOut)
    c9 = c_9(poisson, radIn, radOut)
    d =  d_(poisson, modOfElas, thick)

    yb = 0
    thetab = 0
    ya = 0
    mra = 0
    mrb = -delta*d*c9/(radOut**2*(c2*c9-c3*c8))
    qb = delta*d*c8/(radOut**3*(c2*c9-c3*c8))
    thetaa = delta/radOut*((c6*c8-c5*c9)/(c2*c9-c3*c8))
    qa = qb*(radIn/radOut)

    writeFile7(delta, length, radOut, radIn, poisson, modOfElas, thick, ya, yb, thetaa, thetab, qa, qb, mra, mrb)

def annularPlate7E():
    print "Sorry!  Roark doesn't give equations for this load combination.\n"
def annularPlate7F():
    print "Sorry!  Roark doesn't give equations for this load combination.\n"

def annularPlate7G():
    #Annular Plate with Externally Applied Vertical Deformation
    #Outer Edge Fixed, Inner Edge Simply Supported
    delta, length, radOut, radIn, poisson, modOfElas, thick = promptFile7()

    c1 = c_1(poisson, radIn, radOut)
    c3 = c_3(poisson, radIn, radOut)
    c4 = c_4(poisson, radIn, radOut)
    c6 = c_6(poisson, radIn, radOut)
    c7 = c_7(poisson, radIn, radOut)
    c9 = c_9(poisson, radIn, radOut)
    d =  d_(poisson, modOfElas, thick)

    yb = 0
    mrb = 0
    ya = 0
    thetaa = 0
    thetab = -delta*c6/(radOut*(c1*c6-c3*c4))
    qb = delta*d*c4/(radOut**3*(c1*c6-c3*c4))
    mra = delta*d/radOut**2*((c4*c9-c6*c7)/(c1*c6-c3*c4))
    qa = qb*(radIn/radOut)

    writeFile7(delta, length, radOut, radIn, poisson, modOfElas, thick, ya, yb, thetaa, thetab, qa, qb, mra, mrb)

def annularPlate7H():
    #Annular Plate with Externally Applied Vertical Deformation
    #Outer Edge Fixed, Inner Edge Fixed
    delta, length, radOut, radIn, poisson, modOfElas, thick = promptFile7()

    c2 = c_2(poisson, radIn, radOut)
    c3 = c_3(poisson, radIn, radOut)
    c5 = c_5(poisson, radIn, radOut)
    c6 = c_6(poisson, radIn, radOut)
    c8 = c_8(poisson, radIn, radOut)
    c9 = c_9(poisson, radIn, radOut)
    d =  d_(poisson, modOfElas, thick)

    yb = 0
    thetab = 0
    ya = 0
    thetaa = 0
    mrb = -delta*d*c6/(radOut**2*(c2*c6-c3*c5))
    qb = delta*d*c5/(radOut**3*(c2*c6-c3*c5))
    mra = delta*d/radOut**2*((c5*c9-c6*c8)/(c2*c6-c3*c5))
    qa = qb*(radIn/radOut)

    writeFile7(delta, length, radOut, radIn, poisson, modOfElas, thick, ya, yb, thetaa, thetab, qa, qb, mra, mrb)

def annularPlate7I():
    print "Sorry!  Roark doesn't give equations for this load combination.\n"
def annularPlate7J():
    print "Sorry!  Roark doesn't give equations for this load combination.\n"
def annularPlate7K():
    print "Sorry!  Roark doesn't give equations for this load combination.\n"
def annularPlate7L():
    print "Sorry!  Roark doesn't give equations for this load combination.\n"
    
def annularPlate8A():
    #Annular Plate with Externally Applied Temperature Differential
    #Outer Edge Simply Supported, Inner Edge Free
    temp, gamma, length, radOut, radIn, poisson, modOfElas, thick = promptFile8()

    c1 = c_1(poisson, radIn, radOut)
    c4 = c_4(poisson, radIn, radOut)
    c7 = c_7(poisson, radIn, radOut)
    l2 = l_2(poisson, length, radOut)
    l5 = l_5(poisson, length, radOut)
    l8 = l_8(poisson, length, radOut)
    d =  d_(poisson, modOfElas, thick)

    mrb = 0
    qb = 0
    ya = 0
    mra = 0
    yb = -gamma*(1+poisson)*temp*radOut**2/thick*(l2+(c1/c7)*(1-l8))
    thetab = gamma*(1+poisson)*temp*radOut/(thick*c7)*(1-l8)
    qa = 0
    thetaa = gamma*(1+poisson)*temp*radOut/thick*(l5+(c4/c7)*(1-l8)) 

    writeFile8(temp, gamma, length, radOut, radIn, poisson, modOfElas, thick, ya, yb, thetaa, thetab, qa, qb, mra, mrb)

def annularPlate8B():
    #Annular Plate with Externally Applied Temperature Differential
    #Outer Edge Simply Supported, Inner Edge Guided
    temp, gamma, length, radOut, radIn, poisson, modOfElas, thick = promptFile8()

    c2 = c_2(poisson, radIn, radOut)
    c5 = c_5(poisson, radIn, radOut)
    c8 = c_8(poisson, radIn, radOut)
    l2 = l_2(poisson, length, radOut)
    l5 = l_5(poisson, length, radOut)
    l8 = l_8(poisson, length, radOut)
    d =  d_(poisson, modOfElas, thick)

    thetab = 0
    qb = 0
    ya = 0
    mra = 0
    yb = -gamma*(1+poisson)*temp*radOut**2/thick*(l2+(c2/c8)*(1-l8))
    mrb = gamma*(1+poisson)*temp*d/(thick*c8)*(1-l8)
    thetaa = gamma*(1+poisson)*temp*radOut/thick*(l5+(c5/c8)*(1-l8))
    qa = 0 

    writeFile8(temp, gamma, length, radOut, radIn, poisson, modOfElas, thick, ya, yb, thetaa, thetab, qa, qb, mra, mrb)

def annularPlate8C():
    #Annular Plate with Externally Applied Temperature Differential
    #Outer Edge Simply Supported, Inner Edge Simply Supported
    temp, gamma, length, radOut, radIn, poisson, modOfElas, thick = promptFile8()

    c1 = c_1(poisson, radIn, radOut)
    c3 = c_3(poisson, radIn, radOut)
    c4 = c_4(poisson, radIn, radOut)
    c6 = c_6(poisson, radIn, radOut)
    c7 = c_7(poisson, radIn, radOut)
    c9 = c_9(poisson, radIn, radOut)
    l2 = l_2(poisson, length, radOut)
    l5 = l_5(poisson, length, radOut)
    l8 = l_8(poisson, length, radOut)
    d =  d_(poisson, modOfElas, thick)

    yb = 0
    mrb = 0
    ya = 0
    mra = 0
    thetab = -gamma*(1+poisson)*temp*radOut/thick*((c9+l2+c3*(1-l8))/(c1*c9-c3*c7))
    qb = gamma*(1+poisson)*temp*d/(radOut*thick)*((c7*l2+c1*(1-l8))/(c1*c9-c3*c7))
    thetaa = thetab*c4+qb*(radOut**2/d)*c6+gamma*(1+poisson)*temp*radOut/thick*l5
    qa =  qb*(radIn/radOut)

    writeFile8(temp, gamma, length, radOut, radIn, poisson, modOfElas, thick, ya, yb, thetaa, thetab, qa, qb, mra, mrb)

def annularPlate8D():
    #Annular Plate with Externally Applied Temperature Differential
    #Outer Edge Simply Supported, Inner Edge Fixed
    temp, gamma, length, radOut, radIn, poisson, modOfElas, thick = promptFile8()

    c2 = c_2(poisson, radIn, radOut)
    c3 = c_3(poisson, radIn, radOut)
    c5 = c_5(poisson, radIn, radOut)
    c6 = c_6(poisson, radIn, radOut)
    c8 = c_8(poisson, radIn, radOut)
    c9 = c_9(poisson, radIn, radOut)
    l2 = l_2(poisson, length, radOut)
    l5 = l_5(poisson, length, radOut)
    l8 = l_8(poisson, length, radOut)
    d =  d_(poisson, modOfElas, thick)

    yb = 0
    thetab = 0
    ya = 0
    mra = 0
    mrb = -gamma*(1+poisson)*temp*d/thick*((c9*l2+c3*(1-l8))/(c2*c9-c3*c8))
    qb = gamma*(1+poisson)*temp*d/(radOut*thick)*((c8*l2+c2*(1-l8))/(c2*c9-c3*c8))
    thetaa = mrb*(radOut/d)*c5+qb*(radOut**2/d)*c6+(gamma*(1+poisson)*temp*radOut/thick)*l5
    qa = qb*(radIn/radOut)

    writeFile8(temp, gamma, length, radOut, radIn, poisson, modOfElas, thick, ya, yb, thetaa, thetab, qa, qb, mra, mrb)

def annularPlate8E():
    #Annular Plate with Externally Applied Temperature Differential
    #Outer Edge Fixed, Inner Edge Free
    temp, gamma, length, radOut, radIn, poisson, modOfElas, thick = promptFile8()

    c1 = c_1(poisson, radIn, radOut)
    c4 = c_4(poisson, radIn, radOut)
    c7 = c_7(poisson, radIn, radOut)
    l2 = l_2(poisson, length, radOut)
    l5 = l_5(poisson, length, radOut)
    l8 = l_8(poisson, length, radOut)
    d =  d_(poisson, modOfElas, thick)

    mrb = 0
    qb = 0
    ya = 0
    thetaa = 0
    yb = -gamma*(1+poisson)*temp*radOut**2/thick*(l2-(c1/c4)*l5)
    thetab = -gamma*(1+poisson)*temp*radOut/(thick*c4)*l5
    mra = -gamma*(1+poisson)*temp*d/thick*((c7/c4)*l5+1-l8)
    qa =  0

    writeFile8(temp, gamma, length, radOut, radIn, poisson, modOfElas, thick, ya, yb, thetaa, thetab, qa, qb, mra, mrb)

def annularPlate8F():
    #Annular Plate with Externally Applied Temperature Differential
    #Outer Edge Fixed, Inner Edge Guided
    temp, gamma, length, radOut, radIn, poisson, modOfElas, thick = promptFile8()

    c2 = c_2(poisson, radIn, radOut)
    c5 = c_5(poisson, radIn, radOut)
    c8 = c_8(poisson, radIn, radOut)
    l2 = l_2(poisson, length, radOut)
    l5 = l_5(poisson, length, radOut)
    l8 = l_8(poisson, length, radOut)
    d =  d_(poisson, modOfElas, thick)

    thetab = 0
    qb = 0
    ya = 0
    thetaa = 0
    yb = -gamma*(1+poisson)*temp*radOut**2/thick*(l2-(c2/c5)*l5)
    mrb = -gamma*(1+poisson)*temp*d/(thick*c5)*l5
    mra = -gamma*(1+poisson)*temp*d/thick*((c8/c5)*l5+1-l8)
    qa =  0

    writeFile8(temp, gamma, length, radOut, radIn, poisson, modOfElas, thick, ya, yb, thetaa, thetab, qa, qb, mra, mrb)

def annularPlate8G():
    #Annular Plate with Externally Applied Temperature Differential
    #Outer Edge Fixed, Inner Edge Simply Supported
    temp, gamma, length, radOut, radIn, poisson, modOfElas, thick = promptFile8()

    c1 = c_1(poisson, radIn, radOut)
    c3 = c_3(poisson, radIn, radOut)
    c4 = c_4(poisson, radIn, radOut)
    c6 = c_6(poisson, radIn, radOut)
    c7 = c_7(poisson, radIn, radOut)
    c9 = c_9(poisson, radIn, radOut)
    l2 = l_2(poisson, length, radOut)
    l5 = l_5(poisson, length, radOut)
    l8 = l_8(poisson, length, radOut)
    d =  d_(poisson, modOfElas, thick)

    yb = 0
    mrb = 0
    ya = 0
    thetaa = 0
    thetab = -gamma*(1+poisson)*temp*radOut/thick*((c6*l2-c3*l5)/(c1*c6-c3*c4))
    qb = gamma*(1+poisson)*temp*d/(radOut*thick)*((c4*l2-c1*l5)/(c1*c6-c3*c4))
    mra = thetab*(d/radOut)*c7+qb*radOut*c9-(gamma*(1+poisson)*temp*d/thick)*(1-l8)
    qa =  qb*(radIn/radOut)

    writeFile8(temp, gamma, length, radOut, radIn, poisson, modOfElas, thick, ya, yb, thetaa, thetab, qa, qb, mra, mrb)

def annularPlate8H():
    #Annular Plate with Externally Applied Temperature Differential
    #Outer Edge Fixed, Inner Edge Fixed
    temp, gamma, length, radOut, radIn, poisson, modOfElas, thick = promptFile8()

    c2 = c_2(poisson, radIn, radOut)
    c3 = c_3(poisson, radIn, radOut)
    c5 = c_5(poisson, radIn, radOut)
    c6 = c_6(poisson, radIn, radOut)
    c8 = c_8(poisson, radIn, radOut)
    c9 = c_9(poisson, radIn, radOut)
    l2 = l_2(poisson, length, radOut)
    l5 = l_5(poisson, length, radOut)
    l8 = l_8(poisson, length, radOut)
    d =  d_(poisson, modOfElas, thick)

    yb = 0
    thetab = 0
    ya = 0
    thetaa = 0
    mrb = -gamma*(1+poisson)*temp*d/thick*((c6*l2-c3*l5)/(c2*c6-c3*c5))
    qb = gamma*(1+poisson)*temp*d/(radOut*thick)*((c5*l2-c2*l5)/(c2*c6-c3*c5))
    mra = mrb*c8+qb*radOut*c9-(gamma*(1+poisson)*temp*d/thick)*(1-l8)
    qa =  qb*(radIn/radOut)

    writeFile8(temp, gamma, length, radOut, radIn, poisson, modOfElas, thick, ya, yb, thetaa, thetab, qa, qb, mra, mrb)

def annularPlate8I():
    print "Sorry!  Roark doesn't give equations for this load combination.\n"
def annularPlate8J():
    print "Sorry!  Roark doesn't give equations for this load combination.\n"
def annularPlate8K():
    print "Sorry!  Roark doesn't give equations for this load combination.\n"
def annularPlate8L():
    print "Sorry!  Roark doesn't give equations for this load combination.\n"
    
def writeFile1(load, length, radOut, radIn, poisson, modOfElas, thick, ya, yb, thetaa, thetab, qa, qb, mra, mrb):
    #Creates and writes the output file for Annular Line Load calculations
    fileName = raw_input("Output File Name: ") + ".txt"
    output = open(fileName, 'w')
    project = raw_input("Project Number: ")
    output.write("""
    Roark Equations for Stress and Strain
    Circular Plate of Constant Thickness
    Annular Line Load

    Program Release 20130116
    """)
    output.write("\n    Project Number    %s\n" %(project))
    output.write("    Calculated %s\n" %(str(datetime.now())[:19]))
    output.write("\n\nINPUT DATA\n\n")
    output.write("Annular Line Load:                            %.2f lb\n" %load)
    output.write("Radius of Load Application:                   %.2f in\n" %length)
    output.write("Outer Radius of Plate:                        %.2f in\n" %radOut)
    output.write("Inner Radius of Plate:                        %.2f in\n" %radIn)
    output.write("Poisson's Ratio of Material:                  %.2f \n" %poisson)
    output.write("Modulus of Elasticity of Material:            %.2f in4\n" %modOfElas)
    output.write("Thickness of Plate:                           %.2f in\n" %thick)
    output.write("\n\nOUTPUT DATA\n\n")
    output.write("Vertical Deflection of Plate at Outer Radius: %.2f in\n" %ya)
    output.write("Vertical Deflection of Plate at Inner Radius: %.2f in\n" %yb)
    output.write("Radial Slope of Plate at Outer Radius:        %.2f rad\n" %thetaa)
    output.write("Radial Slope of Plate at Inner Radius:        %.2f rad\n" %thetab)
    output.write("Reaction Load at Outer Radius:                %.2f lb\n" %qa)
    output.write("Reaction Load at Inner Radius:                %.2f lb\n" %qb)
    output.write("Reaction Moment at Outer Radius:              %.2f in-lb\n" %mra)
    output.write("Reaction Moment at Inner Radius:              %.2f in-lb\n" %mrb)
    output.close()

def writeFile2(load, length, radOut, radIn, poisson, modOfElas, thick, ya, yb, thetaa, thetab, qa, qb, mra, mrb):
    #Creates and writes the output file for Constant Pressure Distribution calculations
    fileName = raw_input("Output File Name: ") + ".txt"
    output = open(fileName, 'w')
    project = raw_input("Project Number: ")
    output.write("""
    Roark Equations for Stress and Strain
    Circular Plate of Constant Thickness
    Uniformly Distributed Pressure

    Program Release 20130116
    """)
    output.write("\n    Project Number    %s\n" %(project))
    output.write("    Calculated %s\n" %(str(datetime.now())[:19]))
    output.write("\n\nINPUT DATA\n\n")
    output.write("Pressure Distribution:                                        %.2f lb/in\n" %load)
    output.write("Location of Start of Pressure Distribution from Plate Center: %.2f in\n" %length)
    output.write("Outer Radius of Plate:                                        %.2f in\n" %radOut)
    output.write("Inner Radius of Plate:                                        %.2f in\n" %radIn)
    output.write("Poisson's Ratio of Material:                                  %.2f \n" %poisson)
    output.write("Modulus of Elasticity of Material:                            %.2f in4\n" %modOfElas)
    output.write("Thickness of Plate:                                           %.2f in\n" %thick)
    output.write("\n\nOUTPUT DATA\n\n")
    output.write("Vertical Deflection of Plate at Outer Radius:                 %.2f in\n" %ya)
    output.write("Vertical Deflection of Plate at Inner Radius:                 %.2f in\n" %yb)
    output.write("Radial Slope of Plate at Outer Radius:                        %.2f rad\n" %thetaa)
    output.write("Radial Slope of Plate at Inner Radius:                        %.2f rad\n" %thetab)
    output.write("Reaction Load at Outer Radius:                                %.2f lb\n" %qa)
    output.write("Reaction Load at Inner Radius:                                %.2f lb\n" %qb)
    output.write("Reaction Moment at Outer Radius:                              %.2f in-lb\n" %mra)
    output.write("Reaction Moment at Inner Radius:                              %.2f in-lb\n" %mrb)
    output.close()

def writeFile3(load, length, radOut, radIn, poisson, modOfElas, thick, ya, yb, thetaa, thetab, qa, qb, mra, mrb):
    #Creates and writes the output file for Linear Pressure Distributioncalculations
    fileName = raw_input("Output File Name: ") + ".txt"
    output = open(fileName, 'w')
    project = raw_input("Project Number: ")
    output.write("""
    Roark Equations for Stress and Strain
    Circular Plate of Constant Thickness
    Linearly Increasing Distributed Pressure

    Program Release 20130116
    """)
    output.write("\n    Project Number    %s\n" %(project))
    output.write("    Calculated %s\n" %(str(datetime.now())[:19]))
    output.write("\n\nINPUT DATA\n\n")
    output.write("Maximum of Pressure Distribution:                             %.2f lb/in\n" %load)
    output.write("Location of Start of Pressure Distribution from Plate Center: %.2f in\n" %length)
    output.write("Outer Radius of Plate:                                        %.2f in\n" %radOut)
    output.write("Inner Radius of Plate:                                        %.2f in\n" %radIn)
    output.write("Poisson's Ratio of Material:                                  %.2f \n" %poisson)
    output.write("Modulus of Elasticity of Material:                            %.2f in4\n" %modOfElas)
    output.write("Thickness of Plate:                                           %.2f in\n" %thick)
    output.write("\n\nOUTPUT DATA\n\n")
    output.write("Vertical Deflection of Plate at Outer Radius:                 %.2f in\n" %ya)
    output.write("Vertical Deflection of Plate at Inner Radius:                 %.2f in\n" %yb)
    output.write("Radial Slope of Plate at Outer Radius:                        %.2f rad\n" %thetaa)
    output.write("Radial Slope of Plate at Inner Radius:                        %.2f rad\n" %thetab)
    output.write("Reaction Load at Outer Radius:                                %.2f lb\n" %qa)
    output.write("Reaction Load at Inner Radius:                                %.2f lb\n" %qb)
    output.write("Reaction Moment at Outer Radius:                              %.2f in-lb\n" %mra)
    output.write("Reaction Moment at Inner Radius:                              %.2f in-lb\n" %mrb)
    output.close()

def writeFile4(load, length, radOut, radIn, poisson, modOfElas, thick, ya, yb, thetaa, thetab, qa, qb, mra, mrb):
    #Creates and writes the output file for Parabolic Pressure Distributions calculations
    fileName = raw_input("Output File Name: ") + ".txt"
    output = open(fileName, 'w')
    project = raw_input("Project Number: ")
    output.write("""
    Roark Equations for Stress and Strain
    Circular Plate of Constant Thickness
    Parabolically Increasing Distributed Pressure

    Program Release 20130116
    """)
    output.write("\n    Project Number    %s\n" %(project))
    output.write("    Calculated %s\n" %(str(datetime.now())[:19]))
    output.write("\n\nINPUT DATA\n\n")
    output.write("Maximum of Pressure Distribution:                             %.2f lb/in\n" %load)
    output.write("Location of Start of Pressure Distribution from Plate Center: %.2f in\n" %length)
    output.write("Outer Radius of Plate:                                        %.2f in\n" %radOut)
    output.write("Inner Radius of Plate:                                        %.2f in\n" %radIn)
    output.write("Poisson's Ratio of Material:                                  %.2f \n" %poisson)
    output.write("Modulus of Elasticity of Material:                            %.2f in4\n" %modOfElas)
    output.write("Thickness of Plate:                                           %.2f in\n" %thick)
    output.write("\n\nOUTPUT DATA\n\n")
    output.write("Vertical Deflection of Plate at Outer Radius:                 %.2f in\n" %ya)
    output.write("Vertical Deflection of Plate at Inner Radius:                 %.2f in\n" %yb)
    output.write("Radial Slope of Plate at Outer Radius:                        %.2f rad\n" %thetaa)
    output.write("Radial Slope of Plate at Inner Radius:                        %.2f rad\n" %thetab)
    output.write("Reaction Load at Outer Radius:                                %.2f lb\n" %qa)
    output.write("Reaction Load at Inner Radius:                                %.2f lb\n" %qb)
    output.write("Reaction Moment at Outer Radius:                              %.2f in-lb\n" %mra)
    output.write("Reaction Moment at Inner Radius:                              %.2f in-lb\n" %mrb)
    output.close()


def writeFile5(moment, length, radOut, radIn, poisson, modOfElas, thick, ya, yb, thetaa, thetab, qa, qb, mra, mrb):
    #Creates and writes the output file for Moment calculations
    fileName = raw_input("Output File Name: ") + ".txt"
    output = open(fileName, 'w')
    project = raw_input("Project Number: ")
    output.write("""
    Roark Equations for Stress and Strain
    Circular Plate of Constant Thickness
    Uniform Line Moment

    Program Release 20130116
    """)
    output.write("\n    Project Number    %s\n" %(project))
    output.write("    Calculated %s\n" %(str(datetime.now())[:19]))
    output.write("\n\nINPUT DATA\n\n")
    output.write("Applied Moment:                                               %.2f in-lb\n" %moment)
    output.write("Distance to Moment Application from Plate Center:             %.2f in\n" %length)
    output.write("Outer Radius of Plate:                                        %.2f in\n" %radOut)
    output.write("Inner Radius of Plate:                                        %.2f in\n" %radIn)
    output.write("Poisson's Ratio of Material:                                  %.2f \n" %poisson)
    output.write("Modulus of Elasticity of Material:                            %.2f in4\n" %modOfElas)
    output.write("Thickness of Plate:                                           %.2f in\n" %thick)
    output.write("\n\nOUTPUT DATA\n\n")
    output.write("Vertical Deflection of Plate at Outer Radius:                 %.2f in\n" %ya)
    output.write("Vertical Deflection of Plate at Inner Radius:                 %.2f in\n" %yb)
    output.write("Radial Slope of Plate at Outer Radius:                        %.2f rad\n" %thetaa)
    output.write("Radial Slope of Plate at Inner Radius:                        %.2f rad\n" %thetab)
    output.write("Reaction Load at Outer Radius:                                %.2f lb\n" %qa)
    output.write("Reaction Load at Inner Radius:                                %.2f lb\n" %qb)
    output.write("Reaction Moment at Outer Radius:                              %.2f in-lb\n" %mra)
    output.write("Reaction Moment at Inner Radius:                              %.2f in-lb\n" %mrb)
    output.close()

def writeFile6(theta, length, radOut, radIn, poisson, modOfElas, thick, ya, yb, thetaa, thetab, qa, qb, mra, mrb):
    #Creates and writes the output file for External Slope Deformation calculations
    fileName = raw_input("Output File Name: ") + ".txt"
    output = open(fileName, 'w')
    project = raw_input("Project Number: ")
    output.write("""
    Roark Equations for Stress and Strain
    Circular Plate of Constant Thickness
    Applied Slope Change

    Program Release 20130116
    """)
    output.write("\n    Project Number    %s\n" %(project))
    output.write("    Calculated %s\n" %(str(datetime.now())[:19]))
    output.write("\n\nINPUT DATA\n\n")
    output.write("Applied Change in Slope:                                      %.2f rad\n" %theta)
    output.write("Distance to Slope Change Application from Plate Center:       %.2f in\n" %length)
    output.write("Outer Radius of Plate:                                        %.2f in\n" %radOut)
    output.write("Inner Radius of Plate:                                        %.2f in\n" %radIn)
    output.write("Poisson's Ratio of Material:                                  %.2f \n" %poisson)
    output.write("Modulus of Elasticity of Material:                            %.2f in4\n" %modOfElas)
    output.write("Thickness of Plate:                                           %.2f in\n" %thick)
    output.write("\n\nOUTPUT DATA\n\n")
    output.write("Vertical Deflection of Plate at Outer Radius:                 %.2f in\n" %ya)
    output.write("Vertical Deflection of Plate at Inner Radius:                 %.2f in\n" %yb)
    output.write("Radial Slope of Plate at Outer Radius:                        %.2f rad\n" %thetaa)
    output.write("Radial Slope of Plate at Inner Radius:                        %.2f rad\n" %thetab)
    output.write("Reaction Load at Outer Radius:                                %.2f lb\n" %qa)
    output.write("Reaction Load at Inner Radius:                                %.2f lb\n" %qb)
    output.write("Reaction Moment at Outer Radius:                              %.2f in-lb\n" %mra)
    output.write("Reaction Moment at Inner Radius:                              %.2f in-lb\n" %mrb)
    output.close()

def writeFile7(delta, length, radOut, radIn, poisson, modOfElas, thick, ya, yb, thetaa, thetab, qa, qb, mra, mrb):
    #Creates and writes the output file for External Vertical Deformation calculations
    fileName = raw_input("Output File Name: ") + ".txt"
    output = open(fileName, 'w')
    project = raw_input("Project Number: ")
    output.write("""
    Roark Equations for Stress and Strain
    Circular Plate of Constant Thickness
    Applied Slope Change

    Program Release 20130116
    """)
    output.write("\n    Project Number    %s\n" %(project))
    output.write("    Calculated %s\n" %(str(datetime.now())[:19]))
    output.write("\n\nINPUT DATA\n\n")
    output.write("Applied Change in Vertical Deformation:                       %.2f in\n" %delta)
    output.write("Distance to Vertical Change Application from Plate Center:    %.2f in\n" %length)
    output.write("Outer Radius of Plate:                                        %.2f in\n" %radOut)
    output.write("Inner Radius of Plate:                                        %.2f in\n" %radIn)
    output.write("Poisson's Ratio of Material:                                  %.2f \n" %poisson)
    output.write("Modulus of Elasticity of Material:                            %.2f in4\n" %modOfElas)
    output.write("Thickness of Plate:                                           %.2f in\n" %thick)
    output.write("\n\nOUTPUT DATA\n\n")
    output.write("Vertical Deflection of Plate at Outer Radius:                 %.2f in\n" %ya)
    output.write("Vertical Deflection of Plate at Inner Radius:                 %.2f in\n" %yb)
    output.write("Radial Slope of Plate at Outer Radius:                        %.2f rad\n" %thetaa)
    output.write("Radial Slope of Plate at Inner Radius:                        %.2f rad\n" %thetab)
    output.write("Reaction Load at Outer Radius:                                %.2f lb\n" %qa)
    output.write("Reaction Load at Inner Radius:                                %.2f lb\n" %qb)
    output.write("Reaction Moment at Outer Radius:                              %.2f in-lb\n" %mra)
    output.write("Reaction Moment at Inner Radius:                              %.2f in-lb\n" %mrb)
    output.close()

def writeFile8(temp, gamma, length, radOut, radIn, poisson, modOfElas, thick, ya, yb, thetaa, thetab, qa, qb, mra, mrb):
    #Creates and writes the output file for External Vertical Deformation calculations
    fileName = raw_input("Output File Name: ") + ".txt"
    output = open(fileName, 'w')
    project = raw_input("Project Number: ")
    output.write("""
    Roark Equations for Stress and Strain
    Circular Plate of Constant Thickness
    Applied Slope Change

    Program Release 20130116
    """)
    output.write("\n    Project Number    %s\n" %(project))
    output.write("    Calculated %s\n" %(str(datetime.now())[:19]))
    output.write("\n\nINPUT DATA\n\n")
    output.write("Applied Temperature Differential:                             %.2f degF\n" %temp)
    output.write("Temperature Coefficient of Expansion:                         %.2f in/in/degF\n" %gamma)
    output.write("Distance to Vertical Change Application from Plate Center:    %.2f in\n" %length)
    output.write("Outer Radius of Plate:                                        %.2f in\n" %radOut)
    output.write("Inner Radius of Plate:                                        %.2f in\n" %radIn)
    output.write("Poisson's Ratio of Material:                                  %.2f \n" %poisson)
    output.write("Modulus of Elasticity of Material:                            %.2f in4\n" %modOfElas)
    output.write("Thickness of Plate:                                           %.2f in\n" %thick)
    output.write("\n\nOUTPUT DATA\n\n")
    output.write("Vertical Deflection of Plate at Outer Radius:                 %.2f in\n" %ya)
    output.write("Vertical Deflection of Plate at Inner Radius:                 %.2f in\n" %yb)
    output.write("Radial Slope of Plate at Outer Radius:                        %.2f rad\n" %thetaa)
    output.write("Radial Slope of Plate at Inner Radius:                        %.2f rad\n" %thetab)
    output.write("Reaction Load at Outer Radius:                                %.2f lb\n" %qa)
    output.write("Reaction Load at Inner Radius:                                %.2f lb\n" %qb)
    output.write("Reaction Moment at Outer Radius:                              %.2f in-lb\n" %mra)
    output.write("Reaction Moment at Inner Radius:                              %.2f in-lb\n" %mrb)
    output.close()

