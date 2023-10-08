from cx_Freeze import setup, Executable
import sys

build_exe_options = {
    "packages": ["PyQt5.QtCore", "PyQt5.QtGui", "PyQt5.QtWidgets"],
    "includes": ["atexit"],
    "include_files": ["placeholder.png"],  # Include any additional files
}

base = None
if sys.platform == "win32":
    base = "Win32GUI"

executables = [
    Executable("C:\Users\bassem\Desktop\IMG TO PFD\IMG TO PDF BSM\fils.py", base=base, icon="fils.ico")  # Replace with your script and icon
]

setup(
    name="BSM",
    version="1.0",
    description="Your application description",
    options={"build_exe": build_exe_options},
    executables=executables
)
