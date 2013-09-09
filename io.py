from time import sleep
from datetime import datetime

def prompt(message):

    variable = None
    while variable is None:
        try:
            variable = float(raw_input(message))
        except ValueError:
            time.sleep(0)

    return variable

def fileWriter(elementType, loadCase, inputLabels, inputValues, inputDims, outputLabels, outputValues, outputDims):
    
    fileName = raw_input("Output File Name: ") + ".txt"
    output = open(fileName, 'w')
    project = raw_input("Project Number: ")
    output.write("    Roark Equations for Stress and Strain\n")
    output.write("    %s\n" %(elementType))
    output.write("    %s\n" %(loadCase))
    output.write("\n    Program Release 20130909\n\n")
    output.write("\n    Project Number    %s\n" %(project))
    output.write("    Calculated %s\n" %(str(datetime.now())[:19]))
    output.write("\n\nINPUT DATA\n\n")

    for each in range(len(inputLabels)):
        output.write(inputLabels[each])
        output.write(str(inputValues[each]))
        output.write(inputDims[each])
        output.write("\n")

            
    output.write("\n\nOUTPUT DATA\n\n")

    for each in range(len(outputLabels)):
        output.write(outputLabels[each])
        output.write(str(outputValues[each]))
        output.write(outputDims[each])
        output.write("\n")

    output.close()
