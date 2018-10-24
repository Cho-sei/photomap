import wx

application = wx.App()
frame = wx.Frame(None, wx.ID_ANY, size=(500,500))
frame.SetBackgroundColour('#FF0000')

Left_panel = wx.Panel(frame, wx.ID_ANY, pos=(0,0), size=(100,500))
Right_panel = wx.Panel(frame, wx.ID_ANY, pos=(400,0), size=(100,500))
title = wx.Panel(frame, wx.ID_ANY, pos=(100,0), size=(300,100))
tab = wx.Panel(frame, wx.ID_ANY, pos=(100,100), size=(300,400))

Left_panel.SetBackgroundColour('#AFAFAF')
Right_panel.SetBackgroundColour('#AFAFAF')
title.SetBackgroundColour('#0000FF')
tab.SetBackgroundColour('#00FF00')

notebook = wx.Notebook(tab, -1, style=wx.CLIP_CHILDREN)
map = wx.Panel(notebook, -1)
picture = wx.Panel(notebook, -1)
map.SetBackgroundColour('#000000')
picture.SetBackgroundColour('#FFFFFF')

notebook.InsertPage(0,map,'MAP')
notebook.InsertPage(1,picture,'PICTURE')

frame_layout = wx.FlexGridSizer(rows=2, cols=3, gap=(0, 0))
frame_layout.Add(Left_panel,flag=wx.GROW)
frame_layout.Add(Right_panel,flag=wx.GROW)
frame_layout.Add(title,flag=wx.GROW)
frame_layout.Add(tab,flag=wx.GROW)
frame.SetSizer(frame_layout)

nb_layout = wx.BoxSizer(wx.VERTICAL)
nb_layout.Add(notebook, proportion=1, flag=wx.EXPAND)
tab.SetSizer(nb_layout)

frame.Centre()
frame.Show()
application.MainLoop()