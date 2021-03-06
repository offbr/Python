'''
Created on 2016. 10. 31.

@author: All
'''
import wx
import wx.xrc

import MySQLdb

config = {
    'host' : '127.0.0.1',
    'user' : 'root',
    'password' : '',
    'database' : 'test',
    'port' : 3306,
    'charset' : 'utf8',
    'use_unicode' : True
    }

class MyMember ( wx.Frame ):
    
    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"회원관리", pos = wx.DefaultPosition, size = wx.Size( 271,367 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
        
        #self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
        self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
        
        bSizer5 = wx.BoxSizer( wx.VERTICAL )
        
        self.m_panel3 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer6 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText5 = wx.StaticText( self.m_panel3, wx.ID_ANY, u"번호: ", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText5.Wrap( -1 )
        self.m_staticText5.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
        self.m_staticText5.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
        
        bSizer6.Add( self.m_staticText5, 0, wx.ALL, 5 )
        
        self.txtNo = wx.TextCtrl( self.m_panel3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer6.Add( self.txtNo, 0, wx.ALL, 5 )
        
        self.btnInsert = wx.Button( self.m_panel3, wx.ID_ANY, u"등록", wx.DefaultPosition, wx.Size( 90,-1 ), 0 )
        bSizer6.Add( self.btnInsert, 0, wx.ALL, 5 )
        
        
        self.m_panel3.SetSizer( bSizer6 )
        self.m_panel3.Layout()
        bSizer6.Fit( self.m_panel3 )
        bSizer5.Add( self.m_panel3, 0, wx.EXPAND |wx.ALL, 5 )
        
        self.m_panel4 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer7 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_static6 = wx.StaticText( self.m_panel4, wx.ID_ANY, u"이름: ", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_static6.Wrap( -1 )
        self.m_static6.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
        self.m_static6.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
        
        bSizer7.Add( self.m_static6, 0, wx.ALL, 5 )
        
        self.txtName = wx.TextCtrl( self.m_panel4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer7.Add( self.txtName, 0, wx.ALL, 5 )
        
        self.btnUpdate = wx.Button( self.m_panel4, wx.ID_ANY, u"수정", wx.DefaultPosition, wx.Size( 40,-1 ), 0 )
        bSizer7.Add( self.btnUpdate, 0, wx.ALL, 5 )
        
        self.btnConfirm = wx.Button( self.m_panel4, wx.ID_ANY, u"확인", wx.DefaultPosition, wx.Size( 40,-1 ), 0 )
        bSizer7.Add( self.btnConfirm, 0, wx.ALL, 5 )
        
        
        self.m_panel4.SetSizer( bSizer7 )
        self.m_panel4.Layout()
        bSizer7.Fit( self.m_panel4 )
        bSizer5.Add( self.m_panel4, 0, wx.EXPAND |wx.ALL, 5 )
        
        self.m_panel5 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer8 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText7 = wx.StaticText( self.m_panel5, wx.ID_ANY, u"전화: ", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText7.Wrap( -1 )
        self.m_staticText7.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
        self.m_staticText7.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
        
        bSizer8.Add( self.m_staticText7, 0, wx.ALL, 5 )
        
        self.txtTel = wx.TextCtrl( self.m_panel5, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer8.Add( self.txtTel, 0, wx.ALL, 5 )
        
        self.btnDel = wx.Button( self.m_panel5, wx.ID_ANY, u"삭제", wx.DefaultPosition, wx.Size( 90,-1 ), 0 )
        bSizer8.Add( self.btnDel, 0, wx.ALL, 5 )
        
        
        self.m_panel5.SetSizer( bSizer8 )
        self.m_panel5.Layout()
        bSizer8.Fit( self.m_panel5 )
        bSizer5.Add( self.m_panel5, 0, wx.EXPAND |wx.ALL, 5 )
        
        self.m_panel6 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer9 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.lstMem = wx.ListCtrl( self.m_panel6, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_REPORT )
        bSizer9.Add( self.lstMem, 1, wx.ALL|wx.EXPAND, 5 )
        
        
        self.m_panel6.SetSizer( bSizer9 )
        self.m_panel6.Layout()
        bSizer9.Fit( self.m_panel6 )
        bSizer5.Add( self.m_panel6, 0, wx.ALL, 5 )
        
        self.m_panel7 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer10 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText11 = wx.StaticText( self.m_panel7, wx.ID_ANY, u"인원수: ", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText11.Wrap( -1 )
        self.m_staticText11.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
        self.m_staticText11.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
        
        bSizer10.Add( self.m_staticText11, 0, wx.ALL, 5 )
        
        self.staCount = wx.StaticText( self.m_panel7, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.staCount.Wrap( -1 )
        self.staCount.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
        self.staCount.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
        
        bSizer10.Add( self.staCount, 0, wx.ALL, 5 )
        
        
        self.m_panel7.SetSizer( bSizer10 )
        self.m_panel7.Layout()
        bSizer10.Fit( self.m_panel7 )
        bSizer5.Add( self.m_panel7, 1, wx.EXPAND |wx.ALL, 5 )
        
        
        self.SetSizer( bSizer5 )
        self.Layout()
        
        self.Centre( wx.BOTH )
        
       
        # Connect Events
        self.btnInsert.Bind( wx.EVT_BUTTON, self.onProcess )
        self.btnUpdate.Bind( wx.EVT_BUTTON, self.onProcess )
        self.btnConfirm.Bind( wx.EVT_BUTTON, self.onProcess )
        self.btnDel.Bind( wx.EVT_BUTTON, self.onProcess )
        self.btnInsert.id = 1
        self.btnUpdate.id = 2
        self.btnConfirm.id = 3
        self.btnDel.id = 4
        
        self.btnConfirm.Enable(enable=False) #못누름
        self.lstMem.InsertColumn(0, '번호', width=50)
        self.lstMem.InsertColumn(1, '이름', width=100)
        self.lstMem.InsertColumn(2, '전화', width=100)
    
        
        self.ViewListData()
        
    def ViewListData(self):
        try:
            conn = MySQLdb.connect(**config)
            cursor = conn.cursor()
            sql = "select * from pymem"
            cursor.execute(sql)
            
            self.lstMem.DeleteAllItems() # 표 초기화
            count = 0
            
            for data in cursor:
                i = self.lstMem.InsertItem(65535, 0) #65535 최대/ i값에 의해 행번호 결정 /동적
                self.lstMem.SetItem(i, 0, str(data[0])) #i = 행
                self.lstMem.SetItem(i, 1, str(data[1]))
                self.lstMem.SetItem(i, 2, str(data[2]))
                count += 1
                
            self.staCount.SetLabel(str(count))
        except Exception as e:
            wx.MessageBox('읽기에러 : ', e)    
        
        finally:
            conn.close()      
            
            
    def onProcess( self, event ):
        id = event.GetEventObject().id
        
        if id == 1:
            self.MemInsert()
        elif id == 2: #수정
            self.MemUpdate()
        elif id == 3: #수정확인
            self.MemUpdateOk()
        elif id == 4:
            self.MemDelete()
        elif id == 5:
            self.MemUpdateCancel()

    def MemInsert(self):
        no = self.txtNo.GetValue()
        name = self.txtName.GetValue()
        tel = self.txtTel.GetValue()
        
        if no == '' or name == '' or tel == '':
            wx.MessageBox('자료를 입력하세요', '에러', wx.OK)
            return
        
        try:
            conn = MySQLdb.connect(**config)
            cursor = conn.cursor()
            data = self.SelectData(no) #번호 중복 확인
            if data != None:
                wx.MessageBox('이미 사용 중인 번호입니다.', 'err', wx.OK)
                self.txtNo.SetFocus()
                return
                
            sql = "insert into pymem values(%s,%s,%s)"
            cursor.execute(sql, (no, name, tel))
            conn.commit()
            
            self.ViewListData() #등록후 자료 보기
            self.txtNo.SetValue('') #입력자료 초기화
            self.txtName.SetValue('')
            self.txtTel.SetValue('')
            
        except Exception as e:
            wx.MessageBox('MemInsert err: ', e, 'err', wx.OK)
            conn.rollback()
        finally:
            conn.close()    
        
    def MemUpdate(self):
        dlg = wx.TextEntryDialog(None, '수정할 번호 입력:', '수정')
        
        if dlg.ShowModal() == wx.ID_OK:
            if dlg.GetValue() == '':
                return
            
            upno = dlg.GetValue()
            data = self.SelectData(upno)
            
            if data == None:
                wx.MessageBox(upno + '번은 없습니다.', 'err', wx.OK)
                return
            
            self.txtNo.SetValue(str(data[0]))
            self.txtName.SetValue(str(data[1]))
            self.txtTel.SetValue(str(data[2]))
            
            self.txtNo.SetEditable(False)
            self.btnConfirm.Enable(True)
            self.btnUpdate.SetLabel('취소')
            self.btnUpdate.id = 5
        else:
            return   
            
            
        dlg.Destroy()
        
    def MemUpdateOk(self): #수정 확인
        no = self.txtNo.GetValue()
        name = self.txtName.GetValue()
        tel = self.txtTel.GetValue()
        
        if name == '' or tel == '':
            wx.MessageBox('수정자료를 입력하세요', '에러', wx.OK)
            return
        
        try:
            conn = MySQLdb.connect(**config)
            cursor = conn.cursor()
            
            sql = "update pymem set irum=%s, junhwa=%s where bun=%s"
            cursor.execute(sql, (name, tel, no))
            conn.commit()
            
            self.ViewListData() #등록후 자료 보기
            self.txtNo.SetValue('') #입력자료 초기화
            self.txtName.SetValue('')
            self.txtTel.SetValue('')
            
            self.txtNo.SetEditable(True)
            self.btnConfirm.Enable(False)
            self.btnUpdate.SetLabel('수정')
            self.btnUpdate.id = 2
            
        except Exception as e:
            wx.MessageBox('MemUpdateOk err: ', e, wx.OK)
            conn.rollback()
        finally:
            conn.close()    
        
    def MemDelete(self):
        dlg = wx.TextEntryDialog(None, '삭제할 번호 입력:', '삭제')
        
        if dlg.ShowModal() == wx.ID_OK:
            if dlg.GetValue() == '':
                return
            
            delno = dlg.GetValue()
            data = self.SelectData(delno)
            
            if data == None:
                wx.MessageBox(delno + '번은 없습니다.', 'err', wx.OK)
                return
            
            try:
                conn = MySQLdb.connect(**config)
                cursor = conn.cursor()
                sql = "delete from pymem where bun={}".format(delno)
                cursor.execute(sql)
                conn.commit()
                
                self.ViewListData() #등록후 자료 보기
            except Exception as e:
                wx.MessageBox('MemDelete err: ', e)
                conn.rollback()
            finally:
                conn.close()    
        else:
            return 
        
        dlg.Destroy()
    
    def MemUpdateCancel(self):
        self.txtNo.SetValue('') #입력자료 초기화
        self.txtName.SetValue('')
        self.txtTel.SetValue('')
        
        self.txtNo.SetEditable(True)
        self.btnConfirm.Enable(False)
        self.btnUpdate.SetLabel('수정')
        self.btnUpdate.id = 2

    def SelectData(self, no): #번호로 선택자료 읽기 - 등록, 수정. 삭제용 
        try:
            conn = MySQLdb.connect(**config)
            cursor = conn.cursor()
            sql = "select * from pymem where bun={}".format(no)
            cursor.execute(sql)
            data = cursor.fetchone()
            return data

        except Exception as e:
            wx.MessageBox('선택자료 에러: ', e)
        finally:
            conn.close()    
    
if __name__ == '__main__':
    app = wx.App()
    MyMember(None).Show()
    app.MainLoop()    




