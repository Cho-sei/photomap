import wx

def click_button_1(event):
	frame.SetStatusText('Click Button1')

def click_button(event):
	if event.GetId() == 22:
		frame.SetStatusText('Click Button2')
	elif event.GetId() == 33:
		frame.SetStatusText('Click Button3') 

application = wx.App()

frame = wx.Frame(None, wx.ID_ANY, 'testframe', size=(300,300))
frame.SetBackgroundColour('#000000')
frame.CreateStatusBar();

notebook = wx.Notebook(frame, wx.ID_ANY)

title = wx.Panel(frame, wx.ID_ANY, pos=(0,0), size=(300,30))
title.SetBackgroundColour('#0000FF')
map = wx.Panel(notebook, wx.ID_ANY, pos=(0,30))
map.SetBackgroundColour('#AFAFAF')
picture = wx.Panel(notebook, wx.ID_ANY, pos=(0,30))
picture.SetBackgroundColour('#00FF00')

titletext = wx.StaticText(title, wx.ID_ANY, '-test-')

button_1 = wx.Button(map, wx.ID_ANY, 'button_1')
button_2 = wx.Button(map, 22, 'button_2')
button_3 = wx.Button(map, 33, 'button_3')

button_1.Bind(wx.EVT_BUTTON, click_button_1)
frame.Bind(wx.EVT_BUTTON, click_button, button_2)
frame.Bind(wx.EVT_BUTTON, click_button, button_3)

layout = wx.FlexGridSizer(rows=2, cols=2)
layout.Add(button_1,proportion=1,flag=wx.EXPAND)
layout.Add(button_2,proportion=1,flag=wx.EXPAND)
layout.Add(button_3,proportion=1,flag=wx.EXPAND)

map.SetSizer(layout)

notebook.InsertPage(0,map,'MAP')
notebook.InsertPage(1,picture,'PICTURE')

frame.Centre()
frame.Show()

application.MainLoop()
