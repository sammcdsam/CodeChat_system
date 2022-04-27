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
#. `Boost 1.53.0 <https://sourceforge.net/projects/boost/files/boost/1.53.0/boost_1_53_0.zip/download>`_
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
#. Open up your **Developer Command Prompt** (Search for Developer Command Prompt for VS in the search bar) 
#. Change your directory to boost (**"cd C:/src/boost/tools/build/v2"**)
#. run "bootstrap.bat"
#. enter "b2 install --prefix=PREFIX install"

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

Creating the Notepad++ Plugin DLL
----------------------------------

Tutorial 
https://npp-user-manual.org/docs/plugins/ 

Open CodeChat.vcproj in your Visual Studio.
Define your plugin commands number in PluginDefinition.h
Customize plugin commands names and associated function name (and the other stuff, optional) in PluginDefinition.cpp.
Define the associated functions.

Build the files in visual studio. (If you press the "run" button it builds the file, but gives an error this is ok because you cant run the .dll outside of Notepad++)

Open NotePad++ in debug mode.  (These are the official steps - I could not get the Notepad Debug .exe to work. I just followed the steps with the normal notepad.exe worked)
    - Download the debug mode 32 bit version here https://notepad-plus-plus.org/assets/pluginListTestTools/npp.debug.x32.zip]
    - Copy that version of the exe to your Notedpad++ program folder
    - Download https://notepad-plus-plus.org/assets/pluginListTestTools/wingup.release.x32.zip
    - Copy that version of GUP.exe to Notepad++/updater/
    - Copy the pl.x86.json file from NPP_Extension/basic_plugin into Notepad++/plugins/Config/

    - Select plugins from the top menu and open the plugin folder
    - Create a folder called CodeChat
    - Add your Codechat.dll to the CodeChat folder

CodeChat should appear in the plugins list with the option for a hello world
Currently the plugin creates a new file that says Hello, Notepad++

Building vcpkg
----------------------------------
In order to use the thrift library, 'vcpkg <https://vcpkg.info/port/thrift>`_ was used to install the thrift library.
To build the vcpkg follow this `tutorial <https://thrift.apache.org/lib/cpp.html#thrift-and-the-vcpkg-package-manager>`_ 

Creating Thrift Client in Visual Studio
----------------------------------
In order to use the thrift library, 'vcpkg <https://vcpkg.info/port/thrift>`_ was used to install the thrift library.
For the developers on this task, we found Visual Studio 2019 to work the best for installation of vcpkg. 

When downloading Visual Studio 2019 the following packages need to be installed to properly install vcpkg.
    - Windows Universal C Runtime: Microsoft.VisualStudio.Component.Windows10SDK
    - C++ core desktop features: Microsoft.VisualStudio.ComponentGroup.NativeDesktop.Core
    - Microsoft.VisualStudio.Component.VC.140 (for Visual Studio 2015)
    - Microsoft.VisualStudio.Component.VC.Tools.x86.x64 (for Visual Studio 2017 or later)
    - MSBuild: Microsoft.Component.MSBuild
    - Windows SDK (one of them):
        - 8.1: Microsoft.VisualStudio.Component.Windows81SDK
        - 10.0.18362: Microsoft.VisualStudio.Component.Windows10SDK.18362
        - 10.0.19041: Microsoft.VisualStudio.Component.Windows10SDK.19041
        - 10.0.20348: Microsoft.VisualStudio.Component.Windows10SDK.20348
        - 11.0.22000: Microsoft.VisualStudio.Component.Windows11SDK.22000
    - ARM/ARM64:
        - Visual Studio Build tools for ARM: Microsoft.VisualStudio.Component.VC.Tools.arm
        - Visual Studio Build tools for ARM: Microsoft.VisualStudio.Component.VC.Tools.arm64
    - Visual Studio Build tools for UWP: Microsoft.VisualStudio.ComponentGroup.UWP.VC
    - C++ Desktop Developer Suite

Once the following packages are installed in visual studio, the thrift repository should be downloaded from below
https://github.com/apache/thrift 
During our development, we noticed the thrift compiler was not in the master folder from github. As a result the thrift compiler was found and downloaded from 
https://www.apache.org/dyn/closer.cgi?path=/thrift/0.16.0/thrift-0.16.0.exe 

The compiler was then placed in the tutorial folder of the thrift directory

The thrift client was made using the official client example from apache found `here <https://thrift.apache.org/tutorial/cpp.html>`_ 

The main library used to create the client is the "Calculator.h" header file. This file relies on the tutorial and shared code examples provided by apache. 
In order to retrieve these files, the user must run these two commands in the tutorial folder with the newly downloaded 
thrift compiler. 

thrift-0.16.0.exe -r --gen cpp shared.thrift
thrift-0.16.0.exe -r --gen cpp tutorial.thrift

The two commands above will produce all the necessary cpp and .h files needed to run the example thrift client.

Currently the solution file "NPP_Extension.sln" and the project file "NPP_Extension.vcxproj" contain all of the files 
necessary to correctly compile the example thrift client. However, one can modify the project for futher functionality
by adding in more of the produced files from the shared.thrift and tutorial.thrift commands above. The files will be
located in the "gen-cpp" folder.

The current status of the thrift client is that it will ping the server when executed.
Testing was not able to be fully completed with the setup of the developers for this project, however, to test full functionality of the 
code chat server and the thrift client connection, the following needs to occur.

In one terminal, call the code chat server by first creating a virtual enviroment in python. Then the user should activate the code chat enviroment.
Lastly the user will call "CodeChat_Server serve" to instantiate the server. 

In another window, click on the "NPP_Extension.exe" file in the Debug folder of the NPP_Exention folder in code chat. A terminal should pop-up showing
the client pinging the server on port 27376.

    
    
    
