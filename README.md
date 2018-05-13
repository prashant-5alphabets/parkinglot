This project solves the parking lot problem <br />
Language Used - Python <br />
Build Tool Used - PyInstaller <br />
Executable file is generated on ubuntu 16.04 if any issue in executing binary please follow build steps


To install PyInstaller
----------------------
    pip install pyinstaller

Build Commands
--------------
    pyinstaller init.py --onefile
    cp dist/init ./parking_lot

General things
--------------
    Program will exit automatically if given file ends (in case of file input)
    Pragram will exit if `exit` command is given (in both cases)

To run
------
    cd to project path
    Run command `./parking_lot` to execute with command line input mode
    Run command `./parking_lot ./test_input.txt` to run with test input file added
    Run command `./parking_lot path_to_file` to run with any input file



