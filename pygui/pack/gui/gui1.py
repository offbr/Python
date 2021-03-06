'''
GUI : wxPython
'''
import wx
import wxPython
# app = wx.App()
# frame = wx.Frame(None, title='연습')
# frame.Center()
# frame.Size = (300,250)
# frame.Show(True)
# app.MainLoop()

class Test1(wx.Frame):
    def __init__(self,parent, title):
        super(Test1,self).__init__(parent,title=title,size=(300,250))
        #Frame에 컨트롤 추가
        #self.txtA = wx.TextCtrl(self)
        self.txtA = wx.TextCtrl(self, style = wx.TE_MULTILINE)
        self.CreateStatusBar()
        #Frame에 메뉴 추가
        menuBar = wx.MenuBar()
        mnuFile = wx.Menu()
        
        mnuNew = wx.MenuItem(mnuFile, wx.ID_NEW, 'New','새글')
        
        
        mnuOpen = mnuFile.Append(wx.ID_OPEN, 'Open','열기')
        mnuFile.AppendSeparator()
        mnuExit = mnuFile.Append(wx.ID_EXIT, 'Exit','닫기')
        
        mnuFile.Append(mnuNew)
        menuBar.Append(mnuFile,"file")
        
        self.SetMenuBar(menuBar)
        self.Center()
        
        #메뉴에 이벤트
        self.Bind(wx.EVT_MENU, self.OnFunc,mnuNew)
        self.Bind(wx.EVT_MENU, self.OnFunc2,mnuOpen)
        self.Bind(wx.EVT_MENU, self.OnFunc3,mnuExit)
        
        self.Show(show=True)
    def OnFunc(self, event):
        self.txtA.SetLabelText('새문서')
    def OnFunc2(self,event): #이벤트 핸들러 메소드
        self.Aa()
        
    def Aa(self):
        self.txtA.SetLabelText('열기')
        
    def OnFunc3(self, event):
        self.Close(force=True)     
              
if __name__ == '__main__':
    app = wx.App()
    Test1(None, '메뉴연습')
    app.MainLoop()
    
    
