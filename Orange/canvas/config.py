"""
Orange Canvas Configuration

"""

import os
import sys
import logging
import pickle as pickle
import itertools
import warnings

import pkg_resources

from AnyQt.QtGui import (
    QPainter, QFont, QFontMetrics, QColor, QPixmap, QIcon
)

from AnyQt.QtCore import Qt, QCoreApplication, QPoint, QRect, QSettings

from .utils.settings import Settings, config_slot

log = logging.getLogger(__name__)


def init():
    """
    Initialize the QCoreApplication.organizationDomain, applicationName,
    applicationVersion and the default settings format. Will only run once.

    .. note:: This should not be run before QApplication has been initialized.
              Otherwise it can break Qt's plugin search paths.

    """
    dist = pkg_resources.get_distribution("Orange3")
    version = dist.version
    # Use only major.minor
    version = ".".join(version.split(".", 2)[:2])

    QCoreApplication.setOrganizationDomain("正行软件")
    QCoreApplication.setApplicationName("Orange数据挖掘 V3.16")
    QCoreApplication.setApplicationVersion(version)
    QSettings.setDefaultFormat(QSettings.IniFormat)

    # Make it a null op.
    global init
    init = lambda: None


rc = {}


spec = \
    [("startup/show-splash-screen", bool, True,
      "启动时显示闪屏"),

     ("startup/show-welcome-screen", bool, True,
      "启东市显示欢迎屏幕"),

     ("startup/check-updates", bool, True,
      "启动时检查更新"),

     ("stylesheet", str, "orange",
      "使用QSS样式"),

     ("schemeinfo/show-at-new-scheme", bool, True,
      "创建新工作流时显示工作流属性"),

     ("mainwindow/scheme-margins-enabled", bool, False,
      "显示工作流视图边框"),

     ("mainwindow/show-scheme-shadow", bool, True,
      "显示工作流视图阴影"),

     ("mainwindow/toolbox-dock-exclusive", bool, True,
      "工具箱只展开一个目录"),

     ("mainwindow/toolbox-dock-floatable", bool, False,
      "工具箱是否可浮动"),

     ("mainwindow/toolbox-dock-movable", bool, True,
      "工具箱可移动(左侧或右侧靠边)"),

     ("mainwindow/toolbox-dock-use-popover-menu", bool, True,
      "点击类别按钮时，用悬浮菜单选择组件"),

     ("mainwindow/widgets-float-on-top", bool, False,
      "组件可以负载其他窗口上"),

     ("mainwindow/number-of-recent-schemes", int, 15,
      "历史记录中保留的当前工作流数量"),

     ("schemeedit/show-channel-names", bool, True,
      "显示频道名称"),

     ("schemeedit/show-link-state", bool, True,
      "显示链接状态提示信息。"),

     ("schemeedit/enable-node-animations", bool, True,
      "启用节点动画。"),

     ("schemeedit/freeze-on-load", bool, False,
      "加载工作流时，冻结信号传播。"),

     ("quickmenu/trigger-on-double-click", bool, True,
      "双击显示快捷菜单。"),

     ("quickmenu/trigger-on-right-click", bool, True,
      "右键显示快捷菜单。"),

     ("quickmenu/trigger-on-space-key", bool, True,
      "空格键显示快捷菜单。"),

     ("quickmenu/trigger-on-any-key", bool, False,
      "按任意键显示快捷菜单。"),

     ("logging/level", int, 1, "日志级别"),

     ("logging/show-on-error", bool, True, "出错时显示日志窗口"),

     ("logging/dockable", bool, True, "允许日志窗口停靠"),

     ("help/open-in-external-browser", bool, False,
      "在外部浏览器打开帮助"),

     ("error-reporting/machine-id", str, '',
     "错误报告采用定制名称而不是机器ID"),

     ("add-ons/allow-conda", bool, True,
      "用conda安装插件"),

     ("add-ons/pip-install-arguments", str, '',
      '安装插件时传给"pip install"的参数。'),

     ("network/http-proxy", str, '', 'HTTP代理。'),

     ("network/https-proxy", str, '', 'HTTPS代理。'),
     ]

spec = [config_slot(*t) for t in spec]


def settings():
    init()
    store = QSettings()
    settings = Settings(defaults=spec, store=store)
    return settings


def data_dir():
    """Return the application data directory. If the directory path
    does not yet exists then create it.

    """
    from Orange.misc import environ
    path = os.path.join(environ.data_dir(), "canvas")

    if not os.path.isdir(path):
        os.makedirs(path, exist_ok=True)
    return path


def cache_dir():
    """Return the application cache directory. If the directory path
    does not yet exists then create it.

    """
    from Orange.misc import environ
    path = os.path.join(environ.cache_dir(), "canvas")

    if not os.path.isdir(path):
        os.makedirs(path, exist_ok=True)
    return path


def log_dir():
    """
    Return the application log directory.
    """
    init()
    if sys.platform == "darwin":
        name = str(QCoreApplication.applicationName())
        logdir = os.path.join(os.path.expanduser("~/Library/Logs"), name)
    else:
        logdir = data_dir()

    if not os.path.exists(logdir):
        os.makedirs(logdir)
    return logdir


def widget_settings_dir():
    """
    Return the widget settings directory.
    """
    from Orange.misc import environ
    return environ.widget_settings_dir()


def open_config():
    warnings.warn(
        "open_config was never used and will be removed in the future",
        DeprecationWarning, stacklevel=2
    )
    return


def save_config():
    warnings.warn(
        "save_config was never used and will be removed in the future",
        DeprecationWarning, stacklevel=2
    )


def recent_schemes():
    """Return a list of recently accessed schemes.
    """
    app_dir = data_dir()
    recent_filename = os.path.join(app_dir, "recent.pck")
    recent = []
    if os.path.isdir(app_dir) and os.path.isfile(recent_filename):
        with open(recent_filename, "rb") as f:
            recent = pickle.load(f)

    # Filter out files not found on the file system
    recent = [(title, path) for title, path in recent \
              if os.path.exists(path)]
    return recent


def save_recent_scheme_list(scheme_list):
    """Save the list of recently accessed schemes
    """
    app_dir = data_dir()
    recent_filename = os.path.join(app_dir, "recent.pck")

    if os.path.isdir(app_dir):
        with open(recent_filename, "wb") as f:
            pickle.dump(scheme_list, f)


WIDGETS_ENTRY = "orange.widgets"


# This could also be achieved by declaring the entry point in
# Orange's setup.py, but that would not guaranty this entry point
# is the first in a list.

def default_entry_point():
    """
    Return a default orange.widgets entry point for loading
    default Orange Widgets.

    """
    dist = pkg_resources.get_distribution("Orange3")
    ep = pkg_resources.EntryPoint("Orange Widgets", "Orange.widgets",
                                  dist=dist)
    return ep


def widgets_entry_points():
    """
    Return an `EntryPoint` iterator for all 'orange.widget' entry
    points plus the default Orange Widgets.

    """
    ep_iter = pkg_resources.iter_entry_points(WIDGETS_ENTRY)
    chain = [[default_entry_point()],
             ep_iter
             ]
    return itertools.chain(*chain)

#: Parameters for searching add-on packages in PyPi using xmlrpc api.
ADDON_KEYWORD = 'orange3 add-on'
ADDON_PYPI_SEARCH_SPEC = {"keywords": ADDON_KEYWORD}
#: Entry points by which add-ons register with pkg_resources.
ADDON_ENTRY = "orange3.addon"


def splash_screen():
    """
    """
    pm = QPixmap(
        pkg_resources.resource_filename(
            __name__, "icons/orange-splash-screen.png")
    )

    version = QCoreApplication.applicationVersion()
    size = 21 if len(version) < 5 else 16
    font = QFont("Helvetica")
    font.setPixelSize(size)
    font.setBold(True)
    font.setItalic(True)
    font.setLetterSpacing(QFont.AbsoluteSpacing, 2)
    metrics = QFontMetrics(font)
    br = metrics.boundingRect(version).adjusted(-5, 0, 5, 0)
    br.moveCenter(QPoint(436, 224))

    p = QPainter(pm)
    p.setRenderHint(QPainter.Antialiasing)
    p.setRenderHint(QPainter.TextAntialiasing)
    p.setFont(font)
    p.setPen(QColor("#231F20"))
    p.drawText(br, Qt.AlignCenter, version)
    p.end()
    return pm, QRect(88, 193, 200, 20)


def application_icon():
    """
    Return the main application icon.
    """
    path = pkg_resources.resource_filename(
        __name__, "icons/orange-canvas.svg"
    )
    return QIcon(path)

