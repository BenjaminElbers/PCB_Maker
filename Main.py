import os

os.environ["KICAD_FP_LIB_TABLE"] = r"C:\\Program Files\\KiCad\10.0\\share\\kicad\\fp-lib-table"

os.environ["KICAD6_SYMBOL_DIR"] = r"C:\\Program Files\\KiCad\\10.0\\share\\kicad\\symbols"
os.environ["KICAD7_SYMBOL_DIR"] = r"C:\\Program Files\\KiCad\\10.0\\share\\kicad\\symbols"
os.environ["KICAD8_SYMBOL_DIR"] = r"C:\\Program Files\\KiCad\\10.0\\share\\kicad\\symbols"
os.environ["KICAD9_SYMBOL_DIR"] = r"C:\\Program Files\\KiCad\\10.0\\share\\kicad\\symbols"
os.environ["KICAD_SYMBOL_DIR"]  = r"C:\\Program Files\\KiCad\\10.0\\share\\kicad\\symbols"

os.environ["KICAD6_FOOTPRINT_DIR"] = r"C:\\Program Files\\KiCad\\10.0\\share\\kicad\\footprints"
os.environ["KICAD7_FOOTPRINT_DIR"] = r"C:\\Program Files\\KiCad\\10.0\\share\\kicad\\footprints"
os.environ["KICAD8_FOOTPRINT_DIR"] = r"C:\\Program Files\\KiCad\\10.0\\share\\kicad\\footprints"
os.environ["KICAD9_FOOTPRINT_DIR"] = r"C:\\Program Files\\KiCad\\10.0\\share\\kicad\\footprints"
os.environ["KICAD_FP_DIR"]          = r"C:\\Program Files\\KiCad\\10.0\\share\\kicad\\footprints"


from skidl import *
import Librairy as lib

x = int(input("Enter the number of gates (on x): "))
y = int(input("Enter the number of gates (on y): "))

a = 1

for y_pos in range(y):
    for x_pos in range(x):
        lib.Gated_SR_Latch(a)
        print(f"({x_pos}, {y_pos}), {a}")
        a += 1

generate_netlist()