import pathlib

import wx

from . import controls

BASE_DIR = pathlib.Path(__file__).parent.parent


class Application(wx.App):
    """Creates the application"""

    def OnInit(self):
        window = MainWindow(None, title="MLV", size=(700, 500))
        self.SetTopWindow(window)

        return True


class MainWindow(wx.Frame):
    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)

        self.init()

        self.Center()

        self.Show()

    def init(self):
        menuBar = wx.MenuBar()

        menus = []

        fileMenu = wx.Menu()
        menus.append((fileMenu, "File"))

        costMenu = wx.Menu()
        menus.append((costMenu, "Cost Function"))

        mlAlgMenu = wx.Menu()
        menus.append((mlAlgMenu, "ML Algorithm"))

        optAlgMenu = wx.Menu()
        menus.append((optAlgMenu, "Optimizer"))

        for menu, title in menus:
            menuBar.Append(menu=menu, title=f"&{title}")

        self.SetMenuBar(menuBar)

        self.toolBar = self.CreateToolBar()
        # self.toolBar.SetBackgroundColour("#000000")

        self.mainPanel = MainPanel(self)

        self.statusBar = self.CreateStatusBar()
        # self.statusBar.SetBackgroundColour("#000000")


class MainPanel(wx.Panel):
    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)

        self.mainBackgroundColor = "#191a1f"
        self.textColor = "#dbdada"
        self.textCtrlColor = "#0f0f10"
        self.btnColor = "#5dbea3"

        # self.SetBackgroundColour(self.mainBackgroundColor)

        self.init()
        self.SetAutoLayout(autoLayout=True)

    def init(self):

        self.dataDisp = controls.DataGrid(self)
        self.dataDisp.dataDisp.SetBackgroundColour(self.textCtrlColor)

        mainSizer = wx.BoxSizer(orient=wx.VERTICAL)
        mainSizer.Add(self.dataDisp, proportion=1, flag=wx.EXPAND)

        self.SetSizer(mainSizer)
