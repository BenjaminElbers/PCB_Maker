from skidl import *

# Global power nets
VCC = Net("VCC")
GND = Net("GND")

Last_Gates = []  # numbers of the last gates in the chain

def AND(a, b, Is_End, Num):

    Out = Net("Out_" + str(Num))

    if Is_End:
        Last_Gates.append((Num))

    t1 = Part("Device", "Q_NPN")
    t2 = Part("Device", "Q_NPN")

    r1 = Part("Device", "R", value="10k")

    VCC += r1[1]

    a += t1["B"]
    b += t2["B"]

    t1["C"] += r1[2]
    t2["C"] += r1[2]

    # simple series pull-down approximation
    t1["E"] += t2["C"]
    t2["E"] += Out

    return Out


def NOR(a, b, Is_End, Num):

    Out = Net("Out_" + str(Num))

    if Is_End:
        Last_Gates.append((Num))

    t1 = Part("Device", "Q_NPN")
    t2 = Part("Device", "Q_NPN")

    r1 = Part("Device", "R", value="10k")

    VCC += r1[1]

    a += t1["B"]
    b += t2["B"]

    t1["C"] += r1[2]
    t2["C"] += r1[2]
    r1[2] += Out

    t1["E"] += GND
    t2["E"] += GND

    return Out


def NOT(a, Is_End, Num):

    Out = Net("Out_" + str(Num))

    if Is_End:
        Last_Gates.append((Num))

    t1 = Part("Device", "Q_NPN")
    r1 = Part("Device", "R", value="10k")

    VCC += r1[1]

    a += t1["B"]
    t1["C"] += r1[2]
    t1["E"] += Out

    return Out

def Gated_SR_Latch(num):

    # Inputs
    EN = Net("EN_" + str(num))
    DI = Net("DI_" + str(num))
    RS = Net("RS_" + str(num))

    # Internal feedback nets
    Out  = Net("Out_" + str(num))
    Out_F = Net("Out_F_" + str(num))

    # Gate numbering preserved
    AND_1 = AND(DI, EN, False, num + 1)
    AND_2 = AND(RS, EN, False, num + 2)

    Out  += NOR(AND_1,  Out_F, False, num + 3)
    Out_F += NOR(AND_2,  Out,  False, num + 4)

    return Out, Out_F

if __name__ == "__main__":
    pass
