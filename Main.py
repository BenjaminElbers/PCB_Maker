import os

os.environ["KICAD_SYMBOL_DIR"] = r"C:\\Program Files\\KiCad\\10.0\\share\\kicad\\symbols"
os.environ["KICAD_FP_DIR"] = r"C:\\Program Files\\KiCad\\10.0\\share\\kicad\\footprints"

from skidl import *

And = 2
Or = 2
Not = 1

MakeUp_GT = ["AND", "OR", "NOT"]

Last_Gates = {}  # Set to keep track of the last gates added for potential feedback

def AND(a, b, Is_End, Num):

    # Nets
    vcc = Net("VCC")
    Out = Net("Out" + "_" + str(Num))  # Unique output net for each gate

    if Is_End:
        Last_Gates.add(("AND", Num))

    # Transistors
    t1 = Part("Device", "Q_NPN_BJT")
    t2 = Part("Device", "Q_NPN_BJT")

    # Pull-up resistor
    r1 = Part("Device", "R")
    r1.value = "10k"

    # Wiring (series AND behavior approximation)
    vcc += r1[1]

    a += t1["B"]
    b += t2["B"]

    t1["C"] += r1[2]
    t2["C"] += r1[2]

    t1["E"] += t2["C"]   # series effect
    t2["E"] += Out

    return [t1, t2]

def OR(a, b, Is_End, Num):

    # Nets
    vcc = Net("VCC")
    Out = Net("Out" + "_" + str(Num))  # Unique output net for each gate

    if Is_End:
        Last_Gates.add(("OR", Num))

    # Transistors
    t1 = Part("Device", "Q_NPN_BJT")
    t2 = Part("Device", "Q_NPN_BJT")

    # Pull-up resistor
    r1 = Part("Device", "R")
    r1.value = "10k"

    # Wiring (parallel OR behavior approximation)
    vcc += r1[1]
    
    a += t1["B"]
    b += t2["B"]

    t1["C"] += r1[2]
    t2["C"] += r1[2]

    t1["E"] += Out
    t2["E"] += Out

    return [t1, t2, Out]

def NOT(a, Is_End, Num):
    # Nets
    vcc = Net("VCC")
    Out = Net("Out" + "_" + str(Num))  # Unique output net for each gate

    if Is_End:
        Last_Gates.add(("NOT", Num))

    # Transistor
    t1 = Part("Device", "Q_NPN_BJT")

    # Pull-up resistor
    r1 = Part("Device", "R")
    r1.value = "10k"

    # Wiring (inversion behavior approximation)
    vcc += r1[1]
    
    a += t1["B"]

    t1["C"] += r1[2]
    t1["E"] += Out

    return [t1, Out]


def Gated_Lach():

    # Nets
    vcc = Net("VCC")
    WE = Net("WE")
    DI = Net("DI")
    RE = Net("RE")

    # Gates
    AND_1 = AND(WE, DI, False, 1)
    NOT_1 = NOT(DI, False, 2)
