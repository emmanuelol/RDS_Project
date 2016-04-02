#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: fmReceiver2
# Generated: Sat Apr  2 14:08:58 2016
##################################################

from gnuradio import analog
from gnuradio import audio
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import wxgui
from gnuradio.eng_option import eng_option
from gnuradio.fft import window
from gnuradio.filter import firdes
from gnuradio.wxgui import forms
from gnuradio.wxgui import waterfallsink2
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import osmosdr
import wx

class fmReceiver2(grc_wxgui.top_block_gui):

    def __init__(self):
        grc_wxgui.top_block_gui.__init__(self, title="fmReceiver2")
        _icon_path = "/usr/share/icons/hicolor/32x32/apps/gnuradio-grc.png"
        self.SetIcon(wx.Icon(_icon_path, wx.BITMAP_TYPE_ANY))

        ##################################################
        # Variables
        ##################################################
        self.samp_rep = samp_rep = 44.1e3
        self.samp_rate = samp_rate = 2e6
        self.freq = freq = 99.3e6

        ##################################################
        # Blocks
        ##################################################
        _freq_sizer = wx.BoxSizer(wx.VERTICAL)
        self._freq_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_freq_sizer,
        	value=self.freq,
        	callback=self.set_freq,
        	label="freq",
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._freq_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_freq_sizer,
        	value=self.freq,
        	callback=self.set_freq,
        	minimum=87e6,
        	maximum=108e6,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_freq_sizer)
        self.wxgui_waterfallsink2_0 = waterfallsink2.waterfall_sink_f(
        	self.GetWin(),
        	baseband_freq=0,
        	dynamic_range=100,
        	ref_level=0,
        	ref_scale=2.0,
        	sample_rate=samp_rate,
        	fft_size=512,
        	fft_rate=15,
        	average=False,
        	avg_alpha=None,
        	title="Waterfall Plot",
        )
        self.Add(self.wxgui_waterfallsink2_0.win)
        self.rtlsdr_source_0 = osmosdr.source( args="numchan=" + str(1) + " " + "" )
        self.rtlsdr_source_0.set_sample_rate(samp_rate)
        self.rtlsdr_source_0.set_center_freq(freq, 0)
        self.rtlsdr_source_0.set_freq_corr(0, 0)
        self.rtlsdr_source_0.set_dc_offset_mode(0, 0)
        self.rtlsdr_source_0.set_iq_balance_mode(0, 0)
        self.rtlsdr_source_0.set_gain_mode(0, 0)
        self.rtlsdr_source_0.set_gain(10, 0)
        self.rtlsdr_source_0.set_if_gain(20, 0)
        self.rtlsdr_source_0.set_bb_gain(20, 0)
        self.rtlsdr_source_0.set_antenna("", 0)
        self.rtlsdr_source_0.set_bandwidth(0, 0)
          
        self.low_pass_filter_0 = filter.fir_filter_ccf(1, firdes.low_pass(
        	1, samp_rate, 75e3, 150e3, firdes.WIN_HAMMING, 6.76))
        self.fractional_interpolator_xx_1 = filter.fractional_interpolator_ff(0, 4)
        self.fractional_interpolator_xx_0 = filter.fractional_interpolator_cc(0, 3.968)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vff((4, ))
        self.audio_sink_0 = audio.sink(44100, "", True)
        self.analog_wfm_rcv_0 = analog.wfm_rcv(
        	quad_rate=5e5,
        	audio_decimation=4,
        )
        self.analog_fm_deemph_0 = analog.fm_deemph(fs=samp_rep, tau=50e-6)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.rtlsdr_source_0, 0), (self.low_pass_filter_0, 0))
        self.connect((self.low_pass_filter_0, 0), (self.fractional_interpolator_xx_0, 0))
        self.connect((self.fractional_interpolator_xx_0, 0), (self.analog_wfm_rcv_0, 0))
        self.connect((self.analog_wfm_rcv_0, 0), (self.fractional_interpolator_xx_1, 0))
        self.connect((self.fractional_interpolator_xx_1, 0), (self.analog_fm_deemph_0, 0))
        self.connect((self.analog_fm_deemph_0, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.audio_sink_0, 0))
        self.connect((self.analog_wfm_rcv_0, 0), (self.wxgui_waterfallsink2_0, 0))


# QT sink close method reimplementation

    def get_samp_rep(self):
        return self.samp_rep

    def set_samp_rep(self, samp_rep):
        self.samp_rep = samp_rep

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate, 75e3, 150e3, firdes.WIN_HAMMING, 6.76))
        self.wxgui_waterfallsink2_0.set_sample_rate(self.samp_rate)
        self.rtlsdr_source_0.set_sample_rate(self.samp_rate)

    def get_freq(self):
        return self.freq

    def set_freq(self, freq):
        self.freq = freq
        self._freq_slider.set_value(self.freq)
        self._freq_text_box.set_value(self.freq)
        self.rtlsdr_source_0.set_center_freq(self.freq, 0)

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
    tb = fmReceiver2()
    tb.Start(True)
    tb.Wait()

