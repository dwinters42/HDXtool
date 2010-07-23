#!/usr/bin/env python
# -*- coding: utf-8 -*-
# generated by wxGlade 0.6.3 on Fri Jun 25 12:10:54 2010

# Copyright (c) 2010 Daniel Gruber <daniel@tydirium.org>
#
# Permission to use, copy, modify, and distribute this software for
# any purpose with or without fee is hereby granted, provided that the
# above copyright notice and this permission notice appear in all
# copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL
# WARRANTIES WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE
# AUTHOR BE LIABLE FOR ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL
# DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM LOSS OF USE, DATA
# OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR OTHER
# TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR
# PERFORMANCE OF THIS SOFTWARE.

import wx

# begin wxGlade: extracode
# end wxGlade

import os, pickle
from pylab import *


class MainFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        
        self.ids={'roi':wx.ID_HIGHEST+1,'pick':wx.ID_HIGHEST+2}

        # begin wxGlade: MainFrame.__init__
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.panel_1 = wx.Panel(self, -1)
        
        # Menu Bar
        self.frame_1_menubar = wx.MenuBar()
        wxglade_tmp_menu = wx.Menu()
        wxglade_tmp_menu.Append(wx.ID_OPEN, "Load", "", wx.ITEM_NORMAL)
        wxglade_tmp_menu.Append(wx.ID_SAVE, "Save", "", wx.ITEM_NORMAL)
        wxglade_tmp_menu.Append(wx.ID_EXIT, "Quit", "", wx.ITEM_NORMAL)
        self.frame_1_menubar.Append(wxglade_tmp_menu, "File")
        wxglade_tmp_menu = wx.Menu()
        wxglade_tmp_menu.Append(self.ids['roi'], "set ROI", "", wx.ITEM_NORMAL)
        self.frame_1_menubar.Append(wxglade_tmp_menu, "Fragment")
        wxglade_tmp_menu = wx.Menu()
        wxglade_tmp_menu.Append(wx.ID_ABOUT, "Info", "", wx.ITEM_NORMAL)
        self.frame_1_menubar.Append(wxglade_tmp_menu, "About")
        self.SetMenuBar(self.frame_1_menubar)
        # Menu Bar end
        self.frame_1_statusbar = self.CreateStatusBar(1, 0)
        
        # Tool Bar
        self.frame_1_toolbar = wx.ToolBar(self, -1, style=wx.TB_HORIZONTAL|wx.TB_TEXT)
        self.SetToolBar(self.frame_1_toolbar)
        self.frame_1_toolbar.AddLabelTool(wx.ID_OPEN, "Load", (wx.ArtProvider.GetBitmap(wx.ART_FILE_OPEN, wx.ART_TOOLBAR)), wx.NullBitmap, wx.ITEM_NORMAL, "", "")
        self.frame_1_toolbar.AddLabelTool(wx.ID_SAVE, "Save", (wx.ArtProvider.GetBitmap(wx.ART_FILE_SAVE, wx.ART_TOOLBAR)), wx.NullBitmap, wx.ITEM_NORMAL, "", "")
        self.frame_1_toolbar.AddLabelTool(self.ids['roi'], "ROI", (wx.ArtProvider.GetBitmap(wx.ART_GO_FORWARD, wx.ART_TOOLBAR)), wx.NullBitmap, wx.ITEM_NORMAL, "", "")
        self.frame_1_toolbar.AddLabelTool(self.ids['pick'], "Pick Peaks", (wx.ArtProvider.GetBitmap(wx.ART_TICK_MARK, wx.ART_TOOLBAR)), wx.NullBitmap, wx.ITEM_NORMAL, "", "")
        # Tool Bar end
        self.textCtrlData = wx.TextCtrl(self.panel_1, -1, "", style=wx.TE_MULTILINE)

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_MENU, self.loadData, id=wx.ID_OPEN)
        self.Bind(wx.EVT_MENU, self.saveData, id=wx.ID_SAVE)
        self.Bind(wx.EVT_MENU, self.onExit, id=wx.ID_EXIT)
        self.Bind(wx.EVT_MENU, self.setROI, id=self.ids['roi'])
        self.Bind(wx.EVT_MENU, self.printInfo, id=wx.ID_ABOUT)
        self.Bind(wx.EVT_TOOL, self.loadData, id=wx.ID_OPEN)
        self.Bind(wx.EVT_TOOL, self.saveData, id=wx.ID_SAVE)
        self.Bind(wx.EVT_TOOL, self.setROI, id=self.ids['roi'])
        self.Bind(wx.EVT_TOOL, self.pickPeaks, id=self.ids['pick'])
        # end wxGlade
        
        self.dfile=''
        self.paramfile=''
        self.xdata=None
        self.ydata=None

        # ROI stuff
        self.low=None
        self.high=None
        self.thres=None
        self.hl1=None

        # peak stuff
        self.peaks=[]

    def __set_properties(self):
        # begin wxGlade: MainFrame.__set_properties
        self.SetTitle("HDXtool")
        self.frame_1_statusbar.SetStatusWidths([-1])
        # statusbar fields
        frame_1_statusbar_fields = ["Ready"]
        for i in range(len(frame_1_statusbar_fields)):
            self.frame_1_statusbar.SetStatusText(frame_1_statusbar_fields[i], i)
        self.frame_1_toolbar.Realize()
        self.textCtrlData.SetMinSize((278, 365))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: MainFrame.__do_layout
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        sizer_2 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_2.Add(self.textCtrlData, 1, wx.ALL|wx.EXPAND, 5)
        self.panel_1.SetSizer(sizer_2)
        sizer_1.Add(self.panel_1, 1, wx.EXPAND, 0)
        self.SetSizer(sizer_1)
        sizer_1.Fit(self)
        self.Layout()
        # end wxGlade

    def loadData(self, event): # wxGlade: MainFrame.<event_handler>
        dlg=wx.FileDialog(self)
        if dlg.ShowModal() == wx.ID_OK:
            # load data file, plot data
            self.textCtrlData.Clear()
            self.dfile=dlg.GetPath()
            d=loadtxt(self.dfile)
            self.xdata=d[:,0]
            self.ydata=d[:,1]
            figure(1)
            clf();
            plot(self.xdata,self.ydata)
            show()
            draw()

            # load the file with the parameters
            self.paramfile=os.path.splitext(self.dfile)[0]+"_params.txt"

            if os.access(self.paramfile, os.R_OK | os.W_OK):
                self.textCtrlData.LoadFile(self.paramfile)
                for ii in range(0,self.textCtrlData.GetNumberOfLines()):
                    dline=self.textCtrlData.GetLineText(ii)
                    if len(dline) == 0 or dline[0] == '#':
                        pass
                    else:
                        fields=dline.split(',')
                        axvspan(float(fields[0]),float(fields[1]),\
                                    alpha=0.1,color='k')
                    
                draw()
            else:
                self.textCtrlData.AppendText('# HDXtool parameter file\n')
                self.textCtrlData.AppendText(\
                    '# Columns: low, high, threshold, centroid\n')

            # get the selected peaks from _peaks.dat file
            self.peakfile=os.path.splitext(self.dfile)[0]+"_peaks.dat"
            if os.access(self.peakfile, os.R_OK):
                self.peaks=[]
                df=file(self.peakfile,'rb')
                try:
                    self.peaks=pickle.load(df)
                except:
                    wx.MessageBox(\
                        "Cannot read peak data file!","Warning", wx.OK)
                df.close()

                for ii in range(len(self.peaks)):
                    plot(self.peaks[ii][:,0],self.peaks[ii][:,1],'ro')

                draw()

   
    def setROI(self, event): # wxGlade: MainFrame.<event_handler>
        if self.dfile == '':
            dlg=wx.MessageBox('No data loaded!','Error', wx.ID_OK)
            return

        if self.hl1 is not None:
            self.hl1.remove()
            self.hl4.remove()
            draw()

        # pick threshold and left and right limit
        pos=ginput(1)
        self.thres=pos[0][1]
        self.hl1=axhline(y=self.thres,color='r')
        draw()

        pos=ginput(1)
        self.low=pos[0][0]
        self.hl2=axvline(x=self.low,color='g')
        draw()

        pos=ginput(1)
        self.high=pos[0][0]
        self.hl3=axvline(x=self.high,color='g')
        draw()

        # copy only the data in the region of interest
        self.x=take(self.xdata,find((self.xdata>self.low)&(self.xdata<self.high)))
        self.y=take(self.ydata,find((self.xdata>self.low)&(self.xdata<self.high)))

        # threshold
        self.yth=zeros(len(self.y))
        for ii in range(0,len(self.y)):
            if self.y[ii]<self.thres:
                self.yth[ii]=0
            else:
                self.yth[ii]=self.y[ii]

    def pickPeaks(self, event): # wxGlade: MainFrame.<event_handler>
        # let the user select two peaks
        (x1,y1)=self._pickpeak(self.x,self.yth)
        (x2,y2)=self._pickpeak(self.x,self.yth)
        meandist=(max(x1,x2)-min(x1,x2))
        delta=meandist*0.01

        # start from startpeak, go to the right until self.high and mark
        # peaks, then do the same to the left
        peakvalx=[x1]
        peakvaly=[y1]
        means=[meandist]
        p=x1+meandist
        pold=x1

        while p<self.high:
            (localmaxpos,localmax)=self._localpeak((p,0),self.x,self.yth,delta)
            print(localmaxpos,localmax)
            if localmax>0:
                tmp=axis()
                plot(localmaxpos,localmax,'go')
                axis(tmp)
                peakvalx.append(localmaxpos)
                peakvaly.append(localmax)
                means.append(abs(localmaxpos-pold))
            pold=p
            p=p+(sum(means)/len(means))

        p=x1-meandist
        pold=x1
        while p>self.low:
            (localmaxpos,localmax)=self._localpeak((p,0),self.x,self.yth,delta)
            if localmax>0:
                tmp=axis()
                plot(localmaxpos,localmax,'go')
                axis(tmp)
                peakvalx.append(localmaxpos)
                peakvaly.append(localmax)
                means.append(abs(localmaxpos-pold))
            pold=p
            p=p-(sum(means)/len(means))

        peaks=zeros((len(peakvalx),2))
        peaks[:,0]=peakvalx
        peaks[:,1]=peakvaly

        # # calculate centroid
        # c=0
        # for ii in range(0,len(y)):
        #     c=c+x[ii]*self.yth[ii]

        # c=c/yth.sum()
        # self.textCtrlData.AppendText(\
        #     "%.2f, %.2f, %.2e, %.2f\n" % \
        #         (self.low,self.high,self.thres,c))
        # self.textCtrlData.MarkDirty()
        # self.hl2.remove()
        # self.hl3.remove()
        # self.hl4=axvline(x=c,color='c')
        # tmp=axis()
        # axvspan(low,high,alpha=0.1,color='k')
        # axis(tmp)
        # draw()



    def saveData(self, event): # wxGlade: MainFrame.<event_handler>
        if self.dfile == '':
            dlg=wx.MessageBox('No data loaded!','Error', wx.ID_OK)
            return

        if os.access(self.paramfile,os.R_OK | os.W_OK):
            if wx.MessageBox(\
                "Data files exist, overwrite?","Overwrite", \
                    wx.YES_NO) == wx.NO:
                return
        
        self.textCtrlData.SaveFile(self.paramfile)        
        df=file(self.peakfile,'wb')
        pickle.dump(self.peaks,df)
        df.close()
        
    def onExit(self, event): # wxGlade: MainFrame.<event_handler>
        if self.textCtrlData.IsModified():
            if wx.MessageBox(\
                "Parameters have changed, save?","Save", wx.YES_NO) == wx.YES:
                self.textCtrlData.SaveFile(self.paramfile)

        close()
        self.Destroy()

    def printInfo(self, event): # wxGlade: MainFrame.<event_handler>
        info=wx.AboutDialogInfo()
        info.SetName("HDXtool")
        info.SetDescription("HDX for Clint")
        info.SetCopyright("(c) 2010 Daniel Gruber")
        info.AddDeveloper("Daniel Gruber <daniel@tydirium.org>")
        wx.AboutBox(info)

    def _pickpeak(self,x,y):
        ii=axis()
        # XXX this is a bit dodgy
        delta=(ii[1]-ii[0])/200.0
        pos=ginput(1)
        pos=pos[0]
        (localmaxpos,localmax)=self._localpeak(pos,x,y,delta)

        tmp=axis()
        plot(localmaxpos,localmax,'go')
        axis(tmp)
        return (localmaxpos,localmax)

    def _localpeak(self,pos,x,y,delta):
        localx=take(x,find((x>(pos[0]-delta))&(x<(pos[0]+delta))))
        localy=take(y,find((x>(pos[0]-delta))&(x<(pos[0]+delta))))
    
        localmax=localy.max()
        localmaxpos=take(localx,find(localy==localy.max()))[0]
        
        return (localmaxpos,localmax)

# end of class MainFrame

class MyApp(wx.App):
    def OnInit(self):
        wx.InitAllImageHandlers()
        frame_1 = MainFrame(None, -1, "")
        self.SetTopWindow(frame_1)
        frame_1.Show()
        return 1

# end of class MyApp

if __name__ == "__main__":
    app = MyApp(0)
    app.MainLoop()
