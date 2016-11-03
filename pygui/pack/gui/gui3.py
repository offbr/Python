'''
layout - sizer
'''

import wx

class Test2(wx.Frame):
    def __init__(self,parent, title):
        super(Test2,self).__init__(parent,title=title,size=(300,250))
        
        panel1 = wx.Panel(self, -1, style=wx.SUNKEN_BORDER)
        panel2 = wx.Panel(self, -1, style=wx.SUNKEN_BORDER)
        
        panel1.SetBackgroundColour("BLUE")
        panel2.SetBackgroundColour("ORANGE")
        
        box = wx.BoxSizer(wx.HORIZONTAL)
        box.Add(panel1, 1, wx.EXPAND)
        box.Add(panel2, 2, wx.EXPAND)
        
        self.SetSizer(box)
        
        self.Center()
        self.Show(show=True)
        
if __name__ == '__main__':
    app = wx.App()
    Test2(None, '버튼연습')
    app.MainLoop()        
    
    
    