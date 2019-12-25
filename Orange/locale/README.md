# 关于汉化


## 汉化操作

为python源码文件生成汉化文件ts
pylupdate5 canvasmain.py -ts canvasmain_zh_CN.ts

linguist 翻译工具导入ts文件，翻译后导出qm文件

## 通过BeyondCompare快速获得需汉化文件

    canvas\application\addons.py
    canvas\application\canvasmain.py
    canvas\application\schemeinfo.py
    canvas\application\settings.py
    canvas\application\welcomedialog.py
    canvas\canvas\items\annotationitem.py
    canvas\document\editlinksdialog.py
    canvas\document\interactions.py
    canvas\document\quickmenu.py
    canvas\document\schemeedit.py
    canvas\preview\previewbrowser.py
    canvas\preview\previewdialog.py
    widgets\data\owconcatenate.py
    widgets\data\owdiscretize.py
    widgets\data\owfeatureconstructor.py
    widgets\data\owimpute.py
    widgets\data\owrank.py
    widgets\report\owreport.py
