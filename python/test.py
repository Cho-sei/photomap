import wx

class MyApp(wx.PySimpleApp):
    def OnInit(self):
        Frm = wx.Frame(None, -1, 'Title', size=(500, 500))
        pnl0 = wx.Panel(Frm, -1, size=(450, 450))
        nb = wx.Notebook(pnl0, -1, style=wx.CLIP_CHILDREN)

        pnl1 = wx.Panel(nb, -1)
        pnl2 = wx.Panel(nb, -1)
        nb.AddPage(pnl1, 'Page 1')
        nb.AddPage(pnl2, 'Page 2')

        StTxt = wx.StaticText(pnl1, -1, 'Text', pos=(20,30))

        sizer = wx.BoxSizer(wx.VERTICAL) #追加
        sizer.Add(nb, 1, wx.EXPAND) #追加
        pnl0.SetSizer(sizer) #追加

        Frm.Show()
        return 1

app = MyApp()
app.MainLoop()