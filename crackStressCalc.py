from datetime import datetime
from io import prompt

#Roark 17.3

def promptFile(case):

    height = prompt("Height of Notch (in): ")
    depth = prompt("Depth of Section (in): ")

    if case %2 == 1:
        radius = prompt("Radius of U-Notch (in): ")
                
        return (height, depth, radius)
    
    else:
        theta = prompt("Angle of V-Notch (deg): ")
                
        return (height, depth, theta)

def crackStress1A():
    #Two U-Notches, Elastic Stress, Axial Tension
    height, depth, radius = promptFile(1)

    if height / radius <= 2.0:
        c_1 = 0.85 + 2.628 * (height / radius)**0.5 - 0.413 * (height / radius)
        c_2 = -1.119 - 4.826 * (height / radius)**0.5 + 2.575 * (height / radius)
        c_3 = 3.563 - 0.514 * (height / radius)**0.5 - 2.402 * (height / radius)
        c_4 = -2.294 + 2.713 * (height / radius)**0.5 + 0.24 * (height / radius)
    else:
        c_1 = 0.833 + 2.069 * (height / radius)**0.5 - 0.009 * (height / radius)
        c_2 = 2.732 - 4.157 * (height / radius)**0.5 + 0.176 * (height / radius)
        c_3 = -8.859 + 5.327 * (height / radius)**0.5 - 0.32 * (height / radius)
        c_4 = 6.294 - 3.239 * (height / radius)**0.5 + 0.154 * (height / radius)

    stress = c_1 + c_2 * (2 * height / depth) + c_3 * (2 * height / depth)**2 + c_4 * (2 * height / depth)**3

    writeFile(height, depth, radius, stress, 1)

    
def crackStress1B():
    #Two U-Notches, Elastic Stress, In-Plane Bending
    height, depth, radius = promptFile(1)

    if height / radius <= 2.0:
        c_1 = 0.723 + 2.845 * (height / radius)**0.5 - 0.504 * (height / radius)
        c_2 = -1.836 - 5.746 * (height / radius)**0.5 + 1.314 * (height / radius)
        c_3 = 7.254 - 1.885 * (height / radius)**0.5 + 1.646 * (height / radius)
        c_4 = -5.140 + 4.785 * (height / radius)**0.5 - 2.456 * (height / radius)
    else:
        c_1 = 0.833 + 2.069 * (height / radius)**0.5 - 0.009 * (height / radius)
        c_2 = 0.024 - 5.383 * (height / radius)**0.5 + 0.126 * (height / radius)
        c_3 = -0.856 + 6.460 * (height / radius)**0.5 - 0.199 * (height / radius)
        c_4 = 0.999 - 3.146 * (height / radius)**0.5 + 0.082 * (height / radius)

    stress = c_1 + c_2 * (2 * height / depth) + c_3 * (2 * height / depth)**2 + c_4 * (2 * height / depth)**3

    writeFile(height, depth, radius, stress, 1)
    
    
def crackStress1C():
    #Two U-Notches, Elastic Stress, Out-of-Plane Bending
    height, depth, radius = promptFile(1)

    if height / radius < 0.25 or height / radius > 4.0:
        print "Sorry!  Roark doesn't give equations for this scenario.\n"
    else:
        c_1 = 1.031 + 0.831 * (height / radius)**0.5 + 0.014 * (height / radius)
        c_2 = -1.227 - 1.646 * (height / radius)**0.5 + 0.117 * (height / radius)
        c_3 = 3.337 - 0.75 * (height / radius)**0.5 + 0.469 * (height / radius)
        c_4 = -2.141 + 1.566 * (height / radius)**0.5 - 0.6 * (height / radius)
        stress = c_1 + c_2 * (2 * height / depth) + c_3 * (2 * height / depth)**2 + c_4 * (2 * height / depth)**3

        writeFile(height, depth, radius, stress, 1)
        
        
def crackStress2A():
    #Two V-Notches, Elastic Stress, Axial Tension
    height, depth, radius = promptFile(2)

    if radius > 120:
        print "Sorry!  Roark doesn't give equations for this scenario.\n"
    else:
        if height / radius <= 2.0:
            c_1 = 0.85 + 2.628 * (height / radius)**0.5 - 0.413 * (height / radius)
            c_2 = -1.119 - 4.826 * (height / radius)**0.5 + 2.575 * (height / radius)
            c_3 = 3.563 - 0.514 * (height / radius)**0.5 - 2.402 * (height / radius)
            c_4 = -2.294 + 2.713 * (height / radius)**0.5 + 0.24 * (height / radius)
        else:
            c_1 = 0.833 + 2.069 * (height / radius)**0.5 - 0.009 * (height / radius)
            c_2 = 2.732 - 4.157 * (height / radius)**0.5 + 0.176 * (height / radius)
            c_3 = -8.859 + 5.327 * (height / radius)**0.5 - 0.32 * (height / radius)
            c_4 = 6.294 - 3.239 * (height / radius)**0.5 + 0.154 * (height / radius)

        k_tu = c_1 + c_2 * (2 * height / depth) + c_3 * (2 * height / depth)**2 + c_4 * (2 * height / depth)**3

        if (2 * height / depth) == 0.4:
            k_tt = 1.11 * k_tu - (0.0275 + 0.000145 * radius + 0.0164 * (radius / 120)**8) * k_tu**2
        else:
            k_tt = 1.11 * k_tu - (0.0275 + 0.00042 * radius + 0.0075 * (radius / 120)**8) * k_tu**2

        stress = min(k_tt, k_tu)
        writeFile(height, depth, radius, stress, 2)
        

def crackStress2B():
    print "Sorry!  Roark doesn't give equations for this scenario. \n"

def crackStress2C():
    print "Sorry!  Roark doesn't give equations for this scenario. \n"

def crackStress3A():
    #One U-Notch, Elastic Stress, Axial Tension
    height, depth, radius = promptFile(3)
    
    if height / radius < 0.5 or height / radius > 4.0:
        print "Sorry!  Roark doesn't give equations for this scenario.\n"
    else:
        c_1 = 0.721 + 2.394 * (height / radius)**0.5 - 0.127 * (height / radius)
        c_2 = 1.978 - 11.489 * (height / radius)**0.5 + 2.211 * (height / radius)
        c_3 = -4.413 + 18.751 * (height / radius)**0.5 - 4.596 * (height / radius)
        c_4 = 2.714 - 9.655 * (height / radius)**0.5 + 2.512 * (height / radius)
        stress = c_1 + c_2 * (height / depth) + c_3 * (height / depth)**2 + c_4 * (height / depth)**3              

        writeFile(height, depth, radius, stress, 3)
        
        
def crackStress3B():
    #One U-Notch, Elastic Stress, In-Plane Bending
    height, depth, radius = promptFile(3)

    if height / radius < 0.5 or height / radius > 4.0:
        print "Sorry!  Roark doesn't give equations for this scenario.\n"
    else:
        c_1 = 0.721 + 2.394 * (height / radius)**0.5 - 0.127 * (height / radius)
        c_2 = -0.426 - 8.827 * (height / radius)**0.5 + 1.518 * (height / radius)
        c_3 = 2.161 + 10.968 * (height / radius)**0.5 - 2.455 * (height / radius)
        c_4 = -1.456 - 4.535 * (height / radius)**0.5 + 1.064 * (height / radius)
        stress = c_1 + c_2 * (height / depth) + c_3 * (height / depth)**2 + c_4 * (height / depth)**3              

        writeFile(height, depth, radius, stress, 3)
        

def crackStress3C():
    print "Sorry!  Roark doesn't give equations for this scenario.\n"

def crackStress4A():
    print "Sorry!  Roark doesn't give equations for this scenario.\n"

def crackStress4B():
    #One V-Notch, Elastic Stress, In-Plane Bending
    height, depth, radius = promptFile(4)

    if height / radius < 0.5 or height / radius > 4.0:
        print "Sorry!  Roark doesn't give equations for this scenario.\n"
    else:
        c_1 = 0.721 + 2.394 * (height / radius)**0.5 - 0.127 * (height / radius)
        c_2 = -0.426 - 8.827 * (height / radius)**0.5 + 1.518 * (height / radius)
        c_3 = 2.161 + 10.968 * (height / radius)**0.5 - 2.455 * (height / radius)
        c_4 = -1.456 - 4.535 * (height / radius)**0.5 + 1.064 * (height / radius)
        k_tu = c_1 + c_2 * (height / depth) + c_3 * (height / depth)**2 + c_4 * (height / depth)**3

        k_tt = 1.11 * k_tu - (0.0275 + 0.1125 * (radius / 150)**4) * k_tu**2

        stress = min(k_tt, k_tu)

        writeFile(height, depth, radius, stress, 4)


def crackStress4C():
    print "Sorry!  Roark doesn't give equations for this scenario.\n"

    
def writeFile(height, depth, radius, stress, case):
    #Creates and writes the output file
    fileName = raw_input("Output File Name: ") + ".txt"
    output = open(fileName, 'w')
    project = raw_input("Project Number: ")
    output.write("""
    Roark Equations for Stress and Strain
    Stress Concentrations for Elastic Stress

    Program Release 20130116
    """)
    output.write("\n    Project Number    %s\n" %(project))
    output.write("    Calculated %s\n" %(str(datetime.now())[:19]))
    output.write("\n\nINPUT DATA\n\n")
    output.write("Height of Notch:              %.2f in\n" %height)
    output.write("Depth of Section:             %.2f in\n" %depth)
    if case % 2 == 1:
        output.write("Radius of U-Notch:            %.2f in\n" %radius)
    else:
        output.write("Angle of V-Notch:             %.2f deg\n" %radius)
    output.write("\n\nOUTPUT DATA\n\n")
    output.write("Stress Concentration Factor:      %.2f \n" %stress)
    output.close()



