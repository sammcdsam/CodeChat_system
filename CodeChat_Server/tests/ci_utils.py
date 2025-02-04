# ***************************************************************
# ci_utils.py - Utilities supporting continuous integration tests
# ***************************************************************
#
# Imports
# =======
# These are listed in the order prescribed by `PEP 8`_.
#
# Standard library
# ----------------
import os
import os.path
import subprocess
import sys
from typing import Any, Union, List, Literal


# OS detection
# ============
# This follows the `Python recommendations <https://docs.python.org/3/library/sys.html#sys.platform>`_.
is_win = sys.platform == "win32"
is_linux = sys.platform.startswith("linux")
is_darwin = sys.platform == "darwin"

# Copied from https://docs.python.org/3.5/library/platform.html#cross-platform.
is_64bits = sys.maxsize > 2**32


# Support code
# ============
# xqt
# ---
# Pronounced "execute": provides a simple way to execute a system command.
def xqt(
    # Commands to run. For example, ``'foo -param firstArg secondArg', 'bar |
    # grep alpha'``.
    *cmds: str,
    # Optional keyword arguments to pass on to `subprocess.run <https://docs.python.org/3/library/subprocess.html#subprocess.run>`_.
    **kwargs: Any
) -> Union[subprocess.CompletedProcess, List[subprocess.CompletedProcess]]:

    ret = []
    # Although https://docs.python.org/3/library/subprocess.html#subprocess.Popen
    # states, "The only time you need to specify ``shell=True`` on Windows is
    # when the command you wish to execute is built into the shell (e.g.
    # **dir** or **copy**). You do not need ``shell=True`` to run a batch file
    # or console-based executable.", use ``shell=True`` to both allow shell
    # commands and to support simple redirection (such as ``blah > nul``,
    # instead of passing ``stdout=subprocess.DEVNULL`` to ``check_call``).
    for _ in cmds:
        # Per http://stackoverflow.com/questions/15931526/why-subprocess-stdout-to-a-file-is-written-out-of-order,
        # the ``check_call`` below will flush stdout and stderr, causing all
        # the subprocess output to appear first, followed by all the Python
        # output (such as the print statement above). So, flush the buffers to
        # avoid this.
        flush_print(_)
        # Use bash instead of sh, so that ``source`` and other bash syntax
        # works. See https://docs.python.org/3/library/subprocess.html#subprocess.Popen.
        executable = "/bin/bash" if is_linux or is_darwin else None
        try:
            cp = subprocess.run(
                _, shell=True, executable=executable, check=True, **kwargs  # type: ignore
            )
        except subprocess.CalledProcessError as e:
            flush_print(
                "Subprocess output:\n{}\n{}".format(e.stderr or "", e.stdout or "")
            )
            raise
        ret.append(cp)

    # Return a list only if there were multiple commands to execute.
    return ret[0] if len(ret) == 1 else ret


# pushd
# -----
# A context manager for pushd.
class pushd:
    def __init__(
        self,
        # The path to change to upon entering the context manager.
        path: str,
    ):

        self.path = path

    def __enter__(self):
        flush_print("pushd {}".format(self.path))
        self.cwd = os.getcwd()
        os.chdir(self.path)

    def __exit__(self, type_: Any, value: Any, traceback: Any) -> Literal[False]:
        flush_print("popd - returning to {}.".format(self.cwd))
        os.chdir(self.cwd)
        return False


# Common tools
# ============
#
# chdir
# -----
def chdir(path: str):
    flush_print("cd " + path)
    os.chdir(path)


# mkdir
# -----
def mkdir(path: str):
    flush_print("mkdir " + path)
    os.mkdir(path)


# flush_print
# -----------
# Anything sent to ``print`` won't be printed until Python flushes its buffers,
# which means what CI logs report may be reflect what's actually being executed
# -- until the buffers are flushed.
def flush_print(*args: Any, **kwargs: Any):
    print(*args, **kwargs)
    # Flush both buffers, just in case there's something in ``stdout``.
    sys.stdout.flush()
    sys.stderr.flush()


# isfile
# ------
def isfile(f: str):
    _ = os.path.isfile(f)
    flush_print("File {} {}.".format(f, "exists" if _ else "does not exist"))
    return _


# isdir
# -----
def isdir(f: str):
    _ = os.path.isdir(f)
    flush_print("Directory {} {}.".format(f, "exists" if _ else "does not exist"))
    return _
