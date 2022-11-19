from collections.abc import Sequence
import wx
from wx.lib.mixins.listctrl import CheckListCtrlMixin


class Application(wx.App):
    """Creates the application"""

    def OnInit(self):
        window = MainWindow(None, title="MLV", size=(600, 500))
        window.Show()
        self.SetTopWindow(window)

        return True


# ----------------------------------------------------------------------
# This class is used to provide an interface between a ComboCtrl and the
# ListCtrl that is used as the popup for the combo widget.


class FeatureListCtrl(wx.ListCtrl, CheckListCtrlMixin):
    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)
        CheckListCtrlMixin.__init__(self)

        self.InsertColumn(col=0, heading="Features", format=wx.LIST_FORMAT_LEFT)
        self.InsertColumn(col=1, heading="Data Type", format=wx.LIST_FORMAT_LEFT)


class FeatureComboCtrl(wx.ComboCtrl):
    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)

    def setPopupControl(self):
        popupCtrl = FeatureListCtrlComboPopup()

        # It is important to call SetPopupControl() as soon as possible
        self.SetPopupControl(popupCtrl)

        return popupCtrl


class FeatureListCtrlComboPopup(wx.ComboPopup):
    def __init__(self):
        super().__init__()

    def addItem(self, item: Sequence):
        self.lc.Append(item)

    # The following methods are those that are overridable from the
    # ComboPopup base class.  Most of them are not required, but all
    # are shown here for demonstration purposes.

    # This is called immediately after construction finishes.  You can
    # use self.GetCombo if needed to get to the ComboCtrl instance.
    def Init(self):
        self.value = -1
        self.curitem = -1

    # Create the popup child control.  Return true for success.
    def Create(self, parent):
        self.lc = FeatureListCtrl(parent, style=wx.LC_REPORT)
        # self.lc = wx.ListCtrl(
        #     parent, style=wx.LC_LIST | wx.LC_SINGLE_SEL | wx.SIMPLE_BORDER
        # )
        # self.lc.Bind(wx.EVT_MOTION, self.OnMotion)
        # self.lc.Bind(wx.EVT_LEFT_DOWN, self.OnLeftDown)
        return True

    # Return the widget that is to be used for the popup
    def GetControl(self):
        return self.lc

    # Called just prior to displaying the popup, you can use it to
    # 'select' the current item.
    # def SetStringValue(self, val):
    #     idx = self.lc.FindItem(-1, val)
    #     if idx != wx.NOT_FOUND:
    #         self.lc.Select(idx)

    # Return a string representation of the current item.
    # def GetStringValue(self):
    #     if self.value >= 0:
    #         return self.lc.GetItemText(self.value)
    #     return ""

    # Called immediately after the popup is shown
    def OnPopup(self):
        wx.ComboPopup.OnPopup(self)

    # Called when popup is dismissed
    def OnDismiss(self):
        wx.ComboPopup.OnDismiss(self)

    # This is called to custom paint in the combo control itself
    # (ie. not the popup).  Default implementation draws value as
    # string.
    def PaintComboControl(self, dc, rect):
        wx.ComboPopup.PaintComboControl(self, dc, rect)

    # Receives key events from the parent ComboCtrl.  Events not
    # handled should be skipped, as usual.
    def OnComboKeyEvent(self, event):
        wx.ComboPopup.OnComboKeyEvent(self, event)

    # Implement if you need to support special action when user
    # double-clicks on the parent wxComboCtrl.
    def OnComboDoubleClick(self):
        wx.ComboPopup.OnComboDoubleClick(self)

    # Return final size of popup. Called on every popup, just prior to OnPopup.
    # minWidth = preferred minimum width for window
    # prefHeight = preferred height. Only applies if > 0,
    # maxHeight = max height for window, as limited by screen size
    #   and should only be rounded down, if necessary.
    def GetAdjustedSize(self, minWidth, prefHeight, maxHeight):
        return wx.ComboPopup.GetAdjustedSize(self, minWidth, prefHeight, maxHeight)

    # Return true if you want delay the call to Create until the popup
    # is shown for the first time. It is more efficient, but note that
    # it is often more convenient to have the control created
    # immediately.
    # Default returns false.
    def LazyCreate(self):
        return wx.ComboPopup.LazyCreate(self)


class LabelListCtrl(wx.ListCtrl, CheckListCtrlMixin):
    pass


class MainWindow(wx.Frame):
    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)

        self.init()

        self.Center()

    def init(self):
        toolbar = self.CreateToolBar()
        toolbar.SetBackgroundColour("#000000")
        self.main_panel = MainPanel(self)


class MainPanel(wx.Panel):
    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)

        self.init()

    def init(self):
        fileNameDisplay = wx.TextCtrl(self, style=wx.TE_READONLY, size=(200, 35))
        fileNameDisplay.SetBackgroundColour(colour="#ffffff")

        browseBtn = wx.Button(self, label="Browse", size=(60, 35))
        view_data_btn = wx.Button(self, label="View Data", size=(60, 35))

        hSizer = wx.BoxSizer(orient=wx.HORIZONTAL)
        hSizer.Add(fileNameDisplay, proportion=1, flag=wx.TOP | wx.LEFT, border=10)
        hSizer.Add(browseBtn, flag=wx.TOP, border=10)
        hSizer.Add(view_data_btn, flag=wx.TOP | wx.RIGHT, border=10)

        # comboCtrl = FeatureComboCtrl(self, pos=(100, 100), size=(170, 35))
        # self.popUpCtrl = comboCtrl.setPopupControl()
        # self.popUpCtrl.addItem(("Hello", "World"))

        self.SetSizer(hSizer)
