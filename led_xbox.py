#------------------------------------------------------------
#   coding:utf-8
#------------------------------------------------------------
#   Updata History
#   August  10  12:00, 2019 (Sat)
#------------------------------------------------------------
#   xboxコントローラで4つのLEDをLチカさせていく
#------------------------------------------------------------

from gpiozero import LED
from time import sleep
import struct
import subprocess

device_path = "/dev/input/js0"
EVENT_FORMAT = "LhBB";
EVENT_SIZE = struct.calcsize(EVENT_FORMAT)

#  LEDのセットアップ
led_red = LED(4)
led_green = LED(17)
led_yellow = LED(27)
led_white = LED(22)

def main():
    try:
        with open(device_path, "rb") as device:
            event = device.read(EVENT_SIZE)
            while event:
                (xbox_time, xbox_val, xbox_type, xbox_num) = struct.unpack(EVENT_FORMAT, event)
                if xbox_type == 1:
                    #  LEDの点灯フェーズ
                    #  Aボタンの入力
                    if xbox_num == 0:
                        sw1 = False if xbox_val == 0 else True
                        if sw1: led_green.on()
                        else: led_green.off()
                    #  Bボタンの入力
                    if xbox_num == 1:
                        sw2 = False if xbox_val == 0 else True
                        if sw2: led_red.on()
                        else: led_red.off()
                    #  Xボタンの入力
                    if xbox_num == 2:
                        sw3 = False if xbox_val == 0 else True
                        if sw3: led_yellow.on()
                        else: led_yellow.off()
                    #  Yボタンの入力
                    if xbox_num == 3:
                        sw4 = False if xbox_val == 0 else True
                        if sw4: led_white.on()
                        else: led_white.off()                    

                    #  ランダムフェーズ
                    if xbox_num == 4:
                        print("ランダムスタート!")
                        subprocess.run(["python3", "./Document/led_multi.py"])
                
                    #  終了フェーズ
                    if xbox_num == 5: break

                print( "{0}, {1}, {2}, {3}".format(xbox_time, xbox_val, xbox_type, xbox_num) )
                event = device.read(EVENT_SIZE)
    except IOError:
        print("再起動")
        subprocess.run(["sudo", "reboot"])
    finally:
        pass

if __name__ == "__main__":
    main()