from sys import exit
from choices import *

def menu():
# main menu 'screen' for element type selection

    print '''
    Stress and Strain of Structural Elements

    Options
    1. Elastic Straight Beam
    2. Beam on Elastic Foundation
    3. Annular Plate
    4. Shell of Revolution
    5. Stress Concentration
    6. Exit
    
    '''
    choice = raw_input("> ")

    #checks for appropriate input, continues asking until valid input received
    validOptions = ["1","2","3","4","5","6"]
    while choice not in validOptions:
        print "Not a Valid Option."
        choice = raw_input("> ")

    if choice == "1":
        straightBeam() 
    elif choice == "2":
        elasticFdn()
    elif choice == "3":
        annularPlate()
    elif choice == "4":
        revolveShell()
    elif choice == "5":
        crack()
    elif choice == "6":
        exit(0)
    
    
def straightBeam():
    #'screen' to choose end conditions of beam being tested

    print '''
    Stress and Strain of Structural Elements
    Straight Beams: End Conditions

    Options
    1. Left End Free, Right End Fixed (Cantilever)
    2. Left End Guided, Right End Fixed
    3. Left End Simply Supported, Right End Fixed
    4. Left End Fixed, Right End Fixed
    5. Left End Simply Supported, Right End Simply Supported
    6. Left End Guided, Right End Simply Supported
    7. Return to Menu
    8. Exit
    '''
    endCondition = raw_input("> ")

    #check for valid input
    validOptions = ["1","2","3","4","5","6","7","8"]
    while endCondition not in validOptions:
        print "Not a Valid Option."
        endCondition = raw_input("> ")

    if endCondition == "7":
        menu()
    elif endCondition == "8":
        exit(0)
    else:
        straightBeamLoadCase(endCondition)
        #end condition must be combined with load case to determine calcs used

def straightBeamLoadCase(endCondition):
    #'screen' to choose load case to calculate
    
    print '''
    Stress and Strain of Structural Elements
    Straight Beams: Load Cases

    Options
    1. Concentrated Intermediate Load
    2. Partial Distributed Load
    3. Concentrated Intermediate Moment
    4. Intermediate Externally Created Angular Deformation
    5. Intermediate Externally Created Lateral Displacement
    6. Uniform Temperature Variation (from top to bottom, from a to l)
    7. Return to End Condition Choices
    8. Exit
    '''
    loadCase = raw_input("> ")

    #check for valid input
    validOptions = ["1","2","3","4","5","6","7","8"]
    while loadCase not in validOptions:
        print "Not a Valid Option."
        loadCase = raw_input("> ")

    choice = loadCase+endCondition
    #see choices.py for connection between this file  and calc file
        
    if loadCase == "7":
        straightBeam()
    elif loadCase == "8":
        exit(0)
    else:
        straightBeamChoices(choice)

    straightBeamEnd(choice)
    

def straightBeamEnd(choice):

    print '''
    Analysis Complete.
    What would you like to do now?

    1. Calculate Another Beam of This Type
    2. Return to Main Menu
    3. Exit
    '''
    
    nextStep = raw_input("> ")

    validOptions = ["1","2","3"]
    while nextStep not in validOptions:
        print "Not a Valid Option."
        nextStep = raw_input("> ")

    if nextStep == "1":
        straightBeamChoices(choice)
    elif nextStep == "2":
        menu()
    elif nextStep == "3":
        exit(0)

    straightBeamEnd(choice)


def elasticFdn():
    #'screen' to choose end conditions

    print '''
    Stress and Strain of Structural Elements
    Beam on Elastic Foundation: End Conditions

    Options
    1.  Left End Free, Right End Free
    2.  Left End Free, Right End Guided
    3.  Left End Free, Right End Simply Supported
    4.  Left End Free, Right End Fixed
    5.  Left End Guided, Right End Free
    6.  Left End Guided, Right End Guided
    7.  Left End Guided, Right End Simply Supported
    8.  Left End Guided, Right End Fixed
    9.  Left End Simply Supported, Right End Free
    10. Left End Simply Supported, Right End Guided
    11. Left End Simply Supported, Right End Simply Supported
    12. Left End Simply Supported, Right End Fixed
    13. Left End Fixed, Right End Free
    14. Left End Fixed, Right End Guided
    15. Left End Fixed, Right End Simply Supported
    16. Left End Fixed, Right End Fixed
    17. Return to Menu
    18. Exit
    '''
    endCondition = raw_input("> ")

    #check for valid input
    validOptions = ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18"]
    while endCondition not in validOptions:
        print "Not a Valid Option."
        endCondition = raw_input("> ")

    if endCondition == "17":
        menu()
    elif endCondition == "18":
        exit(0)
    else:
        elasticFdnLoadCase(endCondition)
        #end condition must be combined with load case to determine calcs used

def elasticFdnLoadCase(endCondition):
    #'screen' to choose load case to calculate
    
    print '''
    Stress and Strain of Structural Elements
    Beam on Elastic Foundation: Load Cases

    Options
    1. Concentrated Intermediate Load
    2. Partial Uniformly Distributed Load
    3. Partial Uniformly Increasing Load
    4. Concentrated Intermediate Moment
    5. Externally Created Concentrated Angular Displacement
    6. Externally Created Concentrated Lateral Displacement
    7. Uniform Temperature Differential from Top to Bottom
    8. Return to End Condition Choices
    9. Exit
    '''
    loadCase = raw_input("> ")

    #check for valid input
    validOptions = ["1","2","3","4","5","6","7","8","9"]
    while loadCase not in validOptions:
        print "Not a Valid Option."
        loadCase = raw_input("> ")

    choice = loadCase+endCondition
    #see choices.py for connection between this file  and calc file
        
    if loadCase == "8":
        elasticFdn()
    elif loadCase == "9":
        exit(0)
    else:
        elasticFdnChoices(choice)

    elasticFdnEnd(choice)
    
def elasticFdnEnd(choice):

    print '''
    Analysis Complete.
    What would you like to do now?

    1. Calculate Another Beam/Foundation of This Type
    2. Return to Main Menu
    3. Exit
    '''
    
    nextStep = raw_input("> ")

    validOptions = ["1","2","3"]
    while nextStep not in validOptions:
        print "Not a Valid Option."
        nextStep = raw_input("> ")

    if nextStep == "1":
        elasticFdnChoices(choice)
    elif nextStep == "2":
        menu()
    elif nextStep == "3":
        exit(0)

    elasticFdnEnd(choice)


def annularPlate():
    #annular plate "screen" to choose edge restraints

    print '''
    Stress and Strain of Structural Elements
    Flat Plates:  End Conditions

    1.  Outer Edge Simply Supported, Inner Edge Free
    2.  Outer Edge Simply Supported, Inner Edge Guided
    3.  Outer Edge Simply Supported, Inner Edge Simply Supported
    4.  Outer Edge Simply Supported, Inner Edge Fixed
    5.  Outer Edge Fixed, Inner Edge Free
    6.  Outer Edge Fixed, Inner Edge Guided
    7.  Outer Edge Fixed, Inner Edge Simply Supported
    8.  Outer Edge Fixed, Inner Edge Fixed
    9.  Outer Edge Guided, Inner Edge Simply Supported
    10. Outer Edge Guided, Inner Edge Fixed
    11. Outer Edge Free, Inner Edge Simply Supported
    12. Outer Edge Free, Inner Edge Fixed
    13. Return to Menu
    14. Exit
    '''

    endCondition = raw_input("> ")

    #check for valid input
    validOptions = ["1","2","3","4","5","6","7","8","9","10","11","12","13","14"]
    while endCondition not in validOptions:
        print "Not a Valid Option."
        endCondition = raw_input("> ")

    if endCondition == "13":
        menu()
    elif endCondition == "14":
        exit(0)
    else:
        annularPlateLoadCase(endCondition)

def annularPlateLoadCase(endCondition):
    #"screen" to choose load case

    print '''
    Stress and Strain of Structural Elementss
    Flat Plates:  Load Cases

    1.  Annular Plate with Uniform Annular Line Load
    2.  Annular Plate with Uniformly Distributed Pressure
    3.  Annular Plate with Linearly Distributed Increasing Pressure
    4.  Annular Plate with Parabolically Distributed Increasing Pressure
    5.  Annular Plate with Uniform Line Moment
    6.  Annular Plate with Externally Applied Change in Slope
    7.  Annular Plate with Externally Applied Vertical Deformation
    8.  Annular Plate with Uniform Temperature Differential
    9.  Return to End Condition Choices
    10. Exit
    '''

    loadCase = raw_input("> ")

    #check for valid input
    validOptions = ["1","2","3","4","5","6","7","8","9","10"]
    while loadCase not in validOptions:
        print "Not a Valid Option."
        loadCase = raw_input("> ")

    choice = loadCase+endCondition
    #see choices.py for connection between this file  and calc file
        
    if loadCase == "9":
        annularPlate()
    elif loadCase == "10":
        exit(0)
    else:
        annularPlateChoices(choice)

    annularPlateEnd(choice)


def annularPlateEnd(choice):

    print '''
    Analysis Complete.
    What would you like to do now?

    1. Calculate Another Beam/Foundation of This Type
    2. Return to Main Menu
    3. Exit
    '''
    
    nextStep = raw_input("> ")

    validOptions = ["1","2","3"]
    while nextStep not in validOptions:
        print "Not a Valid Option."
        nextStep = raw_input("> ")

    if nextStep == "1":
        annularPlateChoices(choice)
    elif nextStep == "2":
        menu()
    elif nextStep == "3":
        exit(0)

    annularPlateEnd(choice)
    

def revolveShell():
    #shell of revolution "screen" to choose shell type
    
    print '''
    Stress and Strain of Structural Elements
    Shells of Rotation:  Form of Vessel

    1.  Cylindrical
    2.  Conical
    3.  Spherical
    4.  Smooth Figure
    5.  Toroidal
    6.  Return to Menu
    7.  Exit
    '''
    
    form = raw_input("> ")

    #check for valid input
    validOptions = ["1","2","3","4","5","6","7"]
    while form not in validOptions:
        print "Not a Valid Option."
        form = raw_input("> ")

    if form == "1":
        revolveShellLoadCase1(form)
    elif form == "2":
        revolveShellLoadCase2(form)
    elif form == "3":
        revolveShellLoadCase2(form)
    elif form == "4":
        revolveShellLoadCase4(form)
    elif form == "5":
        revolveShellLoadCase5(form)
    elif form == "6":
        menu()
    elif form == "7":
        exit(0)
    else:
        revolveShellLoadCase(form)

def revolveShellLoadCase1(form):
    #"screen" to choose load case

    print '''
    Stress and Strain of Structural Elementss
    Cylindrical Shell of Rotation:  Load Cases

    1.  Uniform Axial Load
    2.  Uniform Radial Pressure
    3.  Uniform Internal or External Pressure
    4.  Linearly Varying Radial Pressure
    5.  Own Weight, Top Edge Support, Bottom Edge Free
    6.  Uniform Rotation about Central Axis
    7.  Return to Shape Choices
    8.  Exit
    '''

    loadCase = raw_input("> ")

    #check for valid input
    validOptions = ["1","2","3","4","5","6","7","8"]
    while loadCase not in validOptions:
        print "Not a Valid Option."
        loadCase = raw_input("> ")

    choice = form+loadCase
    #see choices.py for connection between this file and calc file
        
    if loadCase == "7":
        revolveShell()
    elif loadCase == "8":
        exit(0)
    else:
        revolveShellChoices(choice)

    revolveShellEnd(choice)

def revolveShellLoadCase2(form):
    #"screen" to choose load case

    print '''
    Stress and Strain of Structural Elementss
    Conical or Spherical Shell of Rotation:  Load Cases

    1.  Uniform Internal or External Pressure, Tangential Edge Support
    2.  Filled with Liquid to Depth, Tangential Edge Support
    3.  Own Weight, Tangential Top Edge Support
    4.  Tangential Loading Only
    5.  Uniform Loading on Horizontal Projected Area, Tangential Top Edge Support
    6.  Uniform Rotation about Central Axis
    7.  Return to Shape Choices
    8.  Exit
    '''

    loadCase = raw_input("> ")

    #check for valid input
    validOptions = ["1","2","3","4","5","6","7","8"]
    while loadCase not in validOptions:
        print "Not a Valid Option."
        loadCase = raw_input("> ")

    choice = form+loadCase
    #see choices.py for connection between this file and calc file
        
    if loadCase == "7":
        revolveShell()
    elif loadCase == "8":
        exit(0)
    else:
        revolveShellChoices(choice)

    revolveShellEnd(choice)

def revolveShellLoadCase4(form):
    #"screen" to choose load case

    print '''
    Stress and Strain of Structural Elementss
    Smooth Figure Shell of Rotation:  Load Cases

    1.  Uniform Internal or External Pressure, Tangential Edge Support
    2.  Filled with Liquid to Depth, Tangential Edge Support
    3.  Own Weight, Tangential Top Edge Support
    4.  Tangential Loading Only
    5.  Uniform Loading on Horizontal Projected Area, Tangential Top Edge Support
    6.  Uniform Rotation about Central Axis
    7.  Return to Shape Choices
    8.  Exit
    '''

    loadCase = raw_input("> ")

    #check for valid input
    validOptions = ["1","2","3","4","5","6","7","8"]
    while loadCase not in validOptions:
        print "Not a Valid Option."
        loadCase = raw_input("> ")

    choice = form+loadCase
    #see choices.py for connection between this file and calc file
        
    if loadCase == "7":
        revolveShell()
    elif loadCase == "8":
        exit(0)
    else:
        revolveShellChoices(choice)

    revolveShellEnd(choice)


def revolveShellLoadCase5(form):
    #"screen" to choose load case

    print '''
    Stress and Strain of Structural Elementss
    Toroidal Shell of Rotation:  Load Cases

    1.  Uniform Internal or External Pressure
    2.  Return to Shape Choices
    3.  Exit
    '''

    loadCase = raw_input("> ")

    #check for valid input
    validOptions = ["1","2","3"]
    while loadCase not in validOptions:
        print "Not a Valid Option."
        loadCase = raw_input("> ")

    choice = form+loadCase
    #see choices.py for connection between this file and calc file
        
    if loadCase == "2":
        revolveShell()
    elif loadCase == "3":
        exit(0)
    else:
        revolveShellChoices(choice)

    revolveShellEnd(choice)

def revolveShellEnd(choice):

    print '''
    Analysis Complete.
    What would you like to do now?

    1. Calculate Another Beam/Foundation of This Type
    2. Return to Main Menu
    3. Exit
    '''
    
    nextStep = raw_input("> ")

    validOptions = ["1","2","3"]
    while nextStep not in validOptions:
        print "Not a Valid Option."
        nextStep = raw_input("> ")

    if nextStep == "1":
        revolveShellChoices(choice)
    elif nextStep == "2":
        menu()
    elif nextStep == "3":
        exit(0)

    revolveShellEnd(choice)

def crack():

    print '''
    Stress and Strain of Structural Elements
    Stress Concentrations:  Crack Type

    1.  Two U-Notches
    2.  Two V-Notches
    3.  One U-Notch
    4.  One V-Notch
    5.  Return to Menu
    6.  Exit
    '''

    crackType = raw_input("> ")

    #check for valid input
    validOptions = ["1","2","3","4","5","6"]
    while crackType not in validOptions:
        print "Not a Valid Option."
        crackType = raw_input("> ")

    if crackType == "5":
        menu()
    elif crackType == "6":
        exit(0)
    else:
        crackStressCase(crackType)

    
def crackStressCase(crackType):

    print '''
    Stress and Strain of Structural Elements
    Stress Concentrations:  Stress Condition

    1.  Elastic Stress, Axial Tension
    2.  Elastic Stress, In-Plane Bending
    3.  Elastic Stress, Out-of-Plane Bending
    4.  Return to Crack Types
    5.  Exit
    '''

    stressCase = raw_input("> ")

    #check for valid input
    validOptions = ["1","2","3","4","5"]
    while stressCase not in validOptions:
        print "Not a Valid Option."
        stressCase = raw_input("> ")

    choice = crackType+stressCase
    #see choices.py for connection between this file and calc file
        
    if stressCase == "4":
        crack()
    elif stressCase == "5":
        exit(0)
    else:
        crackStressChoices(choice)

    crackStressEnd(choice)

def crackStressEnd(choice):

    print '''
    Analysis Complete.
    What would you like to do now?

    1. Calculate Another Stress of This Type
    2. Return to Main Menu
    3. Exit
    '''
    
    nextStep = raw_input("> ")

    validOptions = ["1","2","3"]
    while nextStep not in validOptions:
        print "Not a Valid Option."
        nextStep = raw_input("> ")

    if nextStep == "1":
        crackStressChoices(choice)
    elif nextStep == "2":
        menu()
    elif nextStep == "3":
        exit(0)

    crackStressEnd(choice)
    
    
menu()
