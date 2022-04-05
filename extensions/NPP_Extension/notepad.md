## Required Software

*Notepad++ is a Windows app. Installation of Notepad++ is fairly simple on Linux, but development (and installation) of plugins is problematic.* 

You will need the following on your Windows system for npp/codechat extension development:

[Assignment in Canvas with links to much of what follows](https://msstate.instructure.com/courses/71820/assignments/668417)

[Windows Terminal (recommended)](ms-windows-store://pdp/?ProductId=9n0dx20hk701)

[Visual Studio Code](https://code.visualstudio.com/sha/download?build=stable&os=win32-x64-user)

[Python](https://www.microsoft.com/store/productId/9P7QFQMJRFP7)

[Notepad ++](https://notepad-plus-plus.org/downloads/v8.3.3/)

[CodeChat](https://codechat-system.readthedocs.io/en/latest/CodeChat_Server/install.html)

## Installing Codechat

1. **Install Python** (Note: These directions apply to the Windows Store install of Python. If you install from the web, you need to replace "python" in the following commands with "py" and [make sure Python is in the PATH](https://datatofish.com/add-python-to-windows-path/), possibly by simply checking the “Add Python 3.x to PATH” box, during installation.

2. **Open Windows terminal.** *Be sure to perform the following in Command Prompt, not Powershell*

3. **Update pip**

python -m pip install --upgrade pip

4. **Create a virtual environment named codechat** 

python -m venv codechat

5. **Activate this virtual environment**

.\codechat\Scripts\activate

6. **Install the CodeChat Server**

python -m pip install --upgrade CodeChat_Server

7. **Determine the location of the installed CodeChat Server.** Remember this location - you'll need it when installing the CodeChat extension for VSC.

where CodeChat_Server

## Install the CodeChat extension/plugin for VSC

1. **Open Visual Studio Code**

2. **Ctrl-Shift-X to open the Extensions** 

3. **search for "codechat"**

4. **click Install**

5. **click the gear wheel to modify extension settings**

6. **Enter the location from "where CodeChat_Server" in "Code Chat.Code Chat Server: Command**". 

*Follow the directions and double up on backslashes*.

C:\Users\petel\codechat\Scripts\CodeChat_Server.exe =>
C:\\\Users\\\petel\\\codechat\\\Scripts\\\CodeChat_Server.exe

(used 3 backslashes for the markdown render)


## Notepad++ Links

**Currently you need to install the 32-bit version of Notepad++ since the methods for creating plugins create 32-bit plugins**

[Notepad help](https://notepad-plus-plus.org/resources/)

[Plugins Help](https://npp-user-manual.org/docs/plugins/)

[Plugins List](https://github.com/notepad-plus-plus/nppPluginList/blob/master/doc/plugin_list_x64.md)


[Plugin Developer Forum](https://notepad-plus-plus.org/community/category/5/plugin-development)

## Install a Notepad++ plugin

There are two ways:

1. **Plugins -> Plugin Admin** (for plugins already in the official repository)

2. Manually

    a. get the dll file e.g. SamplePlugin.dll

    b. make a subfolder in Program Files\Notepad++\plugins with the exact name of the plugin (not including extension) e.g. SamplePlugin

### Install MarkdownViewer++ (optional)

This is a Notepad++ plugin with similar functionality as desired in the CodeChat extension (e.g. split screen, rendered HTML of the currently selected file/tab, synchronized scrolling). Use Plugin Admin to install. 

[More info about MarkdownViewer++](https://nea.github.io/MarkdownViewerPlusPlus/)

*Refresh doesn't seem to be working automatically, after a save, or via the menu. To refresh, click on the MarkdownViewer window and press CTRL-R*

# Create a Notepad++ plugin

## Install Visual Studio

You will need this for either method of building a plugin

[Visual Studio](https://visualstudio.microsoft.com/vs/older-downloads/)

1. Select Visual Studio Community 2017 15.3
2. During installation, be sure "Desktop Development with C++" is selected
   
### Method 1

1. Download and unzip the latest release of Notepad++ Plugin Template.

    a. [Source Code](https://github.com/npp-plugins/plugintemplate/archive/refs/tags/v4.2.zip) This is what you need. If you compile it, you will get a DLL file that you can put in a folder of the plugin directory.

    b. [plugin template](https://github.com/npp-plugins/plugintemplate/releases/download/v4.2/pluginTemplate.v4.2.bin.x64.zip) This is the compiled plugin template, i.e. yours should look like 

2. Open NppPluginTemplate.vcproj in your Visual Studio.

3. PluginDefinition.h and PluginDefinition.cpp are the two files to edit when you want to make changes.

4. Be sure all Windows Explorer windows are closed and build with Ctrl-Shift-B

### Method 2

[Described here](https://community.notepad-plus-plus.org/topic/17787/a-new-c-plugin-template)

1. from a command prompt run:

```
pip install cookiecutter

cookiecutter https://github.com/dail8859/cookiecutter-npp-cpp-plugin.git
```

2. All the default options are fine, be sure to choose Visual Studio 2017

3. Open the .SLN file with Visual Studio 2017

4. Be sure all Windows Explorer windows are closed and build with Ctrl-Shift-B