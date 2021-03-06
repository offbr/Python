'''
Created on 2016. 10. 31.

'''

import wx
import wx.xrc
import MySQLdb
import sys

config = {
    'host' : '127.0.0.1',
    'user' : 'root',
    'password' : '',
    'database' : 'test',
    'port' : 3306,
    'charset' : 'utf8',
    'use_unicode' : True
    }
datas = []
rec_r = 0

class MyFrame1 ( wx.Frame ):
    
    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 325,151 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
        
        #self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
        self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
        
        bSizer1 = wx.BoxSizer( wx.VERTICAL )
        
        self.m_panel1 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.TAB_TRAVERSAL )
        self.m_panel1.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
        
        bSizer3 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText2 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"사번", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText2.Wrap( -1 )
        self.m_staticText2.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )
        self.m_staticText2.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
        
        bSizer3.Add( self.m_staticText2, 0, wx.ALL, 5 )
        
        self.txtSabun = wx.TextCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
        bSizer3.Add( self.txtSabun, 0, wx.ALL, 5 )
        
        self.m_staticText3 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"이름", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText3.Wrap( -1 )
        self.m_staticText3.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )
        
        bSizer3.Add( self.m_staticText3, 0, wx.ALL, 5 )
        
        self.txtIrum = wx.TextCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
        bSizer3.Add( self.txtIrum, 0, wx.ALL, 5 )
        
        self.m_staticText4 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"직급", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText4.Wrap( -1 )
        self.m_staticText4.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )
        
        bSizer3.Add( self.m_staticText4, 0, wx.ALL, 5 )
        
        self.txtJik = wx.TextCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
        bSizer3.Add( self.txtJik, 0, wx.ALL, 5 )
        
        
        self.m_panel1.SetSizer( bSizer3 )
        self.m_panel1.Layout()
        bSizer3.Fit( self.m_panel1 )
        bSizer1.Add( self.m_panel1, 1, wx.ALL, 5 )
        
        self.m_panel2 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        self.m_panel2.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
        
        bSizer4 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.btn1 = wx.Button( self.m_panel2, wx.ID_ANY, u"l<", wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
        bSizer4.Add( self.btn1, 0, wx.ALL, 5 )
        
        self.btn2 = wx.Button( self.m_panel2, wx.ID_ANY, u"<<", wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
        bSizer4.Add( self.btn2, 0, wx.ALL, 5 )
        
        self.btn3 = wx.Button( self.m_panel2, wx.ID_ANY, u">>", wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
        bSizer4.Add( self.btn3, 0, wx.ALL, 5 )
        
        self.btn4 = wx.Button( self.m_panel2, wx.ID_ANY, u">l", wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
        bSizer4.Add( self.btn4, 0, wx.ALL, 5 )
        
        
        self.m_panel2.SetSizer( bSizer4 )
        self.m_panel2.Layout()
        bSizer4.Fit( self.m_panel2 )
        bSizer1.Add( self.m_panel2, 1, wx.EXPAND |wx.ALL, 5 )
        
        
        self.SetSizer( bSizer1 )
        self.Layout()
        
        self.Centre( wx.BOTH )
        
        # Connect Events
        self.btn1.Bind( wx.EVT_BUTTON, self.onClick )
        self.btn2.Bind( wx.EVT_BUTTON, self.onClick )
        self.btn3.Bind( wx.EVT_BUTTON, self.onClick )
        self.btn4.Bind( wx.EVT_BUTTON, self.onClick )
        self.btn1.id = 1
        self.btn2.id = 2
        self.btn3.id = 3
        self.btn4.id = 4
        self.DbLoad()
        
    # Virtual event handlers, overide them in your derived class
    def onClick( self, event ):
        id = event.GetEventObject().id
        #print(id)
        
        global rec_r
        
        if id == 1:
            rec_r = 0
        elif id == 2:
            rec_r -= 1
            if rec_r < 0:
                rec_r = 0
                return
        elif id == 3:
            rec_r += 1
            if rec_r > (len(datas) - 1):
                rec_r = len(datas) - 1
                return
        elif id ==4:
            rec_r = len(datas) - 1
            
        self.ShowData(rec_r)
    
    def DbLoad(self):
        try:
            conn = MySQLdb.connect(**config)
            cursor = conn.cursor()
            sql = "select sawon_no, sawon_name, sawon_jik from sawon"
            cursor.execute(sql)
            
            global datas
            datas = cursor.fetchall()
            #print(datas)
            #print(datas[0])
            #print(datas[0][0])
            self.ShowData(rec_r)
            
        except Exception as e:
            wx.MessageBox('db err : ' + str(e))
            
        finally:
            conn.close()        
    
    def ShowData(self, r):
        self.txtSabun.SetLabel(str(datas[r][0]))
        self.txtIrum.SetLabel(str(datas[r][1]))
        self.txtJik.SetLabel(str(datas[r][2]))

if __name__ == '__main__':
    app = wx.App()
    MyFrame1(None).Show()
    app.MainLoop()    


