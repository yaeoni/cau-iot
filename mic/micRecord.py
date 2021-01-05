import RPi.GPIO as GPIO
import time
import threading
import os

GPIO.setmode(GPIO.BOARD)
GPIO.setup(10, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(8, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(16, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(22, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

recordFlag = True
playFlag = True
backFlag = True
mixedFlag = True
count = 0

def threadFuncRecord():
    print("\nLet's record\n")
    os.system("arecord -D plughw:2,0 ./mic/main.wav")

def threadFuncPlay():
    print("\nLet's Listen my voice\n")
    os.system("aplay -D plughw:1,0 ./mic/main.wav")
        os.system("aplay -D plughw:1,0 ./mic/back.wav")

def threadplayback():
    print("\nLet's Listen other instruments.\n")
    os.system("aplay -D plughw:1,0 /home/pi/getmp3/piano.wav & aplay -D plughw:1,0 /home/pi/getmp3/drum.wav & aplay -D plughw:1,0 /home/pi/getmp3/synth.wav")


def playMixed():
    print("\nLet's Listen ALL the things\n")
    os.system("aplay -D plughw:1,0 /home/pi/getmp3/drum.wav & aplay -D plughw:1,0 ./mic/main.wav & aplay -D plughw:1,0 /home/pi/getmp3/synth.wav & aplay -D plughw:0,0 /home/pi/getmp3/piano.wav & aplay -D plughw:1,0 /home/pi/getmp3/piano.wav")

def buttonCallback(pin):
    global recordFlag
    global playFlag
    global backFlag
    global mixedFlag 
    if(pin==22):
        if(mixedFlag):
            print("\nListen mixed version\n")
            thread = threading.Thread(target=playMixed)
            thread.start()
            mixedFlag = False
        else:
            os.system('pidof aplay > playID')
            print("\nStop listen\n")
            f = open("playID", 'r')
            line = f.readline()
            command = "sudo kill -2 " + line
            os.system(command)
            f.close()
            mixedFlag = True

    if(pin==16):
        if(backFlag):
            thread = threading.Thread(target=threadplayback)
            thread.start()
            backFlag = False
        else:
            os.system('pidof aplay > playID')
            print("\nStop listen\n")
            f = open("playID", 'r')
            line = f.readline()
            command = "sudo kill -2 " + line
            os.system(command)
            f.close()
            backFlag = True


    if(pin ==10):
        if(recordFlag):
            thread = threading.Thread(target=threadFuncRecord)
            thread.start()
            recordFlag = False
        else:
            os.system('sudo pidof arecord > recordID')
            print("\nStop record\n")
            f = open("recordID", 'r')
            line = f.readline()
            command = "sudo kill -2 " + line
            os.system(command)
            f.close()
            recordFlag = True
    if(pin == 8):
        if(recordFlag == True):
            if(playFlag):
                print("\nLet's listen\n")
                thread = threading.Thread(target=threadFuncPlay)
                thread.start()
                playFlag = False
            else:
                os.system('pidof aplay > playID')
                print("\nStop listen\n")
                f = open("playID", 'r')
                line = f.readline()
                command = "sudo kill -2 " + line
                os.system(command)
                f.close()
                playFlag = True
        else:
            print("\nIn recording, you can't listen!\n")
try:
    GPIO.add_event_detect(10, GPIO.FALLING, callback=buttonCallback, bouncetime=300)
    GPIO.add_event_detect(8, GPIO.FALLING, callback=buttonCallback, bouncetime=300)

    GPIO.add_event_detect(16, GPIO.FALLING, callback=buttonCallback, bouncetime=300)

    GPIO.add_event_detect(22, GPIO.FALLING, callback=buttonCallback, bouncetime=300)

except KeyboardInterrupt:
    GPIO.cleanup()
while(1):
    time.sleep(1)
GPIO.cleanup()

