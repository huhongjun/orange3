import os  
import sys  
import shutil  
import subprocess  
  
if __name__ == '__main__':

    filelist = [r'canvas\application\addons.py',
        r'canvas\application\canvasmain.py',
        r'canvas\application\schemeinfo.py',
        r'canvas\application\settings.py',
        r'canvas\application\welcomedialog.py',
        r'canvas\canvas\items\annotationitem.py',
        r'canvas\document\editlinksdialog.py',
        r'canvas\document\interactions.py',
        r'canvas\document\quickmenu.py',
        r'canvas\document\schemeedit.py',
        r'canvas\preview\previewbrowser.py',
        r'canvas\preview\previewdialog.py',
        r'widgets\data\owconcatenate.py',
        r'widgets\data\owdiscretize.py',
        r'widgets\data\owfeatureconstructor.py',
        r'widgets\data\owimpute.py',
        r'widgets\data\owrank.py',
        r'widgets\report\owreport.py']

    # The commands to excute
    ls =''
    for file in filelist:
        ls=ls + '..\\..\\' + file +' '
      
    # Run all commands once.  
    cmd= "pylupdate5 %s -ts orange_zh_CN.ts" % (ls)
    print(cmd)
    subprocess.call(cmd)
