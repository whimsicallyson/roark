#Calcuations from Table 8.1: Shear, Moment, Slope, and Deflection Formulas for Elastice Straight Beams
#Table from Roark's Formulas for Stress and Strain, Eighth Edition

from datetime import datetime

def promptFile1():
    #user input section for concentrated load beams
    
    load = None
    while load is None:
        try:
            load = float(raw_input("Concentrated Load (lb): "))
        except ValueError:
            print "Non-Numerical Input.  Try Again."
          
    length = None
    while length is None:
        try:
            length = float(raw_input("Length of Beam (in): "))
        except ValueError:
            print "Non-Numerical Input.  Try Again."

    distance = None
    while distance is None:
        try:
            distance = float(raw_input("Distance from left end to concentrated load (in): "))
        except ValueError:
            print "Non-Numerical Input.  Try Again."

    modOfElas = None
    while modOfElas is None:
        try:
            modOfElas = float(raw_input("Modulus of Elasticity of Material (lb/in2): "))
        except ValueError:
            print "Non-Numerical Input.  Try Again."

    momOfInert = None
    while momOfInert is None:
        try:
            momOfInert = float(raw_input("Area Moment of Inertia of Section (in4): "))
        except ValueError:
            print "Non-Numerical Input.  Try Again."

    return (load, length, distance, modOfElas, momOfInert)

def promptFile2():
    #user input section for distributed load beams

    loada = None
    while loada is None:
        try:
            loada = float(raw_input("Unit Load at Left Edge of Load (lb/in): "))
        except ValueError:
            print "Non-Numerical Input.  Try Again."

    loadb = None
    while loadb is None:
        try:
            loadb = float(raw_input("Unit Load at Right Edge of Load (lb/in): "))
        except ValueError:
            print "Non-Numerical Input.  Try Again."   
          
    length = None
    while length is None:
        try:
            length = float(raw_input("Length of Beam (in): "))
        except ValueError:
            print "Non-Numerical Input.  Try Again."

    distance = None
    while distance is None:
        try:
            distance = float(raw_input("Distance from Left end to Edge of Distributed Load (in): "))
        except ValueError:
            print "Non-Numerical Input.  Try Again."

    modOfElas = None
    while modOfElas is None:
        try:
            modOfElas = float(raw_input("Modulus of Elasticity of Material (lb/in2): "))
        except ValueError:
            print "Non-Numerical Input.  Try Again."

    momOfInert = None
    while momOfInert is None:
        try:
            momOfInert = float(raw_input("Area Moment of Inertia of Section (in4): "))
        except ValueError:
            print "Non-Numerical Input.  Try Again."

    return (loada, loadb, length, distance, modOfElas, momOfInert)

def promptFile3():
    #user input section for concentrated moment beams

    moment = None
    while moment is None:
        try:
            moment = float(raw_input("Applied Moment (in-lb): "))
        except ValueError:
            print "Non-Numerical Input.  Try Again."
        
    length = None
    while length is None:
        try:
            length = float(raw_input("Length of Beam (in): "))
        except ValueError:
            print "Non-Numerical Input.  Try Again."

    distance = None
    while distance is None:
        try:
            distance = float(raw_input("Distance from left end to Moment Location (in): "))
        except ValueError:
            print "Non-Numerical Input.  Try Again."

    modOfElas = None
    while modOfElas is None:
        try:
            modOfElas = float(raw_input("Modulus of Elasticity of Material (lb/in2): "))
        except ValueError:
            print "Non-Numerical Input.  Try Again."

    momOfInert = None
    while momOfInert is None:
        try:
            momOfInert = float(raw_input("Area Moment of Inertia of Section (in4): "))
        except ValueError:
            print "Non-Numerical Input.  Try Again."

    return (moment, length, distance, modOfElas, momOfInert)

def promptFile4():
    #user input section for angular deformation beam

    theta = None
    while theta is None:
        try:
            theta = float(raw_input("Applied Angular Deflection (rad): "))
        except ValueError:
            print "Non-Numerical Input.  Try Again."
        
    length = None
    while length is None:
        try:
            length = float(raw_input("Length of Beam (in): "))
        except ValueError:
            print "Non-Numerical Input.  Try Again."

    distance = None
    while distance is None:
        try:
            distance = float(raw_input("Distance from left end to Location of Deflection (in): "))
        except ValueError:
            print "Non-Numerical Input.  Try Again."

    modOfElas = None
    while modOfElas is None:
        try:
            modOfElas = float(raw_input("Modulus of Elasticity of Material (lb/in2): "))
        except ValueError:
            print "Non-Numerical Input.  Try Again."

    momOfInert = None
    while momOfInert is None:
        try:
            momOfInert = float(raw_input("Area Moment of Inertia of Section (in4): "))
        except ValueError:
            print "Non-Numerical Input.  Try Again."

    return (theta, length, distance, modOfElas, momOfInert)

def promptFile5():
    #user input section for lateral displacement beam

    delta = None
    while delta is None:
        try:
            delta = float(raw_input("Applied Lateral Displacement (in): "))
        except ValueError:
            print "Non-Numerical Input.  Try Again."
        
    length = None
    while length is None:
        try:
            length = float(raw_input("Length of Beam (in): "))
        except ValueError:
            print "Non-Numerical Input.  Try Again."

    distance = None
    while distance is None:
        try:
            distance = float(raw_input("Distance from left end to Location of Displacement (in): "))
        except ValueError:
            print "Non-Numerical Input.  Try Again."

    modOfElas = None
    while modOfElas is None:
        try:
            modOfElas = float(raw_input("Modulus of Elasticity of Material (lb/in2): "))
        except ValueError:
            print "Non-Numerical Input.  Try Again."

    momOfInert = None
    while momOfInert is None:
        try:
            momOfInert = float(raw_input("Area Moment of Inertia of Section (in4): "))
        except ValueError:
            print "Non-Numerical Input.  Try Again."

    return (delta, length, distance, modOfElas, momOfInert)

def promptFile6():
    #user input section for temperature-induced deformation

    temp1 = None
    while temp1 is None:
        try:
            temp1 = float(raw_input("Temperature at Top Face (degF): "))
        except ValueError:
            print "Non-Numerical Input.  Try Again."

    temp2 = None
    while temp2 is None:
        try:
            temp2 = float(raw_input("Temperature at Bottom Face (degF): "))
        except ValueError:
            print "Non-Numerical Input.  Try Again."
  
    gamma = None
    while gamma is None:
        try:
            gamma = float(raw_input("Temperature Coefficient of Expansion (in/in/degF): "))
        except ValueError:
            print "Non-Numerical Input.  Try Again."
        
    length = None
    while length is None:
        try:
            length = float(raw_input("Length of Beam (in): "))
        except ValueError:
            print "Non-Numerical Input.  Try Again."

    depth = None
    while depth is None:
        try:
            depth = float(raw_input("Depth of Beam (in): "))
        except ValueError:
            print "Non-Numerical Input.  Try Again."

    distance = None
    while distance is None:
        try:
            distance = float(raw_input("Distance from left end to Location of Interest (in): "))
        except ValueError:
            print "Non-Numerical Input.  Try Again."

    modOfElas = None
    while modOfElas is None:
        try:
            modOfElas = float(raw_input("Modulus of Elasticity of Material (lb/in2): "))
        except ValueError:
            print "Non-Numerical Input.  Try Again."

    momOfInert = None
    while momOfInert is None:
        try:
            momOfInert = float(raw_input("Area Moment of Inertia of Section (in4): "))
        except ValueError:
            print "Non-Numerical Input.  Try Again."

    return (temp1, temp2, gamma, length, depth, distance, modOfElas, momOfInert)

def straightBeam1A():
    #Concentrated Intermediate Load
    #Left End Free, Right End Fixed
    
    load, length, distance, modOfElas, momOfInert = promptFile1()    

    rLeft = 0
    mLeft = 0
    thetaLeft = load*(length-distance)**2/(2*modOfElas*momOfInert)
    yLeft = (-load/(6*modOfElas*momOfInert))*(2*length**3-3*length**2*distance + distance**3)
    rRight = load
    mRight = -load*(length-distance)
    thetaRight = 0
    yRight = 0

    writeFile1(load, length, distance, modOfElas, momOfInert, rLeft, rRight, mLeft, mRight, thetaLeft, thetaRight, yLeft, yRight)


def straightBeam1B():
    #Concentrated Intermediate Load
    #Left End Guided, Right End Fixed

    load, length, distance, modOfElas, momOfInert = promptFile1()
    
    rLeft = 0
    mLeft = load*(length-distance)**2/(2*length)
    thetaLeft = 0
    yLeft = (-load/(12*modOfElas*momOfInert))*(length-distance)**2*(length+2*distance)
    rRight = load
    mRight = -load*(length**2-distance**2)/(2*length)
    thetaRight = 0
    yRight = 0

    writeFile1(load, length, distance, modOfElas, momOfInert, rLeft, rRight, mLeft, mRight, thetaLeft, thetaRight, yLeft, yRight)

def straightBeam1C():
    #Concentrated Intermediate Load
    #Left End Simply Supported, Right End Fixed

    load, length, distance, modOfElas, momOfInert = promptFile1()

    rLeft = load/(2*length**3)*(length-distance)**2*(2*length+distance)
    mLeft = 0
    thetaLeft = -load*distance/(4*modOfElas*length)*(length-distance)**2
    yLeft = 0
    rRight = load*distance/(2*length**3)*(3*length**2-distance**2)
    thetaRight = 0
    mRight = -load*distance/(2*length**2)*(length**2-distance**2)
    yRight = 0

    writeFile1(load, length, distance, modOfElas, momOfInert, rLeft, rRight, mLeft, mRight, thetaLeft, thetaRight, yLeft, yRight)

def straightBeam1D():
    #Concentrated Intermediate Load
    #Left End Fixed, Right End Fixed

    load, length, distance, modOfElas, momOfInert = promptFile1()

    rLeft = load/length**3*(length-distance)**2*(length+2*distance)
    mLeft = -load*distance/length**2*(length-distance)**2
    thetaLeft = 0
    yLeft = 0
    rRight = load*distance**2/length**3*(3*length-2*distance)
    mRight = -load*distance**2/length**3*(length-distance)
    thetaRight = 0
    yRight = 0

    writeFile1(load, length, distance, modOfElas, momOfInert, rLeft, rRight, mLeft, mRight, thetaLeft, thetaRight, yLeft, yRight)

def straightBeam1E():
    #Concentrated Intermediate Load
    #Left End Simply Supported, Right End Simply Supported

    load, length, distance, modOfElas, momOfInert = promptFile1()

    rLeft = load/length*(length-distance)
    mLeft = 0
    thetaLeft = -load*distance/(6*modOfElas*momOfInert*length)*(2*length-distance)*(length-distance)
    yLeft = 0
    rRight = load*distance/length
    mRight = 0
    thetaRight = load*distance/(6*modOfElas*momOfInert*length)*(length**2-distance**2)
    yRight = 0

    writeFile1(load, length, distance, modOfElas, momOfInert, rLeft, rRight, mLeft, mRight, thetaLeft, thetaRight, yLeft, yRight)

def straightBeam1F():
    #Concentrated Intermediate Load
    #Left End Guided, Right End Simply Supported

    load, length, distance, modOfElas, momOfInert = promptFile1()

    rLeft = 0
    mLeft = load*(length-distance)
    thetaLeft = 0
    yLeft = -load*(length-distance)/(6*modOfElas*momOfInert)*(2*length**2+2*distance*length-distance**2)
    rRight = load
    mRight = 0
    thetaRight = load/(2*modOfElas*momOfInert)*(length**2-distance**2)
    yRight = 0

    writeFile1(load, length, distance, modOfElas, momOfInert, rLeft, rRight, mLeft, mRight, thetaLeft, thetaRight, yLeft, yRight)

def straightBeam2A():
    #Partial Distributed Load
    #Left End Free, Right End Fixed

    loada, loadb, length, distance, modOfElas, momOfInert = promptFile2()

    rLeft = 0
    mLeft = 0
    thetaLeft = loada/(6*modOfElas*momOfInert)*(length-distance)**3+(loadb-loada)/(24*modOfElas*momOfInert)*(length-distance)**3
    yLeft = -loada/(24*modOfElas*momOfInert)*(length-distance)**3*(3*length+distance)-(loadb-loada)/(120*modOfElas*momOfInert)*(length-distance)**3*(4*length+distance)
    rRight = loada-loadb/2*(length-distance)
    mRight = -loada/2*(length-distance)**2-(loadb-loada)/6*(length-distance)**2
    thetaRight = 0
    yRight = 0

    writeFile2(loada, loadb, length, distance, modOfElas, momOfInert, rLeft, rRight, mLeft, mRight, thetaLeft, thetaRight, yLeft, yRight)

def straightBeam2B():
    #Partial Distributed Load
    #Left End Guided, Right End Fixed

    loada, loadb, length, distance, modOfElas, momOfInert = promptFile2()

    rLeft = 0
    thetaLeft = 0
    mLeft = loada/(6*length)*(length-distance)**3+(loadb-loada)/(24*length)*(length-distance)**3
    yLeft = -loada/(24*modOfElas*momOfInert)*(length-distance)**3*(length+distance)-(loadb-loada)/(240*modOfElas*momOfInert)*(length-distance)**3*(3*length+2*distance)
    rRight = (loada+loadb)/2*(length-distance)
    mRight = -loada/(6*length)*(length-distance)**2*(2*length+distance)-(loadb-loada)/(24*length)*(length-distance)**2*(3*length+distance)
    thetaRight = 0
    yRight = 0

    writeFile2(loada, loadb, length, distance, modOfElas, momOfInert, rLeft, rRight, mLeft, mRight, thetaLeft, thetaRight, yLeft, yRight)

def straightBeam2C():
    #Partial Distributed Load
    #Left End Simply Supported, Right End Fixed

    loada, loadb, length, distance, modOfElas, momOfInert = promptFile2()

    rLeft = loada/(8*length**3)*(length-distance)**3*(3*length+distance)+(loadb-loada)/(40*length**3)*(length-distance)**3*(4*length+distance)
    thetaLeft = -loada/(48*modOfElas*momOfInert*length)*(length-distance)**3*(length+3*distance)-(loadb-loada)/(240*modOfElas*momOfInert*length)*(length-distance)**3*(2*length+3*distance)
    mLeft = 0
    yLeft = 0
    rRight = (loada+loadb)/2*(length-distance)-rLeft
    mRight = rLeft*length-loada/2*(length-distance)**2-(loadb-loada)/6*(length-distance)**2
    thetaRight = 0
    yRight = 0

    writeFile2(loada, loadb, length, distance, modOfElas, momOfInert, rLeft, rRight, mLeft, mRight, thetaLeft, thetaRight, yLeft, yRight)
    
def straightBeam2D():
    #Partial Distributed Load
    #Left End Fixed, Right End Fixed

    loada, loadb, length, distance, modOfElas, momOfInert = promptFile2()

    rLeft = loada/(2*length**3)*(length-distance)**3*(length+distance)+(loadb-loada)/(20*length**3)*(length-distance)**3*(3*length+2*distance)
    mLeft = -loada/(12*length**2)*(length-distance)**3*(length+3*distance)-(loadb-loada)/(60*length**2)*(length-distance)**3*(2*length+3*distance)
    thetaLeft = 0
    yLeft = 0
    rRight = (loada+loadb)/2*(length-distance)-rLeft
    mRight = rLeft*length+mLeft-(loada/2)*(length-distance)**2-(loadb-loada)/6*(length-distance)**2
    thetaRight = 0
    yRight = 0

    writeFile2(loada, loadb, length, distance, modOfElas, momOfInert, rLeft, rRight, mLeft, mRight, thetaLeft, thetaRight, yLeft, yRight)

def straightBeam2E():
    #Partial Distributed Load
    #Left End Simply Supported, Right End Simply Supported

    loada, loadb, length, distance, modOfElas, momOfInert = promptFile2()

    rLeft = loada/(2*length)*(length-distance)**2+(loadb-loada)/(6*length)*(length-distance)**2
    mLeft = 0
    yLeft = 0
    thetaLeft = -loada/(24*modOfElas*momOfInert*length)*(length-distance)**2*(length**2+2*distance*length-distance**2)-(loadb-loada)/(360*modOfElas*momOfInert*length)*(length-distance)**2*(7*length**2+6*distance*length-3*distance**2)
    rRight = (loada+lodab)/2*(length-distance)-rLeft
    thetaRight = loada/(24*modOfElas*momOfInert*length)*(length**2-distance**2)**2+(loadb-loada)/(360*modOfElas*momOfInert*length)*(length-distance)**2*(8*length**2+9*distance*length+3*distance**2)
    mRight = 0
    yRight = 0

    writeFile2(loada, loadb, length, distance, modOfElas, momOfInert, rLeft, rRight, mLeft, mRight, thetaLeft, thetaRight, yLeft, yRight)

def straightBeam2F():
    #Partial Distributed Load
    #Left End Guided, Right End Simply Supported

    loada, loadb, length, distance, modOfElas, momOfInert = promptFile2()

    rLeft = 0
    thetaLeft = 0
    mLeft = loada/2*(length-distance)**2+(loadb-loada)/6*(length-distance)**2
    yLeft = -loada/(24*modOfElas*momOfInert)*(length-distance)**2*(5*length**2+2*distance*length-distance**2)-(loadb-loada)/(120*modOfElas*momOfInert)*(length-distance)**2*(9*length**2+2*distance*length-distance**2)
    rRight = (loada+loadb)/2*(length-distance)
    thetaRight = loada/(6*modOfElas*momOfInert)*(length-distance)**2*(2*length+distance)+(loadb-loadb)/(24*modOfElas*momOfInert)*(length-distance)**2*(3*length+distance)
    mRight = 0
    yRight = 0

    writeFile2(loada, loadb, length, distance, modOfElas, momOfInert, rLeft, rRight, mLeft, mRight, thetaLeft, thetaRight, yLeft, yRight)

def straightBeam3A():
    #Concentrated Intermediate Moment
    #Left End Free, Right End Fixed

    moment, length, distance, modOfElas, momOfInert = promptFile3()

    rLeft = 0
    mLeft = 0
    thetaLeft = -moment*(length-distance)/(modOfElas*momOfInert)
    yLeft = moment*(length**2-distance**2)/(2*modOfElas*momOfInert)
    rRight = 0
    mRight = moment
    thetaRight = 0
    yRight = 0

    writeFile3(moment, length, distance, modOfElas, momOfInert, rLeft, rRight, mLeft, mRight, thetaLeft, thetaRight, yLeft, yRight)

def straightBeam3B():
    #Concentrated Intermediate Moment
    #Left End Guided, Right End Fixed

    moment, length, distance, modOfElas, momOfInert = promptFile3()

    rLeft = 0
    thetaLeft = 0
    mLeft = -moment*(length-distance)/length
    yLeft = moment*distance*(length-distance)/(2*modOfElas*momOfInert)
    rRight = 0
    thetaRight = 0
    mRight = moment*distance/length
    yRight = 0

    writeFile3(moment, length, distance, modOfElas, momOfInert, rLeft, rRight, mLeft, mRight, thetaLeft, thetaRight, yLeft, yRight)

def straightBeam3C():
    #Concentrated Intermediate Moment
    #Left End Simply Supported, Right End Fixed

    moment, length, distance, modOfElas, momOfInert = promptFile3()

    rLeft = -3*moment/(2*length**3)*(length**2-distance**2)
    thetaLeft = moment/(4*modOfElas*momOfInert*length)*(length-distance)*(3*distance-length)
    mLeft = 0
    yLeft = 0
    rRight = 3*moment/(2*length**3)*(length**2-distance**2)
    mRight = moment/(2*length**2)*(3*distance**2-length**2)
    thetaRight = 0
    yRight = 0

    writeFile3(moment, length, distance, modOfElas, momOfInert, rLeft, rRight, mLeft, mRight, thetaLeft, thetaRight, yLeft, yRight)

def straightBeam3D():
    #Concentrated Intermediate Moment
    #Left End Fixed, Right End Fixed

    moment, length, distance, modOfElas, momOfInert = promptFile3()

    rLeft = -6*moment*distance/length**3*(length-distance)
    mLeft = -moment/length**2*(length**2-4*distance*length+3*distance**2)
    thetaLeft = 0
    yLeft = 0
    rRight = -rLeft
    mRight = moment/length**2*(3*distance**2-2*distance*length)
    thetaRight = 0
    yRight = 0

    writeFile3(moment, length, distance, modOfElas, momOfInert, rLeft, rRight, mLeft, mRight, thetaLeft, thetaRight, yLeft, yRight)

def straightBeam3E():
    #Concentrated Intermediate Moment
    #Left End Simply Supported, Right End Simply Supported

    moment, length, distance, modOfElas, momOfInert = promptFile3()

    rLeft = -moment/length
    thetaLeft = -moment/(6*modOfElas*momOfInert*length)*(2*length**2-6*distance*length+3*distance**2)
    mLeft = 0
    yLeft = 0
    rRight = moment/length
    thetaRight = moment/(6*modOfElas*momOfInert*length)*(length**2-3*distance**2)
    mRight = 0
    yRight = 0

    writeFile3(moment, length, distance, modOfElas, momOfInert, rLeft, rRight, mLeft, mRight, thetaLeft, thetaRight, yLeft, yRight)

def straightBeam3F():
    #Concentrated Intermediate Moment
    #Left End Guided, Right End Simply Supported

    moment, length, distance, modOfElas, momOfInert = promptFile3()

    rLeft = 0
    thetaLeft = 0
    mLeft = -moment
    yLeft = (moment*distance)/(2*modOfElas*momOfInert)*(2*length-distance)
    rRight = 0
    mRight = 0
    yRight = 0
    thetaRight = -moment*distance/(modOfElas*momOfInert)

    writeFile3(moment, length, distance, modOfElas, momOfInert, rLeft, rRight, mLeft, mRight, thetaLeft, thetaRight, yLeft, yRight)

def straightBeam4A():
    #Intermediate Externally Created Angular Deflection
    #Left End Free, Right End Fixed

    theta, length, distance, modOfElas, momOfInert = promptFile4()

    rLeft = 0
    mLeft = 0
    thetaLeft = -theta
    yLeft = theta*distance
    rRight = 0
    mRight = 0
    thetaRight = 0
    yRight = 0

    writeFile4(theta, length, distance, modOfElas, momOfInert, rLeft, rRight, mLeft, mRight, thetaLeft, thetaRight, yLeft, yRight)

def straightBeam4B():
    #Intermediate Externally Created Angular Deflection
    #Left End Guided, Right End Fixed

    theta, length, distance, modOfElas, momOfInert = promptFile4()
    rLeft = 0
    mLeft = -modOfElas*momOfInert*theta/length
    thetaLeft = 0
    yLeft = theta*(distance - (length/2))
    rRight = 0
    mRight = -modOfElas*momOfInert*theta/length
    thetaRight = 0
    yRight = 0

    writeFile4(theta, length, distance, modOfElas, momOfInert, rLeft, rRight, mLeft, mRight, thetaLeft, thetaRight, yLeft, yRight)

def straightBeam4C():
    #Intermediate Externally Created Angular Deflection
    #Left End Simply Supported, Right End Fixed

    theta, length, distance, modOfElas, momOfInert = promptFile4()
    mLeft = 0
    yLeft = 0
    rLeft = (-3*modOfElas*momOfInert*distance*theta)/length**3
    thetaLeft = -theta*(1-3*distance/(2*length))
    rRight = -rLeft
    mRight = (-3*modOfElas*momOfInert*distance*theta)/length**2
    thetaRight = 0
    yRight = 0

    writeFile4(theta, length, distance, modOfElas, momOfInert, rLeft, rRight, mLeft, mRight, thetaLeft, thetaRight, yLeft, yRight)

def straightBeam4D():
    #Intermediate Externally Created Angular Deflection
    #Left End Fixed, Right End Fixed

    theta, length, distance, modOfElas, momOfInert = promptFile4()
    
    rLeft = 6*modOfElas*momOfInert*theta/length**3*(length-2*distance)
    mLeft = 2*modOfElas*momOfInert*theta/length**2*(3*distance-2*length)
    thetaLeft = 0
    yLeft = 0
    rRight = -rLeft
    mRight = 2*modOfElas*momOfInert*theta/length**2*(length-3*distance)
    thetaRight = 0
    yRight = 0

    writeFile4(theta, length, distance, modOfElas, momOfInert, rLeft, rRight, mLeft, mRight, thetaLeft, thetaRight, yLeft, yRight)

def straightBeam4E():
    #Intermediate Externally Created Angular Deflection
    #Left End Simply Supported, Right End Simply Supported

    theta, length, distance, modOfElas, momOfInert = promptFile4()
    
    rLeft = 0
    mLeft = 0
    thetaLeft = -theta/length*(length-distance)
    yLeft = 0
    rRight = 0
    mRight = 0
    yRight = 0
    thetaRight = theta/length

    writeFile4(theta, length, distance, modOfElas, momOfInert, rLeft, rRight, mLeft, mRight, thetaLeft, thetaRight, yLeft, yRight)

def straightBeam4F():
    #Intermediate Externally Created Angular Deflection
    #Left End Guided, Right End Simply Supported

    theta, length, distance, modOfElas, momOfInert = promptFile4()
    
    rLeft = 0
    mLeft = 0
    thetaLeft = 0
    yLeft = -theta*(length-distance)
    rRight = 0
    mRight = 0
    yRight = 0
    thetaRight = theta

    writeFile4(theta, length, distance, modOfElas, momOfInert, rLeft, rRight, mLeft, mRight, thetaLeft, thetaRight, yLeft, yRight)

def straightBeam5A():
    #Intermediate Externally Created Lateral Displacement
    #Left End Free, Right End Fixed

    delta, length, distance, modOfElas, momOfInert = promptFile5()

    rLeft = 0
    mLeft = 0
    thetaLeft = 0
    yLeft = -delta
    rRight = 0
    mRight = 0
    thetaRight = 0
    yRight = 0

    writeFile5(delta, length, distance, modOfElas, momOfInert, rLeft, rRight, mLeft, mRight, thetaLeft, thetaRight, yLeft, yRight)

def straightBeam5B():
    #Intermediate Externally Created Lateral Displacement
    #Left End Guided, Right End Fixed

    delta, length, distance, modOfElas, momOfInert = promptFile5()

    rLeft = 0
    mLeft = 0
    thetaLeft = 0
    yLeft = -delta
    rRight = 0
    mRight = 0
    thetaRight = 0
    yRight = 0

    writeFile5(delta, length, distance, modOfElas, momOfInert, rLeft, rRight, mLeft, mRight, thetaLeft, thetaRight, yLeft, yRight)

def straightBeam5C():
    #Intermediate Externally Created Lateral Displacement
    #Left End Simply Supported, Right End Fixed

    delta, length, distance, modOfElas, momOfInert = promptFile5()

    rLeft = 3*modOfElas*momOfInert*delta/length**3
    mLeft = 0
    thetaLeft = -3*delta/(2*length)
    yLeft = 0
    rRight = -rLeft
    mRight = 3*modOfElas*momOfInert*delta/length**2
    thetaRight = 0
    yRight = 0

    writeFile5(delta, length, distance, modOfElas, momOfInert, rLeft, rRight, mLeft, mRight, thetaLeft, thetaRight, yLeft, yRight)

def straightBeam5D():
    #Intermediate Externally Created Lateral Displacement
    #Left End Fixed, Right End Fixed

    delta, length, distance, modOfElas, momOfInert = promptFile5()

    rLeft = 12*modOfElas*momOfInert*delta/length**3
    thetaLeft = 0
    mLeft = -6*modOfElas*momOfInert*delta/length**2
    yLeft = 0
    rRight = -rLeft
    mRight = -mLeft
    thetaRight = 0
    yRight = 0

    writeFile5(delta, length, distance, modOfElas, momOfInert, rLeft, rRight, mLeft, mRight, thetaLeft, thetaRight, yLeft, yRight)

def straightBeam5E():
    #Intermediate Externally Created Lateral Displacement
    #Left End Simply Supported, Right End Simply Supported

    delta, length, distance, modOfElas, momOfInert = promptFile5()

    rLeft = 0
    mLeft = 0
    yLeft = 0
    thetaLeft = -delta/length
    rRight = 0
    mRight = 0
    yRight = 0
    thetaRight = -delta/length

    writeFile5(delta, length, distance, modOfElas, momOfInert, rLeft, rRight, mLeft, mRight, thetaLeft, thetaRight, yLeft, yRight)

def straightBeam5F():
    #Intermediate Externally Created Lateral Displacement
    #Left End Guided, Right End Simply Supported

    delta, length, distance, modOfElas, momOfInert = promptFile5()

    rLeft = 0
    mLeft = 0
    thetaLeft = 0
    yLeft = -delta
    rRight = 0
    mRight = 0
    thetaRight = 0
    yRight = 0

    writeFile5(delta, length, distance, modOfElas, momOfInert, rLeft, rRight, mLeft, mRight, thetaLeft, thetaRight, yLeft, yRight)

def straightBeam6A():
    #Uniform Temperature Variation from Top to Bottom from a to l
    #Left End Free, Right End Fixed

    temp1, temp2, gamma, length, depth, distance, modOfElas, momOfInert = promptFile6()

    rLeft = 0
    mLeft = 0
    thetaLeft = -gamma/depth*(temp2-temp1)*(length-distance)
    yLeft = gamma/(2*depth)*(temp2-temp1)*(length**2-distance**2)
    rRight = 0
    mRight = 0
    thetaRight = 0
    yRight = 0

    writeFile6(temp1, temp2, gamma, length, depth, distance, modOfElas, momOfInert, rLeft, rRight, mLeft, mRight, thetaLeft, thetaRight, yLeft, yRight)

def straightBeam6B():
    #Uniform Temperature Variation from Top to Bottom from a to l
    #Left End Guided, Right End Fixed

    temp1, temp2, gamma, length, depth, distance, modOfElas, momOfInert = promptFile6()

    rLeft = 0
    thetaLeft = 0
    mLeft = (-modOfElas*momOfInert*gamma)/(length*depth)*(temp2-temp1)*(length-distance)
    yLeft = distance*gamma/(2*depth)*(temp2-temp1)*(length-distance)
    rRight = 0
    mRight = mLeft
    thetaRight = 0
    yRight = 0

    writeFile6(temp1, temp2, gamma, length, depth, distance, modOfElas, momOfInert, rLeft, rRight, mLeft, mRight, thetaLeft, thetaRight, yLeft, yRight)

def straightBeam6C():
    #Uniform Temperature Variation from Top to Bottom from a to l
    #Left End Simply Supported, Right End Fixed

    temp1, temp2, gamma, length, depth, distance, modOfElas, momOfInert = promptFile6()

    mLeft = 0
    yLeft = 0
    rLeft = -3*modofElas*momOfInert*gamma/(2*depth*length**3)*(temp2-temp1)*(length**2-distance**2)
    thetaLeft = gamma/(4*depth*length)*(temp2-temp1)*(length-distance)*(3*distance-length)
    rRight = -rLeft
    mRight = rLeft*length
    thetaRight = 0
    yRight = 0

    writeFile6(temp1, temp2, gamma, length, depth, distance, modOfElas, momOfInert, rLeft, rRight, mLeft, mRight, thetaLeft, thetaRight, yLeft, yRight)

def straightBeam6D():
    #Uniform Temperature Variation from Top to Bottom from a to l
    #Left End Fixed, Right End Fixed

    temp1, temp2, gamma, length, depth, distance, modOfElas, momOfInert = promptFile6()

    rLeft = -6*modOfElas*momOfInert*distance*gamma/(depth*length**3)*(temp2-temp1)*(length-distance)
    mLeft = modOfElas*momOfInert*gamma/(depth*length**2)*(temp2-temp1)*(length-distance)*(3*distance-length)
    thetaLeft = 0
    yLeft = 0
    rRight = -rLeft
    mRight = -modOfElas*momOfInert*gamma/(depth*length**2)*(temp2-temp1)*(length-distance)*(3*distance+length)
    thetaRight = 0
    yRight = 0

    writeFile6(temp1, temp2, gamma, length, depth, distance, modOfElas, momOfInert, rLeft, rRight, mLeft, mRight, thetaLeft, thetaRight, yLeft, yRight)

def straightBeam6E():
    #Uniform Temperature Variation from Top to Bottom from a to l
    #Left End Simply Supported, Right End Simply Supported

    temp1, temp2, gamma, length, depth, distance, modOfElas, momOfInert = promptFile6()

    rLeft = 0
    mLeft = 0
    yLeft = 0
    thetaLeft = -gamma/(2*depth*length)*(temp2-temp1)*(length-distance)**2
    rRight = 0
    mRight = 0
    yRight = 0
    thetaRight = gamma/(2*depth*length)*(temp2-temp1)*(length**2-distance**2)

    writeFile6(temp1, temp2, gamma, length, depth, distance, modOfElas, momOfInert, rLeft, rRight, mLeft, mRight, thetaLeft, thetaRight, yLeft, yRight)

def straightBeam6F():
    #Uniform Temperature Variation from Top to Bottom from a to l
    #Left End Guided, Right End Simply Supported

    temp1, temp2, gamma, length, depth, distance, modOfElas, momOfInert = promptFile6()

    rLeft = 0
    mLeft = 0
    thetaLeft = 0
    yLeft = -gamma/(2*depth)*(temp2-temp1)*(length-distance)**2
    rRight = 0
    mRight = 0
    yRight = 0
    thetaRight = gamma/length*(temp2-temp1)*(length-distance)

    writeFile6(temp1, temp2, gamma, length, depth, distance, modOfElas, momOfInert, rLeft, rRight, mLeft, mRight, thetaLeft, thetaRight, yLeft, yRight)

def writeFile1(load, length, distance, modOfElas, momOfInert, rLeft, rRight, mLeft, mRight, thetaLeft, thetaRight, yLeft, yRight):
    #Creates and writes the output file for Intermediate Load calculations
    fileName = raw_input("Output File Name: ") + ".txt"
    output = open(fileName, 'w')
    project = raw_input("Project Number: ")
    output.write("""    
    Roark Equations for Stress and Strain
    Straight Beam
    Concentrated Intermediate Load

    Program Release 20130116
    """)
    output.write("\n    Project Number    %s\n" %(project))
    output.write("    Calculated %s\n" %(str(datetime.now())[:19]))
    output.write("\n\nINPUT DATA\n\n")
    output.write("Concentrated Load:                                                %.2f lb\n" %load)
    output.write("Length of Beam:                                                   %.2f in\n" %length)
    output.write("Distance from Left End of Beam to Concentrated Load Location:     %.2f in\n" %distance)
    output.write("Modulus of Elasticity of Material:                                %.2f lb/in2\n" %modOfElas)
    output.write("Area Moment of Inertia of Section:                                %.2f in4\n" %momOfInert)
    output.write("\n\nOUTPUT DATA\n\n")
    output.write("Vertical End Reaction at Left End:                                %.2f lb\n" %rLeft)
    output.write("Vertical End Reaction at Right End:                               %.2f lb\n" %rRight)
    output.write("Reaction End Moment at Left End:                                  %.2f in-lb\n" %mLeft)
    output.write("Reaction End Moment at Right End:                                 %.2f in-lb\n" %mRight)
    output.write("Slope of Beam at Left End:                                        %.2f rad\n" %thetaLeft)
    output.write("Slope of Beam at Right End:                                       %.2f rad\n" %thetaRight)
    output.write("Deflection of Beam at Left End:                                   %.2f in\n" %yLeft)
    output.write("Deflection of Beam at Right End:                                  %.2f in\n" %yRight)
    output.close()

def writeFile2(loada, loadb, length, distance, modOfElas, momOfInert, rLeft, rRight, mLeft, mRight, thetaLeft, thetaRight, yLeft, yRight):
    #Creates and writes the output file for Distributed Load calculations
    fileName = raw_input("Output File Name: ") + ".txt"
    output = open(fileName, 'w')
    project = raw_input("Project Number: ")
    output.write("""
    Roark Equations for Stress and Strain
    Straight Beam
    Partial Distributed Load

    Program Release 20130116
    """)
    output.write("\n    Project Number    %s\n" %(project))
    output.write("    Calculated %s\n" %(str(datetime.now())[:19]))
    output.write("\n\nINPUT DATA\n\n")
    output.write("Unit Load at Left Edge:                                       %.2f lb\n" %loada)
    output.write("Unit Load at Right Edge:                                      %.2f lb\n" %loadb)
    output.write("Length of Beam:                                               %.2f in\n" %length)
    output.write("Distance from Left End of Beam to Edge of Distributed Load:   %.2f in\n" %distance)
    output.write("Modulus of Elasticity of Material:                            %.2f lb/in2\n" %modOfElas)
    output.write("Area Moment of Inertia of Section:                            %.2f in4\n" %momOfInert)
    output.write("\n\nOUTPUT DATA\n\n")
    output.write("Vertical End Reaction at Left End:                            %.2f lb\n" %rLeft)
    output.write("Vertical End Reaction at Right End:                           %.2f lb\n" %rRight)
    output.write("Reaction End Moment at Left End:                              %.2f in-lb\n" %mLeft)
    output.write("Reaction End Moment at Right End:                             %.2f in-lb\n" %mRight)
    output.write("Slope of Beam at Left End:                                    %.2f rad\n" %thetaLeft)
    output.write("Slope of Beam at Right End:                                   %.2f rad\n" %thetaRight)
    output.write("Deflection of Beam at Left End:                               %.2f in\n" %yLeft)
    output.write("Deflection of Beam at Right End:                              %.2f in\n" %yRight)
    output.close()

def writeFile3(moment, length, distance, modOfElas, momOfInert, rLeft, rRight, mLeft, mRight, thetaLeft, thetaRight, yLeft, yRight):
    #Creates and writes the output file for Intermediate Moment calculations
    fileName = raw_input("Output File Name: ") + ".txt"
    output = open(fileName, 'w')
    project = raw_input("Project Number: ")
    output.write("""    
    Roark Equations for Stress and Strain
    Straight Beam
    Concentrated Intermediate Moment

    Program Release 20130116
    """)
    output.write("\n    Project Number    %s\n" %(project))
    output.write("    Calculated %s\n" %(str(datetime.now())[:19]))
    output.write("\n\nINPUT DATA\n\n")
    output.write("Concentrated Moment:                                              %.2f in-lb\n" %moment)
    output.write("Length of Beam:                                                   %.2f in\n" %length)
    output.write("Distance from Left End of Beam to Concentrated Moment Location:   %.2f in\n" %distance)
    output.write("Modulus of Elasticity of Material:                                %.2f lb/in2\n" %modOfElas)
    output.write("Area Moment of Inertia of Section:                                %.2f in4\n" %momOfInert)
    output.write("\n\nOUTPUT DATA\n\n")
    output.write("Vertical End Reaction at Left End:                                %.2f lb\n" %rLeft)
    output.write("Vertical End Reaction at Right End:                               %.2f lb\n" %rRight)
    output.write("Reaction End Moment at Left End:                                  %.2f in-lb\n" %mLeft)
    output.write("Reaction End Moment at Right End:                                 %.2f in-lb\n" %mRight)
    output.write("Slope of Beam at Left End:                                        %.2f rad\n" %thetaLeft)
    output.write("Slope of Beam at Right End:                                       %.2f rad\n" %thetaRight)
    output.write("Deflection of Beam at Left End:                                   %.2f in\n" %yLeft)
    output.write("Deflection of Beam at Right End:                                  %.2f in\n" %yRight)
    output.close()

def writeFile4(theta, length, distance, modOfElas, momOfInert, rLeft, rRight, mLeft, mRight, thetaLeft, thetaRight, yLeft, yRight):
    #Creates and writes the output file for Angular Deformation calculations
    fileName = raw_input("Output File Name: ") + ".txt"
    output = open(fileName, 'w')
    project = raw_input("Project Number: ")
    output.write("""
    Roark Equations for Stress and Strain
    Straight Beam
    Intermediate External Angular Deformation

    Program Release 20130116
    """)
    output.write("\n    Project Number    %s\n" %(project))
    output.write("    Calculated %s\n" %(str(datetime.now())[:19]))
    output.write("\n\nINPUT DATA\n\n")
    output.write("Angular Deformation:                                              %.2f deg\n" %theta)
    output.write("Length of Beam:                                                   %.2f in\n" %length)
    output.write("Distance from Left End of Beam to Angular Deformation Location:   %.2f in\n" %distance)
    output.write("Modulus of Elasticity of Material:                                %.2f lb/in2\n" %modOfElas)
    output.write("Area Moment of Inertia of Section:                                %.2f in4\n" %momOfInert)
    output.write("\n\nOUTPUT DATA\n\n")
    output.write("Vertical End Reaction at Left End:                                %.2f lb\n" %rLeft)
    output.write("Vertical End Reaction at Right End:                               %.2f lb\n" %rRight)
    output.write("Reaction End Moment at Left End:                                  %.2f in-lb\n" %mLeft)
    output.write("Reaction End Moment at Right End:                                 %.2f in-lb\n" %mRight)
    output.write("Slope of Beam at Left End:                                        %.2f rad\n" %thetaLeft)
    output.write("Slope of Beam at Right End:                                       %.2f rad\n" %thetaRight)
    output.write("Deflection of Beam at Left End:                                   %.2f in\n" %yLeft)
    output.write("Deflection of Beam at Right End:                                  %.2f in\n" %yRight)
    output.close()

def writeFile5(delta, length, distance, modOfElas, momOfInert, rLeft, rRight, mLeft, mRight, thetaLeft, thetaRight, yLeft, yRight):
    #Creates and writes the output file for Lateral Displacement calculations
    fileName = raw_input("Output File Name: ") + ".txt"
    output = open(fileName, 'w')
    project = raw_input("Project Number: ")
    output.write("""
    Roark Equations for Stress and Strain
    Straight Beam
    Intermediate External Lateral Displacement

    Program Release 20130116
    """)
    output.write("\n    Project Number    %s\n" %(project))
    output.write("    Calculated %s\n" %(str(datetime.now())[:19]))
    output.write("\n\nINPUT DATA\n\n")
    output.write("Lateral Displacement:                                             %.2f in\n" %delta)
    output.write("Length of Beam:                                                   %.2f in\n" %length)
    output.write("Distance from Left End of Beam to Lateral Displacement Location:  %.2f in\n" %distance)
    output.write("Modulus of Elasticity of Material:                                %.2f lb/in2\n" %modOfElas)
    output.write("Area Moment of Inertia of Section:                                %.2f in4\n" %momOfInert)
    output.write("\n\nOUTPUT DATA\n\n")
    output.write("Vertical End Reaction at Left End:                                %.2f lb\n" %rLeft)
    output.write("Vertical End Reaction at Right End:                               %.2f lb\n" %rRight)
    output.write("Reaction End Moment at Left End:                                  %.2f in-lb\n" %mLeft)
    output.write("Reaction End Moment at Right End:                                 %.2f in-lb\n" %mRight)
    output.write("Slope of Beam at Left End:                                        %.2f rad\n" %thetaLeft)
    output.write("Slope of Beam at Right End:                                       %.2f rad\n" %thetaRight)
    output.write("Deflection of Beam at Left End:                                   %.2f in\n" %yLeft)
    output.write("Deflection of Beam at Right End:                                  %.2f in\n" %yRight)
    output.close()

def writeFile6(temp1, temp2, gamma, length, depth, distance, modOfElas, momOfInert, rLeft, rRight, mLeft, mRight, thetaLeft, thetaRight, yLeft, yRight):
    #Creates and writes the output file for Temperature Variation calculations
    fileName = raw_input("Output File Name: ") + ".txt"
    output = open(fileName, 'w')
    project = raw_input("Project Number: ")
    output.write("""
    Roark Equations for Stress and Strain
    Straight Beam
    Uniform Temperature Variation Along Beam

    Program Release 20130116
    """)
    output.write("\n    Project Number    %s\n" %(project))
    output.write("    Calculated %s\n" %(str(datetime.now())[:19]))
    output.write("\n\nINPUT DATA\n\n")
    output.write("Temperature at Top of Beam:                           %.2f degF\n" %temp1)
    output.write("Temperature at Bottom of Beam:                        %.2f degF\n" %temp2)
    output.write("Temperature Coefficient of Expansion:                 %.2f in/in/degF\n" %gamma)
    output.write("Length of Beam:                                       %.2f in\n" %length)
    output.write("Depth of Beam:                                        %.2f in\n" %depth)
    output.write("Distance from Left End of Beam to Point of Interest:  %.2f in\n" %distance)
    output.write("Modulus of Elasticity of Material:                    %.2f lb/in2\n" %modOfElas)
    output.write("Area Moment of Inertia of Section:                    %.2f in4\n" %momOfInert)
    output.write("\n\nOUTPUT DATA\n\n")
    output.write("Vertical End Reaction at Left End:                    %.2f lb\n" %rLeft)
    output.write("Vertical End Reaction at Right End:                   %.2f lb\n" %rRight)
    output.write("Reaction End Moment at Left End:                      %.2f in-lb\n" %mLeft)
    output.write("Reaction End Moment at Right End:                     %.2f in-lb\n" %mRight)
    output.write("Slope of Beam at Left End:                            %.2f rad\n" %thetaLeft)
    output.write("Slope of Beam at Right End:                           %.2f rad\n" %thetaRight)
    output.write("Deflection of Beam at Left End:                       %.2f in\n" %yLeft)
    output.write("Deflection of Beam at Right End:                      %.2f in\n" %yRight)
    output.close()
