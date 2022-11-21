from pathlib import Path

import wx
from ObjectListView import ObjectListView, ColumnDefn

from . import utils

BASE_DIR = Path(__file__).parent.parent


class Application(wx.App):
    """Creates the application"""

    def OnInit(self):
        window = MainWindow(None, title="MLV", size=(700, 500))
        self.SetTopWindow(window)
        window.Show()

        return True


class Features:
    __slots__ = "name", "dataType"

    def __init__(self, name, dataType) -> None:
        self.name = name
        self.dataType = dataType


class Label:
    __slots__ = "name", "dataType"

    def __init__(self, name, dataType) -> None:
        self.name = name
        self.dataType = dataType


class MainWindow(wx.Frame):
    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)

        self.init()

        self.Center()

    def init(self):
        self.toolBar = self.CreateToolBar()
        self.toolBar.SetBackgroundColour("#000000")

        self.mainPanel = MainPanel(self)

        self.statusBar = self.CreateStatusBar()
        self.statusBar.SetBackgroundColour("#000000")


class MainPanel(wx.Panel):
    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)

        self.init()

    def init(self):
        # self.fileNameDisplay = wx.TextCtrl(self, style=wx.TE_READONLY, size=(200, 35))
        # self.fileNameDisplay.SetBackgroundColour(colour="#ffffff")

        # self.browseBtn = wx.Button(self, label="Browse", size=(60, 35))
        # self.viewDataBtn = wx.Button(self, label="View Data", size=(60, 35))

        # hSizer = wx.BoxSizer(orient=wx.HORIZONTAL)
        # hSizer.Add(
        #     self.fileNameDisplay,
        #     proportion=1,
        #     flag=wx.TOP | wx.LEFT,
        #     border=10,
        # )
        # hSizer.Add(self.browseBtn, flag=wx.TOP, border=10)
        # hSizer.Add(self.viewDataBtn, flag=wx.TOP | wx.RIGHT, border=10)

        costFunction = wx.StaticText(self, label="Cost Function")
        self.costFunctionCtrl = utils.ComboCtrl(self, size=(170, 35))
        self.costFunctionCtrl.setUp()

        mlAlg = wx.StaticText(self, label="Machine Learning Algorithm")
        self.mlAlgoCtrl = utils.ComboCtrl(self, size=(170, 35))
        self.mlAlgoCtrl.setUp()

        optAlg = wx.StaticText(self, label="Optimization Algorithm")
        self.optAlgCtrl = utils.ComboCtrl(self, size=(170, 35))
        self.optAlgCtrl.setUp()

        learningRate = wx.StaticText(self, label="Learning Rate")
        self.learningRateCtrl = wx.TextCtrl(self, size=(170, 35))

        flxGrd = wx.FlexGridSizer(rows=4, cols=2, vgap=20, hgap=10)
        flxGrd.Add(costFunction)
        flxGrd.Add(self.costFunctionCtrl)
        flxGrd.Add(mlAlg)
        flxGrd.Add(self.mlAlgoCtrl)
        flxGrd.Add(optAlg)
        flxGrd.Add(self.optAlgCtrl)
        flxGrd.Add(learningRate)
        flxGrd.Add(self.learningRateCtrl)

        self.dataDisp = ObjectListView(self, style=wx.LC_REPORT)
        self.dataDisp.SetColumns([])
        self.dataDisp.SetEmptyListMsg("No Data-Set Selected")

        self.featureDisp = ObjectListView(self, style=wx.LC_REPORT)
        self.featureDisp.SetColumns(
            [
                ColumnDefn(
                    title="Feature Name(s)", valueGetter="name", isSpaceFilling=True
                ),
                ColumnDefn(
                    title="Data Type", valueGetter="dataType", isSpaceFilling=True
                ),
            ]
        )
        self.featureDisp.SetEmptyListMsg("No Feature(s) Added")

        self.labelDisp = ObjectListView(self, style=wx.LC_REPORT)
        self.labelDisp.SetColumns(
            [
                ColumnDefn(title="Label Name", valueGetter="name", isSpaceFilling=True),
                ColumnDefn(
                    title="Data Type", valueGetter="dataType", isSpaceFilling=True
                ),
            ]
        )
        self.labelDisp.SetEmptyListMsg("No Label Added")

        v2Sizer = wx.BoxSizer(orient=wx.VERTICAL)
        v2Sizer.Add(self.dataDisp, proportion=1, flag=wx.EXPAND, border=10)

        hSizer = wx.BoxSizer(orient=wx.HORIZONTAL)
        hSizer.Add(self.featureDisp, proportion=1, flag=wx.RIGHT | wx.EXPAND, border=5)
        hSizer.Add(self.labelDisp, proportion=1, flag=wx.EXPAND)
        v2Sizer.Add(hSizer, proportion=1, flag=wx.TOP | wx.EXPAND, border=10)

        h2Sizer = wx.BoxSizer(orient=wx.HORIZONTAL)
        h2Sizer.Add(flxGrd, flag=wx.TOP | wx.RIGHT | wx.LEFT, border=10)
        h2Sizer.Add(
            v2Sizer,
            proportion=1,
            flag=wx.TOP | wx.RIGHT | wx.BOTTOM | wx.EXPAND,
            border=10,
        )

        self.SetSizer(h2Sizer)
