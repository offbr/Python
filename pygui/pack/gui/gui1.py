'''
Created on 2016. 10. 27.

gui wxPython
'''
import wx
'''
app = wx.App()
frame = wx.Frame(None, title='연습')
frame.Center()
frame.Size = (300, 250)
frame.Show(True)
app.MainLoop()
'''
class Test1(wx.Frame):
    def __init__(self, parent, title):
        super(Test1, self).__init__(parent, title=title, size=(300,250))
        
        #self.Move(100, 50)
        self.Centre()
        self.Show()
        
if __name__ =='__main__':
    app = wx.App()
    Test1(None, '메뉴연습')
    app.MainLoop()