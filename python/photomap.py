import wx

application = wx.App()
frame = wx.Frame(None, wx.ID_ANY, size=(500,500))

Left_panel = wx.Panel(frame, wx.ID_ANY, pos=(0,0), size=(100,500))
Right_panel = wx.Panel(frame, wx.ID_ANY, pos=(400,0), size=(100,500))
title = wx.Panel(frame, wx.ID_ANY, pos=(100,0), size=(300,100))
tab = wx.Panel(frame, wx.ID_ANY, pos=(100,100), size=(300,400))

Left_panel.SetBackgroundColour('#AFAFAF')
Right_panel.SetBackgroundColour('#AFAFAF')
title.SetBackgroundColour('#0000FF')
tab.SetBackgroundColour('#00FF00')

frame.Show()
application.MainLoop()