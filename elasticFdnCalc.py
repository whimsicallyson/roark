#Calcuations from Table 8.5:
#Shear, Moment, Slope, and Deflection Formulas for Finite-Length Beams on Elastic Foundations
#Table from Roark's Formulas for Stress and Strain, Eighth Edition

from math import cos, sin, cosh, sinh
from io import prompt, fileWriter

def beta_(width,fdnMod,modOfElas,momOfInert):
    return ((width*fdnMod)/(4.0*modOfElas*momOfInert))**.25
def c_1(beta,l):
    return cosh(beta*l)*cos(beta*l)
def c_2(beta,l):
    return cosh(beta*l)*sin(beta*l)+sinh(beta*l)*cos(beta*l)
def c_3(beta,l):
    return sinh(beta*l)*sin(beta*l)
def c_4(beta,l):
    return cosh(beta*l)*sin(beta*l)-sinh(beta*l)*cos(beta*l)
def c_a1(beta,l,a):
    return cosh(beta*(l-a))*cos(beta*(l-a))
def c_a2(beta,l,a):
    return cosh(beta*(l-a))*sin(beta*(l-a))+sinh(beta*(l-a))*cos(beta*(l-a))
def c_a3(beta,l,a):
    return sinh(beta*(l-a))*sin(beta*(l-a))
def c_a4(beta,l,a):
    return cosh(beta*(l-a))*sin(beta*(l-a))-sinh(beta*(l-a))*cos(beta*(l-a))
def c_a5(beta,l,a):
    return 1-ca1(beta,l,a)
def c_a6(beta,l,a):
    return 2*beta*(l-a)-ca2(beta,l,a)
def c_11(beta,l):
    return sinh(beta*l)**2-sin(beta*l)**2
def c_12(beta,l):
    return cosh(beta*l)*sinh(beta*l)+cos(beta*l)*sin(beta*l)
def c_13(beta,l):
    return cosh(beta*l)*sinh(beta*l)-cos(beta*l)*sin(beta*l)
def c_14(beta,l):
    return sinh(beta*l)**2+sin(beta*l)**2


def promptFileAll():

    length = prompt("Length of Beam (in): ")
    modOfElas = prompt("Modulus of Elasticity of Material (lb/in2): ")
    momOfInert = prompt("Area Moment of Inertia of Section (in4): ")
    fdnMod = prompt("Foundation Modulus (lb/in2/in): ")
    width = prompt("Beam Width (in): ")

    return (length, modOfElas, momOfInert, fdnMod, width)

def promptFile1():
    #User Input Section for Intermediate Load

    load = prompt("Concentrated Load (lb): ")
    distance = prompt("Distance from left end to concentrated load (in): ")
    length, modOfElas, momOfInert, fdnMod, width = promptFileAll()
    
    return (load, length, distance, modOfElas, momOfInert, fdnMod, width)

def promptFile2():
    #User Input Section for Uniformly Distributed Load

    load = prompt("Unit Load (lb/in): ")
    distance = prompt("Distance from left end to left edge of distributed load (in): ")
    length, modOfElas, momOfInert, fdnMod, width = promptFileAll()
    
    return (load, length, distance, modOfElas, momOfInert, fdnMod, width)

def promptFile3():
    #User Input section for uniformly increasing load
    
    load = prompt("Unit Load (lb/in): ")
    distance = prompt("Distance from left end to left edge of distributed load (in): ")
    length, modOfElas, momOfInert, fdnMod, width = promptFileAll()
    
    return (load, length, distance, modOfElas, momOfInert, fdnMod, width)

def promptFile4():
    #user input section for concentrated intermediate moment
    moment = prompt("Applied Moment (in-lb): ")         
    distance = prompt("Distance from left end to applied moment (in): ")
    length, modOfElas, momOfInert, fdnMod, width = promptFileAll()
    
    return (moment, length, distance, modOfElas, momOfInert, fdnMod, width)

def promptFile5():
    #user input section for angular displacement

    angle = prompt("Angular Displacement (rad): ")
    distance = prompt("Distance from left end to angular displacement (in): ")
    length, modOfElas, momOfInert, fdnMod, width = promptFileAll()
    
    return (angle, length, distance, modOfElas, momOfInert, fdnMod, width)

def promptFile6():
    #user input section for lateral displacement
    delta = prompt("Lateral Displacement (in): ")
    distance = prompt("Distance from left end to lateral displacement (in): ")
    length, modOfElas, momOfInert, fdnMod, width = promptFileAll()
    
    return (delta, length, distance, modOfElas, momOfInert, fdnMod, width)

def promptFile7():
    #user input section for temperature variation
    t1 = prompt("Temperature on Top Face (degF): ")
    t2 = prompt("Temperature on Bottom Face (degF): ")
    gamma = prompt("Temperature Coefficient of Expansion (in/in/degF): ")
    length, modOfElas, momOfInert, fdnMod, width = promptFileAll()
    depth = prompt("Beam Depth (in): ")

    return (t1, t2, gamma, length, modOfElas, momOfInert, fdnMod, width, depth)

def elasticFdn1A():
    #Concentrated Intermediate Load
    #Left End Free, Right End Free

    load, length, distance, modOfElas, momOfInert, fdnMod, width = promptFile1()

    beta = beta_(width,fdnMod,modOfElas,momOfInert)
    c2 = c_2(beta,length)
    ca2 = c_a2(beta,length,distance)
    c3 = c_3(beta,length)
    ca1 = c_a1(beta,length,distance)
    c11 = c_11(beta,length)
    c4 = c_4(beta,length)
    
    r = 0
    m = 0
    theta = load/(2*modOfElas*momOfInert*beta**2)*((c2*ca2-2*c3*ca1)/c11)
    y = load/(2*modOfElas*momOfInert*beta**3)*((c4*ca1-c3*ca2)/c11)

    writeFile1(load, length, distance, modOfElas, momOfInert, fdnMod, width, r, m, theta, y)
    
def elasticFdn1B():
    #Concentrated Intermediate Load
    #Left End Free, Right End Guided

    load, length, distance, modOfElas, momOfInert, fdnMod, width = promptFile1()

    beta = beta_(width,fdnMod,modOfElas,momOfInert)
    c1 = c_1(beta,length)
    c2 = c_2(beta,length)
    ca3 = c_a3(beta,length,distance)
    c3 = c_3(beta,length)
    ca1 = c_a1(beta,length,distance)
    c12 = c_12(beta,length)
    c4 = c_4(beta,length)
    
    r = 0
    m = 0
    theta = load/(2*modOfElas*momOfInert*beta**2)*((c2*ca3-c4*ca1)/c12)
    y = -load/(2*modOfElas*momOfInert*beta**3)*((c1*ca1-c3*ca3)/c12)

    writeFile1(load, length, distance, modOfElas, momOfInert, fdnMod, width, r, m, theta, y)

def elasticFdn1C():
    #Concentrated Intermediate Load
    #Left End Free, Right End Simply Supported

    load, length, distance, modOfElas, momOfInert, fdnMod, width = promptFile1()
    
    beta = beta_(width,fdnMod,modOfElas,momOfInert)
    c1 = c_1(beta,length)
    c2 = c_2(beta,length)
    ca2 = c_a2(beta,length,distance)
    c3 = c_3(beta,length)
    ca4 = c_a4(beta,length,distance)
    c13 = c_13(beta,length)
    c4 = c_4(beta,length)
    
    r = 0
    m = 0
    theta = load/(2*modOfElas*momOfInert*beta**2)*((c1*ca2+c3*ca4)/c13)
    y = -load/(4*modOfElas*momOfInert*beta**3)*((c4*ca4+c2*ca2)/c13)

    writeFile1(load, length, distance, modOfElas, momOfInert, fdnMod, width, r, m, theta, y)

def elasticFdn1D():
    #Concentrated Intermediate Load
    #Left End Free, Right End Fixed

    load, length, distance, modOfElas, momOfInert, fdnMod, width = promptFile1()

    beta = beta_(width,fdnMod,modOfElas,momOfInert)
    c2 = c_2(beta,length)
    ca3 = c_a3(beta,length,distance)
    c1 = c_1(beta,length)
    ca4 = c_a4(beta,length,distance)
    c11 = c_11(beta,length)
    c4 = c_4(beta,length)
    
    r = 0
    m = 0
    theta = load/(2*modOfElas*momOfInert*beta**2)*((2*c1*ca3+c4*ca4)/(2+c11))
    y = load/(2*modOfElas*momOfInert*beta**3)*((c1*ca4-c2*ca3)/(2+c11))

    writeFile1(load, length, distance, modOfElas, momOfInert, fdnMod, width, r, m, theta, y)

def elasticFdn1E():
    #Concentrated Intermediate Load
    #Left End Guided, Right End Free

    load, length, distance, modOfElas, momOfInert, fdnMod, width = promptFile1()

    beta = beta_(width,fdnMod,modOfElas,momOfInert)
    c1 = c_1(beta,length)
    c2 = c_2(beta,length)
    ca2 = c_a2(beta,length,distance)
    c3 = c_3(beta,length)
    ca1 = c_a1(beta,length,distance)
    c12 = c_12(beta,length)
    c4 = c_4(beta,length)
    
    r = 0
    theta = 0
    m = load/(2*beta)*((c2*ca2-2*c3*ca1)/c12)
    y = -load/(4*modOfElas*momOfInert*beta**3)*((2*c1*ca1+c4*ca2)/c12)

    writeFile1(load, length, distance, modOfElas, momOfInert, fdnMod, width, r, m, theta, y)

def elasticFdn1F():
    #Concentrated Intermediate Load
    #Left End Guided, Right End Guided

    load, length, distance, modOfElas, momOfInert, fdnMod, width = promptFile1()

    beta = beta_(width,fdnMod,modOfElas,momOfInert)
    c2 = c_2(beta,length)
    ca3 = c_a3(beta,length,distance)
    ca1 = c_a1(beta,length,distance)
    c14 = c_14(beta,length)
    c4 = c_4(beta,length)
    
    r = 0
    theta = 0
    m = load/(2*beta)*((c2*ca3-c4*ca1)/c14)
    y = -load/(4*modOfElas*momOfInert*beta**3)*((c2*ca1+c4*ca3)/c14)

    writeFile1(load, length, distance, modOfElas, momOfInert, fdnMod, width, r, m, theta, y)

def elasticFdn1G():
    #Concentrated Intermediate Load
    #Left End Guided, Right End Simply Supported

    load, length, distance, modOfElas, momOfInert, fdnMod, width = promptFile1()

    beta = beta_(width,fdnMod,modOfElas,momOfInert)
    c1 = c_1(beta,length)
    ca2 = c_a2(beta,length,distance)
    c3 = c_3(beta,length)
    ca4 = c_a4(beta,length,distance)
    c11 = c_11(beta,length)
    
    r = 0
    theta = 0
    m = load/(2*beta)*((c1*ca2+c3*ca4)/(1+c11))
    y = load/(4*modOfElas*momOfInert*beta**3)*((c1*ca4+c3*ca2)/(1+c11))
    
    writeFile1(load, length, distance, modOfElas, momOfInert, fdnMod, width, r, m, theta, y)

def elasticFdn1H():
    #Concentrated Intermediate Load
    #Left End Guided, Right End Fixed

    load, length, distance, modOfElas, momOfInert, fdnMod, width = promptFile1()

    beta = beta_(width,fdnMod,modOfElas,momOfInert)
    c1 = c_1(beta,length)
    c2 = c_2(beta,length)
    ca3 = c_a3(beta,length,distance)
    c3 = c_3(beta,length)
    ca4 = c_a4(beta,length,distance)
    c12 = c_12(beta,length)
    c4 = c_4(beta,length)
    
    r = 0
    theta = 0
    m = load/(2*beta)*((2*c1*ca3+c4*ca4)/c12)
    y = load/(4*modOfElas*momOfInert*beta**3)*((c2*ca4-2*c3*ca3)/c12)

    writeFile1(load, length, distance, modOfElas, momOfInert, fdnMod, width, r, m, theta, y)

def elasticFdn1I():
    #Concentrated Intermediate Load
    #Left End Simply Supported, Right End Free

    load, length, distance, modOfElas, momOfInert, fdnMod, width = promptFile1()

    beta = beta_(width,fdnMod,modOfElas,momOfInert)
    c1 = c_1(beta,length)
    c2 = c_2(beta,length)
    ca1 = c_a1(beta,length,distance)
    c3 = c_3(beta,length)
    ca2 = c_a2(beta,length,distance)
    c13 = c_13(beta,length)
    c4 = c_4(beta,length)
    
    m = 0
    y = 0
    r = load*((c3*ca2+c4*ca1)/c13)
    theta = load/(2*modOfElas*momOfInert*beta**2)*((c1*ca2-c2*ca1)/c13)

    writeFile1(load, length, distance, modOfElas, momOfInert, fdnMod, width, r, m, theta, y)

def elasticFdn1J():
    #Concentrated Intermediate Load
    #Left End Simply Supported, Right End Guided

    load, length, distance, modOfElas, momOfInert, fdnMod, width = promptFile1()

    beta = beta_(width,fdnMod,modOfElas,momOfInert)
    c1 = c_1(beta,length)
    ca1 = c_a1(beta,length,distance)
    c3 = c_3(beta,length)
    ca3 = c_a3(beta,length,distance)
    c11 = c_11(beta,length)
    
    m = 0
    y = 0
    r = load*((c1*ca1+c3*ca3)/(1+c11))
    theta = load/(2*modOfElas*momOfInert*beta**2)*((c1*ca3-c3*ca1)/(1+c11))

    writeFile1(load, length, distance, modOfElas, momOfInert, fdnMod, width, r, m, theta, y)
    
def elasticFdn1K():
    #Concentrated Intermediate Load
    #Left End Simply Supported, Right End Simply Supported

    load, length, distance, modOfElas, momOfInert, fdnMod, width = promptFile1()

    beta = beta_(width,fdnMod,modOfElas,momOfInert)
    c2 = c_2(beta,length)
    ca2 = c_a2(beta,length,distance)
    ca4 = c_a4(beta,length,distance)
    c14 = c_14(beta,length)
    c4 = c_4(beta,length)
    
    m = 0
    y = 0
    r = (load/2.0)*((c2*ca2+c4*ca4)/c14)
    theta = load/(4*modOfElas*momOfInert*beta**2)*((c2*ca4-c4*ca2)/c14)

    writeFile1(load, length, distance, modOfElas, momOfInert, fdnMod, width, r, m, theta, y)
    
def elasticFdn1L():
    #Concentrated Intermediate Load
    #Left End Simply Supported, Right End Fixed

    load, length, distance, modOfElas, momOfInert, fdnMod, width = promptFile1()

    beta = beta_(width,fdnMod,modOfElas,momOfInert)
    c1 = c_1(beta,length)
    c2 = c_2(beta,length)
    ca3 = c_a3(beta,length,distance)
    c3 = c_3(beta,length)
    ca4 = c_a4(beta,length,distance)
    c13 = c_13(beta,length)
    c4 = c_4(beta,length)
    
    m = 0
    y = 0
    r = load*((c2*ca3-c1*ca4)/c13)
    theta = load/(2*modOfElas*momOfInert*beta**2)*((c3*ca4-c4*ca3)/c13)

    writeFile1(load, length, distance, modOfElas, momOfInert, fdnMod, width, r, m, theta, y)
    
def elasticFdn1M():
    #Concentrated Intermediate Load
    #Left End Fixed, Right End Free

    load, length, distance, modOfElas, momOfInert, fdnMod, width = promptFile1()

    beta = beta_(width,fdnMod,modOfElas,momOfInert)
    c1 = c_1(beta,length)
    c2 = c_2(beta,length)
    ca1 = c_a1(beta,length,distance)
    ca2 = c_a2(beta,length,distance)
    c11 = c_11(beta,length)
    c4 = c_4(beta,length)
    
    theta = 0
    y = 0
    r = load*((2*c1*ca1+c4*ca2)/(2+c11))
    m = (load/beta)*((c1*ca2-c2*ca1)/(2+c11))

    writeFile1(load, length, distance, modOfElas, momOfInert, fdnMod, width, r, m, theta, y)
    
def elasticFdn1N():
    #Concentrated Intermediate Load
    #Left End Fixed, Right End Guided

    load, length, distance, modOfElas, momOfInert, fdnMod, width = promptFile1()

    beta = beta_(width,fdnMod,modOfElas,momOfInert)
    c1 = c_1(beta,length)
    c2 = c_2(beta,length)
    c3 = c_3(beta,length)
    ca1 = c_a1(beta,length,distance)
    ca3 = c_a3(beta,length,distance)
    c12 = c_12(beta,length)
    c4 = c_4(beta,length)
    
    theta = 0
    y = 0
    r = load*((c4*ca3+c2*ca1)/c12)
    m = (load/beta)*((c1*ca3-c3*ca1)/c12)

    writeFile1(load, length, distance, modOfElas, momOfInert, fdnMod, width, r, m, theta, y)
    
def elasticFdn1O():
    #Concentrated Intermediate Load
    #Left End Fixed, Right End Simply Supported

    load, length, distance, modOfElas, momOfInert, fdnMod, width = promptFile1()

    beta = beta_(width,fdnMod,modOfElas,momOfInert)
    c1 = c_1(beta,length)
    c2 = c_2(beta,length)
    c3 = c_3(beta,length)
    ca4 = c_a4(beta,length,distance)
    ca2 = c_a2(beta,length,distance)
    c13 = c_13(beta,length)
    c4 = c_4(beta,length)
    
    theta = 0
    y = 0
    r = load*((c3*ca2-c1*ca4)/c13)
    m = (load/(2*beta))*((c2*ca4-c4*ca2)/c13)

    writeFile1(load, length, distance, modOfElas, momOfInert, fdnMod, width, r, m, theta, y)
    
def elasticFdn1P():
    #Concentrated Intermediate Load
    #Left End Fixed, Right End Fixed

    load, length, distance, modOfElas, momOfInert, fdnMod, width = promptFile1()

    beta = beta_(width,fdnMod,modOfElas,momOfInert)
    c3 = c_3(beta,length)
    c2 = c_2(beta,length)
    ca3 = c_a3(beta,length,distance)
    ca4 = c_a4(beta,length,distance)
    c11 = c_11(beta,length)
    c4 = c_4(beta,length)
    
    theta = 0
    y = 0
    r = load*((2*c3*ca3-c2*ca4)/c11)
    m = (load/beta)*((c3*ca4-c4*ca3)/c11)

    writeFile1(load, length, distance, modOfElas, momOfInert, fdnMod, width, r, m, theta, y)
    
def elasticFdn2A():
    #Partial Uniformly Distributed Load
    #Left End Free, Right End Free

    load, length, distance, modOfElas, momOfInert, fdnMod, width = promptFile2()

    beta = beta_(width,fdnMod,modOfElas,momOfInert)
    c3 = c_3(beta,length)
    c2 = c_2(beta,length)
    ca3 = c_a3(beta,length,distance)
    ca2 = c_a2(beta,length,distance)
    c11 = c_11(beta,length)
    c4 = c_4(beta,length)
    
    r = 0
    m = 0
    theta = load/(2*modOfElas*momOfInert*beta**3)*((c2*ca3-c3*ca2)/c11)
    y = load/(4*modOfElas*momOfInert*beta**4)*((c4*ca2-2*c3*ca3)/c11)

    writeFile2(load, length, distance, modOfElas, momOfInert, fdnMod, width, r, m, theta, y)
    
def elasticFdn2B():
    #Partial Uniformly Distributed Load
    #Left End Free, Right End Guided

    load, length, distance, modOfElas, momOfInert, fdnMod, width = promptFile2()

    beta = beta_(width,fdnMod,modOfElas,momOfInert)
    c1 = c_1(beta,length)
    c3 = c_3(beta,length)
    c2 = c_2(beta,length)
    ca4 = c_a4(beta,length,distance)
    ca2 = c_a2(beta,length,distance)
    c12 = c_12(beta,length)
    c4 = c_4(beta,length)
    
    r = 0
    m = 0
    theta = load/(4*modOfElas*momOfInert*beta**3)*((c2*ca4-c4*ca2)/c12)
    y = -load/(4*modOfElas*momOfInert*beta**4)*((c1*ca2+c3*ca4)/c12)
    
    writeFile2(load, length, distance, modOfElas, momOfInert, fdnMod, width, r, m, theta, y)

def elasticFdn2C():
    #Partial Uniformly Distributed Load
    #Left End Free, Right End Simply Supported

    load, length, distance, modOfElas, momOfInert, fdnMod, width = promptFile2()

    beta = beta_(width,fdnMod,modOfElas,momOfInert)
    c1 = c_1(beta,length)
    c3 = c_3(beta,length)
    c2 = c_2(beta,length)
    ca3 = c_a3(beta,length,distance)
    ca5 = c_a5(beta,length,distance)
    c13 = c_13(beta,length)
    c4 = c_4(beta,length)
    
    r = 0
    m = 0
    theta = load/(2*modOfElas*momOfInert*beta**3)*((c1*ca3+c3*ca5)/c13)
    y = -load/(4*modOfElas*momOfInert*beta**4)*((c4*ca5+c2*ca3)/c13)

    writeFile2(load, length, distance, modOfElas, momOfInert, fdnMod, width, r, m, theta, y)
    
def elasticFdn2D():
    #Partial Uniformly Distributed Load
    #Left End Free, Right End Fixed

    load, length, distance, modOfElas, momOfInert, fdnMod, width = promptFile2()

    beta = beta_(width,fdnMod,modOfElas,momOfInert)
    c1 = c_1(beta,length)
    c2 = c_2(beta,length)
    ca4 = c_a4(beta,length,distance)
    ca5 = c_a5(beta,length,distance)
    c11 = c_11(beta,length)
    c4 = c_4(beta,length)
    
    r = 0
    m = 0
    theta = load/(2*modOfElas*momOfInert*beta**3)*((c1*ca4+c4*ca5)/(2+c11))
    y = load/(4*modOfElas*momOfInert*beta**4)*((2*c1*ca5-c2*ca4)/(2+c11))
    
    writeFile2(load, length, distance, modOfElas, momOfInert, fdnMod, width, r, m, theta, y)

def elasticFdn2E():
    #Partial Uniformly Distributed Load
    #Left End Guided, Right End Free

    load, length, distance, modOfElas, momOfInert, fdnMod, width = promptFile2()

    beta = beta_(width,fdnMod,modOfElas,momOfInert)
    c1 = c_1(beta,length)
    c3 = c_3(beta,length)
    c2 = c_2(beta,length)
    ca3 = c_a3(beta,length,distance)
    ca2 = c_a2(beta,length,distance)
    c12 = c_12(beta,length)
    c4 = c_4(beta,length)
    
    r = 0
    theta = 0
    m = load/(2*beta**2)*((c2*ca3-c3*ca2)/c12)
    y = -load/(4*modOfElas*momOfInert*beta**4)*((c1*ca2+c4*ca3)/c12)
    
    writeFile2(load, length, distance, modOfElas, momOfInert, fdnMod, width, r, m, theta, y)

def elasticFdn2F():
    #Partial Uniformly Distributed Load
    #Left End Guided, Right End Guided

    load, length, distance, modOfElas, momOfInert, fdnMod, width = promptFile2()

    beta = beta_(width,fdnMod,modOfElas,momOfInert)
    c2 = c_2(beta,length)
    ca4 = c_a4(beta,length,distance)
    ca2 = c_a2(beta,length,distance)
    c14 = c_14(beta,length)
    c4 = c_4(beta,length)
    
    r = 0
    theta = 0
    m = load/(4*beta**2)*((c2*ca4-c4*ca2)/c14)
    y = -load/(8*modOfElas*momOfInert*beta**4)*((c2*ca2+c4*ca4)/c14)

    writeFile2(load, length, distance, modOfElas, momOfInert, fdnMod, width, r, m, theta, y)

def elasticFdn2G():
    #Partial Uniformly Distributed Load
    #Left End Guided, Right End Simply Supported

    load, length, distance, modOfElas, momOfInert, fdnMod, width = promptFile2()

    beta = beta_(width,fdnMod,modOfElas,momOfInert)
    c1 = c_1(beta,length)
    c3 = c_3(beta,length)
    ca3 = c_a3(beta,length,distance)
    ca5 = c_a5(beta,length,distance)
    c11 = c_11(beta,length)
    
    r = 0
    theta = 0
    m = load/(2*beta**2)*((c1*ca3+c3*ca5)/(1+c11))
    y = load/(4*modOfElas*momOfInert*beta**4)*((c1*ca5-c3*ca3)/(1+c11))

    writeFile2(load, length, distance, modOfElas, momOfInert, fdnMod, width, r, m, theta, y)

def elasticFdn2H():
    #Partial Uniformly Distributed Load
    #Left End Guided, Right End Fixed

    load, length, distance, modOfElas, momOfInert, fdnMod, width = promptFile2()

    beta = beta_(width,fdnMod,modOfElas,momOfInert)
    c1 = c_1(beta,length)
    c3 = c_3(beta,length)
    c2 = c_2(beta,length)
    ca4 = c_a4(beta,length,distance)
    ca5 = c_a5(beta,length,distance)
    c12 = c_12(beta,length)
    c4 = c_4(beta,length)
    
    r = 0
    theta = 0
    m = load/(2*beta**2)*((c1*ca4+c4*ca5)/c12)
    y = load/(4*modOfElas*momOfInert*beta**4)*((c2*ca5-c3*ca4)/c12)

    writeFile2(load, length, distance, modOfElas, momOfInert, fdnMod, width, r, m, theta, y)

def elasticFdn2I():
    #Partial Uniformly Distributed Load
    #Left End Simply Supported, Right End Free

    load, length, distance, modOfElas, momOfInert, fdnMod, width = promptFile2()

    beta = beta_(width,fdnMod,modOfElas,momOfInert)
    c1 = c_1(beta,length)
    c2 = c_2(beta,length)
    ca3 = c_a3(beta,length,distance)
    ca2 = c_a2(beta,length,distance)
    c13 = c_13(beta,length)
    c4 = c_4(beta,length)
    
    m = 0
    y = 0
    r = load/(2*beta)*((2*c2*ca3-c4*ca2)/c13)
    theta = load/(4*modOfElas*momOfInert*beta**3)*((2*c1*ca3-c2*ca2)/c13)

    writeFile2(load, length, distance, modOfElas, momOfInert, fdnMod, width, r, m, theta, y)

def elasticFdn2J():
    #Partial Uniformly Distributed Load
    #Left End Simply Supported, Right End Guided

    load, length, distance, modOfElas, momOfInert, fdnMod, width = promptFile2()

    beta = beta_(width,fdnMod,modOfElas,momOfInert)
    c1 = c_1(beta,length)
    c3 = c_3(beta,length)
    ca2 = c_a2(beta,length,distance)
    ca4 = c_a4(beta,length,distance)
    c11 = c_11(beta,length)

    
    m = 0
    y = 0
    r = load/(2*beta)*((c1*ca2+c3*ca4)/(1+c11))
    theta = load/(4*modOfElas*momOfInert*beta**3)*((c1*ca4-c3*ca2)/(1+c11))

    writeFile2(load, length, distance, modOfElas, momOfInert, fdnMod, width, r, m, theta, y)

def elasticFdn2K():
    #Partial Uniformly Distributed Load
    #Left End Simply Supported, Right End Simply Supported

    load, length, distance, modOfElas, momOfInert, fdnMod, width = promptFile2()

    beta = beta_(width,fdnMod,modOfElas,momOfInert)
    c2 = c_2(beta,length)
    c4 = c_4(beta,length)
    ca3 = c_a3(beta,length,distance)
    ca5 = c_a5(beta,length,distance)
    c14 = c_14(beta,length)
    
    m = 0
    y = 0
    r = load/(2*beta)*((c2*ca3+c4*ca5)/c14)
    theta = load/(4*modOfElas*momOfInert*beta**3)*((c2*ca5-c4*ca3)/c14)

    writeFile2(load, length, distance, modOfElas, momOfInert, fdnMod, width, r, m, theta, y)

def elasticFdn2L():
    #Partial Uniformly Distributed Load
    #Left End Simply Supported, Right End Fixed

    load, length, distance, modOfElas, momOfInert, fdnMod, width = promptFile2()

    beta = beta_(width,fdnMod,modOfElas,momOfInert)
    c1 = c_1(beta,length)
    c2 = c_2(beta,length)
    c3 = c_3(beta,length)
    c4 = c_4(beta,length)
    ca4 = c_a4(beta,length,distance)
    ca5 = c_a5(beta,length,distance)
    c13 = c_13(beta,length)
    
    m = 0
    y = 0
    r = load/(2*beta)*((c2*ca4-2*c1*ca5)/c13)
    theta = load/(4*modOfElas*momOfInert*beta**3)*((2*c3*ca5-c4*ca4)/c13)

    writeFile2(load, length, distance, modOfElas, momOfInert, fdnMod, width, r, m, theta, y)

def elasticFdn2M():
    #Partial Uniformly Distributed Load
    #Left End Fixed, Right End Free

    load, length, distance, modOfElas, momOfInert, fdnMod, width = promptFile2()

    beta = beta_(width,fdnMod,modOfElas,momOfInert)
    c1 = c_1(beta,length)
    c2 = c_2(beta,length)
    c4 = c_4(beta,length)
    ca2 = c_a2(beta,length,distance)
    ca3 = c_a3(beta,length,distance)
    c11 = c_11(beta,length)

    
    theta = 0
    y = 0
    r = (load/beta)*((c1*ca2+c4*ca3)/(2+c11))
    m = load/(2*beta**2)*((2*c1*ca3-c2*ca2)/(2+c11))

    writeFile2(load, length, distance, modOfElas, momOfInert, fdnMod, width, r, m, theta, y)

def elasticFdn2N():
    #Partial Uniformly Distributed Load
    #Left End Fixed, Right End Guided

    load, length, distance, modOfElas, momOfInert, fdnMod, width = promptFile2()

    beta = beta_(width,fdnMod,modOfElas,momOfInert)
    c1 = c_1(beta,length)
    c2 = c_2(beta,length)
    c3 = c_3(beta,length)
    c4 = c_4(beta,length)
    ca2 = c_a2(beta,length,distance)
    ca4 = c_a4(beta,length,distance)
    c12 = c_12(beta,length)

    
    theta = 0
    y = 0
    r = load/(2*beta)*((c4*ca4+c2*ca2)/c12)
    m = load/(2*beta**2)*((c1*ca4-c3*ca2)/c12)

    writeFile2(load, length, distance, modOfElas, momOfInert, fdnMod, width, r, m, theta, y)

def elasticFdn2O():
    #Partial Uniformly Distributed Load
    #Left End Fixed, Right End Simply Supported

    load, length, distance, modOfElas, momOfInert, fdnMod, width = promptFile2()

    beta = beta_(width,fdnMod,modOfElas,momOfInert)
    c1 = c_1(beta,length)
    c2 = c_2(beta,length)
    c3 = c_3(beta,length)
    c4 = c_4(beta,length)
    ca3 = c_a3(beta,length,distance)
    ca5 = c_a5(beta,length,distance)
    c13 = c_13(beta,length)

    
    theta = 0
    y = 0
    r = (load/beta)*((c3*ca3-c1*ca5)/c13)
    m = load/(2*beta**2)*((c2*ca5-c4*ca3)/c13)

    writeFile2(load, length, distance, modOfElas, momOfInert, fdnMod, width, r, m, theta, y)

def elasticFdn2P():
    #Partial Uniformly Distributed Load
    #Left End Fixed, Right End Fixed

    load, length, distance, modOfElas, momOfInert, fdnMod, width = promptFile2()

    beta = beta_(width,fdnMod,modOfElas,momOfInert)
    c2 = c_2(beta,length)
    c3 = c_3(beta,length)
    c4 = c_4(beta,length)
    ca4 = c_a4(beta,length,distance)
    ca5 = c_a5(beta,length,distance)
    c11 = c_11(beta,length)

    
    theta = 0
    y = 0
    r = (load/beta)*((c3*ca4-c2*ca5)/c11)
    m = load/(2*beta**2)*((2*c3*ca5-c4*ca4)/c11)

    writeFile2(load, length, distance, modOfElas, momOfInert, fdnMod, width, r, m, theta, y)

def elasticFdn3A():
    #Partial Uniformly Increasing Load
    #Left End Free, Right End Free

    load, length, distance, modOfElas, momOfInert, fdnMod, width = promptFile3()

    beta = beta_(width,fdnMod,modOfElas,momOfInert)
    c2 = c_2(beta,length)
    c3 = c_3(beta,length)
    c4 = c_4(beta,length)
    ca3 = c_a3(beta,length,distance)
    ca4 = c_a4(beta,length,distance)
    c11 = c_11(beta,length)

    
    r = 0
    m = 0
    theta = (load*(c2*ca4-2*c3*ca3))/(4*modOfElas*momOfInert*beta**4*(length-distance)*c11)
    y = (load*(c4*ca3-c3*ca4))/(4*modOfElas*momOfInert*beta**5*(length-distance)*c11)

    writeFile3(load, length, distance, modOfElas, momOfInert, fdnMod, width, r, m, theta, y)

def elasticFdn3B():
    #Partial Uniformly Increasing Load
    #Left End Free, Right End Guided

    load, length, distance, modOfElas, momOfInert, fdnMod, width = promptFile3()

    beta = beta_(width,fdnMod,modOfElas,momOfInert)
    c1 = c_1(beta,length)
    c2 = c_2(beta,length)
    c3 = c_3(beta,length)
    c4 = c_4(beta,length)
    ca3 = c_a3(beta,length,distance)
    ca5 = c_a5(beta,length,distance)
    c12 = c_12(beta,length)

    
    r = 0
    m = 0
    theta = (load*(c2*ca5-c4*ca3))/(4*modOfElas*momOfInert*beta**4*(length-distance)*c12)
    y = (-load*(c1*ca3+c3*ca5))/(4*modOfElas*momOfInert*beta**5*(length-distance)*c12)

    writeFile3(load, length, distance, modOfElas, momOfInert, fdnMod, width, r, m, theta, y)

def elasticFdn3C():
    #Partial Uniformly Increasing Load
    #Left End Free, Right End Simply Supported

    load, length, distance, modOfElas, momOfInert, fdnMod, width = promptFile3()

    beta = beta_(width,fdnMod,modOfElas,momOfInert)
    c1 = c_1(beta,length)
    c2 = c_2(beta,length)
    c3 = c_3(beta,length)
    c4 = c_4(beta,length)
    ca4 = c_a4(beta,length,distance)
    ca6 = c_a6(beta,length,distance)
    c13 = c_13(beta,length)

    
    r = 0
    m = 0
    theta = (load*(c1*ca4+c3*ca6))/(4*modOfElas*momOfInert*beta**4*(length-distance)*c13)
    y = (-load*(c2*ca4+c4*ca6))/(8*modOfElas*momOfInert*beta**5*(length-distance)*c13)

    writeFile3(load, length, distance, modOfElas, momOfInert, fdnMod, width, r, m, theta, y)

def elasticFdn3D():
    #Partial Uniformly Increasing Load
    #Left End Free, Right End Fixed

    load, length, distance, modOfElas, momOfInert, fdnMod, width = promptFile3()

    beta = beta_(width,fdnMod,modOfElas,momOfInert)
    c1 = c_1(beta,length)
    c2 = c_2(beta,length)
    c4 = c_4(beta,length)
    ca5 = c_a5(beta,length,distance)
    ca6 = c_a6(beta,length,distance)
    c11 = c_11(beta,length)

    
    r = 0
    m = 0
    theta = (load*(2*c1*ca5+c4*ca6))/(4*modOfElas*momOfInert*beta**4*(length-distance)*(2+c11))
    y = (load*(c1*ca6-c2*ca5))/(4*modOfElas*momOfInert*beta**5*(length-distance)*(2+c11))

    writeFile3(load, length, distance, modOfElas, momOfInert, fdnMod, width, r, m, theta, y)

def elasticFdn3E():
    #Partial Uniformly Increasing Load
    #Left End Guided, Right End Free

    load, length, distance, modOfElas, momOfInert, fdnMod, width = promptFile3()

    beta = beta_(width,fdnMod,modOfElas,momOfInert)
    c1 = c_1(beta,length)
    c2 = c_2(beta,length)
    c3 = c_3(beta,length)
    c4 = c_4(beta,length)
    ca3 = c_a3(beta,length,distance)
    ca4 = c_a4(beta,length,distance)
    c12 = c_12(beta,length)

    
    r = 0
    theta = 0
    m = (load*(c2*ca4-2*c3*ca3))/(4*beta**3*(length-distance)*c12)
    y = (-load*(2*c1*ca3+c4*ca4))/(8*modOfElas*momOfInert*beta**5*(length-distance)*c12)

    writeFile3(load, length, distance, modOfElas, momOfInert, fdnMod, width, r, m, theta, y)

def elasticFdn3F():
    #Partial Uniformly Increasing Load
    #Left End Guided, Right End Guided

    load, length, distance, modOfElas, momOfInert, fdnMod, width = promptFile3()

    beta = beta_(width,fdnMod,modOfElas,momOfInert)
    c2 = c_2(beta,length)
    c4 = c_4(beta,length)
    ca3 = c_a3(beta,length,distance)
    ca5 = c_a5(beta,length,distance)
    c14 = c_14(beta,length)

    
    r = 0
    theta = 0
    m = (load*(c2*ca5-c4*ca3))/(4*beta**3*(length-distance)*c14)
    y = (-load*(c2*ca3+c4*ca5))/(8*modOfElas*momOfInert*beta**5*(length-distance)*c14)

    writeFile3(load, length, distance, modOfElas, momOfInert, fdnMod, width, r, m, theta, y)

def elasticFdn3G():
    #Partial Uniformly Increasing Load
    #Left End Guided, Right End Simply Supported

    load, length, distance, modOfElas, momOfInert, fdnMod, width = promptFile3()

    beta = beta_(width,fdnMod,modOfElas,momOfInert)
    c1 = c_1(beta,length)
    c3 = c_3(beta,length)
    ca4 = c_a4(beta,length,distance)
    ca6 = c_a6(beta,length,distance)
    c11 = c_11(beta,length)

    
    r = 0
    theta = 0
    m = (load*(c1*ca4+c3*ca6))/(4*beta**3*(length-distance)*(1+c11))
    y = (load*(c1*ca6-c3*ca4))/(8*modOfElas*momOfInert*beta**5*(length-distance)*(1+c11))

    writeFile3(load, length, distance, modOfElas, momOfInert, fdnMod, width, r, m, theta, y)

def elasticFdn3H():
    #Partial Uniformly Increasing Load
    #Left End Guided, Right End Fixed

    load, length, distance, modOfElas, momOfInert, fdnMod, width = promptFile3()

    beta = beta_(width,fdnMod,modOfElas,momOfInert)
    c1 = c_1(beta,length)
    c2 = c_2(beta,length)
    c3 = c_3(beta,length)
    c4 = c_4(beta,length)
    ca5 = c_a5(beta,length,distance)
    ca6 = c_a6(beta,length,distance)
    c12 = c_12(beta,length)

    
    r = 0
    theta = 0
    m = (load*(2*c1*ca5+c4*ca6))/(4*beta**3*(length-distance)*c12)
    y = (load*(c2*ca6-2*c3*ca5))/(8*modOfElas*momOfInert*beta**5*(length-distance)*c12)

    writeFile3(load, length, distance, modOfElas, momOfInert, fdnMod, width, r, m, theta, y)

def elasticFdn3I():
    #Partial Uniformly Increasing Load
    #Left End Simply Supported, Right End Free

    load, length, distance, modOfElas, momOfInert, fdnMod, width = promptFile3()

    beta = beta_(width,fdnMod,modOfElas,momOfInert)
    c1 = c_1(beta,length)
    c2 = c_2(beta,length)
    c3 = c_3(beta,length)
    c4 = c_4(beta,length)
    ca3 = c_a3(beta,length,distance)
    ca4 = c_a4(beta,length,distance)
    c13 = c_13(beta,length)

    
    m = 0
    y = 0
    r = (load*(c3*ca4-c4*ca3))/(2*beta**2*(length-distance)*c13)
    theta = (load*(c1*ca4-c2*ca3))/(4*modOfElas*momOfInert*beta**4*(length-distance)*c13)

    writeFile3(load, length, distance, modOfElas, momOfInert, fdnMod, width, r, m, theta, y)

def elasticFdn3J():
    #Partial Uniformly Increasing Load
    #Left End Simply Supported, Right End Guided

    load, length, distance, modOfElas, momOfInert, fdnMod, width = promptFile3()

    beta = beta_(width,fdnMod,modOfElas,momOfInert)
    c1 = c_1(beta,length)
    c3 = c_3(beta,length)
    ca3 = c_a3(beta,length,distance)
    ca5 = c_a5(beta,length,distance)
    c11 = c_11(beta,length)

    
    m = 0
    y = 0
    r = (load*(c1*ca3+c3*ca5))/(2*beta**2*(length-distance)*(1+c11))
    theta = (load*(c1*ca5-c3*ca3))/(4*modOfElas*momOfInert*beta**4*(length-distance)*(1+c11))

    writeFile3(load, length, distance, modOfElas, momOfInert, fdnMod, width, r, m, theta, y)

def elasticFdn3K():
    #Partial Uniformly Increasing Load
    #Left End Simply Supported, Right End Simply Supported

    load, length, distance, modOfElas, momOfInert, fdnMod, width = promptFile3()

    beta = beta_(width,fdnMod,modOfElas,momOfInert)
    c2 = c_2(beta,length)
    c4 = c_4(beta,length)
    ca4 = c_a4(beta,length,distance)
    ca6 = c_a6(beta,length,distance)
    c14 = c_14(beta,length)

    
    m = 0
    y = 0
    r = (load*(c2*ca4+c4*ca6))/(4*beta**2*(length-distance)*c14)
    theta = (load*(c2*ca6-c4*ca4))/(8*modOfElas*momOfInert*beta**4*(length-distance)*c14)

    writeFile3(load, length, distance, modOfElas, momOfInert, fdnMod, width, r, m, theta, y)

def elasticFdn3L():
    #Partial Uniformly Increasing Load
    #Left End Simply Supported, Right End Fixed

    load, length, distance, modOfElas, momOfInert, fdnMod, width = promptFile3()

    beta = beta_(width,fdnMod,modOfElas,momOfInert)
    c1 = c_1(beta,length)
    c2 = c_2(beta,length)
    c3 = c_3(beta,length)
    c4 = c_4(beta,length)
    ca5 = c_a5(beta,length,distance)
    ca6 = c_a6(beta,length,distance)
    c13 = c_13(beta,length)

    
    m = 0
    y = 0
    r = (load*(c2*ca5-c1*ca6))/(2*beta**2*(length-distance)*c13)
    theta = (load*(c3*ca6-c4*ca5))/(4*modOfElas*momOfInert*beta**4*(length-distance)*c13)

    writeFile3(load, length, distance, modOfElas, momOfInert, fdnMod, width, r, m, theta, y)

def elasticFdn3M():
    #Partial Uniformly Increasing Load
    #Left End Fixed, Right End Free

    load, length, distance, modOfElas, momOfInert, fdnMod, width = promptFile3()

    beta = beta_(width,fdnMod,modOfElas,momOfInert)
    c1 = c_1(beta,length)
    c2 = c_2(beta,length)
    c4 = c_4(beta,length)
    ca3 = c_a3(beta,length,distance)
    ca4 = c_a4(beta,length,distance)
    c11 = c_11(beta,length)

    
    theta = 0
    y = 0
    r = (load*(2*c1*ca3+c4*ca4))/(2*beta**2*(length-distance)*(2+c11))
    m = (load*(c1*ca4-c2*ca3))/(2*beta**3*(length-distance)*(2+c11))

    writeFile3(load, length, distance, modOfElas, momOfInert, fdnMod, width, r, m, theta, y)

def elasticFdn3N():
    #Partial Uniformly Increasing Load
    #Left End Fixed, Right End Guided

    load, length, distance, modOfElas, momOfInert, fdnMod, width = promptFile3()

    beta = beta_(width,fdnMod,modOfElas,momOfInert)
    c1 = c_1(beta,length)
    c2 = c_2(beta,length)
    c3 = c_3(beta,length)
    c4 = c_4(beta,length)
    ca3 = c_a3(beta,length,distance)
    ca5 = c_a5(beta,length,distance)
    c12 = c_12(beta,length)

    
    theta = 0
    y = 0
    r = (load*(c4*ca5+c2*ca3))/(2*beta**2*(length-distance)*c12)
    m = (load*(c1*ca5-c3*ca3))/(2*beta**3*(length-distance)*c12)

    writeFile3(load, length, distance, modOfElas, momOfInert, fdnMod, width, r, m, theta, y)

def elasticFdn3O():
    #Partial Uniformly Increasing Load
    #Left End Fixed, Right End Simply Supported

    load, length, distance, modOfElas, momOfInert, fdnMod, width = promptFile3()

    beta = beta_(width,fdnMod,modOfElas,momOfInert)
    c1 = c_1(beta,length)
    c2 = c_2(beta,length)
    c3 = c_3(beta,length)
    c4 = c_4(beta,length)
    ca4 = c_a4(beta,length,distance)
    ca6 = c_a6(beta,length,distance)
    c13 = c_13(beta,length)

    
    theta = 0
    y = 0
    r = (load*(c3*ca4-c1*ca6))/(2*beta**2*(length-distance)*c13)
    m = (load*(c2*ca6-c4*ca4))/(4*beta**3*(length-distance)*c13)

    writeFile3(load, length, distance, modOfElas, momOfInert, fdnMod, width, r, m, theta, y)

def elasticFdn3P():
    #Partial Uniformly Increasing Load
    #Left End Fixed, Right End Fixed

    load, length, distance, modOfElas, momOfInert, fdnMod, width = promptFile3()

    beta = beta_(width,fdnMod,modOfElas,momOfInert)
    c2 = c_2(beta,length)
    c3 = c_3(beta,length)
    c4 = c_4(beta,length)
    ca5 = c_a5(beta,length,distance)
    ca6 = c_a6(beta,length,distance)
    c11 = c_11(beta,length)

    
    theta = 0
    y = 0
    r = (load*(2*c3*ca5-c2*ca6))/(2*beta**2*(length-distance)*c11)
    m = (load*(c3*ca6-c4*ca5))/(2*beta**3*(length-distance)*c11)

    writeFile3(load, length, distance, modOfElas, momOfInert, fdnMod, width, r, m, theta, y)

def elasticFdn4A():
    #Concentrated Intermediate Moment
    #Left End Free, Right End Free

    moment, length, distance, modOfElas, momOfInert, fdnMod, width = promptFile4()

    beta = beta_(width,fdnMod,modOfElas,momOfInert)
    c2 = c_2(beta,length)
    c3 = c_3(beta,length)
    c4 = c_4(beta,length)
    ca1 = c_a1(beta,length,distance)
    ca4 = c_a4(beta,length,distance)
    c11 = c_11(beta,length)

    r = 0
    m = 0
    theta = -moment/(modOfElas*momOfInert*beta)*((c3*ca4+c2*ca1)/c11)
    y = moment/(2*modOfElas*momOfInert*beta**2)*((2*c3*ca1+c4*ca4)/c11)

    writeFile4(moment, length, distance, modOfElas, momOfInert, fdnMod, width, r, m, theta, y)

def elasticFdn4B():
    #Concentrated Intermediate Moment
    #Left End Free, Right End Guided

    moment, length, distance, modOfElas, momOfInert, fdnMod, width = promptFile4()

    beta = beta_(width,fdnMod,modOfElas,momOfInert)
    c1 = c_1(beta,length)
    c2 = c_2(beta,length)
    c3 = c_3(beta,length)
    c4 = c_4(beta,length)
    ca2 = c_a2(beta,length,distance)
    ca4 = c_a4(beta,length,distance)
    c12 = c_12(beta,length)

    r = 0
    m = 0
    theta = -moment/(2*modOfElas*momOfInert*beta)*((c2*ca2+c4*ca4)/c12)
    y = moment/(2*modOfElas*momOfInert*beta**2)*((c3*ca2-c1*ca4)/c12)

    writeFile4(moment, length, distance, modOfElas, momOfInert, fdnMod, width, r, m, theta, y)

def elasticFdn4C():
    #Concentrated Intermediate Moment
    #Left End Free, Right End Simply Supported

    moment, length, distance, modOfElas, momOfInert, fdnMod, width = promptFile4()

    beta = beta_(width,fdnMod,modOfElas,momOfInert)
    c1 = c_1(beta,length)
    c2 = c_2(beta,length)
    c3 = c_3(beta,length)
    c4 = c_4(beta,length)
    ca1 = c_a1(beta,length,distance)
    ca3 = c_a3(beta,length,distance)
    c13 = c_13(beta,length)

    r = 0
    m = 0
    theta = -moment/(modOfElas*momOfInert*beta)*((c1*ca1+c3*ca3)/c13)
    y = moment/(2*modOfElas*momOfInert*beta**2)*((c4*ca3+c2*ca1)/c13)

    writeFile4(moment, length, distance, modOfElas, momOfInert, fdnMod, width, r, m, theta, y)

def elasticFdn4D():
    #Concentrated Intermediate Moment
    #Left End Free, Right End Fixed

    moment, length, distance, modOfElas, momOfInert, fdnMod, width = promptFile4()

    beta = beta_(width,fdnMod,modOfElas,momOfInert)
    c1 = c_1(beta,length)
    c2 = c_2(beta,length)
    c4 = c_4(beta,length)
    ca2 = c_a2(beta,length,distance)
    ca3 = c_a3(beta,length,distance)
    c11 = c_11(beta,length)

    r = 0
    m = 0
    theta = -moment/(modOfElas*momOfInert*beta)*((c1*ca2+c4*ca3)/(2+c11))
    y = -moment/(2*modOfElas*momOfInert*beta**2)*((2*c1*ca3-c2*ca2)/(2+c11))

    writeFile4(moment, length, distance, modOfElas, momOfInert, fdnMod, width, r, m, theta, y)

def elasticFdn4E():
    #Concentrated Intermediate Moment
    #Left End Guided, Right End Free

    moment, length, distance, modOfElas, momOfInert, fdnMod, width = promptFile4()

    beta = beta_(width,fdnMod,modOfElas,momOfInert)
    c1 = c_1(beta,length)
    c2 = c_2(beta,length)
    c3 = c_3(beta,length)
    c4 = c_4(beta,length)
    ca1 = c_a1(beta,length,distance)
    ca4 = c_a4(beta,length,distance)
    c12 = c_12(beta,length)

    r = 0
    theta = 0
    m = -moment*((c2*ca1+c3*ca4)/c12)
    y = -moment/(2*modOfElas*momOfInert*beta**2)*((c1*ca4-c4*ca1)/c12)

    writeFile4(moment, length, distance, modOfElas, momOfInert, fdnMod, width, r, m, theta, y)

def elasticFdn4F():
    #Concentrated Intermediate Moment
    #Left End Guided, Right End Guided

    moment, length, distance, modOfElas, momOfInert, fdnMod, width = promptFile4()

    beta = beta_(width,fdnMod,modOfElas,momOfInert)
    c2 = c_2(beta,length)
    c4 = c_4(beta,length)
    ca2 = c_a2(beta,length,distance)
    ca4 = c_a4(beta,length,distance)
    c14 = c_14(beta,length)

    r = 0
    theta = 0
    m = -moment/2.0*((c2*ca2+c4*ca4)/c14)
    y = moment/(4*modOfElas*momOfInert*beta**2)*((c4*ca2-c2*ca4)/c14)

    writeFile4(moment, length, distance, modOfElas, momOfInert, fdnMod, width, r, m, theta, y)

def elasticFdn4G():
    #Concentrated Intermediate Moment
    #Left End Guided, Right End Simply Supported

    moment, length, distance, modOfElas, momOfInert, fdnMod, width = promptFile4()

    beta = beta_(width,fdnMod,modOfElas,momOfInert)
    c1 = c_1(beta,length)
    c3 = c_3(beta,length)
    ca1 = c_a1(beta,length,distance)
    ca3 = c_a3(beta,length,distance)
    c11 = c_11(beta,length)

    r = 0
    theta = 0
    m = -moment*((c1*ca1+c3*ca3)/(1+c11))
    y = moment/(2*modOfElas*momOfInert*beta**2)*((c3*ca1-c1*ca3)/(1+c11))

    writeFile4(moment, length, distance, modOfElas, momOfInert, fdnMod, width, r, m, theta, y)

def elasticFdn4H():
    #Concentrated Intermediate Moment
    #Left End Guided, Right End Fixed

    moment, length, distance, modOfElas, momOfInert, fdnMod, width = promptFile4()

    beta = beta_(width,fdnMod,modOfElas,momOfInert)
    c1 = c_1(beta,length)
    c2 = c_2(beta,length)
    c3 = c_3(beta,length)
    c4 = c_4(beta,length)
    ca2 = c_a2(beta,length,distance)
    ca3 = c_a3(beta,length,distance)
    c12 = c_12(beta,length)

    r = 0
    theta = 0
    m = -moment*((c1*ca2+c4*ca3)/c12)
    y = moment/(2*modOfElas*momOfInert*beta**2)*((c3*ca2-c2*ca3)/c12)

    writeFile4(moment, length, distance, modOfElas, momOfInert, fdnMod, width, r, m, theta, y)

def elasticFdn4I():
    #Concentrated Intermediate Moment
    #Left End Simply Supported, Right End Free

    moment, length, distance, modOfElas, momOfInert, fdnMod, width = promptFile4()

    beta = beta_(width,fdnMod,modOfElas,momOfInert)
    c1 = c_1(beta,length)
    c2 = c_2(beta,length)
    c3 = c_3(beta,length)
    c4 = c_4(beta,length)
    ca1 = c_a1(beta,length,distance)
    ca4 = c_a4(beta,length,distance)
    c13 = c_13(beta,length)

    m = 0
    y = 0
    r = -moment*beta*((2*c3*ca1+c4*ca4)/c13)
    theta = -moment/(2*modOfElas*momOfInert*beta)*((2*c1*ca1+c2*ca4)/c13)

    writeFile4(moment, length, distance, modOfElas, momOfInert, fdnMod, width, r, m, theta, y)

def elasticFdn4J():
    #Concentrated Intermediate Moment
    #Left End Simply Supported, Right End Guided

    moment, length, distance, modOfElas, momOfInert, fdnMod, width = promptFile4()

    beta = beta_(width,fdnMod,modOfElas,momOfInert)
    c1 = c_1(beta,length)
    c3 = c_3(beta,length)
    ca2 = c_a2(beta,length,distance)
    ca4 = c_a4(beta,length,distance)
    c11 = c_11(beta,length)

    m = 0
    y = 0
    r = -moment*beta*((c3*ca2-c1*ca4)/(1+c11))
    theta = -moment/(2*modOfElas*momOfInert*beta)*((c1*ca2+c3*ca4)/(1+c11))

    writeFile4(moment, length, distance, modOfElas, momOfInert, fdnMod, width, r, m, theta, y)

def elasticFdn4K():
    #Concentrated Intermediate Moment
    #Left End Simply Supported, Right End Simply Supported

    moment, length, distance, modOfElas, momOfInert, fdnMod, width = promptFile4()

    beta = beta_(width,fdnMod,modOfElas,momOfInert)
    c2 = c_2(beta,length)
    c4 = c_4(beta,length)
    ca1 = c_a1(beta,length,distance)
    ca3 = c_a3(beta,length,distance)
    c14 = c_14(beta,length)

    m = 0
    y = 0
    r = -moment*beta*((c2*ca1+c4*ca3)/c14)
    theta = -moment/(2*modOfElas*momOfInert*beta)*((c2*ca3-c4*ca1)/c14)

    writeFile4(moment, length, distance, modOfElas, momOfInert, fdnMod, width, r, m, theta, y)

def elasticFdn4L():
    #Concentrated Intermediate Moment
    #Left End Simply Supported, Right End Fixed

    moment, length, distance, modOfElas, momOfInert, fdnMod, width = promptFile4()

    beta = beta_(width,fdnMod,modOfElas,momOfInert)
    c1 = c_1(beta,length)
    c2 = c_2(beta,length)
    c3 = c_3(beta,length)
    c4 = c_4(beta,length)
    ca2 = c_a2(beta,length,distance)
    ca3 = c_a3(beta,length,distance)
    c13 = c_13(beta,length)

    m = 0
    y = 0
    r = -moment*beta*((c2*ca2-2*c1*ca3)/c13)
    theta = -moment/(2*modOfElas*momOfInert*beta)*((2*c3*ca3-c4*ca2)/c13)

    writeFile4(moment, length, distance, modOfElas, momOfInert, fdnMod, width, r, m, theta, y)

def elasticFdn4M():
    #Concentrated Intermediate Moment
    #Left End Fixed, Right End Free

    moment, length, distance, modOfElas, momOfInert, fdnMod, width = promptFile4()

    beta = beta_(width,fdnMod,modOfElas,momOfInert)
    c1 = c_1(beta,length)
    c2 = c_2(beta,length)
    c4 = c_4(beta,length)
    ca1 = c_a1(beta,length,distance)
    ca4 = c_a4(beta,length,distance)
    c11 = c_11(beta,length)

    theta = 0
    y = 0
    r = -moment*2*beta*((c4*ca1-c1*ca4)/(2+c11))
    m = -moment*((2*c1*ca1+c2*ca4)/(2+c11))

    writeFile4(moment, length, distance, modOfElas, momOfInert, fdnMod, width, r, m, theta, y)

def elasticFdn4N():
    #Concentrated Intermediate Moment
    #Left End Fixed, Right End Guided

    moment, length, distance, modOfElas, momOfInert, fdnMod, width = promptFile4()

    beta = beta_(width,fdnMod,modOfElas,momOfInert)
    c1 = c_1(beta,length)
    c2 = c_2(beta,length)
    c3 = c_3(beta,length)
    c4 = c_4(beta,length)
    ca2 = c_a2(beta,length,distance)
    ca4 = c_a4(beta,length,distance)
    c12 = c_12(beta,length)

    theta = 0
    y = 0
    r = -moment*beta*((c4*ca2-c2*ca4)/c12)
    m = -moment*((c1*ca2+c3*ca4)/c12)

    writeFile4(moment, length, distance, modOfElas, momOfInert, fdnMod, width, r, m, theta, y)

def elasticFdn4O():
    #Concentrated Intermediate Moment
    #Left End Fixed, Right End Simply Supported

    moment, length, distance, modOfElas, momOfInert, fdnMod, width = promptFile4()

    beta = beta_(width,fdnMod,modOfElas,momOfInert)
    c1 = c_1(beta,length)
    c2 = c_2(beta,length)
    c3 = c_3(beta,length)
    c4 = c_4(beta,length)
    ca1 = c_a1(beta,length,distance)
    ca3 = c_a3(beta,length,distance)
    c13 = c_13(beta,length)

    theta = 0
    y = 0
    r = -moment*2*beta*((c3*ca1-c1*ca3)/c13)
    m = -moment*((c2*ca3-c4*ca1)/c13)

    writeFile4(moment, length, distance, modOfElas, momOfInert, fdnMod, width, r, m, theta, y)

def elasticFdn4P():
    #Concentrated Intermediate Moment
    #Left End Fixed, Right End Fixed

    moment, length, distance, modOfElas, momOfInert, fdnMod, width = promptFile4()

    beta = beta_(width,fdnMod,modOfElas,momOfInert)
    c2 = c_2(beta,length)
    c3 = c_3(beta,length)
    c4 = c_4(beta,length)
    ca2 = c_a2(beta,length,distance)
    ca3 = c_a3(beta,length,distance)
    c11 = c_11(beta,length)

    theta = 0
    y = 0
    r = -moment*2*beta*((c3*ca2-c2*ca3)/c11)
    m = -moment*((2*c3*ca3-c4*ca2)/c11)

    writeFile4(moment, length, distance, modOfElas, momOfInert, fdnMod, width, r, m, theta, y)

def elasticFdn5A():
    #Externally Created Concentrated Angular Displacement
    #Left End Free, Right End Free

    angle, length, distance, modOfElas, momOfInert, fdnMod, width = promptFile5()

    beta = beta_(width,fdnMod,modOfElas,momOfInert)
    c2 = c_2(beta,length)
    c3 = c_3(beta,length)
    c4 = c_4(beta,length)
    ca3 = c_a3(beta,length,distance)
    ca4 = c_a4(beta,length,distance)
    c11 = c_11(beta,length)

    r = 0
    m = 0
    theta = angle*((c2*ca4-2*c3*ca3)/c11)
    y = angle/beta*((c4*ca3-c3*ca4)/c11)

    writeFile5(angle, length, distance, modOfElas, momOfInert, fdnMod, width, r, m, theta, y)

def elasticFdn5B():
    #Externally Created Concentrated Angular Displacement
    #Left End Free, Right End Guided

    angle, length, distance, modOfElas, momOfInert, fdnMod, width = promptFile5()

    beta = beta_(width,fdnMod,modOfElas,momOfInert)
    c1 = c_1(beta,length)
    c2 = c_2(beta,length)
    c3 = c_3(beta,length)
    c4 = c_4(beta,length)
    ca1 = c_a1(beta,length,distance)
    ca3 = c_a3(beta,length,distance)
    c12 = c_12(beta,length)

    r = 0
    m = 0
    theta = -angle*((c2*ca1+c4*ca3)/c12)
    y = angle/beta*((c3*ca1-c1*ca3)/c12)

    writeFile5(angle, length, distance, modOfElas, momOfInert, fdnMod, width, r, m, theta, y)

def elasticFdn5C():
    #Externally Created Concentrated Angular Displacement
    #Left End Free, Right End Simply Supported

    angle, length, distance, modOfElas, momOfInert, fdnMod, width = promptFile5()

    beta = beta_(width,fdnMod,modOfElas,momOfInert)
    c1 = c_1(beta,length)
    c2 = c_2(beta,length)
    c3 = c_3(beta,length)
    c4 = c_4(beta,length)
    ca2 = c_a2(beta,length,distance)
    ca4 = c_a4(beta,length,distance)
    c13 = c_13(beta,length)

    r = 0
    m = 0
    theta = angle*((c1*ca4-c3*ca2)/c13)
    y = angle/(2*beta)*((c4*ca2-c2*ca4)/c13)

    writeFile5(angle, length, distance, modOfElas, momOfInert, fdnMod, width, r, m, theta, y)

def elasticFdn5D():
    #Externally Created Concentrated Angular Displacement
    #Left End Free, Right End Fixed

    angle, length, distance, modOfElas, momOfInert, fdnMod, width = promptFile5()

    beta = beta_(width,fdnMod,modOfElas,momOfInert)
    c1 = c_1(beta,length)
    c2 = c_2(beta,length)
    c4 = c_4(beta,length)
    ca1 = c_a1(beta,length,distance)
    ca2 = c_a2(beta,length,distance)
    c11 = c_11(beta,length)

    r = 0
    m = 0
    theta = -angle*((2*c1*ca1+c4*ca2)/(2+c11))
    y = -angle/beta*((c1*ca2-c2*ca1)/(2+c11))

    writeFile5(angle, length, distance, modOfElas, momOfInert, fdnMod, width, r, m, theta, y)

def elasticFdn5E():
    #Externally Created Concentrated Angular Displacement
    #Left End Guided, Right End Free

    angle, length, distance, modOfElas, momOfInert, fdnMod, width = promptFile5()

    beta = beta_(width,fdnMod,modOfElas,momOfInert)
    c1 = c_1(beta,length)
    c2 = c_2(beta,length)
    c3 = c_3(beta,length)
    c4 = c_4(beta,length)
    ca3 = c_a3(beta,length,distance)
    ca4 = c_a4(beta,length,distance)
    c12 = c_12(beta,length)

    r = 0
    theta = 0
    m = angle*modOfElas*momOfInert*beta*((c2*ca4-2*c3*ca3)/c12)
    y = -angle/(2*beta)*((2*c1*ca3+c4*ca4)/c12)

    writeFile5(angle, length, distance, modOfElas, momOfInert, fdnMod, width, r, m, theta, y)

def elasticFdn5F():
    #Externally Created Concentrated Angular Displacement
    #Left End Guided, Right End Guided

    angle, length, distance, modOfElas, momOfInert, fdnMod, width = promptFile5()

    beta = beta_(width,fdnMod,modOfElas,momOfInert)
    c2 = c_2(beta,length)
    c4 = c_4(beta,length)
    ca1 = c_a1(beta,length,distance)
    ca3 = c_a3(beta,length,distance)
    c14 = c_14(beta,length)

    r = 0
    theta = 0
    m = -angle*modOfElas*momOfInert*beta*((c2*ca1+c4*ca3)/c14)
    y = angle/(2*beta)*((c4*ca1-c2*ca3)/c14)
    
    writeFile5(angle, length, distance, modOfElas, momOfInert, fdnMod, width, r, m, theta, y)
    
def elasticFdn5G():
    #Externally Created Concentrated Angular Displacement
    #Left End Guided, Right End Simply Supported

    angle, length, distance, modOfElas, momOfInert, fdnMod, width = promptFile5()

    beta = beta_(width,fdnMod,modOfElas,momOfInert)
    c1 = c_1(beta,length)
    c3 = c_3(beta,length)
    ca2 = c_a2(beta,length,distance)
    ca4 = c_a4(beta,length,distance)
    c11 = c_11(beta,length)

    r = 0
    theta = 0
    m = angle*modOfElas*momOfInert*beta*((c1*ca4-c3*ca2)/(1+c11))
    y = -angle/(2*beta)*((c1*ca2+c3*ca4)/(1+c11))

    writeFile5(angle, length, distance, modOfElas, momOfInert, fdnMod, width, r, m, theta, y)
    
def elasticFdn5H():
    #Externally Created Concentrated Angular Displacement
    #Left End Guided, Right End Fixed

    angle, length, distance, modOfElas, momOfInert, fdnMod, width = promptFile5()

    beta = beta_(width,fdnMod,modOfElas,momOfInert)
    c1 = c_1(beta,length)
    c2 = c_2(beta,length)
    c3 = c_3(beta,length)
    c4 = c_4(beta,length)
    ca1 = c_a1(beta,length,distance)
    ca2 = c_a2(beta,length,distance)
    c12 = c_12(beta,length)

    r = 0
    theta = 0
    m = -angle*modOfElas*momOfInert*beta*((2*c1*ca1+c4*ca2)/c12)
    y = angle/(2*beta)*((2*c3*ca1-c2*ca2)/c12)

    writeFile5(angle, length, distance, modOfElas, momOfInert, fdnMod, width, r, m, theta, y)
    
def elasticFdn5I():
    #Externally Created Concentrated Angular Displacement
    #Left End Simply Supported, Right End Free

    angle, length, distance, modOfElas, momOfInert, fdnMod, width = promptFile5()

    beta = beta_(width,fdnMod,modOfElas,momOfInert)
    c1 = c_1(beta,length)
    c2 = c_2(beta,length)
    c3 = c_3(beta,length)
    c4 = c_4(beta,length)
    ca3 = c_a3(beta,length,distance)
    ca4 = c_a4(beta,length,distance)
    c13 = c_13(beta,length)

    m = 0
    y = 0
    r = angle*2*modOfElas*momOfInert*beta**2*((c3*ca4-c4*ca3)/c13)
    theta = angle*((c1*ca4-c2*ca3)/c13)

    writeFile5(angle, length, distance, modOfElas, momOfInert, fdnMod, width, r, m, theta, y)
    
def elasticFdn5J():
    #Externally Created Concentrated Angular Displacement
    #Left End Simply Supported, Right End Guided

    angle, length, distance, modOfElas, momOfInert, fdnMod, width = promptFile5()

    beta = beta_(width,fdnMod,modOfElas,momOfInert)
    c1 = c_1(beta,length)
    c3 = c_3(beta,length)
    ca1 = c_a1(beta,length,distance)
    ca3 = c_a3(beta,length,distance)
    c11 = c_11(beta,length)

    m = 0
    y = 0
    r = angle*2*modOfElas*momOfInert*beta**2*((c1*ca3-c3*ca1)/(1+c11))
    theta = -angle*((c1*ca1+c3*ca3)/(1+c11))

    writeFile5(angle, length, distance, modOfElas, momOfInert, fdnMod, width, r, m, theta, y)

def elasticFdn5K():
    #Externally Created Concentrated Angular Displacement
    #Left End Simply Supported, Right End Simply Supported

    angle, length, distance, modOfElas, momOfInert, fdnMod, width = promptFile5()

    beta = beta_(width,fdnMod,modOfElas,momOfInert)
    c2 = c_2(beta,length)
    c4 = c_4(beta,length)
    ca2 = c_a2(beta,length,distance)
    ca4 = c_a4(beta,length,distance)
    c14 = c_14(beta,length)

    m = 0
    y = 0
    r = angle*modOfElas*momOfInert*beta**2*((c2*ca4-c4*ca2)/c14)
    theta = -angle/2*((c2*ca2+c4*ca4)/c14)

    writeFile5(angle, length, distance, modOfElas, momOfInert, fdnMod, width, r, m, theta, y)

def elasticFdn5L():
    #Externally Created Concentrated Angular Displacement
    #Left End Simply Supported, Right End Fixed

    angle, length, distance, modOfElas, momOfInert, fdnMod, width = promptFile5()

    beta = beta_(width,fdnMod,modOfElas,momOfInert)
    c1 = c_1(beta,length)
    c2 = c_2(beta,length)
    c3 = c_3(beta,length)
    c4 = c_4(beta,length)
    ca1 = c_a1(beta,length,distance)
    ca2 = c_a2(beta,length,distance)
    c13 = c_13(beta,length)

    m = 0
    y = 0
    r = angle*2*modOfElas*momOfInert*beta**2*((c1*ca2-c2*ca1)/c13)
    theta = angle*((c4*ca1-c3*ca2)/c13)

    writeFile5(angle, length, distance, modOfElas, momOfInert, fdnMod, width, r, m, theta, y)

def elasticFdn5M():
    #Externally Created Concentrated Angular Displacement
    #Left End Fixed, Right End Free

    angle, length, distance, modOfElas, momOfInert, fdnMod, width = promptFile5()

    beta = beta_(width,fdnMod,modOfElas,momOfInert)
    c1 = c_1(beta,length)
    c2 = c_2(beta,length)
    c4 = c_4(beta,length)
    ca3 = c_a3(beta,length,distance)
    ca4 = c_a4(beta,length,distance)
    c11 = c_11(beta,length)

    theta = 0
    y = 0
    r = angle*2*modOfElas*momOfInert*beta**2*((2*c1*ca3+c4*ca4)/(2+c11))
    m = angle*2*modOfElas*momOfInert*beta*((c1*ca4-c2*ca3)/(2+c11))

    writeFile5(angle, length, distance, modOfElas, momOfInert, fdnMod, width, r, m, theta, y)

def elasticFdn5N():
    #Externally Created Concentrated Angular Displacement
    #Left End Fixed, Right End Guided

    angle, length, distance, modOfElas, momOfInert, fdnMod, width = promptFile5()

    beta = beta_(width,fdnMod,modOfElas,momOfInert)
    c1 = c_1(beta,length)
    c2 = c_2(beta,length)
    c3 = c_3(beta,length)
    c4 = c_4(beta,length)
    ca1 = c_a1(beta,length,distance)
    ca3 = c_a3(beta,length,distance)
    c12 = c_12(beta,length)

    theta = 0
    y = 0
    r = angle*2*modOfElas*momOfInert*beta**2*((c2*ca3-c4*ca1)/c12)
    m = -angle*2*modOfElas*momOfInert*beta*((c1*ca1+c3*ca3)/c12)

    writeFile5(angle, length, distance, modOfElas, momOfInert, fdnMod, width, r, m, theta, y)

def elasticFdn5O():
    #Externally Created Concentrated Angular Displacement
    #Left End Fixed, Right End Simply Supported

    angle, length, distance, modOfElas, momOfInert, fdnMod, width = promptFile5()

    beta = beta_(width,fdnMod,modOfElas,momOfInert)
    c1 = c_1(beta,length)
    c2 = c_2(beta,length)
    c3 = c_3(beta,length)
    c4 = c_4(beta,length)
    ca2 = c_a2(beta,length,distance)
    ca4 = c_a4(beta,length,distance)
    c13 = c_13(beta,length)

    theta = 0
    y = 0
    r = angle*2*modOfElas*momOfInert*beta**2*((c1*ca2+c3*ca4)/c13)
    m = -angle*modOfElas*momOfInert*beta*((c2*ca2+c4*ca4)/c13)

    writeFile5(angle, length, distance, modOfElas, momOfInert, fdnMod, width, r, m, theta, y)

def elasticFdn5P():
    #Externally Created Concentrated Angular Displacement
    #Left End Fixed, Right End Fixed

    angle, length, distance, modOfElas, momOfInert, fdnMod, width = promptFile5()

    beta = beta_(width,fdnMod,modOfElas,momOfInert)
    c2 = c_2(beta,length)
    c3 = c_3(beta,length)
    c4 = c_4(beta,length)
    ca1 = c_a1(beta,length,distance)
    ca2 = c_a2(beta,length,distance)
    c11 = c_11(beta,length)

    theta = 0
    y = 0
    r = angle*2*modOfElas*momOfInert*beta**2*((c2*ca2-2*c3*ca1)/c11)
    m = angle*2*modOfElas*momOfInert*beta*((c4*ca1-c3*ca2)/c11)

    writeFile5(angle, length, distance, modOfElas, momOfInert, fdnMod, width, r, m, theta, y)

def elasticFdn6A():
    #Externally Created Concentrated Lateral Displacement
    #Left End Free, Right End Free

    delta, length, distance, modOfElas, momOfInert, fdnMod, width = promptFile6()

    beta = beta_(width,fdnMod,modOfElas,momOfInert)
    c2 = c_2(beta,length)
    c3 = c_3(beta,length)
    c4 = c_4(beta,length)
    ca2 = c_a2(beta,length,distance)
    ca3 = c_a3(beta,length,distance)
    c11 = c_11(beta,length)

    r = 0
    m = 0
    theta = delta*2*beta*((c2*ca3-c3*ca2)/c11)
    y = delta*((c4*ca2-2*c3*ca3)/c11)

    writeFile6(delta, length, distance, modOfElas, momOfInert, fdnMod, width, r, m, theta, y)

def elasticFdn6B():
    #Externally Created Concentrated Lateral Displacement
    #Left End Free, Right End Guided

    delta, length, distance, modOfElas, momOfInert, fdnMod, width = promptFile6()

    beta = beta_(width,fdnMod,modOfElas,momOfInert)
    c1 = c_1(beta,length)
    c2 = c_2(beta,length)
    c3 = c_3(beta,length)
    c4 = c_4(beta,length)
    ca2 = c_a2(beta,length,distance)
    ca4 = c_a4(beta,length,distance)
    c12 = c_12(beta,length)

    r = 0
    m = 0
    theta = delta*beta*((c2*ca4-c4*ca2)/c12)
    y = -delta*((c1*ca2+c3*ca4)/c12)

    writeFile6(delta, length, distance, modOfElas, momOfInert, fdnMod, width, r, m, theta, y)

def elasticFdn6C():
    #Externally Created Concentrated Lateral Displacement
    #Left End Free, Right End Simply Supported

    delta, length, distance, modOfElas, momOfInert, fdnMod, width = promptFile6()

    beta = beta_(width,fdnMod,modOfElas,momOfInert)
    c1 = c_1(beta,length)
    c2 = c_2(beta,length)
    c3 = c_3(beta,length)
    c4 = c_4(beta,length)
    ca1 = c_a1(beta,length,distance)
    ca3 = c_a3(beta,length,distance)
    c13 = c_13(beta,length)

    r = 0
    m = 0
    theta = delta*2*beta*((c1*ca3-c3*ca1)/c13)
    y = delta*((c4*ca1-c2*ca3)/c13)

    writeFile6(delta, length, distance, modOfElas, momOfInert, fdnMod, width, r, m, theta, y)

def elasticFdn6D():
    #Externally Created Concentrated Lateral Displacement
    #Left End Free, Right End Fixed

    delta, length, distance, modOfElas, momOfInert, fdnMod, width = promptFile6()

    beta = beta_(width,fdnMod,modOfElas,momOfInert)
    c1 = c_1(beta,length)
    c2 = c_2(beta,length)
    c4 = c_4(beta,length)
    ca1 = c_a1(beta,length,distance)
    ca4 = c_a4(beta,length,distance)
    c11 = c_11(beta,length)

    r = 0
    m = 0
    theta = delta*2*beta*((c1*ca4-c4*ca1)/(2+c11))
    y = -delta*((2*c1*ca1+c2*ca4)/(2+c11))

    writeFile6(delta, length, distance, modOfElas, momOfInert, fdnMod, width, r, m, theta, y)

def elasticFdn6E():
    #Externally Created Concentrated Lateral Displacement
    #Left End Guided, Right End Free

    delta, length, distance, modOfElas, momOfInert, fdnMod, width = promptFile6()

    beta = beta_(width,fdnMod,modOfElas,momOfInert)
    c1 = c_1(beta,length)
    c2 = c_2(beta,length)
    c3 = c_3(beta,length)
    c4 = c_4(beta,length)
    ca2 = c_a2(beta,length,distance)
    ca3 = c_a3(beta,length,distance)
    c12 = c_12(beta,length)

    r = 0
    theta = 0
    m = delta*2*modOfElas*momOfInert*beta**2*((c2*ca3-c3*ca2)/c12)
    y = -delta*((c1*ca2+c4*ca3)/c12)

    writeFile6(delta, length, distance, modOfElas, momOfInert, fdnMod, width, r, m, theta, y)

def elasticFdn6F():
    #Externally Created Concentrated Lateral Displacement
    #Left End Guided, Right End Guided

    delta, length, distance, modOfElas, momOfInert, fdnMod, width = promptFile6()

    beta = beta_(width,fdnMod,modOfElas,momOfInert)
    c2 = c_2(beta,length)
    c4 = c_4(beta,length)
    ca2 = c_a2(beta,length,distance)
    ca4 = c_a4(beta,length,distance)
    c14 = c_14(beta,length)

    r = 0
    theta = 0
    m = delta*modOfElas*momOfInert*beta**2*((c2*ca4-c4*ca2)/c14)
    y = -delta/2*((c2*ca2+c4*ca4)/c14)

    writeFile6(delta, length, distance, modOfElas, momOfInert, fdnMod, width, r, m, theta, y)

def elasticFdn6G():
    #Externally Created Concentrated Lateral Displacement
    #Left End Guided, Right End Simply Supported

    delta, length, distance, modOfElas, momOfInert, fdnMod, width = promptFile6()

    beta = beta_(width,fdnMod,modOfElas,momOfInert)
    c1 = c_1(beta,length)
    c3 = c_3(beta,length)
    ca1 = c_a1(beta,length,distance)
    ca3 = c_a3(beta,length,distance)
    c11 = c_11(beta,length)

    r = 0
    theta = 0
    m = delta*2*modOfElas*momOfInert*beta**2*((c1*ca3-c3*ca1)/(1+c11))
    y = -delta*((c1*ca1+c3*ca3)/(1+c11))

    writeFile6(delta, length, distance, modOfElas, momOfInert, fdnMod, width, r, m, theta, y)

def elasticFdn6H():
    #Externally Created Concentrated Lateral Displacement
    #Left End Guided, Right End Fixed

    delta, length, distance, modOfElas, momOfInert, fdnMod, width = promptFile6()

    beta = beta_(width,fdnMod,modOfElas,momOfInert)
    c1 = c_1(beta,length)
    c2 = c_2(beta,length)
    c3 = c_3(beta,length)
    c4 = c_4(beta,length)
    ca1 = c_a1(beta,length,distance)
    ca4 = c_a4(beta,length,distance)
    c12 = c_12(beta,length)

    r = 0
    theta = 0
    m = delta*2*modOfElas*momOfInert*beta**2*((c1*ca4-c4*ca1)/c12)
    y = -delta*((c2*ca1+c3*ca4)/c12)

    writeFile6(delta, length, distance, modOfElas, momOfInert, fdnMod, width, r, m, theta, y)

def elasticFdn6I():
    #Externally Created Concentrated Lateral Displacement
    #Left End Simply Supported, Right End Free

    delta, length, distance, modOfElas, momOfInert, fdnMod, width = promptFile6()

    beta = beta_(width,fdnMod,modOfElas,momOfInert)
    c1 = c_1(beta,length)
    c2 = c_2(beta,length)
    c3 = c_3(beta,length)
    c4 = c_4(beta,length)
    ca2 = c_a2(beta,length,distance)
    ca3 = c_a3(beta,length,distance)
    c13 = c_13(beta,length)

    m = 0
    y = 0
    r = delta*2*modOfElas*momOfInert*beta**3*((2*c3*ca3-c4*ca2)/c13)
    theta = delta*beta*((2*c1*ca3-c2*ca2)/c13)

    writeFile6(delta, length, distance, modOfElas, momOfInert, fdnMod, width, r, m, theta, y)

def elasticFdn6J():
    #Externally Created Concentrated Lateral Displacement
    #Left End Simply Supported, Right End Guided

    delta, length, distance, modOfElas, momOfInert, fdnMod, width = promptFile6()

    beta = beta_(width,fdnMod,modOfElas,momOfInert)
    c1 = c_1(beta,length)
    c3 = c_3(beta,length)
    ca2 = c_a2(beta,length,distance)
    ca4 = c_a4(beta,length,distance)
    c11 = c_11(beta,length)

    m = 0
    y = 0
    r = delta*2*modOfElas*momOfInert*beta**3*((c1*ca2+c3*ca4)/(1+c11))
    theta = delta*beta*((c1*ca4-c3*ca2)/(1+c11))

    writeFile6(delta, length, distance, modOfElas, momOfInert, fdnMod, width, r, m, theta, y)

def elasticFdn6K():
    #Externally Created Concentrated Lateral Displacement
    #Left End Simply Supported, Right End Simply Supported

    delta, length, distance, modOfElas, momOfInert, fdnMod, width = promptFile6()

    beta = beta_(width,fdnMod,modOfElas,momOfInert)
    c2 = c_2(beta,length)
    c4 = c_4(beta,length)
    ca1 = c_a1(beta,length,distance)
    ca3 = c_a3(beta,length,distance)
    c14 = c_14(beta,length)

    m = 0
    y = 0
    r = delta*2*modOfElas*momOfInert*beta**3*((c2*ca3-c4*ca1)/c14)
    theta = -delta*beta*((c2*ca1+c4*ca3)/c14)

    writeFile6(delta, length, distance, modOfElas, momOfInert, fdnMod, width, r, m, theta, y)

def elasticFdn6L():
    #Externally Created Concentrated Lateral Displacement
    #Left End Simply Supported, Right End Fixed

    delta, length, distance, modOfElas, momOfInert, fdnMod, width = promptFile6()

    beta = beta_(width,fdnMod,modOfElas,momOfInert)
    c1 = c_1(beta,length)
    c2 = c_2(beta,length)
    c3 = c_3(beta,length)
    c4 = c_4(beta,length)
    ca1 = c_a1(beta,length,distance)
    ca4 = c_a4(beta,length,distance)
    c13 = c_13(beta,length)

    m = 0
    y = 0
    r = delta*2*modOfElas*momOfInert*beta**3*((c2*ca4+2*c1*ca1)/c13)
    theta = -delta*beta*((2*c3*ca1+c4*ca4)/c13)

    writeFile6(delta, length, distance, modOfElas, momOfInert, fdnMod, width, r, m, theta, y)

def elasticFdn6M():
    #Externally Created Concentrated Lateral Displacement
    #Left End Fixed, Right End Free

    delta, length, distance, modOfElas, momOfInert, fdnMod, width = promptFile6()

    beta = beta_(width,fdnMod,modOfElas,momOfInert)
    c1 = c_1(beta,length)
    c2 = c_2(beta,length)
    c4 = c_4(beta,length)
    ca2 = c_a2(beta,length,distance)
    ca3 = c_a3(beta,length,distance)
    c11 = c_11(beta,length)

    theta = 0
    y = 0
    r = delta*4*modOfElas*momOfInert*beta**3*((c1*ca2+c4*ca3)/(2+c11))
    m = delta*2*modOfElas*momOfInert*beta**2*((2*c1*ca3-c2*ca2)/(2+c11))

    writeFile6(delta, length, distance, modOfElas, momOfInert, fdnMod, width, r, m, theta, y)

def elasticFdn6N():
    #Externally Created Concentrated Lateral Displacement
    #Left End Fixed, Right End Guided

    delta, length, distance, modOfElas, momOfInert, fdnMod, width = promptFile6()

    beta = beta_(width,fdnMod,modOfElas,momOfInert)
    c1 = c_1(beta,length)
    c2 = c_2(beta,length)
    c3 = c_3(beta,length)
    c4 = c_4(beta,length)
    ca2 = c_a2(beta,length,distance)
    ca4 = c_a4(beta,length,distance)
    c12 = c_12(beta,length)

    theta = 0
    y = 0
    r = delta*2*modOfElas*momOfInert*beta**3*((c4*ca4+c2*ca2)/c12)
    m = delta*2*modOfElas*momOfInert*beta**2*((c1*ca4-c3*ca2)/c12)

    writeFile6(delta, length, distance, modOfElas, momOfInert, fdnMod, width, r, m, theta, y)

def elasticFdn6O():
    #Externally Created Concentrated Lateral Displacement
    #Left End Fixed, Right End Simply Supported

    delta, length, distance, modOfElas, momOfInert, fdnMod, width = promptFile6()

    beta = beta_(width,fdnMod,modOfElas,momOfInert)
    c1 = c_1(beta,length)
    c2 = c_2(beta,length)
    c3 = c_3(beta,length)
    c4 = c_4(beta,length)
    ca1 = c_a1(beta,length,distance)
    ca3 = c_a3(beta,length,distance)
    c13 = c_13(beta,length)

    theta = 0
    y = 0
    r = delta*4*modOfElas*momOfInert*beta**3*((c3*ca3+c1*ca1)/c13)
    m = -delta*2*modOfElas*momOfInert*beta**2*((c2*ca1+c4*ca3)/c13)

    writeFile6(delta, length, distance, modOfElas, momOfInert, fdnMod, width, r, m, theta, y)

def elasticFdn6P():
    #Externally Created Concentrated Lateral Displacement
    #Left End Fixed, Right End Fixed

    delta, length, distance, modOfElas, momOfInert, fdnMod, width = promptFile6()

    beta = beta_(width,fdnMod,modOfElas,momOfInert)
    c2 = c_2(beta,length)
    c3 = c_3(beta,length)
    c4 = c_4(beta,length)
    ca1 = c_a1(beta,length,distance)
    ca4 = c_a4(beta,length,distance)
    c11 = c_11(beta,length)

    theta = 0
    y = 0
    r = delta*4*modOfElas*momOfInert*beta**3*((c3*ca4+c2*ca1)/c11)
    m = -delta*2*modOfElas*momOfInert*beta**2*((2*c3*ca1+c4*ca4)/c11)

    writeFile6(delta, length, distance, modOfElas, momOfInert, fdnMod, width, r, m, theta, y)

def elasticFdn7A():
    #Uniform Temperature Differential from Top to Bottom
    #Left End Free, Right End Free

    t1, t2, gamma, length, modOfElas, momOfInert, fdnMod, width, depth = promptFile7()

    beta = beta_(width,fdnMod,modOfElas,momOfInert)
    c1 = c_1(beta,length)
    c2 = c_2(beta,length)
    c3 = c_3(beta,length)
    c4 = c_4(beta,length)
    c11 = c_11(beta,length)

    r = 0
    m = 0
    theta = ((t1-t2)*gamma/(beta*depth))*((c1*c2+c3*c4-c2)/c11)
    y = (-(t1-t2)*gamma/(2*beta**2*depth))*((c4**2+2*c1*c3-2*c3)/c11)

    writeFile7(t1, t2, gamma, length, depth, distance, modOfElas, momOfInert, fdnMod, width, r, m, theta, y)

def elasticFdn7B():
    #Uniform Temperature Differential from Top to Bottom
    #Left End Free, Right End Guided

    t1, t2, gamma, length, modOfElas, momOfInert, fdnMod, width, depth = promptFile7()

    beta = beta_(width,fdnMod,modOfElas,momOfInert)
    c1 = c_1(beta,length)
    c2 = c_2(beta,length)
    c3 = c_3(beta,length)
    c4 = c_4(beta,length)
    c12 = c_12(beta,length)

    r = 0
    m = 0
    theta = ((t1-t2)*gamma/(2*beta*depth))*((c2**2+c4**2)/c12)
    y = (-(t1-t2)*gamma/(2*beta**2*depth))*((c2*c3-c1*c4)/c12)

    writeFile7(t1, t2, gamma, length, depth, distance, modOfElas, momOfInert, fdnMod, width, r, m, theta, y)

def elasticFdn7C():
    #Uniform Temperature Differential from Top to Bottom
    #Left End Free, Right End Simply Supported

    t1, t2, gamma, length, modOfElas, momOfInert, fdnMod, width, depth = promptFile7()

    beta = beta_(width,fdnMod,modOfElas,momOfInert)
    c1 = c_1(beta,length)
    c2 = c_2(beta,length)
    c3 = c_3(beta,length)
    c4 = c_4(beta,length)
    c13 = c_13(beta,length)

    r = 0
    m = 0
    theta = ((t1-t2)*gamma/(beta*depth))*((c1**2+c3-c4)/c13)
    y = (-(t1-t2)*gamma/(beta*depth))*((c1*c2+c3*c4-c2)/c13)

    writeFile7(t1, t2, gamma, length, depth, distance, modOfElas, momOfInert, fdnMod, width, r, m, theta, y)

def elasticFdn7D():
    #Uniform Temperature Differential from Top to Bottom
    #Left End Free, Right End Fixed

    t1, t2, gamma, length, modOfElas, momOfInert, fdnMod, width, depth = promptFile7()

    beta = beta_(width,fdnMod,modOfElas,momOfInert)
    c1 = c_1(beta,length)
    c2 = c_2(beta,length)
    c3 = c_3(beta,length)
    c4 = c_4(beta,length)
    c11 = c_11(beta,length)

    r = 0
    m = 0
    theta = ((t1-t2)*gamma/(2*beta**2*depth))*((c1*c2+c3*c1)/(2+c11))
    y = (-(t1-t2)*gamma/(2*beta**2*depth))*((2*c1*c3-c2**2)/(2+c11))

    writeFile7(t1, t2, gamma, length, depth, distance, modOfElas, momOfInert, fdnMod, width, r, m, theta, y)

def elasticFdn7E():
    #Uniform Temperature Differential from Top to Bottom
    #Left End Guided, Right End Free

    t1, t2, gamma, length, modOfElas, momOfInert, fdnMod, width, depth = promptFile7()

    beta = beta_(width,fdnMod,modOfElas,momOfInert)
    c1 = c_1(beta,length)
    c2 = c_2(beta,length)
    c3 = c_3(beta,length)
    c4 = c_4(beta,length)
    c12 = c_12(beta,length)

    r = 0
    theta = 0
    m = ((t1-t2)*gamma*modOfElas*momOfInert/depth)*((c1*c2+c3*c4-c2)/c12)
    y = ((t1-t2)*gamma/(2*beta**2*depth))*(c4/c12)

    writeFile7(t1, t2, gamma, length, depth, distance, modOfElas, momOfInert, fdnMod, width, r, m, theta, y)

def elasticFdn7F():
    #Uniform Temperature Differential from Top to Bottom
    #Left End Guided, Right End Guided

    t1, t2, gamma, length, modOfElas, momOfInert, fdnMod, width, depth = promptFile7()

    beta = beta_(width,fdnMod,modOfElas,momOfInert)
    c1 = c_1(beta,length)
    c2 = c_2(beta,length)
    c3 = c_3(beta,length)
    c4 = c_4(beta,length)

    r = 0
    theta = 0
    m = (t1-t2)*gamma*modOfElas*momOfInert/depth
    y = 0

    writeFile7(t1, t2, gamma, length, depth, distance, modOfElas, momOfInert, fdnMod, width, r, m, theta, y)

def elasticFdn7G():
    #Uniform Temperature Differential from Top to Bottom
    #Left End Guided, Right End Simply Supported

    t1, t2, gamma, length, modOfElas, momOfInert, fdnMod, width, depth = promptFile7()

    beta = beta_(width,fdnMod,modOfElas,momOfInert)
    c1 = c_1(beta,length)
    c2 = c_2(beta,length)
    c3 = c_3(beta,length)
    c4 = c_4(beta,length)
    c11 = c_11(beta,length)

    r = 0
    theta = 0
    m = ((t1-t2)*gamma*modOfElas*momOfInert/depth)*((c1**2+c3**2-c1)/(1+c11))
    y = ((t1-t2)*gamma/(2*beta**2*depth))*(c3/(1+c11))

    writeFile7(t1, t2, gamma, length, depth, distance, modOfElas, momOfInert, fdnMod, width, r, m, theta, y)

def elasticFdn7H():
    #Uniform Temperature Differential from Top to Bottom
    #Left End Guided, Right End Fixed

    t1, t2, gamma, length, modOfElas, momOfInert, fdnMod, width, depth = promptFile7()

    beta = beta_(width,fdnMod,modOfElas,momOfInert)
    c1 = c_1(beta,length)
    c2 = c_2(beta,length)
    c3 = c_3(beta,length)
    c4 = c_4(beta,length)

    r = 0
    theta = 0
    m = (t1-t2)*gamma*modOfElas*momOfInert/depth
    y = 0

    writeFile7(t1, t2, gamma, length, depth, distance, modOfElas, momOfInert, fdnMod, width, r, m, theta, y)

def elasticFdn7I():
    #Uniform Temperature Differential from Top to Bottom
    #Left End Simply Supported, Right End Free

    t1, t2, gamma, length, modOfElas, momOfInert, fdnMod, width, depth = promptFile7()

    beta = beta_(width,fdnMod,modOfElas,momOfInert)
    c1 = c_1(beta,length)
    c2 = c_2(beta,length)
    c3 = c_3(beta,length)
    c4 = c_4(beta,length)
    c13 = c_13(beta,length)

    m = 0
    y = 0
    r = ((t1-t2)*gamma*beta*modOfElas*momOfInert/depth)*((2*c1*c3+c4**2-2*c3)/c13)
    theta = ((t1-t2)*gamma/(2*beta*depth))*((2*c1**2+c2*c4-2*c1)/c13)

    writeFile7(t1, t2, gamma, length, depth, distance, modOfElas, momOfInert, fdnMod, width, r, m, theta, y)

def elasticFdn7J():
    #Uniform Temperature Differential from Top to Bottom
    #Left End Simply Supported, Right End Guided

    t1, t2, gamma, length, modOfElas, momOfInert, fdnMod, width, depth = promptFile7()

    beta = beta_(width,fdnMod,modOfElas,momOfInert)
    c1 = c_1(beta,length)
    c2 = c_2(beta,length)
    c3 = c_3(beta,length)
    c4 = c_4(beta,length)
    c11 = c_11(beta,length)

    m = 0
    y = 0
    r = ((t1-t2)*gamma*beta*modOfElas*momOfInert/depth)*((c2*c3-c1*c4)/(1+c11))
    theta = ((t1-t2)*gamma/(2*beta*depth))*((c1*c2+c3*c4)/(1+c11))

    writeFile7(t1, t2, gamma, length, depth, distance, modOfElas, momOfInert, fdnMod, width, r, m, theta, y)

def elasticFdn7K():
    #Uniform Temperature Differential from Top to Bottom
    #Left End Simply Supported, Right End Simply Supported

    t1, t2, gamma, length, modOfElas, momOfInert, fdnMod, width, depth = promptFile7()

    beta = beta_(width,fdnMod,modOfElas,momOfInert)
    c1 = c_1(beta,length)
    c2 = c_2(beta,length)
    c3 = c_3(beta,length)
    c4 = c_4(beta,length)
    c14 = c_14(beta,length)

    m = 0
    y = 0
    r = ((t1-t2)*gamma*beta*modOfElas*momOfInert/depth)*((c1*c2+c3*c4-c2)/c14)
    theta = ((t1-t2)*gamma/(2*beta*depth))*((c2*c3-c1*c4+c4)/c14)

    writeFile7(t1, t2, gamma, length, depth, distance, modOfElas, momOfInert, fdnMod, width, r, m, theta, y)

def elasticFdn7L():
    #Uniform Temperature Differential from Top to Bottom
    #Left End Simply Supported, Right End Fixed

    t1, t2, gamma, length, modOfElas, momOfInert, fdnMod, width, depth = promptFile7()

    beta = beta_(width,fdnMod,modOfElas,momOfInert)
    c1 = c_1(beta,length)
    c2 = c_2(beta,length)
    c3 = c_3(beta,length)
    c4 = c_4(beta,length)
    c13 = c_13(beta,length)

    m = 0
    y = 0
    r = ((t1-t2)*gamma*beta*modOfElas*momOfInert/depth)*((c2**2-2*c1*c3)/c13)
    theta = ((t1-t2)*gamma/(2*beta*depth))*((2*c3**2-c2*c4)/c13)

    writeFile7(t1, t2, gamma, length, depth, distance, modOfElas, momOfInert, fdnMod, width, r, m, theta, y)

def elasticFdn7M():
    #Uniform Temperature Differential from Top to Bottom
    #Left End Fixed, Right End Free

    t1, t2, gamma, length, modOfElas, momOfInert, fdnMod, width, depth = promptFile7()

    beta = beta_(width,fdnMod,modOfElas,momOfInert)
    c1 = c_1(beta,length)
    c2 = c_2(beta,length)
    c3 = c_3(beta,length)
    c4 = c_4(beta,length)
    c11 = c_11(beta,length)

    theta = 0
    y = 0
    r = ((t1-t2)*gamma*2*beta*modOfElas*momOfInert/depth)*(-c4/(2+c11))
    m = ((t1-t2)*gamma*modOfElas*momOfInert/depth)*((2*c1**2+c2*c4-2*c1)/(2+c11))

    writeFile7(t1, t2, gamma, length, depth, distance, modOfElas, momOfInert, fdnMod, width, r, m, theta, y)

def elasticFdn7N():
    #Uniform Temperature Differential from Top to Bottom
    #Left End Fixed, Right End Guided

    t1, t2, gamma, length, modOfElas, momOfInert, fdnMod, width, depth = promptFile7()

    beta = beta_(width,fdnMod,modOfElas,momOfInert)

    theta = 0
    y = 0
    r = 0
    m = (t1-t2)*gamma*modOfElas*momOfInert/depth

    writeFile7(t1, t2, gamma, length, depth, distance, modOfElas, momOfInert, fdnMod, width, r, m, theta, y)
    
def elasticFdn7O():
    #Uniform Temperature Differential from Top to Bottom
    #Left End Fixed, Right End Simply Supported

    t1, t2, gamma, length, modOfElas, momOfInert, fdnMod, width, depth = promptFile7()

    beta = beta_(width,fdnMod,modOfElas,momOfInert)
    c1 = c_1(beta,length)
    c2 = c_2(beta,length)
    c3 = c_3(beta,length)
    c4 = c_4(beta,length)
    c13 = c_13(beta,length)

    theta = 0
    y = 0
    r = ((t1-t2)*gamma*beta*modOfElas*momOfInert/depth)*(-2*c3/c13)
    m = ((t1-t2)*gamma*modOfElas*momOfInert/depth)*((c2*c3-c1*c4+c4)/c13)

    writeFile7(t1, t2, gamma, length, depth, distance, modOfElas, momOfInert, fdnMod, width, r, m, theta, y)

def elasticFdn7P():
    #Uniform Temperature Differential from Top to Bottom
    #Left End Fixed, Right End Fixed

    t1, t2, gamma, length, modOfElas, momOfInert, fdnMod, width, depth = promptFile7()

    beta = beta_(width,fdnMod,modOfElas,momOfInert)

    theta = 0
    y = 0
    r = 0
    m = (t1-t2)*gamma*modOfElas*momOfInert/depth

    writeFile7(t1, t2, gamma, length, depth, distance, modOfElas, momOfInert, fdnMod, width, r, m, theta, y)


def writeFile1(load, length, distance, modOfElas, momOfInert, fdnMod, width, r, m, theta, y):
    #Creates and writes the output file for Intermediate Load calculations

    inputLabels = ["Concentrated Load:                                                ", "Length of Beam:                                                   ",
                   "Width of Beam:                                                    ", "Distance from Left End of Beam to Concentrated Load Location:     ",
                   "Modulus of Elasticity of Material:                                ", "Area Moment of Inertia of Section:                                ",
                   "Foundation Modulus:                                               "]
    inputValues = [round(load,2), round(length,2), round(width,2), round(distance,2), round(modOfElas,2), round(momOfInert,2), round(fdnMod,2)]
    inputDims = ['  lb', '  in', '  in', '  in', '  lb/in2', '  in4', '  lb/in2/in']

    outputLabels = ["Vertical End Reaction at Left End:                                ", "Reaction End Moment at Left End:                                  ",
                    "Slope of Beam at Left End:                                        ", "Deflection of Beam at Left End:                                   "]
    outputValues = [round(r,2), round(m,2), round(theta,2), round(y,2)]
    outputDims = ['  lb', '  in-lb', '  rad', '  in']


    return fileWriter("Finite-Length Beam on Elastic Foundations", "Concentrated Intermediate Load",inputLabels, inputValues, inputDims, outputLabels, outputValues, outputDims)    



def writeFile2(load, length, distance, modOfElas, momOfInert, fdnMod, width, r, m, theta, y):
    #Creates and writes the output file for Uniformly Distributed Load calculations

    inputLabels = ["Unit Load:                                                        ", "Length of Beam:                                                   ",
                   "Width of Beam:                                                    ", "Distance from Left End of Beam to Edge of Distributed Load:       ",
                   "Modulus of Elasticity of Material:                                ", "Area Moment of Inertia of Section:                                ",
                   "Foundation Modulus:                                               "]
    inputValues = [round(load,2), round(length,2), round(width,2), round(distance,2), round(modOfElas,2), round(momOfInert,2), round(fdnMod,2)]
    inputDims = ['  lb/in', '  in', '  in', '  in', '  lb/in2', '  in4', '  lb/in2/in']

    outputLabels = ["Vertical End Reaction at Left End:                                ", "Reaction End Moment at Left End:                                  ",
                    "Slope of Beam at Left End:                                        ", "Deflection of Beam at Left End:                                   "]
    outputValues = [round(r,2), round(m,2), round(theta,2), round(y,2)]
    outputDims = ['  lb', '  in-lb', '  rad', '  in']


    return fileWriter("Finite-Length Beam on Elastic Foundations", "Partial Uniformly Distributed Load",inputLabels, inputValues, inputDims, outputLabels, outputValues, outputDims)    


def writeFile3(load, length, distance, modOfElas, momOfInert, fdnMod, width, r, m, theta, y):
    #Creates and writes the output file for Uniformly Increasing Load calculations

    inputLabels = ["Maximum Load:                                                     ", "Length of Beam:                                                   ",
                   "Width of Beam:                                                    ", "Distance from Left End of Beam to Edge of Distributed Load:       ",
                   "Modulus of Elasticity of Material:                                ", "Area Moment of Inertia of Section:                                ",
                   "Foundation Modulus:                                               "]
    inputValues = [round(load,2), round(length,2), round(width,2), round(distance,2), round(modOfElas,2), round(momOfInert,2), round(fdnMod,2)]
    inputDims = ['  lb/in', '  in', '  in', '  in', '  lb/in2', '  in4', '  lb/in2/in']

    outputLabels = ["Vertical End Reaction at Left End:                                ", "Reaction End Moment at Left End:                                  ",
                    "Slope of Beam at Left End:                                        ", "Deflection of Beam at Left End:                                   "]
    outputValues = [round(r,2), round(m,2), round(theta,2), round(y,2)]
    outputDims = ['  lb', '  in-lb', '  rad', '  in']


    return fileWriter("Finite-Length Beam on Elastic Foundations", "Partial Uniformly Increasing Load",inputLabels, inputValues, inputDims, outputLabels, outputValues, outputDims)    
   

def writeFile4(moment, length, distance, modOfElas, momOfInert, fdnMod, width, r, m, theta, y):
    #Creates and writes the output file for Concentrated Moment calculations

    inputLabels = ["Concentrated Moment:                                              ", "Length of Beam:                                                   ",
                   "Width of Beam:                                                    ", "Distance from Left End of Beam to Moment Location:                ",
                   "Modulus of Elasticity of Material:                                ", "Area Moment of Inertia of Section:                                ",
                   "Foundation Modulus:                                               "]
    inputValues = [round(moment,2), round(length,2), round(width,2), round(distance,2), round(modOfElas,2), round(momOfInert,2), round(fdnMod,2)]
    inputDims = ['  in-lb', '  in', '  in', '  in', '  lb/in2', '  in4', '  lb/in2/in']

    outputLabels = ["Vertical End Reaction at Left End:                                ", "Reaction End Moment at Left End:                                  ",
                    "Slope of Beam at Left End:                                        ", "Deflection of Beam at Left End:                                   "]
    outputValues = [round(r,2), round(m,2), round(theta,2), round(y,2)]
    outputDims = ['  lb', '  in-lb', '  rad', '  in']


    return fileWriter("Finite-Length Beam on Elastic Foundations", "Concentrated Intermediate Moment",inputLabels, inputValues, inputDims, outputLabels, outputValues, outputDims)    


def writeFile5(angle, length, distance, modOfElas, momOfInert, fdnMod, width, r, m, theta, y):
    #Creates and writes the output file for Angular Displacement calculations

    inputLabels = ["Angular Displacement:                                             ", "Length of Beam:                                                   ",
                   "Width of Beam:                                                    ", "Distance from Left End of Beam to Angular Displacement Location:  ",
                   "Modulus of Elasticity of Material:                                ", "Area Moment of Inertia of Section:                                ",
                   "Foundation Modulus:                                               "]
    inputValues = [round(angle,2), round(length,2), round(width,2), round(distance,2), round(modOfElas,2), round(momOfInert,2), round(fdnMod,2)]
    inputDims = ['  rad', '  in', '  in', '  in', '  lb/in2', '  in4', '  lb/in2/in']

    outputLabels = ["Vertical End Reaction at Left End:                                ", "Reaction End Moment at Left End:                                  ",
                    "Slope of Beam at Left End:                                        ", "Deflection of Beam at Left End:                                   "]
    outputValues = [round(r,2), round(m,2), round(theta,2), round(y,2)]
    outputDims = ['  lb', '  in-lb', '  rad', '  in']


    return fileWriter("Finite-Length Beam on Elastic Foundations", "Intermediate External Angular Displacement",inputLabels, inputValues, inputDims, outputLabels, outputValues, outputDims)    


def writeFile6(delta, length, distance, modOfElas, momOfInert, fdnMod, width, r, m, theta, y):
    #Creates and writes the output file for Lateral Displacement calculations

    inputLabels = ["Lateral Displacement:                                             ", "Length of Beam:                                                   ",
                   "Width of Beam:                                                    ", "Distance from Left End of Beam to Lateral Displacement Location:  ",
                   "Modulus of Elasticity of Material:                                ", "Area Moment of Inertia of Section:                                ",
                   "Foundation Modulus:                                               "]
    inputValues = [round(delta,2), round(length,2), round(width,2), round(distance,2), round(modOfElas,2), round(momOfInert,2), round(fdnMod,2)]
    inputDims = ['  in', '  in', '  in', '  in', '  lb/in2', '  in4', '  lb/in2/in']

    outputLabels = ["Vertical End Reaction at Left End:                                ", "Reaction End Moment at Left End:                                  ",
                    "Slope of Beam at Left End:                                        ", "Deflection of Beam at Left End:                                   "]
    outputValues = [round(r,2), round(m,2), round(theta,2), round(y,2)]
    outputDims = ['  lb', '  in-lb', '  rad', '  in']


    return fileWriter("Finite-Length Beam on Elastic Foundations", "Intermediate External Lateral Displacement",inputLabels, inputValues, inputDims, outputLabels, outputValues, outputDims)    


def writeFile7(t1, t2, gamma, length, depth, distance, modOfElas, momOfInert, fdnMod, width, r, m, theta, y):
    #Creates and writes the output file for Temperature Variation calculations

    inputLabels = ["Temperature at Top of Beam:                                       ", "Temperature at Bottom of Beam:                                    ",
                   "Temperature Coefficient of Expansion:                             ", "Length of Beam:                                                   ",
                   "Width of Beam:                                                    ", "Depth of Beam:                                                    ",
                   "Distance from Left End of Beam to Lateral Displacement Location:  ", "Modulus of Elasticity of Material:                                ",
                   "Area Moment of Inertia of Section:                                ", "Foundation Modulus:                                               "]
    inputValues = [round(t1,2), round(t2,2), round(gamma,2), round(length,2), round(width,2), round(depth,2), round(distance,2), round(modOfElas,2), round(momOfInert,2), round(fdnMod,2)]
    inputDims = ['  degF', '  degF', '  in/in/degF', '  in', '  in', '  in', '  in', '  lb/in2', '  in4', '  lb/in2/in']

    outputLabels = ["Vertical End Reaction at Left End:                                ", "Reaction End Moment at Left End:                                  ",
                    "Slope of Beam at Left End:                                        ", "Deflection of Beam at Left End:                                   "]
    outputValues = [round(r,2), round(m,2), round(theta,2), round(y,2)]
    outputDims = ['  lb', '  in-lb', '  rad', '  in']


    return fileWriter("Finite-Length Beam on Elastic Foundations", "Uniform Temperature Variation Along Beam",inputLabels, inputValues, inputDims, outputLabels, outputValues, outputDims)    


