import pathlib

import wx
import wx.grid
from ObjectListView import ObjectListView, ColumnDefn

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
        self.fileNameDisplay = wx.TextCtrl(self, style=wx.TE_READONLY, size=(200, 35))
        self.fileNameDisplay.SetBackgroundColour(colour="#ffffff")

        self.browseBtn = wx.Button(self, label="Browse", size=(60, 35))

        topLayout = wx.BoxSizer(orient=wx.HORIZONTAL)
        topLayout.Add(
            self.fileNameDisplay,
            proportion=1,
            flag=wx.TOP | wx.LEFT,
            border=10,
        )
        topLayout.Add(self.browseBtn, flag=wx.TOP, border=10)

        costFunction = wx.StaticText(self, label="Cost Function, J(\u03B8)")
        self.costFunctionCtrl = controls.ComboCtrl(self)
        self.costFunctionCtrl.setUp()

        mlAlg = wx.StaticText(self, label="Machine Learning Algorithm")
        self.mlAlgoCtrl = controls.ComboCtrl(self)
        self.mlAlgoCtrl.setUp()

        optAlg = wx.StaticText(self, label="Optimization Algorithm")
        self.optAlgCtrl = controls.ComboCtrl(self)
        self.optAlgCtrl.setUp()

        learningRate = wx.StaticText(self, label="Learning Rate, \u03B1")
        self.learningRateCtrl = wx.TextCtrl(self, size=(170, 35))

        self.featureDisp = ObjectListView(self, style=wx.LC_REPORT)
        self.featureDisp.SetColumns(
            [
                ColumnDefn(
                    title="Feature Name(s)", valueGetter="name", isSpaceFilling=True
                )
            ]
        )
        self.featureDisp.SetEmptyListMsg("No Feature(s) Added")

        self.labelDisp = ObjectListView(self, style=wx.LC_REPORT)
        self.labelDisp.SetColumns(
            [ColumnDefn(title="Label Name", valueGetter="name", isSpaceFilling=True)]
        )
        self.labelDisp.SetEmptyListMsg("No Label Added")

        paramLayout = wx.FlexGridSizer(rows=5, cols=2, vgap=20, hgap=10)
        paramLayout.Add(costFunction)
        paramLayout.Add(self.costFunctionCtrl, flag=wx.EXPAND)
        paramLayout.Add(mlAlg)
        paramLayout.Add(self.mlAlgoCtrl, flag=wx.EXPAND)
        paramLayout.Add(optAlg)
        paramLayout.Add(self.optAlgCtrl, flag=wx.EXPAND)
        paramLayout.Add(learningRate)
        paramLayout.Add(self.learningRateCtrl, flag=wx.EXPAND)
        paramLayout.Add(self.featureDisp, flag=wx.EXPAND)
        paramLayout.Add(self.labelDisp, flag=wx.EXPAND)

        paramLayout.AddGrowableRow(4, proportion=1)
        paramLayout.AddGrowableCol(0, proportion=1)
        paramLayout.AddGrowableCol(1, proportion=1)

        self.dataDisp = controls.DataGrid(self)

        bottomLayout = wx.BoxSizer(orient=wx.HORIZONTAL)
        bottomLayout.Add(
            paramLayout,
            flag=wx.TOP | wx.RIGHT | wx.LEFT | wx.EXPAND | wx.BOTTOM,
            border=10,
        )
        bottomLayout.Add(
            self.dataDisp, proportion=1, flag=wx.TOP | wx.EXPAND, border=10
        )

        mainSizer = wx.BoxSizer(orient=wx.VERTICAL)
        mainSizer.Add(topLayout, flag=wx.EXPAND | wx.RIGHT, border=10)
        mainSizer.Add(bottomLayout, proportion=1, flag=wx.EXPAND)

        self.SetSizer(mainSizer)
