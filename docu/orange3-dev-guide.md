# Orange3 开发指南 

## 1. 安装软件

* Miniconda3
* 安装[Visual Studio compiler]. 

## 2. Python环境

* `conda create --name orange-dev`
* `activate orange-dev`
* `pip install PyQt5`

## 3. Orange3  

* `git clone https://github.com/huhongjun/orange3.git`
* `cd orange3`
* `pip install -r requirements-core.txt  # For Orange Python library`
* `pip install -r requirements-gui.txt   # For Orange GUI`
* `pip install -r requirements-sql.txt   # To use SQL support`
* `pip install -r requirements-opt.txt   # Optional dependencies, may fail`
* `python setup.py build_ext -i --compiler=msvc install`
* `pip install -e .`

## 4. 启动Orange图形化界面

* `python -m Orange.canvas -l4 --help`
* `python setup.py test`
python create_widget_catalog.py --output m:\

## 5. 界面汉化

    参见 Orange\locale\README.md

## 目录说明

    doc
    docu
    Orange
    scripts
    Orange3 tutorial\    //jupyter notebook

## 附录 文档

### 查看

Documentation in located in doc folder. It is split into three parts:
    - data-mining-library (scripting api)
    - development (development guides)
    - visual-programming (widget help files)

You can build it with:

    pip install  -i https://pypi.tuna.tsinghua.edu.cn/simple sphinx numpydoc sphinx-intl jieba
    cd doc/<part>
    make html
    # Now open build/html/index.html to see it

### 文档汉化

make gettext	=》生成pot文件
sphinx-intl update -p build/locale -l zh_CN
==》 手工翻译source目录下locale\zh_CN下的 po文件
set SPHINXOPTS=-D language=zh_CN
make html

=》 sphinx-intl update -p build/locale  #如果文档有修改，通过新pot文件更新po文件 

