import wx
 
application = wx.App()
 
frame = wx.Frame(None, wx.ID_ANY, 'テストフレーム', size=(300, 300))
frame.SetBackgroundColour('#000000')
 

 
g_panel = wx.Panel(frame, wx.ID_ANY, pos=(80, 0), size=(80, 300))
g_panel.SetBackgroundColour('#00FF00')
 

 
frame.Show()
application.MainLoop()