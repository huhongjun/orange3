Orange
======

[![Join the chat at https://gitter.im/biolab/orange3](https://badges.gitter.im/biolab/orange3.svg)](https://gitter.im/biolab/orange3?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

[![build: passing](https://img.shields.io/travis/biolab/orange3.svg)](https://travis-ci.org/biolab/orange3)
[![codecov](https://codecov.io/gh/biolab/orange3/branch/master/graph/badge.svg)](https://codecov.io/gh/biolab/orange3)

[Orange] is a component-based data mining software. It includes a range of data
visualization, exploration, preprocessing and modeling techniques. It can be
used through a nice and intuitive user interface or, for more advanced users,
as a module for the Python programming language.
[Orange]是一个组件化的数据挖掘软件。它包括一系列的数据可视化、探查、预处理和建模技术。可以通过友好、只能的图形化界面使用，对于高级用户，也可以作为Python开发的模块。

This is a development version of Orange 3. The stable version 2.7 is still
available ([binaries] and [sources]).

[Orange]: http://orange.biolab.si/
[binaries]: http://orange.biolab.si/orange2/
[sources]: https://github.com/biolab/orange


安装
----------
Orange需要Python 3.4 或更高版本。
为构建并安装Orange开发环境：

    # Install some build requirements via your system's package manager
    sudo apt install virtualenv git build-essential python3-dev

    # Create a separate Python environment for Orange and its dependencies ...
    virtualenv --python=python3 --system-site-packages orange3venv
    # ... and make it the active one
    source orange3venv/bin/activate

    # Clone the repository and move into it
    git clone https://github.com/biolab/orange3.git
    cd orange3

    # Install Qt dependencies for the GUI
    pip install PyQt5
    # Of if Python <= 3.4 and/or with package manager
    # sudo apt install python3-pyqt4
    
    # Install other minimum required dependencies
    pip install -r requirements-core.txt  # For Orange Python library
    pip install -r requirements-gui.txt   # For Orange GUI

    pip install -r requirements-sql.txt   # To use SQL support
    pip install -r requirements-opt.txt   # Optional dependencies, may fail

    # 最后一开发模式安装Orange
    pip install -e .

Installation of SciPy and qt-graph-helpers is sometimes challenging because of
their non-python dependencies that have to be installed manually. More
detailed, if mostly obsolete, guides for some platforms can be found in
the [wiki].

[wiki]: https://github.com/biolab/orange3/wiki

Anaconda Installation
---------------------

First, install [Anaconda] for your OS (Python version 3.5+). Create virtual environment for Orange:

    conda create python=3 --name orange3 

In your Anaconda Prompt add conda-forge to your channels:

    conda config --add channels conda-forge

This will enable access to the latest Orange release. Then install Orange3:

    conda install orange3

[Anaconda]: https://www.continuum.io/downloads

启动Orange图形化界面
-------------------

Orange图形化界面需要PyQt

从命令行启动Orange图形化界面，运行：
    orange-canvas
    # 或
    python -m Orange.canvas

后面附加 `--help` 可查看启动选项列表。

如果你是在PyQt5上运行Orange，或者安装了多个PyQT版本，设置环境变量QT_API为指定的PyQT版本，
如：

    export QT_API=pyqt5
    orange-canvas


如何在Windows平台编译
--------------------

下载正确的安装包。需要[numpy+mkl]和[scipy]。

[numpy+mkl]: http://www.lfd.uci.edu/~gohlke/pythonlibs/#numpy
[scipy]: http://www.lfd.uci.edu/~gohlke/pythonlibs/#scipy

安装

    pip install some-wheel.whl

安装[Visual Studio compiler]. 
    [Visual Studio compiler]: http://download.microsoft.com/download/5/F/7/5F7ACAEB-8363-451F-9425-68A90F98B238/visualcppbuildtools_full.exe

在Orange3目录下运行：

    python setup.py build_ext -i --compiler=msvc install
