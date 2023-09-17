
import sys
import time

sys.path.append('C:/my_games/nightcrow/data_nc/mymodule')

import variable as v_


def boss_attack(cla):
    from datetime import date, timedelta, datetime
    from function import imgs_set_, click_pos_reg, imgs_set, text_check_get, int_put_, text_check_get_3, click_pos_2, get_region, image_processing, change_number, in_number_check, drag_pos
    from action import menu_open, dead_die_before, item_open, clean_screen, bag_open, quest_look, out_check, go_quest_ing_, character_change
    from get_item import get_items, get_upjuk, get_event, get_season_pass
    from jadong_crow import jadong_play
    from realtime import soojib, moogi_
    from dungeon import drag_maul_potion_
    import numpy as np
    import pyautogui
    import cv2
    import os
    from potion import maul_potion
    from action import skill_check_
    from sell_potion import sell_potion_start
    import requests
    import git
    import pyautogui
    import pytesseract
    import random
    from one_event import daily_one

    try:

        boss = False

        print("boss_attack")
        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\boss\\boss_click.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(240, 60, 300, 120, cla, img, 0.85)
        if imgs_ is not None and imgs_ != False:
            print("boss 떳다.")
            boss = True

        while boss is True:
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



    except Exception as e:
        print(e)
        return 0




