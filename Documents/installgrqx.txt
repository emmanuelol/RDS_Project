# -----------------------------------------
# script to install components from source

#!/bin/bash

# Set up rtlsdr and gr-osmosdr from source
echo "[`date`] Installing prerequisites..."
apt-get -y install hackrf libhackrf-dev boost-all-dev liblog4cpp5-dev swig fftw3 fftw3-dev doxygen

echo "[`date`] Removing repo versions if installed..."
apt-get remove rtlsdr gr-osmosdr

SDRROOT="/opt/sdr-build"

echo "[`date`] Setting up rtl-sdr..."
if [ -e $SDRROOT/rtl-sdr/build ]; then
    echo "[`date`] found $SDRROOT/rtl-sdr/build.  Uninstalling previous version."
    cd $SDRROOT/rtl-sdr/build/
    make uninstall
    make clean
    cd $SDRROOT
    rm -rf rtl-sdr
fi

cd $SDRROOT

echo "[`date`] Getting rtl-sdr source..."

git clone git://git.osmocom.org/rtl-sdr.git rtl-sdr
mkdir -p $SDRROOT/rtl-sdr/build
cd rtl-sdr/build

cmake ../ -DINSTALL_UDEV_RULES=ON -DDETACH_KERNEL_DRIVER=ON
make
make install
ldconfig
make install-udev-rules

echo "[`date`] Getting osmosdr..."

if [ -e $SDRROOT/gr-osmosdr/build ]; then
    echo "[`date`] found $SDRROOT/gr-osmosdr/build.  Uninstalling previous version."
    cd $SDRROOT/gr-osmosdr/build/
    make uninstall
    make clean
    cd $SDRROOT
    rm -rf $SDRROOT/gr-osmosdr
fi

cd $SDRROOT
git clone git://git.osmocom.org/gr-osmosdr gr-osmosdr
mkdir gr-osmosdr/build
cd gr-osmosdr/build
cmake ../
make
make install
ldconfig

echo "[`date`] Building libosmo-dsp..."
cd $SDRROOT
git clone git://git.osmocom.org/libosmo-dsp.git libosmo-dsp
cd libosmo-dsp

autoreconf -i
./configure
make
make install
ln -s /usr/local/bin/osmocom_fft /usr/bin/osmocom_fft

echo "[`date`] Building gr-iqbal..."
cd $SDRROOT
if [ -e $SDRROOT/gr-iqbal/build ]; then
    echo "[`date`] found $SDRROOT/gr-iqbal/build.  Uninstalling previous version."
    cd $SDRROOT/gr-iqbal/build/
    make uninstall
    make clean
    cd $SDRROOT
    rm -rf gr-iqbal
fi

cd $SDRROOT
git clone git://git.osmocom.org/gr-iqbal.git gr-iqbal
mkdir gr-iqbal/build
cd gr-iqbal/build
cmake ../
make
make install
ldconfig

echo "[`date`] Building gqrx...."
if [ -e $SDRROOT/gqrx/build ]; then
    echo "[`date`] found $SDRROOT/gqrx/build.  Uninstalling previous version."
    cd $SDRROOT/gqrx/build/
    make uninstall
    make clean
    cd $SDRROOT
    rm -rf gqrx
fi

apt-get -y install libqt4-dev libqtcore4 libqtgui4 libqt4-network libqt4-svg
cd $SDRROOT
git clone https://github.com/csete/gqrx.git gqrx
mkdir -p gqrx/build
cd gqrx/build
qmake ..
make
make install
ln -s /usr/local/bin/gqrx /usr/bin/gqrx

echo "[`date`] For a Raspberry Pi 2 add the following lines to /boot/config.txt"
echo "framebuffer_depth=32"
echo "framebuffer_ignore_alpha=1"
echo ""
echo "[`date`] for Pulseaudio to work correctly in gqrx on a Raspberry Pi/2, edit /etc/pulse/default.pa and add the line:"
echo "load-module module-alsa-card device_id=0"
echo "then reboot."

echo ""
echo "[`date`] Done."

# -----------------------------------------
