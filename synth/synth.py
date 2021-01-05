from psonic import *
import wiringpi as wiringpi
import RPi.GPIO as gpio
import threading
import time
import os

CPIN = 2
DPIN = 3
EPIN = 4
FPIN = 5
GPIN = 6
APIN = 7
BPIN = 8
RPIN = 9
SPIN = 10

gpio.setmode(gpio.BCM)
gio,setup(CPIN,gpio,IN)
gio,setup(DPIN,gpio,IN)
gio,setup(EPIN,gpio,IN)
gio,setup(FPIN,gpio,IN)
gio,setup(GPIN,gpio,IN)
gio,setup(APIN,gpio,IN)
gio,setup(BPIN,gpio,IN)
gio,setup(RPIN,gpio,IN)
gio,setup(SPIN,gpio,IN)

Bflag=False
Tflag=False
recording=False

def sound(num) :
    global Tflag
    if num == CPIN :
        play(chord(C3,MAJOR),decay=5)
    elif num == DPIN :
        play(chord(D3,MAJOR),decay=5)
    elif num == EPIN :
        play(chord(E3,MAJOR),decay=5)
    elif num == FPIN:
        play(chord(F3, MAJOR), decay=5)
    elif num == GPIN :
        play(chord(G3,MAJOR),decay=5)
    elif num == APIN :
        play(chord(A3,MAJOR),decay=5)
    elif num == BPIN :
        play(chord(B3,MAJOR),decay=5)
    while True :
        if Tflag :
            stop()
            break

def show_callback(pin):
    global tempo
    global melody
    print(melody)
    print(tempo)

def recode_callback(pin):
    global recording
    if recording :
        print("Finish recording")
        stop_recording
        save_recording('/home/pi/test.wav')
    else :
        print("Start recording")
        start_recording()
        recording =True


def my_callback(pin):
    global start, end
    global rest_start,rest_end
    global Bflag
    global Tflag
    global sound_thread
    if gpio.input(pin) == 1 and Bflag :
        Tflag=True
        Bflag=False
        end=time.time()
        elapsed = end - start
        tempo.append(round(elapsed,1))
        melody.append(pin-1)
        rest_start = time.time()
    if gpio.input(pin) == 0 and not Bflag :
        start = time.time()
        Tflag=False
        Bflag=True
        rest_end=time.time()
        rest=rest_end-rest_start
        tempo.append(round(rest,1))
        melody.append(0)
        sound_thread=threading.Thread(target=sound,args=(pin,))
        sound_thread.start()

try :
    gpio.add_event_detect(SPIN,gpio.FALLING,callback=show_callback,bouncetime=300)
    gpio.add_event_detect(SPIN,gpio.FALLING,callback=recode_callback,bouncetime=300)
    gpio.add_event_detect(CPIN,gpio.BOTH,callback=my_callback,bouncetime=300)
    gpio.add_event_detect(DPIN,gpio.BOTH,callback=my_callback,bouncetime=300)
    gpio.add_event_detect(EPIN,gpio.BOTH,callback=my_callback,bouncetime=300)
    gpio.add_event_detect(FPIN,gpio.BOTH,callback=my_callback,bouncetime=300)
    gpio.add_event_detect(GPIN,gpio.BOTH,callback=my_callback,bouncetime=300)
    gpio.add_event_detect(APIN,gpio.BOTH,callback=my_callback,bouncetime=300)
    gpio.add_event_detect(BPIN,gpio.BOTH,callback=my_callback,bouncetime=300)
    rest_start=time.time()
    while True :
        pass
finally:
    gpio.cleanup()


