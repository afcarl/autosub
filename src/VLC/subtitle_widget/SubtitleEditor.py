# -*- coding: utf-8 -*- 
# # import wx
# # class MyFrame(wx.Frame):
# # 	"""docstring for MyFrame"""
# # 	def __init__(self):
# # 		wx.Frame.__init__(self,None,-1,"My Frame", size=(300,300))
# # 		panel=wx.Panel(self,-1)
# # 		panel.Bind(wx.EVT_MOTION,self.OnMove)
# # 		wx.StaticText(panel,-1,"Pos:",pos=(10,12))
# # 		self.posCtrl=wx.TextCtrl(panel,-1,"",pos=(40,10))
# # 	def OnMove():
# # 			pos=event.GetPosition()
# # 			self.posCtrl.SetValue("%s, %s" % (pos.x,pos.y))

# # if __name__=='__main__' :
# # 	app=wx.PySimpleApp()
# # 	frame=MyFrame()
# # 	frame.Show(True)
# # 	app.MainLoop()
# # ss=raw_input();
# import 	wx
# import 	wx.grid 
# # import 	wx.py.images as images
# # class Frame(wx.Frame):
# # 	def __init__(self,image,parent=None,id=-1,
# # 			pos=wx.DefaultPosition,
# # 			title='Hello, wxPython!'):
# # 		temp=image.ConvertToBitmap()
# # 		size=temp.GetWidth(),temp.GetHeight();
# # 		wx.Frame.__init__(self,parent,id,title,pos,size)
# # 		self.bmp=wx.StaticBitmap(parent=self,bitmap=temp)





# # class App(wx.App):
# # 	"""doc string for  nothing"""
# # 	def OnInit(self):
# # 		image=wx.Image('C:\\Users\\v-liason\\Pictures\\Alienware\\AW1.jpg',wx.BITMAP_TYPE_JPEG)
# # 		self.frame=Frame(image)
# # 		self.frame.Show()
# # 		self.SetTopWindow(self.frame)
# # 		return True

# class ToolBarFrame(wx.Frame):
# 	"""docstring for ToolBarFrame"""
# 	def __init__(self):
# 		wx.Frame.__init__(self,None,id,title='Toolbars',
# 				size=(600,300))
# 		# self.Center()

# 		#grid 

# 		grid=wx.grid.Grid(self);
#         grid.CreateGrid(5,5);
#         for row in range(20):
#             for col in range(6):
#                 grid.SetCellValue(row, col,
#                 	"cell (%d,%d)" % (row, col))
# 		panel=wx.Panel(self)
# 		panel.SetBackgroundColour('White')
# 		statusbar=self.CreateStatusBar()
# 		toolbar=self.CreateToolBar()
# 		# toolbar.AddSimpleTool(wx.NewId(),images.getPyBitmap(),
# 		# 		"New","Long help for 'New'")
# 		toolbar.Realize()
# 		menuBar = wx.MenuBar()
# 		menu1=wx.Menu()
# 		menu1.Append(wx.NewId(),u"新字幕",u"新建一个字幕")
# 		menu1.Append(wx.NewId(),u"打开字幕",u"打开一个字幕")
# 		menu1.Append(wx.NewId(),u"保存字幕",u"保存一个字幕")
# 		menuBar.Append(menu1,u"文件")
# 		menu2=wx.Menu()
# 		menu2.Append(wx.NewId()," ","Copy in status bar")
# 		menu2.Append(wx.NewId(),"C ","")
# 		menu2.Append(wx.NewId(),"Paste","")
# 		menu2.AppendSeparator()
# 		menu2.Append(wx.NewId()," ","Display Options")
# 		menuBar.Append(menu2, u"编辑")
# 		self.SetMenuBar(menuBar)
	   

# def main():
# 	app=App()
# 	app.MainLoop()

# def PopaSingleChoiceDialog():
# 	dlg=wx.SingleChoiceDialog(None,'Which version of Python are you using?',
# 					'Single Choice',['1.0','2.2','2.7','3.2'])
# 	if(dlg.ShowModal()==mx.ID_OK):
# 		response=dlg.GetStringSelection()

# if __name__=='__main__':
# 	app=wx.PySimpleApp()
# 	frame=ToolBarFrame()
# 	frame.Show()
# 	app.MainLoop()
# -*- coding: utf-8 -*-

# absolute.py

import wx
import os
import wx.lib.platebtn as pbtn
from subtitleparser import *
from SubtitleUI import TestFrame
class Subtitle(wx.Panel):
	colLabels = ["homer", "marge", "bart", "lisa", "maggie"]
	def __init__(self, parent, id):
		wx.Panel.__init__(self, parent, id, 
			size=(400, 300))
		self.sizer=self.InitUI()
	def InitUI(self):		
		ctrlbar=wx.BoxSizer(wx.HORIZONTAL); 
		save  = pbtn.PlateButton(self, label="Save",pos=(10,10))
		add   = pbtn.PlateButton(self, label="Add",pos=(50,10))


		# ctrlbar = wx.BoxSizer(wx.VERTICAL)
		ctrlbox = wx.BoxSizer(wx.VERTICAL)
		# box1 = wx.BoxSizer(wx.HORIZONTAL)
		# box2 = wx.BoxSizer(wx.HORIZONTAL)
		box3 = wx.BoxSizer(wx.HORIZONTAL)
		# box4 = wx.BoxSizer(wx.HORIZONTAL)
		# box5 = wx.BoxSizer(wx.HORIZONTAL)
		# box1 contains the timeslider
	 
		# box1.Add(self.timeslider,1)
		# # box2 contains the bufferslider
		# box2.Add(self.buffergauge,1)
		# box3 contains some buttons and the volume controls
		box3.Add(save, flag=wx.RIGHT, border=5)
		box3.Add(add,flag=wx.RIGHT,border=5)
		box3.Add((-1, -1), 1)
		self.Bind(wx.EVT_BUTTON, self.SaveItem, save)
		self.Bind(wx.EVT_BUTTON, self.Additem, add)
		# box3.Add(stop,flag=wx.RIGHT,border=5)
		# box3.Add((-1, -1), 1)
		# box3.Add(fullscreen,flag=wx.RIGHT,border=5)
		# box3.Add(volume,flag=wx.RIGHT,border=5)
		# box3.Add(self.volslider, flag=wx.TOP | wx.LEFT, border=5)

		# # box4 contains the playtime
		# box4.Add(self.displaytime,1)
		# # box5 contains the buffertime
		# box5.Add(self.buffertime, 1)

		
		# Merge box to the ctrlsizer
		# ctrlbox.Add(box4, flag=wx.EXPAND | wx.BOTTOM, border=0)
		# ctrlbox.Add(box1, flag=wx.EXPAND | wx.BOTTOM, border=0)
		# ctrlbox.Add(box5, flag=wx.EXPAND | wx.BOTTOM, border=0)
		# ctrlbox.Add(box2, flag=wx.EXPAND | wx.BOTTOM, border=5)

		
		self.begintext=wx.StaticText(self,-1,"Start time",(33,43));
		self.endtext=wx.StaticText(self,-1,"End time",(183,43));
		# ctrlbar.Add(save, flag=wx.RIGHT, border=5)
		# ctrlbar.Add(add,flag=wx.RIGHT,border=5)
		# # ctrlbar.Add(stop,flag=wx.LEFT,border=5)
		# ctrlbox=wx.BoxSizer(wx.VERTICAL);
		# ctrlbox.Add(ctrlbar,1,wx.EXPAND)
		# ctrlpanel.SetSizer(ctrlbox)

		# right=wx.BoxSizer(wx.VERTICAL)
		# timerow=wx.BoxSizer(wx.HORIZONTAL)
		# titlerow=wx.BoxSizer(wx.HORIZONTAL)
		# subrow=wx.BoxSizer(wx.HORIZONTAL)

		# right.Add(ctrlpanel,flag=wx.EXPAND | wx.BOTTOM | wx.TOP,border=10)
		# right.Add(timerow,flag=wx.EXPAND);
		# right.Add(titlerow,flag=wx.EXPAND);
		# right.Add(subrow,flag=wx.EXPAND);
		
		# panel.SetSizer(right);
		self.text=wx.StaticText(self,-1,"Content",(170,60))
		

		self.TextCtrl=wx.TextCtrl(self, pos=(3, 80), size=(350, 50))
		self.num=wx.TextCtrl(self,pos=(3,43),size=(28,20))
		self.begintime=wx.TextCtrl(self,pos=(80,43),size=(100,20))
		self.endtime=wx.TextCtrl(self,pos=(230,43),size=(100,20))

		samplelist=['1 00:00','2 00:01'];
		self.listBox=wx.ListBox(self,-1,(3,140),(350,100),samplelist,wx.LB_SINGLE)
		self.listBox.SetSelection(1)

		# menubar = wx.MenuBar()
		# filem = wx.Menu()
		# editm = wx.Menu()
		# helpm = wx.Menu()
		# menubar.Append(filem, '&File')
		# menubar.Append(editm, '&Edit')
		# menubar.Append(helpm, '&Help')
		# openb=filem.Append(wx.NewId(),u"Open","Open a File")
		# saveb=filem.Append(wx.NewId(),"Save","Save a File")
		# saveitemb=editm.Append(wx.NewId(),"save subtitle","save");
		# additemb=editm.Append(wx.NewId(),"add subtitle","add");

		# self.Bind(wx.EVT_MENU, self.Additem, additemb)
		# self.Bind(wx.EVT_MENU, self.SaveItem, saveitemb)
		# self.Bind(wx.EVT_MENU, self.OpenFile, openb)
		# self.Bind(wx.EVT_MENU, self.SaveFile, saveb)
		self.Bind(wx.EVT_LISTBOX_DCLICK,self.ChooseOneItem,self.listBox);
		# self.SetMenuBar(menubar)
		# statusbar=self.CreateStatusBar()

		ctrlbox.Add(box3, 1, wx.EXPAND)
		
		# Put everything togheter
		self.sizer = wx.BoxSizer(wx.VERTICAL)

		self.BigSizer = wx.BoxSizer(wx.HORIZONTAL)

		# sizer.Add(self.videopanel, 1, flag=wx.EXPAND)
		self.sizer.Add(ctrlbox, flag=wx.EXPAND | wx.BOTTOM | wx.TOP, border=0)
		# self.sizer.Add(subpanel, flag=wx.EXPAND | wx.BOTTOM | wx.TOP, border=0)


		####################################CUTTING LINE######################################

		self.BigSizer.Add(self.sizer,flag=wx.EXPAND)
		self.SetSizer(self.BigSizer)
		# return self.BigSizer
		# hbox.Add(frid, proportion=1, flag=wx.ALL|wx.EXPAND, border=15)

	def ChooseOneItem(self,event):
		index=self.listBox.GetSelection()
		content=self.listBox.GetString(index)
		tmp=content.split(' ')

		self.num.SetValue(tmp[0])
		if(len(tmp)>1):
			self.begintime.SetValue(tmp[1])
		if(len(tmp)>3):
			self.endtime.SetValue(tmp[3])
		ct=0
		subti=""
		for i in tmp:
			if(ct>3):
				subti=subti+' '+i;
			ct=ct+1;
		# print type(subti);
		self.TextCtrl.SetValue(subti)
	def SaveFile(self,event):
		file_wildcard="All files(*.*)|*.*"
		dlg=wx.FileDialog(self,"Save subtitles",
						os.getcwd(),style=wx.SAVE,wildcard=file_wildcard)
		if(dlg.ShowModal()==wx.ID_OK):
			self.filename=dlg.GetPath()
		myfile=self.filename;
		f=open(myfile,"w");
		num=self.listBox.GetCount()

		for i in range(0,num):
			tmp=self.listBox.GetString(i);
			item=tmp.split(' ');
			f.write(item[0]+'\n');
			if(len(item)>3):
				f.write(item[1]+' '+item[2]+' '+item[3]+'\n')
			ct=0
			subti=""
			for i in item:
				if(ct>4):
					subti=subti+' '+i;
				ct=ct+1;
			csub=(subti)
			# print subti;
			# print csub
			# print type(subti)
			f.write(csub+'\n'+'\n');
		f.close()
	def SaveItem(self,event):
		num=self.num.GetValue();
		time=self.begintime.GetValue()+' --> '+self.endtime.GetValue()
		text=self.TextCtrl.GetValue();
		res=num+' '+time+' '+text;
		num=self.listBox.GetSelection()	
		self.listBox.SetString(num,res)

	def Additem(self,event):
		num=self.num.GetValue();
		time=self.begintime.GetValue()+' --> '+self.endtime.GetValue()
		text=self.TextCtrl.GetValue();
		res=num+' '+time+' '+text;
		num=self.listBox.GetSelection()	
		ans=[];
		ans.append(res);	
		self.listBox.InsertItems(ans,num)
			
	def OpenFile(self,event):
		file_wildcard = "All files(*.*)|*.*"
		dlg = wx.FileDialog(self, "Open subtitle file...",
							os.getcwd(), 
							style = wx.OPEN,
							wildcard = file_wildcard)
		if(dlg.ShowModal() == wx.ID_OK):
			self.filename=dlg.GetPath()
		# print unicode.__doc__
		else :
			return;
		foot=self.filename

		if(foot[len(foot)-1] == 't' ):
			li=SrtParser(foot)
		elif (foot[len(foot)-1]== 's'):
			li=AssParser(foot);
		self.listBox.Clear()
		for i in li:
			srt=str(i[0])+' '+i[1]+' --> '+i[2]+' '+i[3];
			ad=srt.decode('utf-8','ignore');
			self.listBox.Append(ad);
			# print ad;



class Example(wx.Frame):
		   
	def __init__(self, *args, **kw):
		super(Example, self).__init__(*args, **kw) 
		
		self.InitUI()
		
	def InitUI(self):    

		panel = wx.Panel(self)
		lnk = Subtitle(panel, -1)
		# motto.SetFont(wx.Font(9, wx.SWISS, wx.NORMAL, wx.BOLD, False, 'Verdana'))

		self.SetSize((400, 400))
		self.Centre()
		self.Show(True)


if __name__ == '__main__':
	app = wx.App(redirect=False)
	Example(None);
	app.MainLoop()
