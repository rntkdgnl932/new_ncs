import time

from screeninfo import get_monitors
# import os
import sys
sys.path.append('C:/my_games/nightcrow/data_nc/mymodule')

import variable as v_



def go_test():
    from datetime import date, timedelta, datetime
    from function import imgs_set_, click_pos_reg, imgs_set, text_check_get, int_put_, text_check_get_3, click_pos_2, get_region, image_processing, change_number, in_number_check, drag_pos, imgs_set_num, mouse_move_cpp
    from action import menu_open, dead_die_before, item_open, clean_screen, bag_open, quest_look, out_check, go_quest_ing_, character_change
    from get_item import get_items, get_upjuk, get_event, get_season_pass, guild_jilyung
    from jadong_crow import jadong_play
    from realtime import soojib, moogi_, jaelyo_
    from dungeon import drag_maul_potion_
    import numpy as np
    import pyautogui
    import cv2
    import os
    from potion import maul_potion, potion_check, available_potion, maul_potion_only
    from action import skill_check_
    from sell_potion import sell_potion_start
    import requests
    import git
    import pyautogui
    import pytesseract
    import random
    from one_event import daily_one
    from schedule import myQuest_play_check
    from auction_nc import auction_start, jaelyo_out, auction_ready, auction_start2
    from gyucjunji import scan_jungye_setting

    cla = "one"

    # cla = "two"

    if cla == 'one':
        plus = 0
    if cla == 'two':
        plus = 960
    if cla == 'three':
        plus = 960 + 960
    if cla == 'four':
        plus = 960 + 960 + 960

    print("여긴 테스트")

    v_.what_cla = "one클라"
    full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\gyucjunji\\arrive_killdebat.PNG"
    img_array = np.fromfile(full_path, np.uint8)
    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    imgs_ = imgs_set_(250, 390, 370, 450, cla, img, 0.8)
    if imgs_ is not None and imgs_ != False:
        print('kill')
    else:
        print('notttt')


    # result_equal = auction_start(cla)
    # print("result_equal", result_equal)

    # full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\auction\\many\\1000.PNG"
    # img_array = np.fromfile(full_path, np.uint8)
    # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    # imgs_ = imgs_set_num(590, 500, 620, 520, cla, img, 0.99)
    # if imgs_ is not None and imgs_ != False:
    #     print("1000", imgs_)
    # else:
    #     print("1000 안보여")
    #
    # full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\auction\\num\\1000.PNG"
    # img_array = np.fromfile(full_path, np.uint8)
    # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    # imgs_ = imgs_set_num(377, 603, 410, 620, cla, img, 0.99)
    # if imgs_ is not None and imgs_ != False:
    #     print("마지막 거래 금액 : , ", imgs_)

    # moveY = max(-4, -20)
    # print("moveY", moveY)

    # monitors = get_monitors()
    #
    # print("zzzzz", monitors)
    #
    # monitors = get_monitors()
    # last_monitor_number = 0
    # for idx, monitor in enumerate(monitors, start=1):
    #     last_monitor_number = idx
    #
    # print("모니터 갯수", last_monitor_number)

    # for idx, monitor in enumerate(monitors, start=1):
    #     print(f"모니터 {idx} 가로 너비: {monitor.width} 픽셀")
    #     print(f"모니터 {idx} 세로 높이: {monitor.height} 픽셀")
    #     print(f"모니터 {idx} 왼쪽 상단 X 좌표: {monitor.x} 픽셀")
    #     print(f"모니터 {idx} 왼쪽 상단 Y 좌표: {monitor.y} 픽셀")
    #     print(f"모니터 {idx} 오른쪽 하단 X 좌표: {monitor.x + monitor.width} 픽셀")
    #     print(f"모니터 {idx} 오른쪽 하단 Y 좌표: {monitor.y + monitor.height} 픽셀")
    #     print("=" * 50)



    # img = pyautogui.screenshot(region=(get_region(170, 235, 220, 260, cla)))
    # white_img = image_processing(img, (148, 148, 148), (255, 255, 255))
    # potion_ready = pytesseract.image_to_string(white_img, lang=None)
    # # potion_ready = text_check_get(730, 1004, 759, 1016, cla)
    # print("전체4자리 potion_?1111111111111111111", potion_ready)
    #
    # potion_ready = text_check_get(170, 235, 220, 260, cla)
    # print("전체4자리 potion_?222222222222222", potion_ready)

    # sell_potion_start(cla)

    # dir_path = "C:\\my_games\\nightcrow\\data_nc"
    # file_path = dir_path + "\\mymodule\\version.txt"
    #
    # with open(file_path, "r", encoding='utf-8-sig') as file:
    #     v_.version_ = file.read()
    #     print("v_.version_", v_.version_)
    #
    # url = "https://raw.githubusercontent.com/rntkdgnl932/ncs/master/mymodule/version.txt"
    # response = requests.get(url)
    # version_data = response.text
    # print("테스트가 될까?", version_data)
    # if v_.version_ == version_data:
    #     print("버젼이 같다")
    # else:
    #     print("버젼이 다르다. git pull 하고 재실행하자")
    #     # git pull 실행 부분
    #     git_dir = '{https://github.com/rntkdgnl932/ncs.git}'
    #     g = git.cmd.Git(git_dir)
    #     g.pull()
    #     # 실행 후 재시작 부분
    #     os.execl(sys.executable, sys.executable, *sys.argv)



    #
    # full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\check\\point.PNG"
    # img_array = np.fromfile(full_path, np.uint8)
    # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    # imgs_ = imgs_set_(925, 110, 950, 150, cla, img, 0.8)
    # if imgs_ is not None and imgs_ != False:
    #     print("point : soojib", imgs_)

    # hp_ = text_check_get(79, 980, 165, 1030, cla)
    # print("내 체력?", hp_)
    #
    # result_ = go_quest_ing_(cla)
    # print("quest", result_)
    # for i in range(5):
    #     pyautogui.keyDown('a')
    #     time.sleep(0.1)
    #     pyautogui.keyUp('a')
    #     print("aaaaaaaaaaaaaaaa")
    #     time.sleep(1)

    # potion_ = text_check_get(733, 1004, 758, 1016, cla)
    # print("전체4자리 potion_?", potion_)
    # potion_bool = potion_.isdigit()
    # if potion_bool == True:
    #     print("potion_[0]", potion_[0])
    #     if potion_[0] == "0":
    #         potion_ = "1" + potion_
    #         print("potion_ = '1' + potion_", potion_)
    #
    # full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\dungeon\juljun_potion.PNG"
    # img_array = np.fromfile(full_path, np.uint8)
    # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    # imgs_ = imgs_set_(440, 960, 510, 1030, cla, img, 0.8)
    # if imgs_ is not None and imgs_ != False:
    #     print("juljun_potion 일딴 물약 있다", imgs_)
    #
    # potion_ = text_check_get(476, 1007, 505, 1022, cla)
    # print("전체4자리 potion_475?", potion_)
    #
    #
    # for i in range(10):
    #     potion_ = text_check_get(472 + i, 1007, 505, 1022, cla)
    #     print(472 + i)
    #     print("전체4자리", potion_)
    #
    #
    # potion_ = text_check_get(475, 1007, 497, 1022, cla)
    # print("앞3자리 potion_?", potion_)
    #
    # potion_ = text_check_get(482, 1007, 505, 1022, cla)
    # print("뒷3자리 potion_??", potion_)





    # full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\potion\\random_move.PNG"
    # img_array = np.fromfile(full_path, np.uint8)
    # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    # imgs_ = imgs_set_(680, 110, 920, 1000, cla, img, 0.8)
    # if imgs_ is not None and imgs_ != False:
    #     print("already_in___1", imgs_)
    #
    #     if cla == "one":
    #         potion_ = text_check_get(imgs_.x - 10, imgs_.y + 10, imgs_.x + 30, imgs_.y + 30, cla)
    #     if cla == "two":
    #         potion_ = text_check_get(imgs_.x - 10 - 960, imgs_.y + 10, imgs_.x + 30 - 960, imgs_.y + 30, cla)
    #     print("how many 1?", potion_)
    #     print("int_put_(potion_) 1?", int(int_put_(potion_)))
    #
    # full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\potion\\maul_move_.PNG"
    # img_array = np.fromfile(full_path, np.uint8)
    # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    # imgs_ = imgs_set_(680, 110, 920, 1000, cla, img, 0.8)
    # if imgs_ is not None and imgs_ != False:
    #     print("already_in___2", imgs_)
    #
    #     if cla == "one":
    #         potion_ = text_check_get(imgs_.x - 10, imgs_.y + 10, imgs_.x + 30, imgs_.y + 30, cla)
    #     if cla == "two":
    #         potion_ = text_check_get(imgs_.x - 10 - 960, imgs_.y + 10, imgs_.x + 30 - 960, imgs_.y + 30, cla)
    #     print("how many 2?", potion_)
    #     print("int_put_(potion_) 2?", int(int_put_(potion_)))


    # for z in range(3):
    #     last_x = 0
    #     last_y = 0
    #     print("z ? ", z)
    #     if z != 0:
    #         pic_ = "talgut_" + str(z)
    #         full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\grow\\grow_1\\" + pic_ + ".PNG"
    #         img_array = np.fromfile(full_path, np.uint8)
    #         img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    #         for i in pyautogui.locateAllOnScreen(img, region=(680 + plus, 90, 40, 170), confidence=0.7):
    #             last_x = i.left
    #             last_y = i.top
    #             print("last_x", last_x)
    #             print("last_y", last_y)
    #         if last_x != 0:
    #             print("얏호")

    # click_pos_2(700, 110, cla)
    #
    # time.sleep(0.5)
    #
    # full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\grow\\grow_1\\no_talgut_1.PNG"
    # img_array = np.fromfile(full_path, np.uint8)
    # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    # imgs_ = imgs_set_(365, 85, 450, 115, cla, img, 0.8)
    # if imgs_ is not None and imgs_ != False:
    #     print("no_talgut_1", imgs_)
####################################################################
    # full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\potion\\out_potion.PNG"
    # img_array = np.fromfile(full_path, np.uint8)
    # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    # imgs_ = imgs_set_(700, 950, 760, 1030, cla, img, 0.8)
    # if imgs_ is not None and imgs_ != False:
    #     print("화면에 물약 존재한다", imgs_)
    # 
    #     potion_ = text_check_get(730, 1004, 752, 1016, cla)
    #     print("처음3자리 potion_?", potion_)
    #     if len(potion_) != 0:
    # 
    #         if " " in potion_:
    #             potion_ = potion_.replace(' ', '')
    # 
    #             print("!!!!!! ['   '] !!!!!!!", potion_)
    # 
    #         if "|" in potion_:
    #             potion_ = potion_.replace('|', '1')
    # 
    #             print("!!!!!!![   |   ]!!!!!!!!!!!", potion_)
    # 
    #         if "B" in potion_:
    #             potion_ = potion_.replace('B', '8')
    # 
    #             print("!!!!!!!!![  B  ]!!!!!!!!!!!!!", potion_)
    # 
    #         potion = int_put_(potion_)
    #         potion_bloon = potion.isdigit()
    #         if potion_bloon == True:
    #             potion = int(potion)
    #             print("potion?", potion)
    #         else:
    #             print("potion => 숫자 아님")
    #     # else:
    # 
    #     potion_ = text_check_get(738, 1004, 759, 1016, cla)
    #     print("뒷3자리 potion_?", potion_)
    #     if len(potion_) != 0:
    # 
    #         if " " in potion_:
    #             potion_ = potion_.replace(' ', '')
    # 
    #             print("!!!!!! ['   '] !!!!!!!", potion_)
    # 
    #         if "|" in potion_:
    #             potion_ = potion_.replace('|', '1')
    # 
    #             print("!!!!!!![   |   ]!!!!!!!!!!!", potion_)
    # 
    #         if "B" in potion_:
    #             potion_ = potion_.replace('B', '8')
    # 
    #             print("!!!!!!!!![  B  ]!!!!!!!!!!!!!", potion_)
    #         potion = int_put_(potion_)
    #         potion_bloon = potion.isdigit()
    #         if potion_bloon == True:
    #             potion = int(potion)
    #             print("potion?", potion)
    #         else:
    #             print("potion => 숫자 아님")
    # 
    #     potion_ = text_check_get(730, 1004, 758, 1016, cla)
    #     print("전체4자리 potion_?", potion_)
    #     if len(potion_) != 0:
    # 
    #         if " " in potion_:
    #             potion_ = potion_.replace(' ', '')
    # 
    #             print("!!!!!! ['   '] !!!!!!!", potion_)
    # 
    #         if "|" in potion_:
    #             potion_ = potion_.replace('|', '1')
    # 
    #             print("!!!!!!![   |   ]!!!!!!!!!!!", potion_)
    # 
    #         if "B" in potion_:
    #             potion_ = potion_.replace('B', '8')
    # 
    #             print("!!!!!!!!![  B  ]!!!!!!!!!!!!!", potion_)
    #         potion = int_put_(potion_)
    #         potion_bloon = potion.isdigit()
    #         if potion_bloon == True:
    #             potion = int(potion)
    #             print("potion?", potion)
    #         else:
    #             print("potion => 숫자 아님")
    #     potion_ = text_check_get(731, 1004, 758, 1016, cla)
    #     print("전체4자리 potion_2?", potion_)
    #     potion_ = text_check_get(732, 1004, 758, 1016, cla)
    #     print("전체4자리 potion_3?", potion_)
    #     potion_ = text_check_get(733, 1004, 758, 1016, cla)
    #     print("전체4자리 potion_4?", potion_)
    #     potion_ = text_check_get(734, 1004, 758, 1016, cla)
    #     print("전체4자리 potion_5?", potion_)
    ###########################################################################
    # print("<< point 파악 >>")
    #
    # if cla == 'one':
    #     plus = 0
    # if cla == 'two':
    #     plus = 960
    # count_ = 0
    # full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\check\\point.PNG"
    # img_array = np.fromfile(full_path, np.uint8)
    # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    # for i in pyautogui.locateAllOnScreen(img, region=(0 + plus, 0, 960, 1030), confidence=0.75):
    #     count_ += 1
    #
    #     last_x = i.left
    #     last_y = i.top
    #     print("point 넘버 : ", count_)
    #     print("last_x", last_x)
    #     print("last_y", last_y)




