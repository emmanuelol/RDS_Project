%FM generation
clc;
clear all;
close all;
fc=input('Enter the carrier signal freq in hz,fc=');
fm=input('Enter the modulating signal freq in hz,fm =');
m=input('Modulation index,m= ');
t=0:0.0001:0.1;
c=cos(2*pi*fc*t);%carrier signal
M=sin(2*pi*fm*t);% modulating signal
subplot(3,1,1);plot(t,c);
ylabel('amplitude');xlabel('time index');title('Carrier signal');
subplot(3,1,2);plot(t,M);
ylabel('amplitude');xlabel('time index');title('Modulating signal');
y=cos(2*pi*fc*t-(m.*cos(2*pi*fm*t)));
subplot(3,1,3);plot(t,y);
ylabel('amplitude');xlabel('time index');title('Frequency Modulated signal');
fs=10000;
p=fmdemod(y,fc,fs,(fc-fm));
figure;
subplot(1,1,1);plot(p);