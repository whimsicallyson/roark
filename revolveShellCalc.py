from math import sin, cos, tan, log, pi
from io import prompt


def revolveShell1A():
    
    load = prompt("Unit Load (lb/in): ")
    thick = prompt("Thickness of Shell (in): ")
    radius = prompt("Radius of Curvature (in): ")
    length = prompt("Length of Shell (in): ")
    modOfElas = prompt("Modulus of Elasticity of Material (lb/in2): ")
    poisson = prompt("Poisson's Ratio of Material: ")

    sigma1 = load / thick
    sigma2 = 0
    deltaR = -load * poisson * radius / (modOfElas * thick)
    deltaY = load * length / (modOfElas * thick)
    psi = 0

    inputLabels = ["Unit Load:                                    ", "Thickness of Shell:                           ",
                   "Radius of Curvature of Shell:                 ", "Length of Shell:                              ",
                   "Modulus of Elasticity of Material:            ", "Poisson's Ratio of Material:                  "]
    inputValues = [round(load,2), round(thick,2), round(radius,2), round(length,2), round(modOfElas,2), round(poisson,2)]
    inputDims = ['  lb/in', '  in', '  in', '  in', '  lb/in2', '  ']

    outputLabels = ["Meridian Stress:                              ", "Hoop Stress:                                  ",
                    "Change in Vessel Radius:                      ", "Change in Vessel Height:                      ",
                    "Rotation from Unloaded Position:              "]
    outputValues = [round(sigma1,2), round(sigma2,2), round(deltaR,2), round(deltaY,2), round(psi,2)]
    outputDims = ['  lb/in2', '  lb/in2', '  in', '  in', '  rad']


    return fileWriter("Thin-Walled Cylindrical Pressure Vessel", "Uniform Axial Load",inputLabels, inputValues, inputDims, outputLabels, outputValues, outputDims)    


def revolveShell1B():
      
    pressure = prompt("Unit Pressure (lb/in2): ")
    thick = prompt("Thickness of Shell (in): ")
    radius = prompt("Radius of Curvature (in): ")
    length = prompt("Length of Shell (in): ")
    modOfElas = prompt("Modulus of Elasticity of Material (lb/in2): ")
    poisson = prompt("Poisson's Ratio of Material: ")

    sigma1 = 0
    sigma2 = pressure * radius / thick
    deltaR = pressure * radius ** 2 / (modOfElas * thick)
    deltaY = -pressure * radius * poisson * length / (modOfElas * thick)
    psi = 0


    inputLabels = ["Unit Pressure:                                ", "Thickness of Shell:                           ",
                   "Radius of Curvature of Shell:                 ", "Length of Shell:                              ",
                   "Modulus of Elasticity of Material:            ", "Poisson's Ratio of Material:                  "]
    inputValues = [round(pressure,2), round(thick,2), round(radius,2), round(length,2), round(modOfElas,2), round(poisson,2)]
    inputDims = ['  lb/in2', '  in', '  in', '  in', '  lb/in2', '  ']

    outputLabels = ["Meridian Stress:                              ", "Hoop Stress:                                  ",
                    "Change in Vessel Radius:                      ", "Change in Vessel Height:                      ",
                    "Rotation from Unloaded Position:              "]
    outputValues = [round(sigma1,2), round(sigma2,2), round(deltaR,2), round(deltaY,2), round(psi,2)]
    outputDims = ['  lb/in2', '  lb/in2', '  in', '  in', '  rad']


    return fileWriter("Thin-Walled Cylindrical Pressure Vessel", "Uniform Radial Pressure",inputLabels, inputValues, inputDims, outputLabels, outputValues, outputDims)    


def revolveShell1C():

    pressure = prompt("Unit Pressure (lb/in2): ")
    thick = prompt("Thickness of Shell (in): ")
    radius = prompt("Radius of Curvature (in): ")
    length = prompt("Length of Shell (in): ")
    modOfElas = prompt("Modulus of Elasticity of Material (lb/in2): ")
    poisson = prompt("Poisson's Ratio of Material: ")

    sigma1 = pressure * radius / (2 * thick)
    sigma2 = pressure * radius / thick
    deltaR = pressure * radius**2 / (modOfElas * thick) * (1 - poisson / 2)
    deltaY = pressure * radius * length / (modOfElas * thick) * (0.5 - poisson)
    psi = 0

    inputLabels = ["Unit Pressure:                                ", "Thickness of Shell:                           ",
                   "Radius of Curvature of Shell:                 ", "Length of Shell:                              ",
                   "Modulus of Elasticity of Material:            ", "Poisson's Ratio of Material:                  "]
    inputValues = [round(pressure,2), round(thick,2), round(radius,2), round(length,2), round(modOfElas,2), round(poisson,2)]
    inputDims = ['  lb/in2', '  in', '  in', '  in', '  lb/in2', '  ']

    outputLabels = ["Meridian Stress:                              ", "Hoop Stress:                                  ",
                    "Change in Vessel Radius:                      ", "Change in Vessel Height:                      ",
                    "Rotation from Unloaded Position:              "]
    outputValues = [round(sigma1,2), round(sigma2,2), round(deltaR,2), round(deltaY,2), round(psi,2)]
    outputDims = ['  lb/in2', '  lb/in2', '  in', '  in', '  rad']


    return fileWriter("Thin-Walled Cylindrical Pressure Vessel", "Uniform Internal/External Pressure",inputLabels, inputValues, inputDims, outputLabels, outputValues, outputDims)    


def revolveShell1D():
    
    pressure = prompt("Max Unit Pressure (lb/in2): ")
    thick = prompt("Thickness of Shell (in): ")
    radius = prompt("Radius of Curvature (in): ")
    length = prompt("Length of Shell (in): ")
    distance = prompt("Location of Interest (in): ")
    modOfElas = prompt("Modulus of Elasticity of Material (lb/in2): ")
    poisson = prompt("Poisson's Ratio of Material: ")

    sigma1 = 0
    sigma2 = pressure * radius * distance / (length * thick)
    deltaR = pressure * radius**2 * distance / (modOfElas * thick * length)
    deltaY = -pressure * radius * poisson * distance**2 / (2 * modOfElas * thick * length)
    psi = pressure * radius**2 / (modOfElas * thick * length)


    inputLabels = ["Max Unit Pressure:                            ", "Thickness of Shell:                           ",
                   "Radius of Curvature of Shell:                 ", "Length of Shell:                              ",
                   "Point of Interest:                            ", "Modulus of Elasticity of Material:            ",
                   "Poisson's Ratio of Material:                  "]
    inputValues = [round(pressure,2), round(thick,2), round(radius,2), round(length,2), round(distance,2), round(modOfElas,2), round(poisson,2)]
    inputDims = ['  lb/in2', '  in', '  in', '  in', '  in', '  lb/in2', '  ']

    outputLabels = ["Meridian Stress:                              ", "Hoop Stress:                                  ",
                    "Change in Vessel Radius:                      ", "Change in Vessel Height:                      ",
                    "Rotation from Unloaded Position:              "]
    outputValues = [round(sigma1,2), round(sigma2,2), round(deltaR,2), round(deltaY,2), round(psi,2)]
    outputDims = ['  lb/in2', '  lb/in2', '  in', '  in', '  rad']


    return fileWriter("Thin-Walled Cylindrical Pressure Vessel", "Linearly Varying Radial Pressure",inputLabels, inputValues, inputDims, outputLabels, outputValues, outputDims)    


def revolveShell1E():
    
    density = prompt("Density (lb/in3): ")
    radius = prompt("Radius of Curvature (in): ")
    length = prompt("Length of Shell (in): ")
    modOfElas = prompt("Modulus of Elasticity of Material (lb/in2): ")
    poisson = prompt("Poisson's Ratio of Material: ")

    sigma1 = density * length
    sigma2 = 0
    deltaR = -density * poisson * radius * length / modOfElas
    deltaY = density * length**2 / (2 * modOfElas)
    psi = -density * poisson * radius / modOfElas


    inputLabels = ["Density of Material:                          ", "Radius of Curvature of Shell:                 ",
                   "Length of Shell:                              ", "Modulus of Elasticity of Material:            ",
                   "Poisson's Ratio of Material:                  "]
    inputValues = [round(density,2), round(radius,2), round(length,2), round(modOfElas,2), round(poisson,2)]
    inputDims = ['  lb/in3', '  in', '  in', '  lb/in2', '  ']

    outputLabels = ["Meridian Stress:                              ", "Hoop Stress:                                  ",
                    "Change in Vessel Radius:                      ", "Change in Vessel Height:                      ",
                    "Rotation from Unloaded Position:              "]
    outputValues = [round(sigma1,2), round(sigma2,2), round(deltaR,2), round(deltaY,2), round(psi,2)]
    outputDims = ['  lb/in2', '  lb/in2', '  in', '  in', '  rad']


    return fileWriter("Thin-Walled Cylindrical Pressure Vessel", "Self Weight",inputLabels, inputValues, inputDims, outputLabels, outputValues, outputDims)    


def revolveShell1F():
    
    density = prompt("Mass Density (lb/in3): ")
    rotate = prompt("Rate of Rotation (rad/sec): ")
    radius = prompt("Radius of Curvature (in): ")
    length = prompt("Length of Shell (in): ")
    modOfElas = prompt("Modulus of Elasticity of Material (lb/in2): ")
    poisson = prompt("Poisson's Ratio of Material: ")

    sigma1 = 0
    sigma2 = density * radius**2 * rotate**2
    deltaR = density * radius**3 * rotate**2 / modOfElas
    deltaY = -poisson * density * radius**2 * rotate**2 * length / modOfElas
    psi = 0


    inputLabels = ["Material Density:                             ", "Rate of Rotation:                             ",
                   "Radius of Curvature of Shell:                 ", "Length of Shell:                              ",
                   "Modulus of Elasticity of Material:            ", "Poisson's Ratio of Material:                  "]
    inputValues = [round(density,2), round(rotate,2), round(radius,2), round(length,2), round(modOfElas,2), round(poisson,2)]
    inputDims = ['  lb/in3', '  rad/sec', '  in', '  in', '  lb/in2', '  ']

    outputLabels = ["Meridian Stress:                              ", "Hoop Stress:                                  ",
                    "Change in Vessel Radius:                      ", "Change in Vessel Height:                      ",
                    "Rotation from Unloaded Position:              "]
    outputValues = [round(sigma1,2), round(sigma2,2), round(deltaR,2), round(deltaY,2), round(psi,2)]
    outputDims = ['  lb/in2', '  lb/in2', '  in', '  in', '  rad']


    return fileWriter("Thin-Walled Cylindrical Pressure Vessel", "Uniform Rotation About Central Axis",inputLabels, inputValues, inputDims, outputLabels, outputValues, outputDims)    


def revolveShell2A():
    
    pressure = prompt("Unit Pressure (lb/in2): ")
    thick = prompt("Thickness of Shell (in): ")
    radius = prompt("Radius of Curvature (in): ")
    alpha = prompt("Half-Angle Apex (rad): ")
    modOfElas = prompt("Modulus of Elasticity of Material (lb/in2): ")
    poisson = prompt("Poisson's Ratio of Material: ")

    sigma1 = pressure * radius / (2 * thick * cos(alpha))
    sigma2 = pressure * radius / (thick * cos(alpha))
    deltaR = pressure * radius**2 / (modOfElas * thick * cos(alpha)) * (1 - poisson / 2)
    deltaY = pressure * radius**2 / (4 * modOfElas * thick * sin(alpha)) * (1 - 2* poisson - 3 * tan(alpha)**2)
    psi = 3 * pressure * radius * tan(alpha) / (2 * modOfElas * thick * cos(alpha))


    inputLabels = ["Unit Pressure:                                ", "Thickness of Shell:                           ",
                   "Radius of Curvature of Shell:                 ", "Half-Angle Apex:                              ",
                   "Modulus of Elasticity of Material:            ", "Poisson's Ratio of Material:                  "]
    inputValues = [round(pressure,2), round(thick,2), round(radius,2), round(alpha,2), round(modOfElas,2), round(poisson,2)]
    inputDims = ['  lb/in2', '  in', '  in', '  rad', '  lb/in2', '  ']

    outputLabels = ["Meridian Stress:                              ", "Hoop Stress:                                  ",
                    "Change in Vessel Radius:                      ", "Change in Vessel Height:                      ",
                    "Rotation from Unloaded Position:              "]
    outputValues = [round(sigma1,2), round(sigma2,2), round(deltaR,2), round(deltaY,2), round(psi,2)]
    outputDims = ['  lb/in2', '  lb/in2', '  in', '  in', '  rad']


    return fileWriter("Thin-Walled Conical Pressure Vessel", "Uniform Internal/External Pressure",inputLabels, inputValues, inputDims, outputLabels, outputValues, outputDims)    


def revolveShell2B():
    
    density = prompt("Density (lb/in3): ")
    thick = prompt("Thickness of Shell (in): ")
    depth = prompt("Depth of Liquid (in): ")
    height = prompt("Height of Point of Interest (in): ")
    alpha = prompt("Half-Angle Apex (rad): ")
    modOfElas = prompt("Modulus of Elasticity of Material (lb/in2): ")
    poisson = prompt("Poisson's Ratio of Material: ")

    if height <= depth:
        sigma1 = density * height * tan(alpha) / (2 * thick * cos(alpha)) * (depth - 2 * height / 3)
        sigma2 = height * (depth - height) * density * tan(alpha) / (thick * cos(alpha))
        deltaR = density * height**2 * tan(alpha)**2 / (modOfElas * thick * cos(alpha)) * (depth * (1 - poisson / 2) - height * (1 - poisson / 3))
        deltaY = density * height**2 * sin(alpha) / (modOfElas * thick * cos(alpha)**4) * (depth / 4 * (1 - 2 * poisson) - height / 9 * (1 - 3 * poisson) - sin(alpha)**2 * (depth / 2 * (2 - poisson) - height / 3 * (3 - poisson)))
        psi = density * height * sin(alpha)**2 / (6 * modOfElas * thick * cos(alpha)**3) * (9* depth - 16 * height)
    else:
        sigma1 = density * depth**3 * tan(alpha) / (6 * thick * height * cos(alpha))
        sigma2 = 0
        deltaR = -poisson * density * depth**3 * tan(alpha)**2 / (6 * modOfElas * thick * cos(alpha))
        deltaY = density * depth**3 * sin(alpha) / (6 * modOfElas * thick * cos(alpha)**4) * (5 / 6 - poisson * (1 - sin(alpha)**2) + log(height / depth))
        psi = -density * depth**3 * sin(alpha)**2/ (6 * modOfElas * thick * cos(alpha)**2) * (1 / height)


    inputLabels = ["Density of Liquid:                            ", "Thickness of Shell:                           ",
                   "Depth of Liquid:                              ", "Height of Point of Interest:                  ",
                   "Half-Angle Apex:                              ", "Modulus of Elasticity of Material:            ",
                   "Poisson's Ratio of Material:                  "]
    inputValues = [round(density,2), round(thick,2), round(depth,2), round(height,2), round(alpha,2), round(modOfElas,2), round(poisson,2)]
    inputDims = ['  lb/in3', '  in', '  in', '  in', '  rad', '  lb/in2', '  ']

    outputLabels = ["Meridian Stress:                              ", "Hoop Stress:                                  ",
                    "Change in Vessel Radius:                      ", "Change in Vessel Height:                      ",
                    "Rotation from Unloaded Position:              "]
    outputValues = [round(sigma1,2), round(sigma2,2), round(deltaR,2), round(deltaY,2), round(psi,2)]
    outputDims = ['  lb/in2', '  lb/in2', '  in', '  in', '  rad']


    return fileWriter("Thin-Walled Conical Pressure Vessel", "Filled With Liquid to Depth",inputLabels, inputValues, inputDims, outputLabels, outputValues, outputDims)    



def revolveShell2C():
    
    density = prompt("Density (lb/in3): ")
    radius = prompt("Radius of Curvature (in): ")
    alpha = prompt("Half-Angle Apex(rad): ")
    modOfElas = prompt("Modulus of Elasticity of Material (lb/in2): ")
    poisson = prompt("Poisson's Ratio of Material: ")

    sigma1 = density * radius / (2 * sin(alpha) * cos(alpha))
    sigma2 = density * radius * tan(alpha)
    deltaR = density * radius**2 / (modOfElas * cos(alpha)) * (sin(alpha) - poisson / (2 * sin(alpha)))
    deltaY = density * radius**2 / (modOfElas * cos(alpha)**2) * (1 / (4 * sin(alpha)**2) - sin(alpha)**2)
    psi = 2 * density * radius / (modOfElas * cos(alpha)**2) * (sin(alpha)**2 * (1 + poisson / 2) - 0.25 * (1 + 2 * poisson))


    inputLabels = ["Density of Material:                          ", "Radius of Shell:                              ",
                   "Half-Angle Apex:                              ", "Modulus of Elasticity of Material:            ",
                   "Poisson's Ratio of Material:                  "]
    inputValues = [round(density,2), round(radius,2), round(alpha,2), round(modOfElas,2), round(poisson,2)]
    inputDims = ['  lb/in3', '  in', '  rad', '  lb/in2', '  ']

    outputLabels = ["Meridian Stress:                              ", "Hoop Stress:                                  ",
                    "Change in Vessel Radius:                      ", "Change in Vessel Height:                      ",
                    "Rotation from Unloaded Position:              "]
    outputValues = [round(sigma1,2), round(sigma2,2), round(deltaR,2), round(deltaY,2), round(psi,2)]
    outputDims = ['  lb/in2', '  lb/in2', '  in', '  in', '  rad']


    return fileWriter("Thin-Walled Conical Pressure Vessel", "Self Weight",inputLabels, inputValues, inputDims, outputLabels, outputValues, outputDims)    


def revolveShell2D():
    
    load = prompt("Load (lb): ")
    radiusBig = prompt("Large Radius of Curvature (in): ")
    radiusSmall = prompt("Small Radius of Curvature (in): ")
    alpha = prompt("Half-Angle Apex (rad): ")
    thick = prompt("Thickness of Shell (in): ")
    modOfElas = prompt("Modulus of Elasticity of Material (lb/in2): ")
    poisson = prompt("Poisson's Ratio of Material: ")

    sigma1 = load / (2 * pi * radiusBig * thick * cos(alpha))
    sigma2 = 0
    deltaR = -poisson * load / (2 * pi * modOfElas * thick * cos(alpha))
    deltaY = load / (2 * pi * modOfElas * sin(alpha) * cos(alpha)**2) * log(radiusBig / radiusSmall)
    psi = - load * sin(alpha) / (2 * pi * modOfElas * radiusBig * thick * cos(alpha)**2)


    inputLabels = ["Load:                                         ", "Large Radius of Curvature:                    ",
                   "Small Radius of Curvature:                    ", "Half-Angle Apex:                              ",
                   "Thickness of Shell:                           ", "Modulus of Elasticity of Material:            ",
                   "Poisson's Ratio of Material:                  "]
    inputValues = [round(density,2), round(radiusBig,2), round(radiusSmall,2), round(alpha,2), round(thick,2), round(modOfElas,2), round(poisson,2)]
    inputDims = ['  lb', '  in', '  in', '  rad', '  in', '  lb/in2', '  ']

    outputLabels = ["Meridian Stress:                              ", "Hoop Stress:                                  ",
                    "Change in Vessel Radius:                      ", "Change in Vessel Height:                      ",
                    "Rotation from Unloaded Position:              "]
    outputValues = [round(sigma1,2), round(sigma2,2), round(deltaR,2), round(deltaY,2), round(psi,2)]
    outputDims = ['  lb/in2', '  lb/in2', '  in', '  in', '  rad']


    return fileWriter("Thin-Walled Conical Pressure Vessel", "Tangential Loading",inputLabels, inputValues, inputDims, outputLabels, outputValues, outputDims)    


def revolveShell2E():
    
    pressure = prompt("Unit Pressure (lb/in2): ")
    radius = prompt("Radius of Curvature (in): ")
    alpha = prompt("Half-Angle Apex (rad): ")
    thick = prompt("Thickness of Shell (in): ")
    modOfElas = prompt("Modulus of Elasticity of Material (lb/in2): ")
    poisson = prompt("Poisson's Ratio of Material: ")

    sigma1 = pressure * radius / (2 * thick * cos(alpha))
    sigma2 = pressure * radius * sin(alpha)**2 / (thick * cos(alpha))
    deltaR = pressure * radius**2 / (modOfElas * thick * cos(alpha)) * (sin(alpha)**2 - poisson / 2)
    deltaY = pressure * radius**2 / (2 * modOfElas * thick * cos(alpha)**2) * (1 / (2 * sin(alpha)) + poisson * (1 - sin(alpha)) - 2* sin(alpha)**2)
    psi = pressure * radius * sin(alpha) / (2 * modOfElas * cos(alpha)**2) * (4 * sin(alpha)**2 - 1 - 2 * poisson * cos(alpha)**2)


    inputLabels = ["Unit Pressure:                                ", "Radius of Curvature:                          ",
                   "Half-Angle Apex:                              ", "Thickness of Shell:                           ",
                   "Modulus of Elasticity of Material:            ", "Poisson's Ratio of Material:                  "]
    inputValues = [round(pressure,2), round(radius,2), round(alpha,2), round(thick,2), round(modOfElas,2), round(poisson,2)]
    inputDims = ['  lb/in2', '  in', '  rad', '  in', '  lb/in2', '  ']

    outputLabels = ["Meridian Stress:                              ", "Hoop Stress:                                  ",
                    "Change in Vessel Radius:                      ", "Change in Vessel Height:                      ",
                    "Rotation from Unloaded Position:              "]
    outputValues = [round(sigma1,2), round(sigma2,2), round(deltaR,2), round(deltaY,2), round(psi,2)]
    outputDims = ['  lb/in2', '  lb/in2', '  in', '  in', '  rad']


    return fileWriter("Thin-Walled Conical Pressure Vessel", "Uniform Loading",inputLabels, inputValues, inputDims, outputLabels, outputValues, outputDims)    


def revolveShell2F():
    
    density = prompt("Mass Density (lb/in3): ")
    radius = prompt("Radius of Curvature (in): ")
    rotate = prompt("Rate of Rotation (rad/sec): ")
    alpha = prompt("Half-Angle Apex (rad): ")
    modOfElas = prompt("Modulus of Elasticity of Material (lb/in2): ")

    sigma1 = 0
    sigma2 = density * radius**2 * rotate**2
    deltaR = density * radius**3 * rotate**2 / modOfElas
    deltaY = -density * radius**3 * rotate**2 / (modOfElas * cos(alpha)) * (sin(alpha) + poisson / (3 * sin(alpha)))
    psi = density * radiu**2 * rotate**2 * tan(alpha) / modOfElas * (3 + poisson)


    inputLabels = ["Mass Density:                                 ", "Radius of Curvature:                          ",
                   "Rate of Rotation:                             ", "Half-Angle Apex:                              ",
                   "Modulus of Elasticity of Material:            "]
    inputValues = [round(density,2), round(radius,2), round(rotate,2), round(alpha,2), round(modOfElas,2)]
    inputDims = ['  lb/in3', '  in', '  rad/sec', '  rad', '  lb/in2']

    outputLabels = ["Meridian Stress:                              ", "Hoop Stress:                                  ",
                    "Change in Vessel Radius:                      ", "Change in Vessel Height:                      ",
                    "Rotation from Unloaded Position:              "]
    outputValues = [round(sigma1,2), round(sigma2,2), round(deltaR,2), round(deltaY,2), round(psi,2)]
    outputDims = ['  lb/in2', '  lb/in2', '  in', '  in', '  rad']


    return fileWriter("Thin-Walled Conical Pressure Vessel", "Uniform Rotation",inputLabels, inputValues, inputDims, outputLabels, outputValues, outputDims)    


def revolveShell3A():
    
    pressure = prompt("Unit Pressure (lb/in2): ")
    radius = prompt("Radius of Curvature (in): ")
    thick = prompt("Thickness of Shell (in): ")
    theta = prompt("Loaded Sector (rad): ")
    modOfElas = prompt("Modulus of Elasticity of Material (lb/in2): ")
    poisson = prompt("Poisson's Ratio of Material: ")

    sigma1 = pressure * radius / (2 * thick)
    sigma2 = sigma1
    deltaR = pressure * radius**2 * (1 - poisson) * sin(theta) / (2 * modOfElas * thick)
    deltaR2 = pressure * radius**2 * (1 - poisson) / (2 * modOfElas * thick)
    deltaY = pressure * radius**2 * (1 - poisson) * (1 - cos(theta)) / (2 * modOfElas * thick)
    psi = 0

    inputLabels = ["Unit Pressure:                                ", "Radius of Curvature:                          ",
                   "Thickness of Shell:                           ", "Loaded Sector:                                ",
                   "Modulus of Elasticity of Material:            ", "Poisson's Ratio of Material:                  "]
    inputValues = [round(pressure,2), round(radius,2), round(thick,2), round(theta,2), round(modOfElas,2), round(poisson,2)]
    inputDims = ['  lb/in2', '  in', '  in', '  rad', '  lb/in2', '  ']

    outputLabels = ["Meridian Stress:                              ", "Hoop Stress:                                  ",
                    "Change in Vessel Chord Length:                ", "Change in Vessel Radius:                      ",
                    "Change in Vessel Height:                      ", "Rotation from Unloaded Position:              "]
    outputValues = [round(sigma1,2), round(sigma2,2), round(deltaR,2), round(deltaR2,2), round(deltaY,2), round(psi,2)]
    outputDims = ['  lb/in2', '  lb/in2', '  in', '  in', '  in', '  rad']


    return fileWriter("Thin-Walled Spherical Pressure Vessel", "Uniform Internal/External Pressure",inputLabels, inputValues, inputDims, outputLabels, outputValues, outputDims)    


def revolveShell3B():
    
    density = prompt("Density (lb/in3): ")
    radius = prompt("Radius of Curvature (in): ")
    thick = prompt("Thickness of Shell (in): ")
    theta = prompt("Loaded Sector (rad): ")
    depth = prompt("Depth of Liquid (in): ")
    modOfElas = prompt("Modulus of Elasticity of Material (lb/in2): ")
    poisson = prompt("Poisson's Ratio of Material: ")

    sigma1 = density * radius**2 / (6 * thick) * (3 * (depth / radius) - 1 + 2 * cos(theta)**2 / (1 + cos(theta)))
    sigma2 = density * radius**2 / (6 * thick) * (3 * (depth / radius) - 5 + (3 + 2 * cos(theta)) * 2* cos(theta) / (1 + cos(theta)))
    deltaR = density * radius**3 / (6 * thick) * (3 * (1 - poisson) - 5 + (3 + 2 * cos(theta)) * 2 * cos(theta)) / (1 + cos(theta))
    deltaY = density * radius**3 / (6 * modOfElas * thick) * (3 * (1 - poisson) * (depth / radius * (1 - cos(theta)) + cos(theta)) - (2 - poisson) * cos(theta)**2 + (1 + poisson) * (1 + 2 * log(2 / (1+ cos(theta)))))
    psi = -density * radius**2 / (modOfElas * thick) * sin(theta)


    inputLabels = ["Density of Liquid:                            ", "Radius of Curvature:                          ",
                   "Thickness of Shell:                           ", "Loaded Sector:                                ",
                   "Depth of Liquid:                              ", "Modulus of Elasticity of Material:            ",
                   "Poisson's Ratio of Material:                  "]
    inputValues = [round(density,2), round(radius,2), round(thick,2), round(theta,2), round(depth,2), round(modOfElas,2), round(poisson,2)]
    inputDims = ['  lb/in3', '  in', '  in', '  rad', '  in', '  lb/in2', '  ']

    outputLabels = ["Meridian Stress:                              ", "Hoop Stress:                                  ",
                    "Change in Vessel Radius:                      ", "Change in Vessel Height:                      ",
                    "Rotation from Unloaded Position:              "]
    outputValues = [round(sigma1,2), round(sigma2,2), round(deltaR,2), round(deltaY,2), round(psi,2)]
    outputDims = ['  lb/in2', '  lb/in2', '  in', '  in', '  rad']


    return fileWriter("Thin-Walled Spherical Pressure Vessel", "Filled to Depth with Liquid",inputLabels, inputValues, inputDims, outputLabels, outputValues, outputDims)    


def revolveShell3C():
    
    density = prompt("Density (lb/in3): ")
    radius = prompt("Radius of Curvature (in): ")
    theta = prompt("Loaded Sector (rad): ")
    modOfElas = prompt("Modulus of Elasticity of Material (lb/in2): ")
    poisson = prompt("Poisson's Ratio of Material: ")

    sigma1 = density * radius / (1 + cos(theta))
    sigma2 = -density * radius * (1 / (1 + cos(theta)) - cos(theta))
    deltaR = -density * radius**2 * sin(theta) / modOfElas * (1 + poisson / (1 + cos(theta)) - cos(theta))
    deltaY = density * radius**2 / modOfElas * (sin(theta)**2 + (1 + poisson) * log(2 / (1 + cos(theta))))
    psi = -density * radius / modOfElas * (2 + poisson) * sin(theta)

    inputLabels = ["Density of Material:                          ", "Radius of Curvature:                          ",
                   "Loaded Sector:                                ", "Modulus of Elasticity of Material:            ",
                   "Poisson's Ratio of Material:                  "]
    inputValues = [round(density,2), round(radius,2), round(theta,2), round(modOfElas,2), round(poisson,2)]
    inputDims = ['  lb/in3', '  in', '  rad', '  lb/in2', '  ']

    outputLabels = ["Meridian Stress:                              ", "Hoop Stress:                                  ",
                    "Change in Vessel Radius:                      ", "Change in Vessel Height:                      ",
                    "Rotation from Unloaded Position:              "]
    outputValues = [round(sigma1,2), round(sigma2,2), round(deltaR,2), round(deltaY,2), round(psi,2)]
    outputDims = ['  lb/in2', '  lb/in2', '  in', '  in', '  rad']


    return fileWriter("Thin-Walled Spherical Pressure Vessel", "Self Weight",inputLabels, inputValues, inputDims, outputLabels, outputValues, outputDims)    


def revolveShell3D():
    
    load = prompt("Load (lb): ")
    radius = prompt("Radius of Curvature (in): ")
    theta = prompt("Top of Loaded Sector (rad): ")
    thetaNot = prompt("Bottom of Loaded Sector (rad): ")
    thick = prompt("Thickness of Shell (in): ")
    modOfElas = prompt("Modulus of Elasticity of Material (lb/in2): ")
    poisson = prompt("Poisson's Ratio of Material: ")

    sigma1 = load / (2 * pi * radius * thick * sin(theta)**2)
    sigma2 = -sigma1
    deltaR = -load * (1 + poisson) / (2 * pi * modOfElas * thick * sin(theta))
    deltaY = load * (1 + poisson) / (2 * pi * modOfElas * thick) * (log(tan(theta / 2)) - log(tan(thetaNot / 2)))
    psi = 0


    inputLabels = ["Load:                                         ", "Radius of Curvature:                          ",
                   "Top of Loaded Sector:                         ", "Bottom of Loaded Sector:                      ",
                   "Thickness of Shell:                           ", "Modulus of Elasticity of Material:            ",
                   "Poisson's Ratio of Material:                  "]
    inputValues = [round(load,2), round(radius,2), round(theta,2), round(thetaNot,2), round(thick,2), round(modOfElas,2), round(poisson,2)]
    inputDims = ['  lb', '  in', '  rad', '  rad', '  in', '  lb/in2', '  ']

    outputLabels = ["Meridian Stress:                              ", "Hoop Stress:                                  ",
                    "Change in Vessel Radius:                      ", "Change in Vessel Height:                      ",
                    "Rotation from Unloaded Position:              "]
    outputValues = [round(sigma1,2), round(sigma2,2), round(deltaR,2), round(deltaY,2), round(psi,2)]
    outputDims = ['  lb/in2', '  lb/in2', '  in', '  in', '  rad']


    return fileWriter("Thin-Walled Spherical Pressure Vessel", "Tangential Loading",inputLabels, inputValues, inputDims, outputLabels, outputValues, outputDims)    


def revolveShell3E():
    
    pressure = prompt("Unit Pressure (lb/in2): ")
    radius = prompt("Radius of Curvature (in): ")
    theta = prompt("Top of Loaded Sector (rad): ")
    thick = prompt("Thickness of Shell (in): ")
    modOfElas = prompt("Modulus of Elasticity of Material (lb/in2): ")
    poisson = prompt("Poisson's Ratio of Material: ")

    sigma1 = pressure * radius / (2 * thick)
    sigma2 = pressure * radius / (2 * thick) * cos(2 * theta)
    deltaR = pressure * radius**2 * sin(theta) / (2 * modOfElas * thick) * (cos(2 * theta) - poisson)
    deltaY = pressure * radius**2 / (2 * modOfElas * thick) * (2 * (1 - cos(theta)**3) + (1 + poisson) * (1 - cos(theta)))
    psi = -pressure * radius / (modOfElas * thick) * (3 + poisson) * sin(theta) * cos(theta)

    inputLabels = ["Unit Pressure:                                ", "Radius of Curvature:                          ",
                   "Loaded Sector:                                ", "Thickness of Shell:                           ",
                   "Modulus of Elasticity of Material:            ", "Poisson's Ratio of Material:                  "]
    inputValues = [round(pressure,2), round(radius,2), round(theta,2), round(thick,2), round(modOfElas,2), round(poisson,2)]
    inputDims = ['  lb/in2', '  in', '  rad', '  in', '  lb/in2', '  ']

    outputLabels = ["Meridian Stress:                              ", "Hoop Stress:                                  ",
                    "Change in Vessel Radius:                      ", "Change in Vessel Height:                      ",
                    "Rotation from Unloaded Position:              "]
    outputValues = [round(sigma1,2), round(sigma2,2), round(deltaR,2), round(deltaY,2), round(psi,2)]
    outputDims = ['  lb/in2', '  lb/in2', '  in', '  in', '  rad']


    return fileWriter("Thin-Walled Spherical Pressure Vessel", "Uniform Loading on Horizontal Projected Area",inputLabels, inputValues, inputDims, outputLabels, outputValues, outputDims)    


def revolveShell3F():
    
    density = prompt("Mass Density (lb/in3): ")
    radius = prompt("Radius of Curvature (in): ")
    theta = prompt("Top of Loaded Sector (rad): ")
    rotate = prompt("Rate of Rotation (rad/sec): ")
    modOfElas = prompt("Modulus of Elasticity of Material (lb/in2): ")
    poisson = prompt("Poisson's Ratio of Material: ")

    sigma1 = 0
    sigma2 = density * radius**2 * rotate**2
    deltaR = density * radius**3 * rotate**2 / modOfElas
    deltaY = -density * radius**3 * rotate**2 / modOfElas * (1 + poisson - poisson * cos(theta) - cos(theta)**3)
    psi = density * radius**2 * rotate**2 * sin(theta) * cos(theta) / modOfElas * (3 + poisson)

    inputLabels = ["Density of Material:                          ", "Radius of Curvature:                          ",
                   "Loaded Sector:                                ", "Rate of Rotation:                             ",
                   "Modulus of Elasticity of Material:            ", "Poisson's Ratio of Material:                  "]
    inputValues = [round(density,2), round(radius,2), round(theta,2), round(rotate,2), round(modOfElas,2), round(poisson,2)]
    inputDims = ['  lb/in3', '  in', '  rad', '  rad/sec', '  lb/in2', '  ']

    outputLabels = ["Meridian Stress:                              ", "Hoop Stress:                                  ",
                    "Change in Vessel Radius:                      ", "Change in Vessel Height:                      ",
                    "Rotation from Unloaded Position:              "]
    outputValues = [round(sigma1,2), round(sigma2,2), round(deltaR,2), round(deltaY,2), round(psi,2)]
    outputDims = ['  lb/in2', '  lb/in2', '  in', '  in', '  rad']


    return fileWriter("Thin-Walled Spherical Pressure Vessel", "Uniform Rotation",inputLabels, inputValues, inputDims, outputLabels, outputValues, outputDims)    


def revolveShell4A():
    
    pressure = prompt("Unit Pressure (lb/in2): ")
    radius1 = prompt("First Radius of Curvature (in): ")
    radius2 = prompt("Second Radius of Curvature (in): ")
    theta = prompt("Top of Loaded Sector (rad): ")
    height = prompt("Height of Point (in): ")
    thick = prompt("Thickness of Shell (in): ")
    modOfElas = prompt("Modulus of Elasticity of Material (lb/in2): ")
    poisson = prompt("Poisson's Ratio of Material: ")

    sigma1 = pressure * radius2 / (2 * thick)
    sigma2 = pressure * radius2 / (2 * thick) * (2 - radius2 / radius1)
    deltaR = pressure * radius2**2 * sin(theta) / (2 * modOfElas * thick) * (2 - (radius2 / radius1) - poisson)
    psi = pressure * radius2**2 / (2 * modOfElas * thick * radius1 * tan(theta)) * (3 * radius1 / radius2 - 5 + Radius2 / Radius1 * (2 + 1 / radius1 * depth * radius1 / (depth * theta) * tan(theta)))

    inputLabels = ["Unit Pressure:                                ", "First Radius of Curvature:                    ",
                   "Second Radius of Curvature:                   ", "Loaded Sector:                                ",
                   "Distance to Point of Interest:                ", "Thickness of Shell:                           ",
                   "Modulus of Elasticity of Material:            ", "Poisson's Ratio of Material:                  "]
    inputValues = [round(pressure,2), round(radius1,2), round(radius2,2), round(theta,2), round(height,2), round(thick,2), round(modOfElas,2), round(poisson,2)]
    inputDims = ['  lb/in2', '  in', '  in', '  rad', '  in', '  in', '  lb/in2', '  ']

    outputLabels = ["Meridian Stress:                              ", "Hoop Stress:                                  ",
                    "Change in Vessel Radius:                      ", "Rotation from Unloaded Position:              "]
    outputValues = [round(sigma1,2), round(sigma2,2), round(deltaR,2), round(psi,2)]
    outputDims = ['  lb/in2', '  lb/in2', '  in', '  rad']


    return fileWriter("Thin-Walled Pressure Vessel, Smooth Figure of Revolution", "Uniform Internal/External Pressure",inputLabels, inputValues, inputDims, outputLabels, outputValues, outputDims)    


def revolveShell4B():
    
    density = prompt("Density of Liquid (lb/in3): ")
    radius1 = prompt("First Radius of Curvature (in): ")
    radius2 = prompt("Second Radius of Curvature (in): ")
    theta = prompt("Top of Loaded Sector (rad): ")
    weight = prompt("Weight of Liquid to Point (in): ")
    depth = prompt("Depth of Liquid (in): ")
    height = prompt("Distance to Point (in): ")
    thick = prompt("Thickness of Shell (in): ")
    modOfElas = prompt("Modulus of Elasticity of Material (lb/in2): ")
    poisson = prompt("Poisson's Ratio of Material: ")

    sigma1 = weight / (2 * pi * radius2 * thick * sin(theta)**2) + density * radius2 * (depth - height) / (2 * thick)
    sigma2 = -weight / (2 * pi * radius1 * thick * sin(theta)**2) + density * radius2 * (depth - height) / (2 * thick) * (2 - radius2 / radius1)
    deltaR = radius2 * sin(theta) / modOfElas * (sigma2 - poisson * sigma1)


    inputLabels = ["Density of Liquid:                            ", "First Radius of Curvature:                    ",
                   "Second Radius of Curvature:                   ", "Loaded Sector:                                ",
                   "Weight of Liquid:                             ", "Depth of Liquid:                              ",
                   "Distance to Point of Interest:                ", "Thickness of Shell:                           ",
                   "Modulus of Elasticity of Material:            ", "Poisson's Ratio of Material:                  "]
    inputValues = [round(density,2), round(radius1,2), round(radius2,2), round(theta,2), round(weight,2), round(depth,2), round(height,2), round(thick,2), round(modOfElas,2), round(poisson,2)]
    inputDims = ['  lb/in3', '  in', '  in', '  rad', '  lb', '  in', '  in', '  in', '  lb/in2', '  ']

    outputLabels = ["Meridian Stress:                              ", "Hoop Stress:                                  ",
                    "Change in Vessel Radius:                      "]
    outputValues = [round(sigma1,2), round(sigma2,2), round(deltaR,2)]
    outputDims = ['  lb/in2', '  lb/in2', '  in']


    return fileWriter("Thin-Walled Pressure Vessel, Smooth Figure of Revolution", "Filled to Depth with Liquid",inputLabels, inputValues, inputDims, outputLabels, outputValues, outputDims)    


def revolveShell4C():

    density = prompt("Density (lb/in3): ")
    radius1 = prompt("First Radius of Curvature (in): ")
    radius2 = prompt("Second Radius of Curvature (in): ")
    theta = prompt("Top of Loaded Sector (rad): ")
    weight = prompt("Weight of Vessel to Point (in): ")
    thick = prompt("Thickness of Shell (in): ")
    modOfElas = prompt("Modulus of Elasticity of Material (lb/in2): ")
    poisson = prompt("Poisson's Ratio of Material: ")

    sigma1 = weight / (2 * pi * radius2 * thick * sin(theta)**2)
    sigma2 = weight / (2 * pi * radius1 * thick * sin(theta)**2) + density * radius2 * cos(theta)
    deltaR = radius2 * sin(theta) / modOfElas * (sigma2 - poisson * sigma1)


    inputLabels = ["Density:                                      ", "First Radius of Curvature:                    ",
                   "Second Radius of Curvature:                   ", "Loaded Sector:                                ",
                   "Weight of Vessel to Point:                    ", "Thickness of Shell:                           ",
                   "Modulus of Elasticity of Material:            ", "Poisson's Ratio of Material:                  "]
    inputValues = [round(density,2), round(radius1,2), round(radius2,2), round(theta,2), round(weight,2), round(thick,2), round(modOfElas,2), round(poisson,2)]
    inputDims = ['  lb/in3', '  in', '  in', '  rad', '  lb', '  in', '  lb/in2', '  ']

    outputLabels = ["Meridian Stress:                              ", "Hoop Stress:                                  ",
                    "Change in Vessel Radius:                      "]
    outputValues = [round(sigma1,2), round(sigma2,2), round(deltaR,2)]
    outputDims = ['  lb/in2', '  lb/in2', '  in']


    return fileWriter("Thin-Walled Pressure Vessel, Smooth Figure of Revolution", "Self Weight",inputLabels, inputValues, inputDims, outputLabels, outputValues, outputDims)    


def revolveShell4D():

    load = prompt("Load (lb): ")           
    radius1 = prompt("First Radius of Curvature (in): ")
    radius2 = prompt("Second Radius of Curvature (in): ")
    theta = prompt("Top of Loaded Sector (rad): ")
    height = prompt("Height to Point (in): ")
    thick = prompt("Thickness of Shell (in): ")
    modOfElas = prompt("Modulus of Elasticity of Material (lb/in2): ")
    poisson = prompt("Poisson's Ratio of Material: ")

    sigma1 = load / (2 * pi * radius2 * thick * sin(theta)**2)
    sigma2 = -load / (2 * pi * radius1 * thick * sin(theta)**2)
    deltaR = -load / (2 * pi * modOfElas * thick * sin(theta)) * (radius2 / radius1 + poisson)
    psi = -load / (2 * pi * modOfElas * thick * radius1 * sin(theta)**2) * (1 / tan(theta) * (1 + radius1 / radius2 - 2 * radius2 / radius1) - radius2 / radius1**2 * height * radius1 / (height * theta))


    inputLabels = ["Load:                                         ", "First Radius of Curvature:                    ",
                   "Second Radius of Curvature:                   ", "Loaded Sector:                                ",
                   "Distance to Point of Interest:                ", "Thickness of Shell:                           ",
                   "Modulus of Elasticity of Material:            ", "Poisson's Ratio of Material:                  "]
    inputValues = [round(density,2), round(radius1,2), round(radius2,2), round(theta,2), round(height,2), round(thick,2), round(modOfElas,2), round(poisson,2)]
    inputDims = ['  lb', '  in', '  in', '  rad', '  in', '  in', '  lb/in2', '  ']

    outputLabels = ["Meridian Stress:                              ", "Hoop Stress:                                  ",
                    "Change in Vessel Radius:                      ", "Rotation from Unloaded Position:              "]
    outputValues = [round(sigma1,2), round(sigma2,2), round(deltaR,2), round(psi,2)]
    outputDims = ['  lb/in2', '  lb/in2', '  in', '  rad']


    return fileWriter("Thin-Walled Pressure Vessel, Smooth Figure of Revolution", "Tangential Loading",inputLabels, inputValues, inputDims, outputLabels, outputValues, outputDims)    


def revolveShell4E():

    pressure = prompt("Unit Pressure (lb/in2): ")
    radius1 = prompt("First Radius of Curvature (in): ")
    radius2 = prompt("Second Radius of Curvature (in): ")
    theta = prompt("Top of Loaded Sector (rad): ")
    height = prompt("Height to Point (in): ")
    thick = prompt("Thickness of Shell (in): ")
    modOfElas = prompt("Modulus of Elasticity of Material (lb/in2): ")
    poisson = prompt("Poisson's Ratio of Material: ")

    sigma1 = pressure * radius2 / (2 * thick)
    sigma2 = pressure * radius2 / (2 * thick) * (2 * cos(theta)**2 - radius2 / radius1)
    deltaR = pressure * radius2**2 * sin(theta) / (2 * modOfElas * thick) * (2 * cos(theta)**2 - radius2 / radius1 - poisson)
    psi = pressure / (2 * modOfElas * thick * radius1 * tan(theta)) * (radius1 * radius2 * (4 * cos(theta)**2 - 1 - 2 * poisson * sin(theta)**2) - radius2**2 * (7 - 2 * cos(theta)) + radius2**3 / radius1 * (2 + tan(theta) / radius1 * height * radius1 / (height * theta)))


    inputLabels = ["Unit Pressure:                                ", "First Radius of Curvature:                    ",
                   "Second Radius of Curvature:                   ", "Loaded Sector:                                ",
                   "Distance to Point of Interest:                ", "Thickness of Shell:                           ",
                   "Modulus of Elasticity of Material:            ", "Poisson's Ratio of Material:                  "]
    inputValues = [round(pressure,2), round(radius1,2), round(radius2,2), round(theta,2), round(height,2), round(thick,2), round(modOfElas,2), round(poisson,2)]
    inputDims = ['  lb/in2', '  in', '  in', '  rad', '  in', '  in', '  lb/in2', '  ']

    outputLabels = ["Meridian Stress:                              ", "Hoop Stress:                                  ",
                    "Change in Vessel Radius:                      ", "Rotation from Unloaded Position:              "]
    outputValues = [round(sigma1,2), round(sigma2,2), round(deltaR,2), round(psi,2)]
    outputDims = ['  lb/in2', '  lb/in2', '  in', '  rad']


    return fileWriter("Thin-Walled Pressure Vessel, Smooth Figure of Revolution", "Uniform Loading on Horizontal Projected Area",inputLabels, inputValues, inputDims, outputLabels, outputValues, outputDims)    


def revolveShell4F():

    density = prompt("Mass Density (lb/in3): ")
    radius1 = prompt("First Radius of Curvature (in): ")
    radius2 = prompt("Second Radius of Curvature (in): ")
    theta = prompt("Top of Loaded Sector (rad): ")
    rotate = prompt("Rate of Rotation (rad/sec): ")
    modOfElas = prompt("Modulus of Elasticity of Material (lb/in2): ")
    poisson = prompt("Poisson's Ratio of Material: ")

    sigma1 = 0
    sigma2 = density * radius2**2 * rotate**2
    deltaR = density * radius2**3 * rotate**2 / modOfElas
    psi = density * radius2**2 * rotate**2 / (modOfElas * tan(theta)) * (3 + poisson)


    inputLabels = ["Load:                                         ", "First Radius of Curvature:                    ",
                   "Second Radius of Curvature:                   ", "Loaded Sector:                                ",
                   "Rate of Rotation:                             ", "Modulus of Elasticity of Material:            ",
                   "Poisson's Ratio of Material:                  "]
    inputValues = [round(density,2), round(radius1,2), round(radius2,2), round(theta,2), round(rotate,2), round(modOfElas,2), round(poisson,2)]
    inputDims = ['  lb', '  in', '  in', '  rad', '  rad/sec', '  lb/in2', '  ']

    outputLabels = ["Meridian Stress:                              ", "Hoop Stress:                                  ",
                    "Change in Vessel Radius:                      ", "Rotation from Unloaded Position:              "]
    outputValues = [round(sigma1,2), round(sigma2,2), round(deltaR,2), round(psi,2)]
    outputDims = ['  lb/in2', '  lb/in2', '  in', '  rad']


    return fileWriter("Thin-Walled Pressure Vessel, Smooth Figure of Revolution", "Uniform Rotation",inputLabels, inputValues, inputDims, outputLabels, outputValues, outputDims)    


def revolveShell5A():

    pressure = prompt("Unit Pressure (lb/in2): ")
    radius1 = prompt("Radius to Centerline of Toroid (in): ") #a
    radius2 = prompt("Radius of Toroid (in): ") #b
    thick = prompt("Thickness of Shell (in): ")
    height = prompt("Distance to Point (in): ")
    modOfElas = prompt("Modulus of Elasticity of Material (lb/in2): ")
    poisson = prompt("Poisson's Ratio of Material: ")

    sigma1 = pressure * radius2 / (2 * thick) * (height + radius1) / height
    sigma2 = pressure * radius2 / (2 * thick)
    deltaR = pressure * radius2 / (2 * modOfElas * thick) * (height - poisson * (height + radius1))


    inputLabels = ["Unit Pressure:                                ", "Radius to Centerline of Toroid:               ",
                   "Radius of Toroid:                             ", "Distance to Point of Interest:                ",
                   "Thickness of Shell:                           ", "Modulus of Elasticity of Material:            ",
                   "Poisson's Ratio of Material:                  "]
    inputValues = [round(pressure,2), round(radius1,2), round(radius2,2), round(height,2), round(thick,2), round(modOfElas,2), round(poisson,2)]
    inputDims = ['  lb/in2', '  in', '  in', '  in', '  in', '  lb/in2', '  ']

    outputLabels = ["Meridian Stress:                              ", "Hoop Stress:                                  ",
                    "Change in Vessel Radius:                      "]
    outputValues = [round(sigma1,2), round(sigma2,2), round(deltaR,2)]
    outputDims = ['  lb/in2', '  lb/in2', '  in']


    return fileWriter("Thin-Walled Toroidal Pressure Vessel", "Uniform Internal/External Pressure",inputLabels, inputValues, inputDims, outputLabels, outputValues, outputDims)    
