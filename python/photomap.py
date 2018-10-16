import wx

application = wx.App()

frame = wx.Frame(None, wx.ID_ANY, 'testframe', size=(300,300))
frame.SetBackgroundColour('#000000')

panel = wx.Panel(frame, wx.ID_ANY, size=(80,80))
panel.SetBackgroundColour('#AFAFAF')

button_1 = wx.Button(panel, wx.ID_ANY, 'button_1')
button_2 = wx.Button(panel, wx.ID_ANY, 'button_2')
button_3 = wx.Button(panel, wx.ID_ANY, 'button_3')

layout = wx.BoxSizer(wx.HORIZONTAL)
layout.Add(button_1,proportion=1)
layout.Add(button_2,proportion=1)
layout.Add(button_3,proportion=1)

panel.SetSizer(layout)

frame.Centre()
frame.Show()

application.MainLoop()
