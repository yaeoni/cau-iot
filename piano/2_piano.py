from pythonosc  import osc_message_builder
from pythonosc  import udp_client
import random
import time 
from psonic import *
import RPi.GPIO as GPIO 
from threading import Thread
from modify import Modify
import socket
from scp_things import SSHManager
#-----------
import serial
arduino = serial.Serial('/dev/ttyACM0', 9600)
#----------


GPIO.setmode(GPIO.BCM)
BTN=[21,20,16,26,18,15,14]
GPIO.setup(BTN[0], GPIO.IN)
GPIO.setup(BTN[1], GPIO.IN)
GPIO.setup(BTN[2], GPIO.IN)
GPIO.setup(BTN[3], GPIO.IN)
GPIO.setup(BTN[4], GPIO.IN)
GPIO.setup(BTN[5], GPIO.IN)
GPIO.setup(BTN[6], GPIO.IN)
GPIO.setup(19, GPIO.IN)
GPIO.setup(13, GPIO.IN)
GPIO.setup(6, GPIO.IN)
GPIO.setup(5, GPIO.IN)
GPIO.setup(12, GPIO.IN)
sheet_t =[]
sheet_s=[]
r_start=0 
r_end=0
blank_time=0
OCT = 0
SUSTAIN = 10000
do_FLAG = True
re_FLAG = True
mi_FLAG = True
fa_FLAG = True
sol_FLAG = True
la_FLAG = True
si_FLAG = True

_do_FLAG = True
_re_FLAG = True
_fa_FLAG = True
_sol_FLAG = True
record_least_once =False
recording = False
MODE= True
mode_str = ""
    
#------------------------
def print_lcd(content):
     
    arduino.write(b'2')
    arduino.write(content.encode())

def send_lcd(melody, oct_num, beat):
    #----- change-start------
    if oct_num >0:
        melody = melody+"+"+str(int(oct_num/12))
    elif oct_num <0:
        oct_num =oct_num * (-1)
        melody = melody +"-"+str(int(oct_num/12))
    #----- change--end------
    melody = "Melody :"+melody 
    beat = "Beat:"+str(beat)
    arduino.write(b'1')
    arduino.write(melody.encode())
    arduino.write(b'9')
    arduino.write(beat.encode())
 
#------------------------
def do(pin):
    global do_FLAG
    start = time.time()
    global r_start,r_end
    if  GPIO.input(21)==1 and do_FLAG:
        do_FLAG = False
        if r_start !=0 :
            r_end = time.time()
            sheet_t.append(round(r_end-r_start,2))
            sheet_s.append(-1)
            
        use_synth(PIANO)
        play(72+OCT,decay=SUSTAIN)
        #sleep(SUSTAIN)
        while True :
            if GPIO.input(21)==0 :
                do_FLAG = True
                stop()
                end = time.time()
                r_start = end
                total = round(end- start,2)
                if  total > 0:
                    sheet_t.append(total)
                    sheet_s.append(72+OCT)
                    send_lcd("C",OCT,total)
                return 
            else:
                pass
   


def re(pin):
    global re_FLAG
    start = time.time()
    global r_start,r_end
    if  GPIO.input(20)==1 and do_FLAG:
        re_FLAG = False
        if r_start !=0 :
            r_end = time.time()
            sheet_t.append(round(r_end-r_start,2))
            sheet_s.append(-1)
            
        use_synth(PIANO)
        play(74+OCT,decay=SUSTAIN)
        #sleep(SUSTAIN)
        while True :
            if GPIO.input(20)==0 :
                re_FLAG = True
                stop()
                end = time.time()
                r_start = end
                total = round(end- start,2)
                if  total > 0:
                    sheet_t.append(total)
                    sheet_s.append(74+OCT)
                    send_lcd("D",OCT,total)
                return 
            else:
                pass
 
def mi(pin):
    global mi_FLAG
    start = time.time()
    global r_start,r_end
    if  GPIO.input(16)==1 and mi_FLAG:
        mi_FLAG = False
        if r_start !=0 :
            r_end = time.time()
            sheet_t.append(round(r_end-r_start,2))
            sheet_s.append(-1)
            
        use_synth(PIANO)
        play(76+OCT,decay=SUSTAIN)
        #sleep(SUSTAIN)
        while True :
            if GPIO.input(16)==0 :
                mi_FLAG = True
                stop()
                end = time.time()
                r_start = end
                total = round(end- start,2)
                if  total > 0:
                    sheet_t.append(total)
                    sheet_s.append(76+OCT)
                    send_lcd("E",OCT,total)
                return 
            else:
                pass
 
def fa(pin):
    global fa_FLAG
    start = time.time()
    global r_start,r_end
    if  GPIO.input(26)==1 and fa_FLAG:
        fa_FLAG = False
        if r_start !=0 :
            r_end = time.time()
            sheet_t.append(round(r_end-r_start,2))
            sheet_s.append(-1)
            
        use_synth(PIANO)
        play(77+OCT,decay=SUSTAIN)
        #sleep(SUSTAIN)
        while True :
            if GPIO.input(26)==0 :
                fa_FLAG = True
                stop()
                end = time.time()
                r_start = end
                total = round(end- start,2)
                if  total > 0:
                    sheet_t.append(total)
                    sheet_s.append(77+OCT)
                    send_lcd("F",OCT,total)
                return 
            else:
                pass
 
def sol(pin):
    global sol_FLAG
    start = time.time()
    global r_start,r_end
    if  GPIO.input(18)==1 and sol_FLAG:
        sol_FLAG = False
        if r_start !=0 :
            r_end = time.time()
            sheet_t.append(round(r_end-r_start,2))
            sheet_s.append(-1)
            
        use_synth(PIANO)
        play(79+OCT,decay=SUSTAIN)
        #sleep(SUSTAIN)
        while True :
            if GPIO.input(18)==0 :
                sol_FLAG = True
                stop()
                end = time.time()
                r_start = end
                total = round(end- start,2)
                if  total > 0:
                    sheet_t.append(total)
                    sheet_s.append(79+OCT)
                    send_lcd("G",OCT,total)
                return 
            else:
                pass
 
def la(pin):
    global la_FLAG
    start = time.time()
    global r_start,r_end
    if  GPIO.input(15)==1 and la_FLAG:
        la_FLAG = False
        if r_start !=0 :
            r_end = time.time()
            sheet_t.append(round(r_end-r_start,2))
            sheet_s.append(-1)
            
        use_synth(PIANO)
        play(81+OCT,decay=SUSTAIN)
        #sleep(SUSTAIN)
        while True :
            if GPIO.input(15)==0 :
                la_FLAG = True
                stop()
                end = time.time()
                r_start = end
                total = (round(end- start,2))
                if  total > 0:
                    sheet_t.append(total)
                    sheet_s.append(81+OCT)
                    send_lcd("A",OCT,total)
                return 
            else:
                pass
 
def si(pin):
    global si_FLAG
    start = time.time()
    global r_start,r_end
    if  GPIO.input(14)==1 and si_FLAG:
        si_FLAG = False
        if r_start !=0 :
            r_end = time.time()
            sheet_t.append(round(r_end-r_start,2))
            sheet_s.append(-1)
            
        use_synth(PIANO)
        play(83+OCT,decay=SUSTAIN)
        #sleep(SUSTAIN)
        while True :
            if GPIO.input(14)==0 :
                si_FLAG = True
                stop()
                end = time.time()
                r_start = end
                total = (round(end- start,2))
                if  total > 0:
                    sheet_t.append(total)
                    sheet_s.append(83+OCT)
                    send_lcd("B",OCT,total)
                return 
            else:
                pass


def _do(pin):
    global _do_FLAG
    start = time.time()
    global r_start,r_end
    if  pin ==19  and _do_FLAG:
        _do_FLAG = False
        if r_start !=0 :
            r_end = time.time()
            sheet_t.append(round(r_end-r_start,2))
            sheet_s.append(-1)
            
        use_synth(PIANO)
        play(73+OCT,decay=SUSTAIN)
        #sleep(SUSTAIN)
        while True :
            if GPIO.input(19)==0 :
                _do_FLAG = True
                stop()
                end = time.time()
                r_start = end
                total = (round(end- start,2))
                if  total > 0:
                    sheet_t.append(total)
                    sheet_s.append(73+OCT)
                    send_lcd("C#",OCT,total)
                return 
            else:
                pass
           
def _re(pin):
    global _re_FLAG
    start = time.time()
    global r_start,r_end
    if  GPIO.input(13)==1 and _re_FLAG:
        _re_FLAG = False
        if r_start !=0 :
            r_end = time.time()
            sheet_t.append(round(r_end-r_start,2))
            sheet_s.append(-1)
            
        use_synth(PIANO)
        play(75+OCT,decay=SUSTAIN)
        #sleep(SUSTAIN)
        while True :
            if GPIO.input(13)==0 :
                _re_FLAG = True
                stop()
                end = time.time()
                r_start = end
                total = (round(end- start,2))
                if  total > 0:
                    sheet_t.append(total)
                    sheet_s.append(75+OCT)
                    send_lcd("D#",OCT,total)
                return 
            else:
                pass

def _fa(pin):
    global _fa_FLAG
    start = time.time()
    global r_start,r_end
    if  GPIO.input(6)==1 and _fa_FLAG:
        _fa_FLAG = False
        if r_start !=0 :
            r_end = time.time()
            sheet_t.append(round(r_end-r_start,2))
            sheet_s.append(-1)
            
        use_synth(PIANO)
        play(78+OCT,decay=SUSTAIN)
        #sleep(SUSTAIN)
        while True :
            if GPIO.input(6)==0 :
                _fa_FLAG = True
                stop()
                end = time.time()
                r_start = end
                total = (round(end- start,2))
                if  total > 0:
                    sheet_t.append(total)
                    sheet_s.append(78+OCT)
                    send_lcd("F#",OCT,total)
                return 
            else:
                pass

def _sol(pin):
    global _sol_FLAG
    start = time.time()
    global r_start,r_end
    if  GPIO.input(5)==1 and _sol_FLAG:
        _sol_FLAG = False
        if r_start !=0 :
            r_end = time.time()
            sheet_t.append(round(r_end-r_start,2))
            sheet_s.append(-1)
            
        use_synth(PIANO)
        play(80+OCT,decay=SUSTAIN)
        #sleep(SUSTAIN)
        while True :
            if GPIO.input(5)==0 :
                _sol_FLAG = True
                stop()
                end = time.time()
                r_start = end
                total = (round(end- start,2))
                if  total > 0:
                    sheet_t.append(total)
                    sheet_s.append(80+OCT)
                    send_lcd("G#",OCT,total)
                return 
            else:
                pass





def OCT_up(pin):
            global OCT
            if GPIO.input(13)==1 and MODE:
                OCT = OCT + 12
                print_lcd("oct up : "+str(OCT))
            elif GPIO.input(13)==1 and not MODE :
                _re(pin)

             
def OCT_down(pin):
        
            global OCT
            if GPIO.input(19)==1 and MODE:
                OCT = OCT -12
                print_lcd("oct down : "+str(OCT))
            elif GPIO.input(19)==1 and not MODE :
                _do(pin)


def record(pin):
    if GPIO.input(6)==1 and MODE:
        global recording, sheet_t, sheet_s
        if recording :
            print_lcd("record end")
            record_least_once =True
            stop_recording
            save_recording('/home/pi/piano.wav')
            print_lcd("name: piano.wav")
            recording = False
        else:
            print_lcd("record start")
            sheet_t =[]
            sheet_s=[]
            start_recording()
            recording = True
    elif GPIO.input(6)==1 and not MODE:
                _fa(pin)


def geT_melody(mel_num):
    ret=""
    if mel_num ==0 or mel_num ==12:
        ret="C "
    elif mel_num ==1:
        ret="C#"
    elif mel_num ==2:
        ret="D "
    elif mel_num ==3:
        ret="D#"
    elif mel_num ==4:
        ret="E "

    elif mel_num ==5:
        ret="F "
    elif mel_num ==6:
        ret="F#"
    elif mel_num ==7:
        ret="G "
    elif mel_num ==8:
        ret="G#"
    elif mel_num ==9:
        ret="A "
    elif mel_num ==10:
         ret="A#"
    elif mel_num ==11:
        ret="B "

    return ret


def num2str(time_num, melody_num):
    time_str =[]
    melody_str =[]
    for melody in melody_num:

        ret=""
        if melody ==-1:
            ret="_   "
        else:
            tmp = melody-72
            if tmp >0:
                oct_num=int(tmp/12)
                mel_num=int(tmp%12)
                oct_str="  "
                ret =geT_melody(mel_num)
                if oct_num >0:
                    oct_str="+"+str(oct_num)
                ret=ret+oct_str
                
            elif tmp ==0:
                ret="C   "
            elif tmp<0:
                tmp = tmp*-1
                oct_num=int(tmp/12)
                mel_num=12-int(tmp%12)
                oct_str="  "
                ret =geT_melody(mel_num)
                if mel_num ==12:
                    oct_str="-"+str(oct_num)
                else:


                    oct_str="-"+str(oct_num+1)
                ret=ret+oct_str
        melody_str.append(ret)
    for _time in time_num:
        time_str.append(str(_time))
    return time_str, melody_str 

def send(pin):
    print_lcd('sending wav')
    '''
    host=[]
    port=[]
    host.append("165.194.35.5")
    host.append("165.194.35.5")
    port.append(2201)
    port.append(2202)
    for i in range(0,len(host)):
        s=socket.socket(family=socket.AF_INET,type=socket.SOCK_STREAM)
        s.connect((host[i],port[i]))
        with open('piano.wav','rb') as f:
            for l in f : s.sendall(l)
        s.close()
     '''
    ssh_manager = SSHManager()
    ssh_manager.create_ssh_client("", "pi", "1234") # 세션생성
    ssh_manager.send_file("./piano.wav", "/home/pi/Desktop/getmp3") # 파일전송
    ssh_manager.close_ssh_client() # 세션종료

def listen(pin):
    global sheet_t, sheet_s
    if GPIO.input(5)==1 and MODE:  
        time_stamp =[]
        melody_stamp=[]
        if record_least_once :
            # sheet_t is for beat and sheet_s is for melody 
            # and they are both global variable
            if sheet_t is not None and sheet_s is not None:
                # before modify we have to change melody int(72) to melody string(C or 도)
                # they should be nice and dlean
                time_stamp, melody_stamp = num2str(sheet_t, sheet_s)        
                print_lcd('modify mode')
                '''
                a = ["C   ", "D   ", "C+  ", "-   ", "E#  ", "Ab  "]
                b = ["1   ", "1   ", "1   ", "1   ", "2   ", "3   "]
                '''
                print("박자")
                print(time_stamp)
                print("음표")
                print(melody_stamp)
                opt = input("\n 수정하시겠습니까? y/n \n")
                if opt == 'y' or opt =='Y':
                    # make instance for CLI
                    md=Modify(melody_stamp,time_stamp)
                    # do modify
                    sheet_t, sheet_s =md.main()
                    # change num to string for showing
                    time_stamp, melody_stamp = num2str(sheet_t, sheet_s)        
                    print("\n\n-------수정종료------\n\n")
                    print("박자")
                    print(time_stamp)
                    print("음표")
                    print(melody_stamp)
                    print("==========================\n\n")

                else:
                    return
            else:
                print("입력이 부족합니다.\n\n")
        else :
            print("녹음된 파일이 없습니다.\n\n")
    elif GPIO.input(5)==1 and not MODE:
            _sol(pin)


def change_mode(pin):
    if GPIO.input(12)==1:
        global MODE
        if MODE :
            print_lcd("piano mode")
            MODE = False
        else:
            print_lcd("oct and record")
            MODE = True

GPIO.add_event_detect(BTN[0], GPIO.BOTH, callback=do, bouncetime=100)
GPIO.add_event_detect(BTN[1], GPIO.BOTH, callback=re, bouncetime=100)
GPIO.add_event_detect(BTN[2], GPIO.BOTH, callback=mi, bouncetime=100)
GPIO.add_event_detect(BTN[3], GPIO.BOTH, callback=fa, bouncetime=100)
GPIO.add_event_detect(BTN[4], GPIO.BOTH, callback=sol, bouncetime=100)
GPIO.add_event_detect(BTN[5], GPIO.BOTH, callback=la, bouncetime=100)
GPIO.add_event_detect(BTN[6], GPIO.BOTH, callback=si, bouncetime=100)
#GPIO.add_event_detect(12, GPIO.BOTH, callback=change_mode, bouncetime=100)
GPIO.add_event_detect(12, GPIO.BOTH, callback=send, bouncetime=100)
GPIO.add_event_detect(19, GPIO.BOTH, callback=OCT_down, bouncetime=100)
GPIO.add_event_detect(13, GPIO.BOTH, callback=OCT_up, bouncetime=100)
GPIO.add_event_detect(5, GPIO.BOTH, callback=listen, bouncetime=100)
GPIO.add_event_detect(6, GPIO.BOTH, callback=record, bouncetime=100)

try:
    while True:
        #pass
        sleep(30)
       #piano(0)
    #except KeyboardInterrupt:
     
     
finally:
  
    GPIO.cleanup()
    #    break

   
