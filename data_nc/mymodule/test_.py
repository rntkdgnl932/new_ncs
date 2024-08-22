import time

from screeninfo import get_monitors
# import os
import sys
sys.path.append('C:/my_games/nightcrow/data_nc/mymodule')

import variable as v_



def go_test():
    from datetime import date, timedelta, datetime
    from function import imgs_set_, click_pos_reg, imgs_set, text_check_get, int_put_, text_check_get_3, click_pos_2, get_region, image_processing, change_number, in_number_check, drag_pos, imgs_set_num, mouse_move_cpp
    from action import menu_open, dead_die_before, item_open, clean_screen, bag_open, quest_look, out_check, go_quest_ing_, character_change, move_check, dead_die
    from get_item import get_items, get_upjuk, get_event, get_season_pass, guild_jilyung, guild_check, get_post
    from jadong_crow import jadong_play
    from realtime import soojib, moogi_, jaelyo_
    from dungeon import drag_maul_potion_
    import numpy as np
    import pyautogui
    import cv2
    import os
    from potion import maul_potion, potion_check, available_potion, maul_potion_only, juljun_potion_check
    from action import skill_check_, mine_check, juljun_fullbag_check
    from sell_potion import sell_potion_start
    import requests
    import git
    import pyautogui
    import pytesseract
    import random
    from one_event import daily_one
    from schedule import myQuest_play_check
    from auction_nc import auction_start, jaelyo_out, auction_ready, auction_open, auction_start2
    from gyucjunji import scan_jungye_setting
    from property_nc import my_property_upload
    from get_item import get_sangjum_gyohwan
    from realtime import boonhae_

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



    #333
    # if dungeon_[1] == "번영":
    #     dungeon_name = "bunyuong_1"
    # elif dungeon_[1] == "수련":
    #     dungeon_name = "soolyun_1"
    # elif dungeon_[1] == "신전":
    #     dungeon_name = "sinjun_1"
    # elif dungeon_[1] == "유적":
    #     dungeon_name = "youjuk_1"

    # for i in range(10):
    #     full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\auction\\many\\" + str(i) + ".PNG"
    #     img_array = np.fromfile(full_path, np.uint8)
    #     img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    #     imgs_ = imgs_set_num(590, 490, 660, 520, cla, img, 0.99)
    #     if imgs_ is not None and imgs_ != False:
    #         data = "현재 최저 금액 : 숫자 " + str(i) + " 보여"
    #         print(data, imgs_)

    get_sangjum_gyohwan(cla)

    # result1 = auction_start("three")
    # print("result1", result1)
    #
    # result2 = auction_start2("three")
    # print("result2", result2)


    # full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\dungeon\juljun_potion_2.PNG"
    # img_array = np.fromfile(full_path, np.uint8)
    # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    # imgs_ = imgs_set_(250, 960, 750, 1030, cla, img, 0.7)
    # if imgs_ is not None and imgs_ != False:
    #     print("juljun_potion 일딴 물약 있다")
    #
    # full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\potion\juljun_not_middle_potion.PNG"
    # img_array = np.fromfile(full_path, np.uint8)
    # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    # imgs_ = imgs_set_(250, 960, 750, 1030, cla, img, 0.8)
    # if imgs_ is not None and imgs_ != False:
    #     print("what_potion_ = 'not middle'")

    # for i in range(5):
    #     num = i + 6
    #     add_x = 0
    #     if num == 10:
    #         add_x = 10
    #     full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\check\\juljun_full_bag_num\\" + str(num) + ".PNG"
    #     img_array = np.fromfile(full_path, np.uint8)
    #     img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    #     imgs_ = imgs_set_num(50, 200, 65 + add_x, 230, cla, img, 0.75)
    #     if imgs_ is not None and imgs_ != False:
    #         print("juljun_full_bag : ", num)
    #         break

    # maul_potion_only(cla)

    # for i in range(10):
    #
    #     full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\potion\\out_number\\" + str(i) + ".PNG"
    #     img_array = np.fromfile(full_path, np.uint8)
    #     img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    #     imgs_ = imgs_set_(390, 1004, 406, 1016, cla, img, 0.83)
    #     if imgs_ is not None and imgs_ != False:
    #         print("숫자는? ", i)
    #         break
    #     else:
    #         full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\potion\\out_number\\out_middle_100.PNG"
    #         img_array = np.fromfile(full_path, np.uint8)
    #         img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    #         imgs_ = imgs_set_(380, 985, 426, 1020, cla, img, 0.83)
    #         if imgs_ is not None and imgs_ != False:
    #             print("물량 100개 이하")
    #             potion_zero = True
    #             break
    #         else:
    #             full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\potion\\out_number\\out_middle_100_2.PNG"
    #             img_array = np.fromfile(full_path, np.uint8)
    #             img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    #             imgs_ = imgs_set_(380, 985, 426, 1020, cla, img, 0.83)
    #             if imgs_ is not None and imgs_ != False:
    #                 print("물량 100개 이하...")
    #                 potion_zero = True
    #                 break
    #
    # full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\potion\\gujum.PNG"
    # img_array = np.fromfile(full_path, np.uint8)
    # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    # imgs_ = imgs_set_(70, 100, 200, 700, cla, img, 0.83)
    # if imgs_ is not None and imgs_ != False:
    #     print("gujum", imgs_)

    # juljun_fullbag_check(cla)

    # full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\boss\\boss_attack.PNG"
    # img_array = np.fromfile(full_path, np.uint8)
    # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    # imgs_ = imgs_set_(600, 80, 910, 240, cla, img, 0.75)
    # if imgs_ is not None and imgs_ != False:
    #     print("boss_attack 떳다.", imgs_)
    #
    # full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\check\\hunting_1.PNG"
    # img_array = np.fromfile(full_path, np.uint8)
    # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    # imgs_ = imgs_set_(350, 850, 600, 900, cla, img, 0.7)
    # if imgs_ is not None and imgs_ != False:
    #     print("보스 hunting_1", imgs_)
    # full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\check\\hunting_2.PNG"
    # img_array = np.fromfile(full_path, np.uint8)
    # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    # imgs_ = imgs_set_(350, 850, 600, 900, cla, img, 0.7)
    # if imgs_ is not None and imgs_ != False:
    #     print("보스 hunting_2", imgs_)
    # full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\check\\hunting_3.PNG"
    # img_array = np.fromfile(full_path, np.uint8)
    # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    # imgs_ = imgs_set_(350, 850, 600, 900, cla, img, 0.7)
    # if imgs_ is not None and imgs_ != False:
    #     print("보스 hunting_3", imgs_)

    # for i in range(5):
    #     full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\dead_die\\dead_gold.PNG"
    #     img_array = np.fromfile(full_path, np.uint8)
    #     img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    #     imgs_ = imgs_set_(220, 870, 270, 910, cla, img, 0.75)
    #     if imgs_ is not None and imgs_ != False:
    #         print("dead_gold 떳다.", imgs_)
    #         break
    #     else:
    #         click_pos_2(95, 895, cla)
    #     time.sleep(0.5)



    # full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\check\\maul_move_1.PNG"
    # img_array = np.fromfile(full_path, np.uint8)
    # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    # imgs_ = imgs_set_(250, 960, 420, 1030, "three", img, 0.7)
    # if imgs_ is not None and imgs_ != False:
    #     print("마을 이동서 있다.", imgs_)
    #
    # full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\check\\random_move_1.PNG"
    # img_array = np.fromfile(full_path, np.uint8)
    # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    # imgs_ = imgs_set_(250, 960, 420, 1030, "three", img, 0.7)
    # if imgs_ is not None and imgs_ != False:
    #     print("랜덤 이동서 있다.", imgs_)


    # result = text_check_get(390, 1004, 406, 1016, cla)
    #
    # for i in range(10):
    #
    #     full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\potion\\out_number\\" + str(i) + ".PNG"
    #     img_array = np.fromfile(full_path, np.uint8)
    #     img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    #     imgs_ = imgs_set_(390, 1004, 406, 1016, cla, img, 0.83)
    #     if imgs_ is not None and imgs_ != False:
    #         print("숫자는? ", i)
    #         break
    #     else:
    #         full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\potion\\out_number\\out_middle_100.PNG"
    #         img_array = np.fromfile(full_path, np.uint8)
    #         img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    #         imgs_ = imgs_set_(380, 985, 406, 1016, cla, img, 0.83)
    #         if imgs_ is not None and imgs_ != False:
    #             print("물량 100개 이하")
    #             break

    # full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\check\\point.PNG"
    # img_array = np.fromfile(full_path, np.uint8)
    # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    # imgs_ = imgs_set_(740, 220, 770, 270, cla, img, 0.8)
    # if imgs_ is not None and imgs_ != False:
    #     print("point 1", imgs_)
    #
    # full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\guild\\guild_des_point.PNG"
    # img_array = np.fromfile(full_path, np.uint8)
    # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    # imgs_ = imgs_set_(450, 920, 490, 970, cla, img, 0.8)
    # if imgs_ is not None and imgs_ != False:
    #     print("guild_des_point 1", imgs_)
    #     click_pos_reg(imgs_.x - 40, imgs_.y + 10, cla)
    #
    # full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\guild\\guild_des_point.PNG"
    # img_array = np.fromfile(full_path, np.uint8)
    # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    # imgs_ = imgs_set_(845, 940, 895, 985, cla, img, 0.8)
    # if imgs_ is not None and imgs_ != False:
    #     print("guild_des_point 2", imgs_)
    #     click_pos_reg(imgs_.x - 40, imgs_.y + 10, cla)

    # full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\dungeon\juljun_potion_2.PNG"
    # img_array = np.fromfile(full_path, np.uint8)
    # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    # imgs_ = imgs_set_(250, 960, 750, 1030, cla, img, 0.9)
    # if imgs_ is not None and imgs_ != False:
    #     print("uljun_potion_2 일딴 물약 있다", imgs_)
    #
    #     full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\potion\juljun_not_middle_potion.PNG"
    #     img_array = np.fromfile(full_path, np.uint8)
    #     img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    #     imgs_ = imgs_set_(250, 960, 750, 1030, cla, img, 0.8)
    #     if imgs_ is not None and imgs_ != False:
    #         print("what_potion_ = 'not middle'")
    #     else:
    #         print("진짜 물약 있다.")
    #
    # else:
    #     print("물약 없다")
    #
    #
    # full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\dungeon\\gujum.PNG"
    # img_array = np.fromfile(full_path, np.uint8)
    # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    # imgs_ = imgs_set_(400, 880, 560, 960, cla, img, 0.9)
    # if imgs_ is not None and imgs_ != False:
    #     print("거점이다. 동굴 끝난듯 하다.", imgs_)
    #
    # full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\dungeon\\dongool_hunting.PNG"
    # img_array = np.fromfile(full_path, np.uint8)
    # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    # imgs_ = imgs_set_(400, 880, 560, 960, cla, img, 0.9)
    # if imgs_ is not None and imgs_ != False:
    #     print("동굴 사냥중인듯 하다", imgs_)
    #
    # full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\dungeon\juljun_mode.PNG"
    # img_array = np.fromfile(full_path, np.uint8)
    # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    # imgs_ = imgs_set_(400, 50, 600, 100, cla, img, 0.8)
    # if imgs_ is not None and imgs_ != False:
    #     print("juljun_mode", imgs_)


    # full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\dungeon\\dungeon_clear.PNG"
    # img_array = np.fromfile(full_path, np.uint8)
    # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    # imgs_ = imgs_set_(30, 360, 120, 400, cla, img, 0.8)
    # if imgs_ is not None and imgs_ != False:
    #     print("dungeon_clear", imgs_)
    # else:
    #     print("nononononononono")
    #
    # full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\dungeon\\dungeon_clear2.PNG"
    # img_array = np.fromfile(full_path, np.uint8)
    # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    # imgs_ = imgs_set_(400, 190, 460, 240, cla, img, 0.8)
    # if imgs_ is not None and imgs_ != False:
    #     print("dungeon_clear2", imgs_)
    # else:
    #     print("nononononononono2222222222222222")

    # my_property_upload(cla)

    # full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\potion\\maul_move_.PNG"
    # img_array = np.fromfile(full_path, np.uint8)
    # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    # imgs_ = imgs_set_(680, 110, 920, 1000, cla, img, 0.8)
    # if imgs_ is not None and imgs_ != False:
    #     x_reg = imgs_.x
    #     if cla == "two":
    #         x_reg = x_reg - 960
    #     y_reg = imgs_.y
    #
    #     img = pyautogui.screenshot(region=(get_region(x_reg - 2, y_reg + 13, x_reg + 28, y_reg + 33, cla)))
    #     white_img = image_processing(img, (148, 148, 148), (255, 255, 255))
    #     move_ = pytesseract.image_to_string(white_img, lang=None)
    #     print("how many random_move?", move_)
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




