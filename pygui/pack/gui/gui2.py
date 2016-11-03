'''
버튼
'''

import wx

class Test2(wx.Frame):
    def __init__(self,parent, title):
        super(Test2,self).__init__(parent,title=title,size=(300,250))
        
        self.InitUi()
        self.Center()
        self.Show(show=True)
    
    def InitUi(self):
        panel = wx.Panel(self)
        wx.StaticText(panel, label = 'i d : ', pos = (5, 5))
        wx.StaticText(panel, label = 'pwd : ', pos = (5, 40))
        self.txt1 = wx.TextCtrl(panel, pos = (50, 5), size = (50, -1))  #-1 : text의 높이(기본값)만큼 알아서 잡아줌
        self.txt2 = wx.TextCtrl(panel, pos = (50, 40))
        
        #Button
        btn1 = wx.Button(panel, label='일반버튼', pos = (5, 100))
        btn2 = wx.ToggleButton(panel, label='토글버튼', pos = (100, 100))
        btn3 = wx.Button(panel, label='종료', pos = (200, 100), size = (50, -1))
        
        '''
        #event
        btn1.Bind(wx.EVT_BUTTON, self.onClick1)
        btn2.Bind(wx.ToggleButton, self.onClick2)
        btn3.Bind(wx.EVT_BUTTON, self.onClick3)
        '''
        
        #event
        btn1.Bind(wx.EVT_BUTTON, self.onMethod)
        btn2.Bind(wx.EVT_TOGGLEBUTTON, self.onMethod)
        btn3.Bind(wx.EVT_BUTTON, self.onMethod)
        btn1.id=1; btn2.id=2; btn3.id=3;
        
    def onClick1(self, event):
        #대화상자
        dlg = wx.MessageDialog(self, '배고파ㅠㅠ', '밥먹자', wx.OK)
        dlg.ShowModal()
        dlg.Destroy()
        
        self.txt1.SetLabelText('kbs')
        self.txt2.SetLabelText('7')
        
    def onClick2(self, event):
        if event.GetEventObject().GetValue():
            self.SetTitle('동규')
        else:
            self.SetTitle('만세')
    def onClick3(self, event):
        self.Close(force=True)
        
    def onMethod(self, event):
#         print(event.GetEventObject().id)
        if event.GetEventObject().id == 1:
            self.txt1.SetLabelText('kbs')
            self.txt2.SetLabelText('7')
        elif event.GetEventObject().id == 2:
            self.txt1.SetLabelText('jtbc')
            self.txt2.SetLabelText('15')
        elif event.GetEventObject().id == 3:
            self.Close(force=True)
            
if __name__ == '__main__':
    app = wx.App()
    Test2(None, '버튼연습')
    app.MainLoop()

    
