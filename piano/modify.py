from pythonosc  import osc_message_builder
from pythonosc  import udp_client
import time 
import re
from psonic import *

# 음은 4자리, 박자는 4자리
# 향식 예시
a = ["C   ", "D   ", "C+  ", "-   ", "E#  ", "Ab  "]
b = ["1   ", "1   ", "1   ", "1   ", "2   ", "3   "]

# this variables are
#for not saving the changes
orig_time_stamp=[]
orig_melody_stamp=[]

# change C (string)=> 72(int)

'''
!!!Change required(1)!!!
---------start---------
'''
def getNum(str0, str1):
   ret=0
   if str0 =="C":
        if str1.find("#")!=-1:
            ret =73
        else:
            ret = 72

   if str0 =="D":
        if str1.find("#")!=-1:
            ret =75
        else:
            ret = 74

   if str0 =="E":
        ret = 76
   if str0 =="F":
        if str1.find("#")!=-1:
            ret =78
        else:
            ret = 77
   if str0 =="G":
        if str1.find("#")!=-1:
            ret =80
        else:
            ret = 79

   if str0 =="A":
        if str1.find("#")!=-1:
            ret =82
        else:
            ret = 81
   if str0 =="B":
        if str1.find("#")!=-1:
            ret =84
        else:
            ret = 83

   return  ret

def str2num(time_str, melody_str):
    time_num=[]
    melody_num=[]
    for melody in melody_str:
        ret =0
        if melody[0]=="_":
            ret =-1
        else :
            ret=getNum(melody[0],melody)
            if melody.find("+")!=-1:
                ret = ret+12*int(re.findall("\d+",melody)[0])
            elif melody.find("-")!=-1:
                ret = ret-12*int(re.findall("\d+",melody)[0])
        melody_num.append(ret)
    for _time in time_str:
        time_num.append(round(float(_time),2))
    return time_num, melody_num
           

# class for CLI
class Modify:
    def __init__(self, scales, durations):
        self.scales = scales
        self.durations = durations
        orig_time_stamp = scales
        orig_melody_stamp = durations
    # play with the changes
    def play_song(self):
        use_synth(PIANO)
        time_stamp=[]
        melody_stamp=[]
        time_stamp,melody_stamp=str2num(self.durations,self.scales)
        for  i   in range(0,len(time_stamp)):
            if melody_stamp[i] !=   -1:
                play(melody_stamp[i],decay=time_stamp[i])
                sleep(time_stamp[i])
            else  :
                sleep(time_stamp[i])    

    # show the time and melody
    def show(self):
        print("번호", end = ' ')
        for i, val in enumerate(self.scales):
            print(i+1, end ='    ')
        t=0
        j=0
        print('\n음  ', end = ' ')

        for scale in self.scales:
            t=t+1
            if t>10:
                print(scale, end= '  ')
            else:
                print(scale, end= ' ')

        print('\n박자', end = ' ')

        for duration in self.durations:
            j=j+1
            if j>10:
                print(duration, end= '  ')
            else:
                print(duration, end= ' ')


    # show the beat
    def showDurations(self):
        print("번호", end = ' ')
        for i, val in enumerate(self.scales):
            print(i+1, end ='    ')

        print('\n박자', end = ' ')

        j=0
        for duration in self.durations:
            j=j+1
            if j>10:
                print(duration, end= '  ')
            else:
                print(duration, end= ' ')


    # show the melody
    def showScales(self):
        print("번호", end = ' ')
        for i, val in enumerate(self.scales):
            print(i+1, end ='    ')
        print('\n음  ', end = ' ')
        t=0
        for scale in self.scales:
            t=t+1
            if t>10:
                print(scale, end= '  ')
            else:
                print(scale, end= ' ')


    
    def modifyDuration(self):
        self.showDurations()
        print("\n\n=======================================")
        index = input("수정을 원하시는 박자의 번호를 눌러주세요! ")
        modur = input("어떤 박자로 바꿀까요? : ")

        
        while(len(modur) != 4):
            modur.append(" ")

        self.durations[int(index)-1] = modur
        print("성공적으로 바뀌었습니다 :)")
    
    def modifyScales(self):
        self.showScales()
        print("\n\n=======================================")
        index = input("수정을 원하시는 음계의 번호를 눌러주세요! ")
        print("\n(예시 입력) C#, C+1(옥타브 올림), E-1(옥타브 내림)\n")
        modur = input("어떤 음으로 바꿀까요? : ")

        while(len(modur) != 4):
            modur= modur+" "

        self.scales[int(index)-1] = modur
        print("성공적으로 바뀌었습니다 :)")

    def deleteScale(self):
        self.showScales()
        print("\n\n=======================================")
        index = input("지우기 원하시는 음계의 번호를 눌러주세요! ")

        del self.scales[int(index)-1]
        del self.durations[int(index)-1]
        print("성공적으로 지웠습니다. :)")

    def insertScale(self):
        self.showScales()
        print("\n\n=======================================")
        index = input("\n삽입하고 싶은 음의 위치는 어디인가요? : ")

        print("\n1. 해당 음의 왼쪽에 추가! ")
        print("2. 해당 음의 오른쪽에 추가! ")
        isWhere = input("\n어떻게 추가하시겠어요 : ")

        print("\n(예시 입력) C#, C+1(옥타브 올림), E-1(옥타브 내림)\n")
        modur = input("어떤 음을 추가할까요? : ")
        dur = input("박자는 어떻게 설정하시겠어요 ? : ")
        while(len(modur) != 4):
            modur=modur+" "

        while(len(dur) != 4):
            dur=dur+" "

        if(isWhere=="1"):
            self.scales.insert(int(index)-1, modur)
            self.durations.insert(int(index)-1, dur)
        elif(isWhere=="2"):
            self.scales.insert(int(index), modur)
            self.durations.insert(int(index), dur)
        else:
            print("잘못된 입력입니다~ 처음부터 다시 하세요!")


        print("성공적으로 추가 되었어요 :)! ")

    

    def main(self):
        while(1):
            print("=======================================")
            print("                  수정                  ")
            print("=======================================")
            print("[현재 상태]")
            self.show()
            print("\n=======================================")
            print("1. 음 바꾸기, 음 지우기, 음 추가하기")
            print("2. 박자 고치기(수정만 가능합니다.)")
            print("3. 현재 상태 들어보기")
            print("0. 종료하기")
            print("=======================================")
            num = input("원하시는 기능의 숫자를 입력 해주세요 ! : ")

            if(num=="1"):
                print("\n[ 옵션을 선택해주세요 ]\n")
                print("1. 음 바꾸기")
                print("2. 음 지우기(박자도 함께 지워집니다.)")
                print("3. 음 추가하기(박자도 함께 추가됩니다.)")
                opt = input("\n\n원하시는 옵션의 번호를 눌러주세요! ")
                if(opt == "1"):
                    print("=======================================")
                    print("\n [ 음 수정 ]\n")
                    self.modifyScales()
                elif(opt == "2"):
                    print("=======================================")
                    print("\n [ 음 삭제 ]\n")
                    self.deleteScale()
                elif(opt == "3"):
                    print("=======================================")
                    print("\n [ 음 추가 ]\n")
                    self.insertScale()
            elif(num=="2"):
                print("=======================================")
                print("\n [ 박자 수정 ]\n")
                self.showDurations()
                self.modifyDuration()
            elif(num=="3"):
                print("=======================================")
                print("\n[ 음악이 흐릅니다 :) ] ")
                self.play_song()
            elif(num=="0"):
                print("=======================================")
                opt = input("\n\n 수정사항을 저장하시겠습니까? y/n \n\n")
                time_stamp=[]
                melody_stamp=[]
                if opt == 'n' or opt =='N':
                    time_stamp,melody_stamp=str2num(orig_time_stamp, orig_melody_stamp)
                else:
                    # if ou want to save the changes record will be done again
                    time_stamp,melody_stamp=str2num(self.durations,self.scales)
                    start_recording()
                    self.play_song()
                    stop_recording
                    save_recording('/home/pi/piano.wav')

                print("\n\n프로그램이 종료됩니다.\n\n")
                time.sleep(1)
                # return original tyoe(int) not type for modify/showing (string)
                return time_stamp, melody_stamp
                break
            else:
                print("=======================================")
                print("\n\n잘못된 입력입니다. 다시 입력해주세요!\n\n")
                time.sleep(1)
        
    
