Orange
======

[![Join the chat at https://gitter.im/biolab/orange3](https://badges.gitter.im/biolab/orange3.svg)](https://gitter.im/biolab/orange3?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

[![build: passing](https://img.shields.io/travis/biolab/orange3.svg)](https://travis-ci.org/biolab/orange3)
[![codecov](https://codecov.io/gh/biolab/orange3/branch/master/graph/badge.svg)](https://codecov.io/gh/biolab/orange3)

[Orange]是一个组件化的数据挖掘软件。它包括一系列的数据可视化、探查、预处理和建模技术。可以通过友好、只能的图形化界面使用，对于高级用户，也可以作为Python开发的模块。

这是Orange 3 开发版本，稳定版2.7可从([binaries] and [sources])获得。

[Orange]: http://orange.biolab.si/
[binaries]: http://orange.biolab.si/orange2/
[sources]: https://github.com/biolab/orange


安装
----------
Orange需要Python 3.4 或更高版本。
为构建并安装Orange开发环境：

    # 通过包管理器安装一些构建依赖
    sudo apt install virtualenv git build-essential python3-dev

    # 为Orange及其依赖包创建独立的Python环境
    virtualenv --python=python3 --system-site-packages orange3venv
    # 切换到位Orange3创建的Python环境
    source orange3venv/bin/activate

    # 克隆github仓库
    git clone https://github.com/biolab/orange3.git
    cd orange3

    # 安装GUI需要的Qt依赖
    pip install PyQt5
    # 如果Python <= 3.4，可以用包管理器
    # sudo apt install python3-pyqt4
    
    # 安装其他依赖
    pip install -r requirements-core.txt  # Orange需要的Python库
    pip install -r requirements-gui.txt   # Orange GUI需要

    pip install -r requirements-sql.txt   # SQL支持
    pip install -r requirements-opt.txt   # 可选

    # 最后以开发模式安装Orange
    pip install -e .

安装SciPy和qt-graph-helpers有时比较难，因为它们的非python依赖必须手动安装。更详细的知道参看 [wiki].

[wiki]: https://github.com/biolab/orange3/wiki

Anaconda安装
---------------------

首先，安装 [Anaconda] ，为Orange创建虚拟环境:

    conda create python=3 --name orange3 

添加conda-forge：

    conda config --add channels conda-forge

从conda-forge可获得最新版Orange3。安装Orange3:

    conda install orange3

[Anaconda]: https://www.continuum.io/downloads

启动Orange图形化界面
-------------------

Orange图形化界面需要PyQt，PyQt在Python3没法用pip安装。你只能下载和安装为全局模式。确保Orange的虚拟环境创建时加上`--system-site-packages`,这样就能访问安装的PyQt4

从命令行启动Orange图形化界面，运行：
    orange-canvas
    # 或
    python3 -m Orange.canvas

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

然后，在Orange3目录下运行：

    python setup.py build_ext -i --compiler=msvc install
