import wx
import wx.grid
import wx.lib.scrolledpanel
import wx.lib.mixins.gridlabelrenderer as glr
from wx.lib.mixins.listctrl import ListRowHighlighter, ListCtrlAutoWidthMixin


class Grid(wx.grid.Grid, glr.GridWithLabelRenderersMixin):
    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)
        glr.GridWithLabelRenderersMixin.__init__(self)


class ColumnRenderer(glr.GridLabelRenderer):
    # def __init__(self, bgColor) -> None:
    #     self.bgColor = bgColor

    def Draw(self, grid, dc, rect, col):
        # dc.SetBrush(wx.Brush(self.bgColor))
        # dc.SetPen(wx.TRANSPARENT_PEN)
        dc.DrawRectangle(rect)

        hAlign, vAlign = grid.GetColLabelAlignment()
        text = grid.GetColLabelValue(col)

        self.DrawBorder(grid, dc, rect)
        self.DrawText(grid, dc, rect, text, hAlign, vAlign)


class RowRenderer(glr.GridLabelRenderer):
    # def __init__(self, bgColor) -> None:
    #     self.bgColor = bgColor

    def Draw(self, grid, dc, rect, row):
        # dc.SetBrush(wx.Brush(self.bgColor))
        # dc.SetPen(wx.TRANSPARENT_PEN)
        dc.DrawRectangle(rect)

        hAlign, vAlign = grid.GetColLabelAlignment()
        text = grid.GetRowLabelValue(row)

        self.DrawBorder(grid, dc, rect)
        self.DrawText(grid, dc, rect, text, hAlign, vAlign)


class DataGrid(wx.lib.scrolledpanel.ScrolledPanel):
    def __init__(
        self,
        parent,
        id=-1,
        pos=wx.DefaultPosition,
        size=wx.DefaultSize,
        style=wx.TAB_TRAVERSAL,
        name="scrolledpanel",
    ):
        super().__init__(parent, id, pos, size, style, name)

        self.labelBgColor = "#202227"

        self.dataDisp = Grid(self)
        self.dataDisp.CreateGrid(100, 50)
        self.dataDisp.SetDefaultColSize(width=60, resizeExistingCols=True)
        self.dataDisp.SetDefaultRowSize(height=40, resizeExistingRows=True)

        pen = self.dataDisp.GetDefaultGridLinePen()
        pen.SetColour("#ff0000")
        self.dataDisp.ForceRefresh()

        # for col in range(self.dataDisp.GetNumberCols()):
        #     self.dataDisp.SetColLabelRenderer(col, ColumnRenderer())

        # for row in range(self.dataDisp.GetNumberRows()):
        #     self.dataDisp.SetRowLabelRenderer(row, RowRenderer())

        sizer = wx.BoxSizer(orient=wx.VERTICAL)
        sizer.Add(self.dataDisp, 1, wx.EXPAND)

        self.SetSizer(sizer)
        self.SetupScrolling()
