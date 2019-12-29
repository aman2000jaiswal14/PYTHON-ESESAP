import cx_Freeze
import sys
import os 
base = None

if sys.platform == 'win32':
    base = "Win32GUI"

os.environ['TCL_LIBRARY'] = r"C:\Users\aman2\AppData\Local\Programs\Python\Python37-32\tcl\tcl8.6"
os.environ['TK_LIBRARY'] = r"C:\Users\aman2\AppData\Local\Programs\Python\Python37-32\tcl\tk8.6"

executables = [cx_Freeze.Executable("esesap.py", base=base, icon="e32.ico")]


cx_Freeze.setup(
    name = "Easy File Seperator",
    options = {"build_exe": {"packages":["tkinter","os"], "include_files":['tcl86t.dll','tk86t.dll',"e32.ico"]}},
    version = "0.01",
    description = "Easy File seperator Tkinter application",
    executables = executables
    )
