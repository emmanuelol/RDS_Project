#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: Radio1
# Generated: Wed Mar 30 19:43:15 2016
##################################################

from gnuradio import eng_notation
from gnuradio import gr
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.wxgui import forms
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import wx

class Radio1(grc_wxgui.top_block_gui):

    def __init__(self):
        grc_wxgui.top_block_gui.__init__(self, title="Radio1")
        _icon_path = "/usr/share/icons/hicolor/32x32/apps/gnuradio-grc.png"
        self.SetIcon(wx.Icon(_icon_path, wx.BITMAP_TYPE_ANY))

        ##################################################
        # Variables
        ##################################################
        self.tv_stick_5 = tv_stick_5 = 2800000
        self.samp_rate = samp_rate = 44100
        self.f_rx = f_rx = 96600000

        ##################################################
        # Blocks
        ##################################################
        _f_rx_sizer = wx.BoxSizer(wx.VERTICAL)
        self._f_rx_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_f_rx_sizer,
        	value=self.f_rx,
        	callback=self.set_f_rx,
        	label="f_rx",
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._f_rx_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_f_rx_sizer,
        	value=self.f_rx,
        	callback=self.set_f_rx,
        	minimum=87000000,
        	maximum=108000000,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.GridAdd(_f_rx_sizer, 0, 0, 10, 20)


# QT sink close method reimplementation

    def get_tv_stick_5(self):
        return self.tv_stick_5

    def set_tv_stick_5(self, tv_stick_5):
        self.tv_stick_5 = tv_stick_5

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate

    def get_f_rx(self):
        return self.f_rx

    def set_f_rx(self, f_rx):
        self.f_rx = f_rx
        self._f_rx_slider.set_value(self.f_rx)
        self._f_rx_text_box.set_value(self.f_rx)

if __name__ == '__main__':
    import ctypes
    import os
    if os.name == 'posix':
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"
    parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
    (options, args) = parser.parse_args()
    tb = Radio1()
    tb.Start(False)
    tb.Wait()

