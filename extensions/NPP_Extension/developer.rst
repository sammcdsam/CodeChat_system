=====================================
NPP_Extension Developer Documentation
=====================================

This document is meant to show how a developer would proceed in:

#. Installing necessary extensions, libraries, and compilation tools
#. Setting up the development enviroment for a thrift server
#. Developing a Thrift server
#. Rendering a source file into html to be displayed to a browser window

Installing the Necessary Extensions, Libraries, and Compilation tools
=====================================================================
These Tools are what are needed to build the thrift includes and libraries to be used in the server setup:

#. `Visual Studio 2022 Community <https://visualstudio.microsoft.com/vs>`_ (What I used, might be up for changes based off of if there's any conflicts with the version of VS that is used to build the plugin)
#. `Developer Command Prompt for VS 2022` This should have downloaded with the main Visual Studio 2022, search for it in the windows search bar
#. `thrift-0.15.0.exe <http://archive.apache.org/dist/thrift/0.15.0>`_
#. `thrift 0.15.0 source code <https://github.com/apache/thrift/releases>`_
#. `win_flex_bison <https://github.com/lexxmark/winflexbison/releases/tag/v2.5.25>`_
#. `Boost 1.53.0 <https://sourceforge.net/projects/boost>`_
#. `libevent <https://github.com/libevent/libevent/releases>`_

Installing necessary libraries
------------------------------

A major thing to get right is the version number of the tools we are using, especially when it comes to **boost**. Boost's newest version (1.73) is massive, and mostly unnecessary. Thrift only requires Boost v.1.53.0, so that is the version we will be using.

File Directory setup
````````````````````

 .. Note:: 
     
     I did all of my installations in a directory close to the "C:". My specific path is "C:/src/" Then create seperate folders for all of the parts that you need. This is because we will have to access these files from the **Developer Command Prompt** and the shorter the file path the quicker it is to type into a command.

My folders inside of my **"C:/src"** directory looks like this:
    - `boost`
    - `Include`
    - `libevent`
    - `thrift`
    - `win_flex_bison`

Installing Boost
````````````````
To install boost:
#. Open up your **Developer Command Prompt** (`windows key + R` and then `cmd`)
#. Change your directory to boost (**"cd C:/src/boost/tools/build/v2"**)
#. run "bootstrap.bat"
#. enter "./b2 install --prefix=PREFIX install"

Installing libevent
```````````````````

To install the libevent libraries:
#. **"cd C:/src/libevent"** (if you have the folder created)
#. **"md build"** to make a build directory
#. **"cd build"** to change to the new build directory 
#. **"cmake -G "Visual Studio 17 2022" -A "x64" .."** This runs Cmake, which will setup and install all we need 
- **"start libevent.sln"** Compiles libevent

.. IMPORTANT::
    
    Grabbed this `event-config.h <https://code.woboq.org/linux/include/event2/event-config.h.html>`_ copy pasted the contents into a created `envent-config.h` inside "C:/src/libevent/include" Did this because thrift needs this header, but it was not inside of the libevent on download.

    **Also, I am unsure that this has actually worked on my system. When Debugging this is a decent place to start.**

Creating Thrift Libraries
-------------------------
Creating the thrift libraries involves opening the solution of libthrift (`thrift.sln`). This should be in **"C:/src/thrift/lib/cpp/thrift/sln"**. This solution has two projects, `libthrift` and `libthriftnb`. 

Our thrift implementation uses `libthrift` so in the solution explorer right click `libthriftnb` and press "Unload Project"

Placing Includes Together
`````````````````````````

Next let's make sure that we have the includes in order. 

Create a Folder called **"Include"** inside of the **"src"** directory

Create a **"boost"** folder inside of **"Include"**
copy the boost includes from: **"C:/src/boost/boost"** (press ctrl + a to grab all) to the new folder.

Copy libevent contents from **"C:/src/libevent/include"** to the Include directory, 
you'll have some `.h` in the general "Include" directory, but that's okay for how we're going to use the includes.

Right Click on libthrift and select properties
    - click on C/C++ and click Additional Include Directories then the down arrow
    - press the icon with the folder and star
    - press the three dots
    - find the "Include" folder and press select folder
        - The window should have something like "C:/src/Include"

    - press the icon with the folder and star again
    - press the three dots again
    - find the "thrift/lib/cpp/src" folder and press select folder
    
    - Press OK
    - Press Apply

Inside of THttpClient.cpp change `config.h` to `windows/config.h`

This, unfortunately, does not completely resolve errors in compilation. The Visual Studio 2022 build output lists multiple files as not existing, taking an immense amount of time to sort through.