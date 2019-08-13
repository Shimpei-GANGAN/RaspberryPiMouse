#------------------------------------------------------------
#   coding:utf-8
#------------------------------------------------------------
#   Updata History
#   August  14  00:00, 2019 (Wed)
#------------------------------------------------------------
#   xboxコントローラでRaspberry Pi Mouseを動かす
#    ・A,B,X,YでLED0〜LED3を点灯・消灯
#    ・矢印キーでモータ操作(デジタル入力)
#    ・左スティック・右スティックでモータ操作(アナログ入力)
#------------------------------------------------------------
import struct
import subprocess
import time

device_path = "/dev/input/js0"
rt_cmd = []
EVENT_FORMAT = "LhBB";
EVENT_SIZE = struct.calcsize(EVENT_FORMAT)
straight = 0
curbe = 0
speed = 500

def main():
    try:
        with open(device_path, "rb") as device:
            event = device.read(EVENT_SIZE)
            while event:
                (xbox_time, xbox_val, xbox_type, xbox_num) = struct.unpack(EVENT_FORMAT, event)
                if xbox_type == 1 and xbox_val == 1:
                    #  Aボタンの入力
                    if xbox_num == 0: subprocess.call(["echo 1 > /dev/rtled0"], shell=True)
                    #  Bボタンの入力
                    elif xbox_num == 1: subprocess.call(["echo 1 > /dev/rtled1"], shell=True)
                    #  Xボタンの入力
                    elif xbox_num == 2: subprocess.call(["echo 1 > /dev/rtled2"], shell=True)
                    #  Yボタンの入力
                    elif xbox_num == 3: subprocess.call(["echo 1 > /dev/rtled3"], shell=True)
                    #  ブザーON
                    elif xbox_num == 4: subprocess.call(["echo 440 > /dev/rtbuzzer0"], shell=True)
                    #  終了フェーズ
                    elif xbox_num == 5: break
                elif xbox_type == 1 and xbox_val == 0:
                    #  Aボタンの入力
                    if xbox_num == 0: subprocess.call(["echo 0 > /dev/rtled0"], shell=True)
                    #  Bボタンの入力
                    elif xbox_num == 1: subprocess.call(["echo 0 > /dev/rtled1"], shell=True)
                    #  Xボタンの入力
                    elif xbox_num == 2: subprocess.call(["echo 0 > /dev/rtled2"], shell=True)
                    #  Yボタンの入力
                    elif xbox_num == 3: subprocess.call(["echo 0 > /dev/rtled3"], shell=True)
                    #  ブザーOFF
                    elif xbox_num == 4: subprocess.call(["echo 0 > /dev/rtbuzzer0"], shell=True)
                elif xbox_type == 2:
                    subprocess.call(["echo 1 > /dev/rtmotoren0"], shell=True)
                    
                    if xbox_num == 1:
                        straight = -round((xbox_val / 32767) * speed)
                        print("motor_power: {}".format(straight))
                        subprocess.call(["echo {} > /dev/rtmotor_raw_r0".format(straight)], shell=True)
                        subprocess.call(["echo {} > /dev/rtmotor_raw_l0".format(straight)], shell=True)
#                        time.sleep(0.2)
                    #  左正転
                    elif xbox_num == 2:
                        subprocess.call(["echo -{} > /dev/rtmotor_raw_r0".format(speed)], shell=True)
                        subprocess.call(["echo {} > /dev/rtmotor_raw_l0".format(speed)], shell=True)
                    #  右正転
                    elif xbox_num == 5:
                        subprocess.call(["echo {} > /dev/rtmotor_raw_r0".format(speed)], shell=True)
                        subprocess.call(["echo -{} > /dev/rtmotor_raw_l0".format(speed)], shell=True)
                    #  矢印キー入力
                    elif xbox_num == 6:
                        #  矢印(左)：左回転
                        if xbox_val < 0:
                            subprocess.call(["echo -{} > /dev/rtmotor_raw_r0".format(speed)], shell=True)
                            subprocess.call(["echo {} > /dev/rtmotor_raw_l0".format(speed)], shell=True)
                        #  矢印(右)：右回転
                        elif xbox_val > 0:
                            subprocess.call(["echo {} > /dev/rtmotor_raw_r0".format(speed)], shell=True)
                            subprocess.call(["echo -{} > /dev/rtmotor_raw_l0".format(speed)], shell=True)
                    elif xbox_num == 7:
                        #  矢印(上)：前進
                        if xbox_val < 0:
                            subprocess.call(["echo {} > /dev/rtmotor_raw_r0".format(speed)], shell=True)
                            subprocess.call(["echo {} > /dev/rtmotor_raw_l0".format(speed)], shell=True)
                        elif xbox_val > 0:
                        #  矢印(下)：後進
                            subprocess.call(["echo -{} > /dev/rtmotor_raw_r0".format(speed)], shell=True)
                            subprocess.call(["echo -{} > /dev/rtmotor_raw_l0".format(speed)], shell=True)
                    else:
                        subprocess.call(["echo 0 > /dev/rtmotor_raw_r0"], shell=True)
                        subprocess.call(["echo 0 > /dev/rtmotor_raw_l0"], shell=True)
                    subprocess.call(["echo 0 > /dev/rtmotoren0"], shell=True)

#                print( "{0}, {1}, {2}, {3}".format(xbox_time, xbox_val, xbox_type, xbox_num) )
                event = device.read(EVENT_SIZE)
    except IOError:
        print("再起動")
        subprocess.run(["sudo", "reboot"])
    finally:
        pass

if __name__ == "__main__":
    main()