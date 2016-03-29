from freqdemod import Signal
#matplotlib inline

import numpy as np
import matplotlib.pylab as plt

font = {'family' : 'serif',
        'weight' : 'normal',
        'size'   : 20}

plt.rc('font', **font)
plt.rcParams['figure.figsize'] = 8, 6
fd = 50.0e3    # digitization frequency
f0 = 2.00e3    # signal frequency
nt = 60e3      # number of signal points
sn = 1.0       # signal zero-to-peak amplitude
sn_rms = 0.01  # noise rms amplitude

dt = 1 / fd
t = dt * np.arange(nt)
signal = sn * np.sin(2*np.pi*f0*t) + np.random.normal(0, sn_rms, t.size)


plt.plot(1E3*t[0:100], signal[0:100])
plt.xlabel('time [ms]')
plt.ylabel('amplitude [nm]')
plt.show()

s = Signal()     # Create a signal
s.load_nparray(signal,"x","nm",dt)   # Load the data into the file


s.time_mask_binarate("middle")  # Pull out the middle section
s.time_window_cyclicize(3E-3)   # Force the data to start and end at zero
s.fft()                         # Fourier transform the data
s.freq_filter_Hilbert_complex() # Take the complex Hilbert transform
s.freq_filter_bp(1.00)          # Apply a 1 kHz wide bandpass filter
s.time_mask_rippleless(15E-3)   # Set up a filter to remove ripple
s.ifft()                        # Inverse Fourier transform the data
s.fit_phase(221.34E-6)          # Fit the phase vs time data

latex = False
s.plot('y', LaTeX=latex)


s.plot('workup/time/mask/binarate', LaTeX=latex)



s.plot('workup/time/window/cyclicize', LaTeX=latex)

s.plot('workup/freq/FT', LaTeX=latex, component='abs')
s.plot('workup/freq/filter/Hc', LaTeX=latex)
s.plot('workup/freq/filter/bp', LaTeX=latex)
s.plot('workup/time/mask/rippleless', LaTeX=latex)
print(s)
