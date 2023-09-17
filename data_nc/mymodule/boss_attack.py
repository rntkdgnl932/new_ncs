
import sys
import time

sys.path.append('C:/my_games/nightcrow/data_nc/mymodule')

import variable as v_


def boss_attack_start(cla):
    from function import imgs_set_, click_pos_reg, click_pos_2
    import numpy as np
    import cv2
    import pyautogui
    from gyucjunji import scan_jungye_setting
    try:

        boss1 = False
        boss2 = False

        print("boss_attack")
        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\boss\\boss_click.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(240, 60, 300, 120, cla, img, 0.85)
        if imgs_ is not None and imgs_ != False:
            print("boss 떳다.")
            boss1 = True

        while boss1 is True:
            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\boss\\boss_click.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(240, 60, 300, 120, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:
                click_pos_reg(imgs_.x, imgs_.y, cla)
                time.sleep(0.1)
            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\boss\\boss_in.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(440, 700, 520, 765, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:
                click_pos_reg(imgs_.x, imgs_.y, cla)
                time.sleep(0.1)
            for i in range(10):
                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\boss\\boss.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(30, 200, 110, 240, cla, img, 0.85)
                if imgs_ is not None and imgs_ != False:
                    click_pos_2(600, 600, cla)
                    pyautogui.keyDown('w')
                    time.sleep(3)
                    pyautogui.keyUp('w')
                    time.sleep(0.1)
                    boss1 = False
                    boss2 = True
                    break
                time.sleep(1)

        while boss2 is True:

            in_ = False

            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\check\\hunting_1.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(400, 850, 600, 900, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("hunting_1", imgs_)
                in_ = True
            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\check\\hunting_2.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(400, 850, 600, 900, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("hunting_2", imgs_)
                in_ = True
            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\check\\hunting_3.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(400, 850, 600, 900, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("hunting_3", imgs_)
                in_ = True

            if in_ == False:
                click_pos_2(930, 850, cla)
                time.sleep(0.1)
            else:
                scan_jungye_setting(cla)
                time.sleep(0.1)
                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\boss\\boss_attack.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(600, 80, 910, 240, cla, img, 0.75)
                if imgs_ is not None and imgs_ != False:
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                    time.sleep(0.1)

            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\boss\\boss_out.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(30, 200, 110, 240, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:
                click_pos_2(230, 90, cla)
                time.sleep(0.5)
                click_pos_2(565, 605, cla)
                time.sleep(0.5)
                boss2 = False

            time.sleep(5)

    except Exception as e:
        print(e)
        return 0




