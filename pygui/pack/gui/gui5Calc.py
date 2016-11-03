'''
Created on 2016. 10. 28.

wxFormBuilder
'''
# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Aug 23 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MyCalc
###########################################################################

class MyCalc ( wx.Frame ):
    
    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"간단한 계산기", pos = wx.DefaultPosition, size = wx.Size( 247,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
        
        #self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
        
        self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
        self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )
        
        bSizer7 = wx.BoxSizer( wx.VERTICAL )
        
        self.m_panel5 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer8 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText1 = wx.StaticText( self.m_panel5, wx.ID_ANY, u"숫자 1:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText1.Wrap( -1 )
        bSizer8.Add( self.m_staticText1, 0, wx.ALL, 5 )
        
        self.txtNum1 = wx.TextCtrl( self.m_panel5, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer8.Add( self.txtNum1, 1, wx.ALL, 5 )
        
        
        self.m_panel5.SetSizer( bSizer8 )
        self.m_panel5.Layout()
        bSizer8.Fit( self.m_panel5 )
        bSizer7.Add( self.m_panel5, 1, wx.EXPAND |wx.ALL, 5 )
        
        self.m_panel6 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer81 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText2 = wx.StaticText( self.m_panel6, wx.ID_ANY, u"숫자 2:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText2.Wrap( -1 )
        bSizer81.Add( self.m_staticText2, 0, wx.ALL, 5 )
        
        self.txtNum2 = wx.TextCtrl( self.m_panel6, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer81.Add( self.txtNum2, 1, wx.ALL, 5 )
        
        
        self.m_panel6.SetSizer( bSizer81 )
        self.m_panel6.Layout()
        bSizer81.Fit( self.m_panel6 )
        bSizer7.Add( self.m_panel6, 1, wx.EXPAND |wx.ALL, 5 )
        
        self.m_panel7 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer1 = wx.BoxSizer( wx.HORIZONTAL )
        
        rdoOpChoices = [ u"+", u"-", u"*", u"/" ]
        self.rdoOp = wx.RadioBox( self.m_panel7, wx.ID_ANY, u"연산자선택", wx.DefaultPosition, wx.Size( 200,-1 ), rdoOpChoices, 1, wx.RA_SPECIFY_ROWS )
        self.rdoOp.SetSelection( 0 )
        bSizer1.Add( self.rdoOp, 1, wx.ALL|wx.EXPAND, 5 )
        
        
        self.m_panel7.SetSizer( bSizer1 )
        self.m_panel7.Layout()
        bSizer1.Fit( self.m_panel7 )
        bSizer7.Add( self.m_panel7, 1, wx.EXPAND |wx.ALL, 5 )
        
        self.m_panel8 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer15 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText19 = wx.StaticText( self.m_panel8, wx.ID_ANY, u"연산결과:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText19.Wrap( -1 )
        bSizer15.Add( self.m_staticText19, 0, wx.ALL, 5 )
        
        self.staResult = wx.StaticText( self.m_panel8, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.staResult.Wrap( -1 )
        bSizer15.Add( self.staResult, 0, wx.ALL, 5 )
        
        
        self.m_panel8.SetSizer( bSizer15 )
        self.m_panel8.Layout()
        bSizer15.Fit( self.m_panel8 )
        bSizer7.Add( self.m_panel8, 1, wx.EXPAND |wx.ALL, 5 )
        
        self.m_panel9 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer16 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.btnCalc = wx.Button( self.m_panel9, wx.ID_ANY, u"계산", wx.DefaultPosition, wx.Size( 70,-1 ), 0 )
        bSizer16.Add( self.btnCalc, 0, wx.ALL, 5 )
        
        self.btnClear = wx.Button( self.m_panel9, wx.ID_ANY, u"초기화", wx.DefaultPosition, wx.Size( 70,-1 ), 0 )
        bSizer16.Add( self.btnClear, 0, wx.ALL, 5 )
        
        self.btnExit = wx.Button( self.m_panel9, wx.ID_ANY, u"종료", wx.DefaultPosition, wx.Size( 70,-1 ), 0 )
        bSizer16.Add( self.btnExit, 0, wx.ALL, 5 )
        
        
        self.m_panel9.SetSizer( bSizer16 )
        self.m_panel9.Layout()
        bSizer16.Fit( self.m_panel9 )
        bSizer7.Add( self.m_panel9, 1, wx.EXPAND |wx.ALL, 5 )
        
        
        self.SetSizer( bSizer7 )
        self.Layout()
        
        self.Centre( wx.BOTH )
        
        # Connect Events
        self.btnCalc.id = 1
        self.btnClear.id = 2
        self.btnExit.id = 3
        
        self.btnCalc.Bind( wx.EVT_BUTTON, self.OnProcess )
        self.btnClear.Bind( wx.EVT_BUTTON, self.OnProcess )
        self.btnExit.Bind( wx.EVT_BUTTON, self.OnProcess )
    
    def __del__( self ):
        pass
    
    
    # Virtual event handlers, overide them in your derived class
    def OnProcess( self, event ):
        sel_id = event.GetEventObject().id
        #print(sel_id)        
        if sel_id == 1:
            op = self.rdoOp.GetStringSelection()
            #print(op)
            
            num1 = self.txtNum1.GetValue()
            num2 = self.txtNum2.GetValue()
            
            if num1 == '' or num2 == '':
                wx.MessageBox('값을 입력하세요', '에러', wx.OK)
                return
            try:
                mes = eval(num1 + op + num2)
            except Exception as e:
                wx.MessageBox('연산오류: ' + str(e), '에러', wx.OK)
                return  
                
            self.staResult.SetLabel(str(mes))    
                
        elif sel_id == 2:
            self.txtNum1.SetLabel('')
            self.txtNum2.SetLabel('')
            self.staResult.SetLabel('')
            self.rdoOp.SetSelection(0)
            self.txtNum1.SetFocus()
            
        elif sel_id == 3:   
            dlg = wx.MessageDialog(self, '정말 종료할까요?', '알림', wx.YES_NO)
            imsi = dlg.ShowModal()
            if imsi == wx.ID_YES:
                dlg.Destroy()
                self.Close()
    
    
if __name__ == '__main__':
    app = wx.App()
    MyCalc(None).Show()
    app.MainLoop()        
    













