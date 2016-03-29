clc;
clear all;
close all;
fm=input('Message Frequency=');
fc=input('Carrier Frequency=');
mi=input('Modulation Index=');
t=0:0.0001:0.1;
m=sin(2*pi*fm*t);
subplot(3,1,1);
plot(t,m);
xlabel('Time');
ylabel('Amplitude');
title('Message Signal');
grid on;

c=sin(2*pi*fc*t);
subplot(3,1,2);
plot(t,c);
xlabel('Time');
ylabel('Amplitude');
title('Carrier Signal');
grid on;

y=sin(2*pi*fc*t+(mi.*sin(2*pi*fm*t)));%Frequency changing w.r.t Message
subplot(3,1,3);
plot(t,y);
xlabel('Time');
ylabel('Amplitude');
title('FM Signal');
grid on;