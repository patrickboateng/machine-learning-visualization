import wx


class MainPanel(wx.Panel):
    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)


class MainWindow(wx.Frame):
    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)

        self.Center()


def main():
    app = wx.App(useBestVisual=True)

    frame = MainWindow(None, title="Machine Learning Visualization")
    frame.Show()

    app.MainLoop()


if __name__ == "__main__":
    main()
