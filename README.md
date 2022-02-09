# Cpp-Make
Run this program to compile your c++ project with MinGW32

## Usage
* First, download the executable file: [here](https://github.com/Monkvy/Cpp-Make/releases/tag/v1.0.0)
* The window antivirus may dont like this file (but its not a virus trust me).
* Add the file to your main directory inside your C++ project.
* Run the file. On the first run, errors are normal. To avoid them, configure the Make.json config-file which has been created after the first run.

## Default project structure (can be changed in Make.json)
```
../project/

└──bin
│   └──project.exe
│   └──somebinary.dll
└──libs
│   └──somelib
│       └──include
│       │   └──...
│       └──lib
│           └──...
└──src
│   └──some_subdir
│   │   └──somefile.h
│   │   └──somefile.cpp
│   └──main.cpp
│
└──Make.exe
└──Make.json
```