#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: PlayFile
# Generated: Wed Mar 30 20:27:13 2016
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
from gnuradio.wxgui import fftsink2
from gnuradio.wxgui import forms
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import wx

class PlayFileTest(grc_wxgui.top_block_gui):

    def __init__(self):
        grc_wxgui.top_block_gui.__init__(self, title="PlayFile")
        _icon_path = "/usr/share/icons/hicolor/32x32/apps/gnuradio-grc.png"
        self.SetIcon(wx.Icon(_icon_path, wx.BITMAP_TYPE_ANY))

        ##################################################
        # Variables
        ##################################################
        self.trans = trans = 40
        self.samp_rate = samp_rate = 250000
        self.cutoff = cutoff = 30
        self.xlate_filter_taps = xlate_filter_taps = firdes.low_pass(1, samp_rate, cutoff*1000, trans*1000, firdes.WIN_HAMMING, 6.76)
        self.usrp_freq = usrp_freq = 105310000
        self.rx_freq = rx_freq = 105310000
        self.rf_gain = rf_gain = 25
        self.offset_fine = offset_fine = 0
        self.offset_coarse = offset_coarse = -45000
        self.af_gain = af_gain = 4

        ##################################################
        # Blocks
        ##################################################
        self._usrp_freq_text_box = forms.text_box(
        	parent=self.GetWin(),
        	value=self.usrp_freq,
        	callback=self.set_usrp_freq,
        	label="USRP",
        	converter=forms.float_converter(),
        )
        self.GridAdd(self._usrp_freq_text_box, 5, 1, 1, 1)
        _trans_sizer = wx.BoxSizer(wx.VERTICAL)
        self._trans_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_trans_sizer,
        	value=self.trans,
        	callback=self.set_trans,
        	label="Filter trans(kHz)",
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._trans_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_trans_sizer,
        	value=self.trans,
        	callback=self.set_trans,
        	minimum=20,
        	maximum=60,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.GridAdd(_trans_sizer, 8, 0, 1, 1)
        self._rx_freq_static_text = forms.static_text(
        	parent=self.GetWin(),
        	value=self.rx_freq,
        	callback=self.set_rx_freq,
        	label="Receive",
        	converter=forms.float_converter(),
        )
        self.Add(self._rx_freq_static_text)
        _rf_gain_sizer = wx.BoxSizer(wx.VERTICAL)
        self._rf_gain_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_rf_gain_sizer,
        	value=self.rf_gain,
        	callback=self.set_rf_gain,
        	label="RF",
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._rf_gain_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_rf_gain_sizer,
        	value=self.rf_gain,
        	callback=self.set_rf_gain,
        	minimum=0,
        	maximum=50,
        	num_steps=50,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.GridAdd(_rf_gain_sizer, 7, 1, 1, 1)
        self.rational_resampler_xxx_0 = filter.rational_resampler_fff(
                interpolation=441,
                decimation=500,
                taps=None,
                fractional_bw=None,
        )
        _offset_fine_sizer = wx.BoxSizer(wx.VERTICAL)
        self._offset_fine_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_offset_fine_sizer,
        	value=self.offset_fine,
        	callback=self.set_offset_fine,
        	label="Fine tune",
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._offset_fine_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_offset_fine_sizer,
        	value=self.offset_fine,
        	callback=self.set_offset_fine,
        	minimum=-1000,
        	maximum=1000,
        	num_steps=400,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.GridAdd(_offset_fine_sizer, 6, 0, 1, 2)
        _offset_coarse_sizer = wx.BoxSizer(wx.VERTICAL)
        self._offset_coarse_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_offset_coarse_sizer,
        	value=self.offset_coarse,
        	callback=self.set_offset_coarse,
        	label="Coarse tune",
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._offset_coarse_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_offset_coarse_sizer,
        	value=self.offset_coarse,
        	callback=self.set_offset_coarse,
        	minimum=-120000,
        	maximum=120000,
        	num_steps=960,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.GridAdd(_offset_coarse_sizer, 6, 2, 1, 2)
        self.freq_xlating_fir_filter_xxx_0 = filter.freq_xlating_fir_filter_ccc(1, (xlate_filter_taps), -50000, samp_rate)
        self.fftsink = fftsink2.fft_sink_c(
        	self.GetWin(),
        	baseband_freq=usrp_freq,
        	y_per_div=10,
        	y_divs=10,
        	ref_level=0,
        	ref_scale=13490.0,
        	sample_rate=samp_rate,
        	fft_size=512,
        	fft_rate=15,
        	average=True,
        	avg_alpha=0.5,
        	title="",
        	peak_hold=False,
        	win=window.hamming,
        	size=(800,300),
        )
        self.GridAdd(self.fftsink.win, 0, 0, 5, 4)
        _cutoff_sizer = wx.BoxSizer(wx.VERTICAL)
        self._cutoff_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_cutoff_sizer,
        	value=self.cutoff,
        	callback=self.set_cutoff,
        	label="Filter cutoff (kHz)",
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._cutoff_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_cutoff_sizer,
        	value=self.cutoff,
        	callback=self.set_cutoff,
        	minimum=20,
        	maximum=60,
        	num_steps=800,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.GridAdd(_cutoff_sizer, 7, 0, 1, 1)
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vff((1.5, ))
        self.blocks_file_source_0 = blocks.file_source(gr.sizeof_gr_complex*1, "/home/emmanuel/Documentos/RDSProject/RDS_Project/Code MATLAB/wfm1053_10s.dat", False)
        self.audio_sink_0 = audio.sink(44100, "", True)
        self.analog_wfm_rcv_0 = analog.wfm_rcv(
        	quad_rate=250000,
        	audio_decimation=5,
        )
        _af_gain_sizer = wx.BoxSizer(wx.VERTICAL)
        self._af_gain_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_af_gain_sizer,
        	value=self.af_gain,
        	callback=self.set_af_gain,
        	label="VOL",
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._af_gain_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_af_gain_sizer,
        	value=self.af_gain,
        	callback=self.set_af_gain,
        	minimum=0,
        	maximum=5,
        	num_steps=500,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.GridAdd(_af_gain_sizer, 8, 1, 1, 1)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_file_source_0, 0), (self.blocks_throttle_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.fftsink, 0))
        self.connect((self.blocks_throttle_0, 0), (self.freq_xlating_fir_filter_xxx_0, 0))
        self.connect((self.freq_xlating_fir_filter_xxx_0, 0), (self.analog_wfm_rcv_0, 0))
        self.connect((self.analog_wfm_rcv_0, 0), (self.rational_resampler_xxx_0, 0))
        self.connect((self.rational_resampler_xxx_0, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.audio_sink_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.audio_sink_0, 1))


# QT sink close method reimplementation

    def get_trans(self):
        return self.trans

    def set_trans(self, trans):
        self.trans = trans
        self.set_xlate_filter_taps(firdes.low_pass(1, self.samp_rate, self.cutoff*1000, self.trans*1000, firdes.WIN_HAMMING, 6.76))
        self._trans_slider.set_value(self.trans)
        self._trans_text_box.set_value(self.trans)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.set_xlate_filter_taps(firdes.low_pass(1, self.samp_rate, self.cutoff*1000, self.trans*1000, firdes.WIN_HAMMING, 6.76))
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)
        self.fftsink.set_sample_rate(self.samp_rate)

    def get_cutoff(self):
        return self.cutoff

    def set_cutoff(self, cutoff):
        self.cutoff = cutoff
        self.set_xlate_filter_taps(firdes.low_pass(1, self.samp_rate, self.cutoff*1000, self.trans*1000, firdes.WIN_HAMMING, 6.76))
        self._cutoff_slider.set_value(self.cutoff)
        self._cutoff_text_box.set_value(self.cutoff)

    def get_xlate_filter_taps(self):
        return self.xlate_filter_taps

    def set_xlate_filter_taps(self, xlate_filter_taps):
        self.xlate_filter_taps = xlate_filter_taps
        self.freq_xlating_fir_filter_xxx_0.set_taps((self.xlate_filter_taps))

    def get_usrp_freq(self):
        return self.usrp_freq

    def set_usrp_freq(self, usrp_freq):
        self.usrp_freq = usrp_freq
        self._usrp_freq_text_box.set_value(self.usrp_freq)
        self.fftsink.set_baseband_freq(self.usrp_freq)

    def get_rx_freq(self):
        return self.rx_freq

    def set_rx_freq(self, rx_freq):
        self.rx_freq = rx_freq
        self._rx_freq_static_text.set_value(self.rx_freq)

    def get_rf_gain(self):
        return self.rf_gain

    def set_rf_gain(self, rf_gain):
        self.rf_gain = rf_gain
        self._rf_gain_slider.set_value(self.rf_gain)
        self._rf_gain_text_box.set_value(self.rf_gain)

    def get_offset_fine(self):
        return self.offset_fine

    def set_offset_fine(self, offset_fine):
        self.offset_fine = offset_fine
        self._offset_fine_slider.set_value(self.offset_fine)
        self._offset_fine_text_box.set_value(self.offset_fine)

    def get_offset_coarse(self):
        return self.offset_coarse

    def set_offset_coarse(self, offset_coarse):
        self.offset_coarse = offset_coarse
        self._offset_coarse_slider.set_value(self.offset_coarse)
        self._offset_coarse_text_box.set_value(self.offset_coarse)

    def get_af_gain(self):
        return self.af_gain

    def set_af_gain(self, af_gain):
        self.af_gain = af_gain
        self._af_gain_slider.set_value(self.af_gain)
        self._af_gain_text_box.set_value(self.af_gain)

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
    tb = PlayFileTest()
    tb.Start(True)
    tb.Wait()

