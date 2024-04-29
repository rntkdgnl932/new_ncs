import time

import requests
import json
# import os
import sys
sys.path.append('C:/my_games/nightcrow/data_nc/mymodule')

import variable as v_


def dungeon_play(cla, result_schedule_):
    try:
        import cv2
        import numpy as np
        from function import text_check_get, int_put_, imgs_set_, click_pos_2, click_pos_reg, drag_pos
        from action import menu_open, clean_screen, in_maul_check, out_check
        from massenger import line_to_me
        from potion import maul_potion_only, juljun_potion_check, juljun_maul_potion
        from get_item import guild_jilyung_get

        print("dungeon")



        complete_ = False

        dungeon_ = result_schedule_.split("_")

        print("던전 시작")

        if dungeon_[1] == "번영":
            dungeon_name = "bunyuong_1"
        elif dungeon_[1] == "수련":
            dungeon_name = "soolyun_1"
        elif dungeon_[1] == "신전":
            dungeon_name = "sinjun_1"
        elif dungeon_[1] == "유적":
            dungeon_name = "youjuk_1"
        elif dungeon_[1] == "동굴":
            dungeon_name = "dongool_1"
        elif dungeon_[1] == "기암":
            dungeon_name = "giam_1"

        dungeon_clear = False

        in_dungeon__ = False

        in_dungeon__count = 0
        while in_dungeon__ is False:
            in_dungeon__count += 1
            if in_dungeon__count > 3:
                in_dungeon__count = 0
                in_dungeon__ = True

            print("던전체크", in_dungeon__count)

            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\dungeon\\different.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(520, 410, 620, 450, cla, img, 0.83)
            if imgs_ is not None and imgs_ != False:
                print("던전 중 실수로 다른 퀘스트 클릭한 경우", imgs_)
                click_pos_2(410, 640, cla)
            else:
                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\character_start\\y_.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(0, 0, 960, 1030, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    click_pos_reg(imgs_.x, imgs_.y, cla)

            time.sleep(1)

            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\dungeon\\juljun_mode.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(400, 50, 600, 160, cla, img, 0.88)
            if imgs_ is not None and imgs_ != False:
                print("juljun_dungeon", imgs_)
                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\dungeon\\dongool_2.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(40, 40, 200, 80, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("dongool_2", imgs_)
                    full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\dungeon\\dongool_hunting.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(400, 880, 560, 960, cla, img, 0.9)
                    if imgs_ is not None and imgs_ != False:
                        print("동굴 사냥중인듯 하다")
                        # 동굴 진입해서 사냥중
                        juljun_attack(cla, dungeon_[1], dungeon_[2])
                    else:
                        for i in range(6):
                            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\dungeon\\juljun_mode.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(400, 50, 600, 160, cla, img, 0.88)
                            if imgs_ is not None and imgs_ != False:
                                print("드래그 중...")
                                drag_pos(360, 550, 600, 550, cla)
                                time.sleep(0.3)
                            else:
                                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\dungeon\\y_1.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(300, 400, 800, 800, cla, img, 0.9)
                                if imgs_ is not None and imgs_ != False:
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                            time.sleep(0.5)
                else:
                    # hereeeee
                    full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\dungeon\\juljun\\" + dungeon_name + ".PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(40, 40, 200, 80, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\dungeon\\gujum.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(400, 880, 560, 960, cla, img, 0.9)
                        if imgs_ is not None and imgs_ != False:
                            for i in range(6):
                                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\dungeon\\juljun_mode.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(400, 50, 600, 160, cla, img, 0.88)
                                if imgs_ is not None and imgs_ != False:
                                    print("드래그 중...")
                                    drag_pos(360, 550, 600, 550, cla)
                                    time.sleep(0.3)
                                else:
                                    full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\dungeon\\y_1.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(300, 400, 800, 800, cla, img, 0.9)
                                    if imgs_ is not None and imgs_ != False:
                                        click_pos_reg(imgs_.x, imgs_.y, cla)

                        else:
                            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\dungeon\\dongool_hunting.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(400, 880, 560, 960, cla, img, 0.9)
                            if imgs_ is not None and imgs_ != False:
                                print("던전 중", dungeon_name)
                                need_count = 0
                                for i in range(10):
                                    result_need = juljun_potion_check(cla)
                                    if result_need == False:
                                        break
                                    else:
                                        need_count += 1
                                        if need_count > 2:
                                            juljun_maul_potion(cla)
                                    time.sleep(0.1)
                            else:
                                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\dungeon\\juljun\\ready.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(400, 880, 560, 960, cla, img, 0.9)
                                if imgs_ is not None and imgs_ != False:

                                    for i in range(6):
                                        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\dungeon\\juljun_mode.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(400, 50, 600, 160, cla, img, 0.88)
                                        if imgs_ is not None and imgs_ != False:
                                            print("드래그 중...")
                                            drag_pos(360, 550, 600, 550, cla)
                                            time.sleep(0.3)
                                        else:
                                            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\dungeon\\y_1.PNG"
                                            img_array = np.fromfile(full_path, np.uint8)
                                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                            imgs_ = imgs_set_(300, 400, 800, 800, cla, img, 0.9)
                                            if imgs_ is not None and imgs_ != False:
                                                click_pos_reg(imgs_.x, imgs_.y, cla)
                                        time.sleep(0.5)
                                    for i in range(10):
                                        result_out = out_check(cla)
                                        if result_out == True:
                                            click_pos_2(930, 850, cla)
                                            break
                                        else:
                                            clean_screen(cla)


                    else:

                        for i in range(6):
                            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\dungeon\\juljun_mode.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(400, 50, 600, 160, cla, img, 0.88)
                            if imgs_ is not None and imgs_ != False:
                                print("드래그 중...")
                                drag_pos(360, 550, 600, 550, cla)
                                time.sleep(0.3)
                            else:
                                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\dungeon\\y_1.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(300, 400, 800, 800, cla, img, 0.9)
                                if imgs_ is not None and imgs_ != False:
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                            time.sleep(0.5)






            else:
                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\dungeon\\" + dungeon_name + ".PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(30, 75, 200, 110, cla, img, 0.75)
                if imgs_ is not None and imgs_ != False:
                    print(dungeon_[1], imgs_)

                    in_dungeon__ = True

                    complete_ = now_playing(cla, dungeon_[1], dungeon_[2])
                else:
                    # 던전 끝났을때
                    full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\dungeon\\y_1.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(300, 400, 800, 800, cla, img, 0.9)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        time.sleep(0.1)


                    # 던전 진입하기
                    in_dungeon_title = False
                    in_dungeon_title_count = 0
                    while in_dungeon_title is False:
                        in_dungeon_title_count += 1
                        if in_dungeon_title_count > 10:
                            in_dungeon_title = True
                        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\dungeon\\dungeon_title.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(40, 40, 100, 80, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            in_dungeon_title = True

                            #던전 진입 전 골드
                            my_money = text_check_get(495, 40, 570, 60, cla)

                            print("내 골드?", my_money)
                            my_money = int_put_(my_money)
                            money_bool = my_money.isdigit()
                            if money_bool == True:
                                my_money = int(my_money)
                                if my_money > 0:

                                    onFG_ = int_put_(v_.onForceGold)
                                    onFG = int(onFG_) * 10000
                                    if my_money < onFG:
                                        in_dungeon__ = True
                                        print("강제로 서브퀘스트 수행하기, 기준골드 : ", v_.onForceGold)
                                        if v_.force_sub_quest != True:
                                            v_.force_sub_quest = True
                                            mg_ = str(my_money) + "골드 있다. 거지다. ㅠㅠ"
                                            line_to_me(cla, mg_)
                                    else:
                                        print("기준골드보다 돈 많다 강제노역 해제하기, 기준골드 : ", v_.onForceGold)
                                        v_.force_sub_quest = False

                            if v_.force_sub_quest == False:
                                if dungeon_[1] == "번영":

                                    click_pos_2(80, 110, cla)
                                    time.sleep(0.2)
                                    click_pos_2(200, 200, cla)

                                    time.sleep(0.2)
                                    for i in range(10):
                                        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\dungeon\\dungeon_clear.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(30, 170, 120, 210, cla, img, 0.8)
                                        if imgs_ is not None and imgs_ != False:
                                            dungeon_clear = True
                                        else:
                                            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\dungeon\\dungeon_clear2.PNG"
                                            img_array = np.fromfile(full_path, np.uint8)
                                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                            imgs_ = imgs_set_(400, 190, 460, 240, cla, img, 0.8)
                                            if imgs_ is not None and imgs_ != False:
                                                dungeon_clear = True
                                            else:
                                                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\dungeon\\event\\manlyo.PNG"
                                                img_array = np.fromfile(full_path, np.uint8)
                                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                                imgs_ = imgs_set_(390, 180, 540, 240, cla, img, 0.8)
                                                if imgs_ is not None and imgs_ != False:
                                                    dungeon_clear = True
                                        time.sleep(0.2)

                                    full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\dungeon\\not_open.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(30, 140, 260, 230, cla, img, 0.8)
                                    if imgs_ is not None and imgs_ != False:
                                        print("not_open 보여", imgs_)
                                        line_to_me(cla, "번영 아직 오픈 못했다.")
                                        dungeon_clear = True

                                    if dungeon_clear == False:
                                        click_pos_2(200, 200, cla)
                                elif dungeon_[1] == "수련":

                                    click_pos_2(80, 110, cla)
                                    time.sleep(0.2)
                                    click_pos_2(200, 300, cla)
                                    time.sleep(0.2)
                                    for i in range(10):
                                        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\dungeon\\dungeon_clear.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(30, 270, 120, 310, cla, img, 0.8)
                                        if imgs_ is not None and imgs_ != False:
                                            dungeon_clear = True
                                        else:
                                            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\dungeon\\dungeon_clear2.PNG"
                                            img_array = np.fromfile(full_path, np.uint8)
                                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                            imgs_ = imgs_set_(400, 190, 460, 240, cla, img, 0.8)
                                            if imgs_ is not None and imgs_ != False:
                                                dungeon_clear = True
                                            else:
                                                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\dungeon\\event\\manlyo.PNG"
                                                img_array = np.fromfile(full_path, np.uint8)
                                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                                imgs_ = imgs_set_(390, 180, 540, 240, cla, img, 0.8)
                                                if imgs_ is not None and imgs_ != False:
                                                    dungeon_clear = True
                                        time.sleep(0.2)

                                    full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\dungeon\\not_open.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(30, 240, 260, 330, cla, img, 0.8)
                                    if imgs_ is not None and imgs_ != False:
                                        print("not_open 보여", imgs_)
                                        line_to_me(cla, "수련 아직 오픈 못했다.")
                                        dungeon_clear = True

                                    if dungeon_clear == False:
                                        click_pos_2(200, 300, cla)
                                elif dungeon_[1] == "신전":
                                    click_pos_2(80, 110, cla)
                                    time.sleep(0.2)
                                    click_pos_2(200, 400, cla)
                                    time.sleep(0.2)
                                    for i in range(10):
                                        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\dungeon\\dungeon_clear.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(30, 370, 120, 410, cla, img, 0.8)
                                        if imgs_ is not None and imgs_ != False:
                                            dungeon_clear = True
                                        else:
                                            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\dungeon\\dungeon_clear2.PNG"
                                            img_array = np.fromfile(full_path, np.uint8)
                                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                            imgs_ = imgs_set_(400, 190, 460, 240, cla, img, 0.8)
                                            if imgs_ is not None and imgs_ != False:
                                                dungeon_clear = True
                                            else:
                                                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\dungeon\\event\\manlyo.PNG"
                                                img_array = np.fromfile(full_path, np.uint8)
                                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                                imgs_ = imgs_set_(390, 180, 540, 240, cla, img, 0.8)
                                                if imgs_ is not None and imgs_ != False:
                                                    dungeon_clear = True
                                        time.sleep(0.2)

                                    full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\dungeon\\not_open.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(30, 340, 260, 430, cla, img, 0.8)
                                    if imgs_ is not None and imgs_ != False:
                                        print("not_open 보여", imgs_)
                                        line_to_me(cla, "신전 아직 오픈 못했다.")
                                        dungeon_clear = True

                                    if dungeon_clear == False:
                                        click_pos_2(200, 400, cla)
                                elif dungeon_[1] == "유적":
                                    click_pos_2(80, 110, cla)
                                    time.sleep(0.2)
                                    click_pos_2(200, 500, cla)
                                    time.sleep(0.2)
                                    for i in range(10):
                                        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\dungeon\\dungeon_clear.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(30, 470, 120, 510, cla, img, 0.8)
                                        if imgs_ is not None and imgs_ != False:
                                            dungeon_clear = True
                                        else:
                                            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\dungeon\\dungeon_clear2.PNG"
                                            img_array = np.fromfile(full_path, np.uint8)
                                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                            imgs_ = imgs_set_(400, 190, 460, 240, cla, img, 0.8)
                                            if imgs_ is not None and imgs_ != False:
                                                dungeon_clear = True
                                            else:
                                                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\dungeon\\event\\manlyo.PNG"
                                                img_array = np.fromfile(full_path, np.uint8)
                                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                                imgs_ = imgs_set_(390, 180, 540, 240, cla, img, 0.8)
                                                if imgs_ is not None and imgs_ != False:
                                                    dungeon_clear = True
                                        time.sleep(0.2)

                                    full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\dungeon\\not_open.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(30, 440, 260, 530, cla, img, 0.8)
                                    if imgs_ is not None and imgs_ != False:
                                        print("not_open 보여", imgs_)
                                        line_to_me(cla, "유적 아직 오픈 못했다.")
                                        dungeon_clear = True

                                    if dungeon_clear == False:
                                        click_pos_2(200, 500, cla)
                                elif dungeon_[1] == "동굴":
                                    click_pos_2(210, 110, cla)
                                    time.sleep(0.2)

                                    for i in range(10):
                                        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\dungeon\\dungeon_clear.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(30, 260, 120, 300, cla, img, 0.8)
                                        if imgs_ is not None and imgs_ != False:
                                            dungeon_clear = True
                                        else:
                                            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\dungeon\\dungeon_clear2.PNG"
                                            img_array = np.fromfile(full_path, np.uint8)
                                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                            imgs_ = imgs_set_(400, 190, 460, 240, cla, img, 0.8)
                                            if imgs_ is not None and imgs_ != False:
                                                dungeon_clear = True
                                            else:
                                                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\dungeon\\manlyo.PNG"
                                                img_array = np.fromfile(full_path, np.uint8)
                                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                                imgs_ = imgs_set_(100, 130, 240, 200, cla, img, 0.8)
                                                if imgs_ is not None and imgs_ != False:
                                                    dungeon_clear = True
                                        time.sleep(0.2)



                                    full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\dungeon\\not_open.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(70, 140, 260, 270, cla, img, 0.8)
                                    if imgs_ is not None and imgs_ != False:
                                        print("not_open 보여", imgs_)
                                        line_to_me(cla, "동굴 아직 오픈 못했다.")
                                        dungeon_clear = True

                                    if dungeon_clear == False:
                                        click_pos_2(200, 200, cla)
                                        
                                # 얼음 동굴 서버 꽉 찰 경우 클리어 해버리기 추후에 하기
                                # 얼음 동굴 서버 꽉 찰 경우 클리어 해버리기 추후에 하기
                                # 얼음 동굴 서버 꽉 찰 경우 클리어 해버리기 추후에 하기
                                # 얼음 동굴 서버 꽉 찰 경우 클리어 해버리기 추후에 하기
                                # 얼음 동굴 서버 꽉 찰 경우 클리어 해버리기 추후에 하기
                                # 얼음 동굴 서버 꽉 찰 경우 클리어 해버리기 추후에 하기
                                # 얼음 동굴 서버 꽉 찰 경우 클리어 해버리기 추후에 하기
                                # 얼음 동굴 서버 꽉 찰 경우 클리어 해버리기 추후에 하기
                                # 얼음 동굴 서버 꽉 찰 경우 클리어 해버리기 추후에 하기# 얼음 동굴 서버 꽉 찰 경우 클리어 해버리기 추후에 하기
                                # 얼음 동굴 서버 꽉 찰 경우 클리어 해버리기 추후에 하기
                                # 얼음 동굴 서버 꽉 찰 경우 클리어 해버리기 추후에 하기
                                # for i in range(20):
                                #     full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\dungeon\\chogwa_.PNG"
                                #     img_array = np.fromfile(full_path, np.uint8)
                                #     img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                #     imgs_ = imgs_set_(200, 80, 700, 120, cla, img, 0.85)
                                #     if imgs_ is not None and imgs_ != False:
                                #         print("chogwa_!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!", imgs_)
                                #         in_dungeon__ = True
                                #         dungeon_clear = True
                                #         complete_ = True
                                #         break
                                #     else:
                                #         full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\dungeon\\already_in.PNG"
                                #         img_array = np.fromfile(full_path, np.uint8)
                                #         img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                #         imgs_ = imgs_set_(420, 80, 500, 120, cla, img, 0.8)
                                #         if imgs_ is not None and imgs_ != False:
                                #             print("already_in!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!", imgs_)
                                #             click_pos_2(930, 60, cla)
                                #             break
                                #
                                #     full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\dead_die\\not_enough_gold.PNG"
                                #     img_array = np.fromfile(full_path, np.uint8)
                                #     img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                #     imgs_ = imgs_set_(400, 60, 600, 120, cla, img, 0.8)
                                #     if imgs_ is not None and imgs_ != False:
                                #         v_.force_sub_quest = True
                                #         in_dungeon__ = True
                                #         in_dungeon_title = True
                                #         click_pos_2(930, 60, cla)
                                #         print("not_enough_gold")
                                #         break
                                #     else:
                                #         full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\dead_die\\not_enough_gold.PNG"
                                #         img_array = np.fromfile(full_path, np.uint8)
                                #         img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                #         imgs_ = imgs_set_(400, 60, 600, 120, cla, img, 0.8)
                                #         if imgs_ is not None and imgs_ != False:
                                #             v_.force_sub_quest = True
                                #             in_dungeon__ = True
                                #             in_dungeon_title = True
                                #             click_pos_2(930, 60, cla)
                                #             print("not_enough_gold2")
                                #             break
                                #
                                #     time.sleep(0.1)
                                time.sleep(0.2)

                        else:

                            # if dungeon_name == "dongool_1":
                            #     result_maul = in_maul_check(cla)
                            #     if result_maul == True:
                            #         maul_potion_only(v_.now_cla)

                            menu_open(cla)
                            click_pos_2(840, 200, cla)
                            for i in range(10):
                                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\dungeon\\dungeon_title.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(40, 40, 100, 80, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    break
                                else:
                                    print("진입중")
                                time.sleep(0.5)
                            time.sleep(1)

                        # 들어가기 클릭한 상태임.

                        time.sleep(0.2)
                        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\dungeon\\y_1.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(300, 400, 800, 900, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                        time.sleep(2)

                    if v_.force_sub_quest == False:

                        for i in range(5):
                            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\dungeon\\dungeon_clear2.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(400, 190, 460, 240, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                dungeon_clear = True
                            time.sleep(0.1)

                        if dungeon_clear == False:
                            step_ready = int(dungeon_[2])
                            if dungeon_[1] == "신전":
                                if step_ready == 7:
                                    step_ready = 6
                            print("step_ready", step_ready)
                            # 기암 등 업뎃 이전까지 동굴은 일단 2층만...
                            if dungeon_[1] == "동굴":
                                click_pos_2(800, 220, cla)
                            else:
                                step = 115 + (step_ready * 50)
                                click_pos_2(800, step, cla)
                            time.sleep(1)

                            # 얼음 동굴 서버 꽉 찰 경우 클리어 해버리기 추후에 하기
                            # 얼음 동굴 서버 꽉 찰 경우 클리어 해버리기 추후에 하기
                            # 얼음 동굴 서버 꽉 찰 경우 클리어 해버리기 추후에 하기
                            # 얼음 동굴 서버 꽉 찰 경우 클리어 해버리기 추후에 하기
                            # 얼음 동굴 서버 꽉 찰 경우 클리어 해버리기 추후에 하기
                            # 얼음 동굴 서버 꽉 찰 경우 클리어 해버리기 추후에 하기
                            # 얼음 동굴 서버 꽉 찰 경우 클리어 해버리기 추후에 하기
                            # 얼음 동굴 서버 꽉 찰 경우 클리어 해버리기 추후에 하기
                            # 얼음 동굴 서버 꽉 찰 경우 클리어 해버리기 추후에 하기


                            # click_pos_2(550, 620, cla)
                            # time.sleep(0.3)
                            # click_pos_2(880, 1010, cla)
                            # time.sleep(0.3)

                            for i in range(20):

                                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\clean_screen\\confirm_1.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(480, 600, 620, 640, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    print("confirm_1", imgs_)
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                                    break
                                else:

                                    click_pos_2(880, 1010, cla)
                                    time.sleep(0.5)

                                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\dungeon\\chogwa_.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(200, 80, 700, 120, cla, img, 0.85)
                                if imgs_ is not None and imgs_ != False:
                                    print("chogwa_!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!", imgs_)
                                    in_dungeon__ = True
                                    dungeon_clear = True
                                    complete_ = True
                                    break
                                else:
                                    full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\dungeon\\already_in.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(420, 80, 500, 120, cla, img, 0.8)
                                    if imgs_ is not None and imgs_ != False:
                                        print("already_in!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!", imgs_)
                                        click_pos_2(930, 60, cla)
                                        break
                                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\dead_die\\not_enough_gold.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(400, 60, 600, 120, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    v_.force_sub_quest = True
                                    in_dungeon__ = True
                                    click_pos_2(930, 60, cla)
                                    print("not_enough_gold")
                                    break
                                else:
                                    full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\dead_die\\not_enough_gold.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(400, 60, 600, 120, cla, img, 0.8)
                                    if imgs_ is not None and imgs_ != False:
                                        v_.force_sub_quest = True
                                        in_dungeon__ = True
                                        click_pos_2(930, 60, cla)
                                        print("not_enough_gold2")
                                        break
                                time.sleep(0.3)


                            loop_y = False
                            loop_y_count = 0
                            while loop_y is False:
                                loop_y_count += 1
                                if loop_y_count > 10:
                                    loop_y = True
                                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\dungeon\\y_1.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(300, 400, 700, 800, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    print("y_1", imgs_)
                                    loop_y = True
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\clean_screen\\confirm_1.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(300, 400, 700, 800, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    print("confirm_1", imgs_)
                                    loop_y = True
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                                time.sleep(0.3)
                            time.sleep(0.4)

                            for i in range(10):
                                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\dungeon\\dungeon_title.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(40, 40, 100, 80, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    print("진입중")
                                else:
                                    full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\dungeon\\" + dungeon_name + ".PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(30, 75, 200, 110, cla, img, 0.75)
                                    if imgs_ is not None and imgs_ != False:
                                        print("진입완료")
                                        break
                                time.sleep(1)


                            time.sleep(1)
                            # 진입할때까지 있어보자 3초?
                            three_second = False
                            three_second_count = 0
                            while three_second is False:
                                three_second_count += 1
                                if three_second_count > 10:
                                    three_second = True
                                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\dungeon\\" + dungeon_name + ".PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(30, 75, 200, 110, cla, img, 0.75)
                                if imgs_ is not None and imgs_ != False:
                                    three_second = True
                                    print("던전 진입 완료", dungeon_name)
                                    if dungeon_[1] != "동굴":
                                        guild_jilyung_get(cla, "dungeon")
                                time.sleep(1)

                        else:
                            in_dungeon__ = True
                            complete_ = True
                            print("던전클리어", result_schedule_)
                            time.sleep(0.2)
            time.sleep(1)
        return complete_
    except Exception as e:
        print(e)

def dungeon_1(cla):
    try:
        import cv2
        import numpy as np


        print("hi")


    except Exception as e:
        print(e)

def now_playing(cla, dun_, nowstep):
    import cv2
    import numpy as np
    import random
    from function import text_check_get, int_put_, click_pos_2, click_pos_reg, imgs_set_, drag_pos
    from potion import potion_check, maul_potion_only, maul_potion
    from action import move_check
    from action import clean_screen, out_check, bag_open, skill_check_, in_maul_check, dead_die, fullbag_check
    from get_item import guild_jilyung
    from schedule import myQuest_play_add
    try:

        print("now_dungeon_playing")

        complete_ = False

        if dun_ == "번영":
            dungeon_name = "bunyuong_1"
        elif dun_ == "수련":
            dungeon_name = "soolyun_1"
        elif dun_ == "신전":
            dungeon_name = "sinjun_1"
        elif dun_ == "유적":
            dungeon_name = "youjuk_1"
        elif dun_ == "동굴":
            dungeon_name = "dongool_1"

        #play_ = False

        in_ = False
        in__count = 0
        while in_ is False:

            in__count += 1
            if in__count > 7:
                in_ = True

            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\dungeon\\" + dungeon_name + ".PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(30, 75, 200, 110, cla, img, 0.75)
            if imgs_ is not None and imgs_ != False:


                # 서브퀘스트
                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\grow\\grow_1\\quest_soolock_2.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(800, 90, 960, 800, cla, img, 0.83)
                if imgs_ is not None and imgs_ != False:
                    print("던전 서브 수락", imgs_)
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\grow\\grow_1\\quest_complete_2.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(800, 90, 960, 800, cla, img, 0.83)
                if imgs_ is not None and imgs_ != False:
                    print("던전 서브 완료", imgs_)
                    click_pos_reg(imgs_.x, imgs_.y, cla)

                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\dungeon\\different.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(520, 410, 620, 450, cla, img, 0.83)
                if imgs_ is not None and imgs_ != False:
                    print("던전 중 실수로 다른 퀘스트 클릭한 경우", imgs_)
                    click_pos_2(410, 640, cla)

                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\check\\pvp_1.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(900, 275, 960, 365, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("메뉴 닫자", imgs_)
                    click_pos_2(930, 60, cla)
                    time.sleep(0.1)

                if dun_ != "동굴":
                    full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\clean_screen\\gabang_title.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(820, 80, 910, 120, cla, img, 0.83)
                    if imgs_ is not None and imgs_ != False:
                        print("10초 뒤 가방 닫자")
                        time.sleep(10)
                        click_pos_2(935, 100, cla)

                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\check\\hunting_1.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(300, 850, 600, 900, cla, img, 0.85)
                if imgs_ is not None and imgs_ != False:
                    print("던전이름 : ", dungeon_name, "hunting_1", imgs_)
                    in_ = True
                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\check\\hunting_2.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(300, 850, 600, 900, cla, img, 0.85)
                if imgs_ is not None and imgs_ != False:
                    print("던전이름 : ", dungeon_name, "hunting_2", imgs_)
                    in_ = True
                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\check\\hunting_3.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(300, 850, 600, 900, cla, img, 0.85)
                if imgs_ is not None and imgs_ != False:
                    print("던전이름 : ", dungeon_name, "hunting_3", imgs_)
                    in_ = True

                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\dungeon\\juljun_mode.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(400, 50, 600, 160, cla, img, 0.88)
                if imgs_ is not None and imgs_ != False:
                    full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\dungeon\dongool_2.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(40, 40, 200, 80, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("now_playing...", imgs_)
                        in_ = True


                if in_ == False:
                    clean_screen(cla)


                    if v_.skill_checked_ == False:
                        skill_check_(cla)

                    # drag_pos(480, 250, 480, 600, cla)
                    # time.sleep(1)
                    # click_pos_2(480, 280, cla)
                    # time.sleep(3)
                    if dun_ == "동굴":
                        print("동굴 진입 하즈아!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                        dongool_move(cla, nowstep)
                    # 위까지 동굴 끝

                    # 아래에는 공통 랜덤 이동동



                    else:
                        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\check\\random_move_1.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(250, 960, 420, 1030, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:
                            print("random_move_1", imgs_)
                            in_ = True
                            click_pos_2(345, 995, cla)

                            in_dungeon__ = False

                            in_dungeon__count = 0
                            while in_dungeon__ is False:
                                in_dungeon__count += 1
                                if in_dungeon__count > 10:
                                    in_dungeon__count = 0
                                    in_dungeon__ = True

                                print("랜덤 이동 후 던전 진입 여부 체크")

                                for i in range(10):
                                    full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\dungeon\\" + dungeon_name + ".PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(30, 75, 200, 110, cla, img, 0.75)
                                    if imgs_ is not None and imgs_ != False:
                                        print(dun_, imgs_)
                                        in_dungeon__ = True
                                    time.sleep(1)

                            click_pos_2(930, 850, cla)
                            time.sleep(1)
                        else:
                            bag_open(cla)
                            time.sleep(1)
                            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\check\\random_move_1.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(680, 100, 920, 900, cla, img, 0.7)
                            if imgs_ is not None and imgs_ != False:
                                in_ = True
                                click_pos_2(710, 935, cla)
                                time.sleep(0.5)
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                                time.sleep(0.5)
                                click_pos_2(345, 1000, cla)
                                time.sleep(0.5)
                                clean_screen(cla)

                                in_dungeon__ = False

                                in_dungeon__count = 0
                                while in_dungeon__ is False:
                                    in_dungeon__count += 1
                                    if in_dungeon__count > 10:
                                        in_dungeon__count = 0
                                        in_dungeon__ = True

                                    print("랜덤 이동 후 던전 진입 여부 체크2")
                                    time.sleep(1)

                                    full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\dungeon\\" + dungeon_name + ".PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(30, 75, 200, 110, cla, img, 0.75)
                                    if imgs_ is not None and imgs_ != False:
                                        print(dun_, imgs_)

                                        in_dungeon__ = True

                                click_pos_2(930, 850, cla)
                                time.sleep(1)
                            else:
                                print("랜덤이동서가 없다. 마을 포션 구매하러 가자")

                                maul_che_ = False
                                maul_che_count = 0
                                while maul_che_ is False:
                                    maul_che_count += 1
                                    if maul_che_count > 8:
                                        maul_che_ = True
                                    result_in_maul = in_maul_check(cla)
                                    if result_in_maul == True:
                                        maul_che_ = True
                                        in_ = True
                                        maul_potion(cla)
                                    else:
                                        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\check\\maul_move_1.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(250, 960, 420, 1030, cla, img, 0.7)
                                        if imgs_ is not None and imgs_ != False:
                                            click_pos_reg(imgs_.x, imgs_.y, cla)
                                        # full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\dungeon\\" + dungeon_name + ".PNG"
                                        # img_array = np.fromfile(full_path, np.uint8)
                                        # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        # imgs_ = imgs_set_(30, 75, 200, 110, cla, img, 0.75)
                                        # if imgs_ is not None and imgs_ != False:
                                        #     print("마을로 가주앗 dun_", dun_)
                                        #     full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\check\\maul_move_1.PNG"
                                        #     img_array = np.fromfile(full_path, np.uint8)
                                        #     img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        #     imgs_ = imgs_set_(250, 960, 420, 1030, cla, img, 0.8)
                                        #     if imgs_ is not None and imgs_ != False:
                                        #         click_pos_reg(imgs_.x, imgs_.y, cla)
                                    time.sleep(1)



                else:
                    v_.skill_checked_ = True

                    full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\dungeon\\dongool_1.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(30, 75, 200, 110, cla, img, 0.75)
                    if imgs_ is not None and imgs_ != False:
                        print("동굴 공격중")
                        click_pos_2(25, 970, cla)
                        time.sleep(0.1)
                        # if v_.who_attack_ == False:
                        #     click_pos_2(25, 970, cla)
                        #     v_.who_attack_ = True
                        # else:
                        #     juljun_attack(cla, dun_, nowstep)
                        #     v_.who_attack_ = False
                    else:
                        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\dungeon\\dongool_3.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(30, 75, 200, 110, cla, img, 0.75)
                        if imgs_ is not None and imgs_ != False:
                            print("동굴 공격중")
                            click_pos_2(25, 970, cla)
                            time.sleep(0.1)
                        else:
                            # 던전중일때만
                            print("동굴 말고 다른 던전 공격중...던전이름 : ", dungeon_name)
                            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\dungeon\\" + dungeon_name + ".PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(30, 75, 200, 110, cla, img, 0.75)
                            if imgs_ is not None and imgs_ != False:

                                print("정상적으로 사냥중...총 10초 딜레이중")
                                # 이동서 체크


                                # 포션 체크
                                move_check(cla)
                                time.sleep(0.1)

                                fullbag_check(cla)
                                time.sleep(0.1)

                                potion_check(cla)
                                time.sleep(10)
                                # play_ = True
                                # 여긴 길드 지령 체크하기
                                # 길드 지령..
                                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\guild\\guild_jilyung.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(660, 90, 730, 300, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:

                                    jilyung_is_ = False
                                    jilyung_is_count = 0
                                    while jilyung_is_ is False:
                                        jilyung_is_count += 1
                                        if jilyung_is_count > 5:
                                            jilyung_is_ = True

                                        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\guild\\guild_title.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(20, 30, 100, 80, cla, img, 0.8)
                                        if imgs_ is not None and imgs_ != False:
                                            guild_jilyung(cla, "dungeon")
                                            jilyung_is_ = True
                                        else:
                                            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\guild\\guild_jilyung.PNG"
                                            img_array = np.fromfile(full_path, np.uint8)
                                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                            imgs_ = imgs_set_(660, 90, 730, 300, cla, img, 0.8)
                                            if imgs_ is not None and imgs_ != False:
                                                click_pos_reg(imgs_.x, imgs_.y, cla)

                                        time.sleep(0.4)

                                # start......hereeee

                                # 절전하기
                                click_pos_2(25, 970, cla)
                                time.sleep(0.1)

                            else:
                                print("던전 안이 아니당.")
                                in_ = True
            else:
                print("던전 안이 아니다.")
                in_ = True
        return complete_
    except Exception as e:
        print(e)


def dongool_move(cla, nowstep):
    import numpy as np
    import cv2
    from function import imgs_set_, click_pos_2, click_pos_reg
    from action import dead_die, in_maul_check
    import random
    try:
        print("dongool_move")

        complete_ = False

        go_ice_1 = False
        go_ice_count = 0
        while go_ice_1 is False:
            print("go_ice_count_1", go_ice_count)
            go_ice_count += 1
            if go_ice_count > 10:
                go_ice_1 = True
            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\dungeon\\dongool_1.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(30, 75, 200, 110, cla, img, 0.75)
            if imgs_ is not None and imgs_ != False:
                print("dongool_1", imgs_)
                go_ice_1 = True

            else:
                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\dungeon\\dongool_3.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(30, 75, 200, 110, cla, img, 0.75)
                if imgs_ is not None and imgs_ != False:
                    print("dongool_3", imgs_)
                    go_ice_1 = True
            if go_ice_1 == True:
                go_ice_2 = False
                go_ice_count = 0
                while go_ice_2 is False:
                    print("go_ice_count_2", go_ice_count)
                    go_ice_count += 1
                    if go_ice_count > 10:
                        go_ice_2 = True
                    full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\dungeon\\dungeon_map_1.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(30, 30, 100, 80, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\dungeon\\dungeon_move_1.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(260, 260, 670, 870, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("자동이동")
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                            time.sleep(1)
                            go_ice_2 = True
                            go_ice_3 = False
                            go_ice_count = 0
                            while go_ice_3 is False:
                                print("go_ice_count_3", go_ice_count)
                                go_ice_count += 1
                                if go_ice_count > 10:
                                    go_ice_3 = True
                                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\dungeon\\dungeon_move_1.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(260, 260, 670, 870, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                                    time.sleep(1)
                                else:
                                    full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\dungeon\\dungeon_map_1.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(30, 30, 100, 80, cla, img, 0.8)
                                    if imgs_ is not None and imgs_ != False:
                                        click_pos_2(930, 60, cla)
                                    else:
                                        go_ice_3 = True

                                        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\check\\pvp_1.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(900, 275, 960, 365, cla, img, 0.8)
                                        if imgs_ is not None and imgs_ != False:
                                            print("메뉴 닫자", imgs_)
                                            click_pos_2(930, 60, cla)
                                            time.sleep(0.1)
                                        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\clean_screen\\gabang_title.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(820, 80, 910, 120, cla, img, 0.83)
                                        if imgs_ is not None and imgs_ != False:
                                            print("가방 닫자")
                                            click_pos_2(935, 100, cla)
                                            time.sleep(0.1)
                                        # 여기에 이동중 나타내고 없어질때까지...이동하기
                                        # 이동하다 죽을 경우 dead_die 적용 후 카운트 +1
                                        last_move = False
                                        last_move_count = 0
                                        while last_move is False:
                                            if last_move_count > 5:
                                                last_move = True
                                            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\jadong\\in_spot_walking_2.PNG"
                                            img_array = np.fromfile(full_path, np.uint8)
                                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                            imgs_ = imgs_set_(480, 880, 500, 900, cla, img, 0.8)
                                            if imgs_ is not None and imgs_ != False:
                                                last_move_count = 0
                                                print("동굴 : in_spot_walking_2 보여", last_move_count)

                                                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\check\\pvp_1.PNG"
                                                img_array = np.fromfile(full_path, np.uint8)
                                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                                imgs_ = imgs_set_(900, 275, 960, 365, cla, img, 0.8)
                                                if imgs_ is not None and imgs_ != False:
                                                    print("메뉴 닫자", imgs_)
                                                    click_pos_2(930, 60, cla)
                                                    time.sleep(0.1)
                                                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\clean_screen\\gabang_title.PNG"
                                                img_array = np.fromfile(full_path, np.uint8)
                                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                                imgs_ = imgs_set_(820, 80, 910, 120, cla, img, 0.83)
                                                if imgs_ is not None and imgs_ != False:
                                                    print("가방 닫자")
                                                    click_pos_2(935, 100, cla)
                                                    time.sleep(0.1)

                                            else:
                                                last_move_count += 1
                                                print("동굴 : in_spot_walking_2 안 보여", last_move_count)
                                                # 죽었을 경우...카운트 +1
                                                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\dead_die\\dead_die.PNG"
                                                img_array = np.fromfile(full_path, np.uint8)
                                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                                imgs_ = imgs_set_(700, 800, 960, 1030, cla, img, 0.8)
                                                if imgs_ is not None and imgs_ != False:
                                                    v_.dongool_dead_count += 1
                                                    print("v_.dongool_dead_count (1)", v_.dongool_dead_count)
                                                    dead_die(cla)
                                                    if v_.dongool_dead_count > 3:
                                                        v_.dongool_dead_count = 0
                                                        complete_ = True
                                            time.sleep(0.5)

                                            if last_move == True:
                                                print("도착!!")
                                                click_pos_2(930, 850, cla)
                                            else:
                                                # 죽었을 경우...카운트 +1
                                                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\dead_die\\dead_die.PNG"
                                                img_array = np.fromfile(full_path, np.uint8)
                                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                                imgs_ = imgs_set_(700, 800, 960, 1030, cla, img, 0.8)
                                                if imgs_ is not None and imgs_ != False:
                                                    v_.dongool_dead_count += 1
                                                    print("v_.dongool_dead_count (2)", v_.dongool_dead_count)
                                                    dead_die(cla)
                                                    if v_.dongool_dead_count > 3:
                                                        v_.dongool_dead_count = 0
                                                        complete_ = True
                        else:
                            # 동굴 지도 찍는 위치
                            if int(nowstep) == 1:
                                result_x = random.randint(350, 600)
                                result_y = random.randint(510, 690)
                                click_pos_2(result_x, result_y, cla)
                            if int(nowstep) == 2:
                                result_x = random.randint(410, 555)
                                result_y = random.randint(370, 640)
                                click_pos_2(result_x, result_y, cla)
                            if int(nowstep) == 3:
                                result_x = random.randint(330, 600)
                                result_y = random.randint(460, 680)
                                click_pos_2(result_x, result_y, cla)
                            if int(nowstep) == 4:
                                result_x = random.randint(365, 630)
                                result_y = random.randint(435, 620)
                                click_pos_2(result_x, result_y, cla)
                        time.sleep(0.2)
                    else:
                        # 여기에 눈알 표시 있도록 하기
                        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\jadong\\maul_eye_check.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(0, 0, 55, 80, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("눈알 있다.", imgs_)
                            click_pos_2(110, 160, cla)
                        else:
                            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\jadong\\close_eye_check.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(0, 0, 55, 80, cla, img, 0.84)
                            if imgs_ is not None and imgs_ != False:
                                print("눈알 없다.", imgs_)
                                click_pos_2(30, 55, cla)
                                time.sleep(1)
                                click_pos_2(110, 160, cla)

                    time.sleep(0.3)
            else:
                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\dead_die\\dead_die.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(700, 800, 960, 1030, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    v_.dongool_dead_count += 1
                    print("v_.dongool_dead_count (3)", v_.dongool_dead_count)
                    dead_die(cla)
                    if v_.dongool_dead_count > 3:
                        v_.dongool_dead_count = 0
                        complete_ = True
                else:
                    result_maul_ = in_maul_check
                    if result_maul_ == True:
                        v_.dongool_dead_count += 1
                        print("v_.dongool_dead_count(4)", v_.dongool_dead_count)
                        if v_.dongool_dead_count > 3:
                            v_.dongool_dead_count = 0
                            complete_ = True

            time.sleep(0.3)
        return complete_
    except Exception as e:
        print(e)

def juljun_attack(cla, dun_, nowstep):
    import cv2
    import numpy as np
    from datetime import date, timedelta, datetime
    from function import text_check_get, int_put_, click_pos_2, click_pos_reg, imgs_set_, drag_pos, change_number, imgs_set_num
    from massenger import line_to_me
    from action import in_number_check, bag_open, maul_check, in_maul_check, clean_screen, dead_die, juljun_fullbag_check
    from schedule import myQuest_play_add
    try:
        continue_juljun = False
        while continue_juljun is False:

            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\check\\touching.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(0, 0, 960, 1030, v_.now_cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("touching", imgs_)
            else:
                print("touching 없")

                in_maul_ = False
                print("마을일경우에만 절전 전투모드 잠시 해제")
                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\potion\\janhwa_1.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(0, 90, 220, 350, cla, img, 0.9)
                if imgs_ is not None and imgs_ != False:
                    print("마을이면 스케쥴 진행 ㄱㄱ", imgs_)
                    in_maul_ = True
                else:
                    result_maul = maul_check(v_.now_cla)
                    if result_maul == True:
                        click_pos_2(230, 90, v_.now_cla)
                        in_maul_ = True
                    else:
                        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\dungeon\\gujum.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(400, 880, 560, 960, cla, img, 0.9)
                        if imgs_ is not None and imgs_ != False:
                            in_maul_ = True
                            print("거점이다. 동굴 끝난듯 하다.", imgs_)
                            drag_pos(360, 550, 600, 550, cla)
                            time.sleep(1)

                            for i in range(5):
                                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\dungeon\\gujum.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(400, 880, 560, 960, cla, img, 0.9)
                                if imgs_ is not None and imgs_ != False:
                                    print("드래그중")
                                else:
                                    break
                                time.sleep(0.5)

                            for i in range(5):
                                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\dungeon\\y_1.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(300, 400, 800, 800, cla, img, 0.9)
                                if imgs_ is not None and imgs_ != False:
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                                time.sleep(0.1)
                        else:
                            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\dungeon\\dongool_hunting.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(400, 880, 560, 960, cla, img, 0.9)
                            if imgs_ is not None and imgs_ != False:
                                print("동굴 사냥중인듯 하다", imgs_)
                            else:
                                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\dungeon\\juljun_mode.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(400, 50, 600, 160, cla, img, 0.88)
                                if imgs_ is not None and imgs_ != False:
                                    print("juljun_mode", imgs_)
                                    in_maul_ = True
                                    print("사냥중이지 않다. 다시 체크해보자")
                                    drag_pos(360, 550, 600, 550, cla)

                                    for i in range(5):
                                        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\dungeon\\juljun_mode.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(400, 50, 600, 160, cla, img, 0.88)
                                        if imgs_ is not None and imgs_ != False:
                                            print("드래그 중...")
                                        else:
                                            break
                                        time.sleep(0.5)
                                    time.sleep(0.5)

                                    full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\dungeon\\y_1.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(300, 400, 800, 800, cla, img, 0.9)
                                    if imgs_ is not None and imgs_ != False:
                                        click_pos_reg(imgs_.x, imgs_.y, cla)

                                else:
                                    print("공격 당하는 듯 하다. 이동해버리자")
                                    # continue_juljun
                                    # full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\dungeon\\dongool_1.PNG"
                                    # img_array = np.fromfile(full_path, np.uint8)
                                    # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    # imgs_ = imgs_set_(30, 75, 200, 110, cla, img, 0.75)
                                    # if imgs_ is not None and imgs_ != False:
                                    #     full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\check\\random_move_1.PNG"
                                    #     img_array = np.fromfile(full_path, np.uint8)
                                    #     img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    #     imgs_ = imgs_set_(250, 960, 420, 1030, cla, img, 0.8)
                                    #     if imgs_ is not None and imgs_ != False:
                                    #         print("동굴던전 : 랜덤이동 보여서 클릭")
                                    #         click_pos_reg(imgs_.x, imgs_.y, cla)
                if in_maul_ == True:

                    continue_juljun = True
                    dead_die(cla)
                    print("절전모드 잠시 중지...", v_.dongool_dead_count)
                    if v_.dongool_dead_count > 4:
                        v_.dongool_dead_count = 0
                        myQuest_play_add(cla, v_.now_ing_schedule)
                else:


                    if dun_ == "번영":
                        dungeon_name = "bunyuong_1"
                    elif dun_ == "수련":
                        dungeon_name = "soolyun_1"
                    elif dun_ == "신전":
                        dungeon_name = "sinjun_1"
                    elif dun_ == "유적":
                        dungeon_name = "youjuk_1"
                    elif dun_ == "동굴":
                        dungeon_name = "dongool_1"

                    print("절전모드 피격시 옮기기 모드...동굴에서 죽은 횟수", v_.dongool_dead_count)
                    full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\dungeon\\juljun_mode.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(400, 50, 600, 160, cla, img, 0.88)
                    if imgs_ is not None and imgs_ != False:
                        print("juljun_mode", imgs_)

                        # 공격불가 체크
                        juljun_fullbag_check(cla)
                        time.sleep(0.1)


                        what_potion_ = "none"

                        # 물약 파악
                        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\dungeon\juljun_potion.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(250, 960, 750, 1030, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:
                            what_potion_ = 'small'
                            print("what_potion_ = 'small'")
                        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\dungeon\juljun_potion_2.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(250, 960, 750, 1030, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:
                            what_potion_ = 'middle'
                            print("what_potion_ = 'middle'")

                        if what_potion_ == 'small':

                            potion_need = False

                            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\dungeon\juljun_potion.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(250, 960, 750, 1030, cla, img, 0.7)
                            if imgs_ is not None and imgs_ != False:

                                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\potion\juljun_not_small_potion.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(250, 960, 750, 1030, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    print("what_potion_ = 'not small'")
                                    potion_need = True
                                else:
                                    full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\dungeon\juljun_potion.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(250, 960, 750, 1030, cla, img, 0.7)
                                    if imgs_ is not None and imgs_ != False:
                                        print("juljun_potion 일딴 물약 있다")
                                        x_reg = imgs_.x
                                        y_reg = imgs_.y
                                        if cla == "two":
                                            x_reg = x_reg - 960
                                        elif cla == "three":
                                            x_reg = x_reg - 960 - 960
                                        elif cla == "four":
                                            x_reg = x_reg - 960 - 960 - 960

                                        # potion_ready = text_check_get(476, 1007, 505, 1022, cla)
                                        potion_ready = text_check_get(x_reg - 3, y_reg + 14, x_reg + 26, y_reg + 29, cla)
                                        print("전체4자리 potion_?", potion_ready)
                                        result_num_in = in_number_check(cla, potion_ready)
                                        if result_num_in == True:
                                            potion_ = change_number(potion_ready)
                                            potion = int_put_(potion_)
                                            potion_bloon = potion.isdigit()
                                            if potion_bloon == True:
                                                potion = int(potion)
                                                print("potion?", potion)
                                                if cla == "one":
                                                    v_.mypotion_1 = potion
                                                if cla == "two":
                                                    v_.mypotion_2 = potion
                                                if cla == "three":
                                                    v_.mypotion_3 = potion
                                                if cla == "four":
                                                    v_.mypotion_4 = potion

                                                if potion < 50:
                                                    v_.potion_count += 1
                                                    if v_.potion_count > 3:
                                                        v_.potion_count = 0
                                                        drag_maul_potion_(cla, dun_)
                                                        continue_juljun = True

                                                else:
                                                    v_.potion_count = 0
                                            else:
                                                print("potion => 숫자 아님")
                                        else:
                                            # potion_ready = text_check_get(475, 1007, 497, 1022, cla)
                                            potion_ready = text_check_get(x_reg - 4, y_reg + 14, x_reg + 18, y_reg + 29, cla)
                                            print("앞3자리 potion_2?", potion_ready)
                                            result_num_in = in_number_check(cla, potion_ready)
                                            if result_num_in == True:
                                                potion_ = change_number(potion_ready)
                                                potion = int_put_(potion_)
                                                potion_bloon = potion.isdigit()
                                                if potion_bloon == True:
                                                    potion = int(potion)
                                                    print("potion?", potion)
                                                    if cla == "one":
                                                        v_.mypotion_1 = potion
                                                    if cla == "two":
                                                        v_.mypotion_2 = potion
                                                    if cla == "three":
                                                        v_.mypotion_3 = potion
                                                    if cla == "four":
                                                        v_.mypotion_4 = potion

                                                    if potion < 10:
                                                        v_.potion_count += 1
                                                        if v_.potion_count > 5:
                                                            v_.potion_count = 0
                                                            drag_maul_potion_(cla, dun_)
                                                            continue_juljun = True
                                                    else:
                                                        v_.potion_count = 0
                                                else:
                                                    print("potion => 숫자 아님")
                                            else:
                                                # potion_ready = text_check_get(482, 1007, 505, 1022, cla)
                                                potion_ready = text_check_get(x_reg + 3, y_reg + 14, x_reg + 26, y_reg + 29, cla)
                                                print("뒷3자리 potion_3 =>", potion_ready)
                                                result_num_in = in_number_check(cla, potion_ready)
                                                if result_num_in == True:
                                                    potion_ = change_number(potion_ready)
                                                    potion = int_put_(potion_)
                                                    potion_bloon = potion.isdigit()
                                                    if potion_bloon == True:
                                                        potion = int(potion)
                                                        print("potion?", potion)
                                                        if cla == "one":
                                                            v_.mypotion_1 = potion
                                                        if cla == "two":
                                                            v_.mypotion_2 = potion
                                                        if cla == "three":
                                                            v_.mypotion_3 = potion
                                                        if cla == "four":
                                                            v_.mypotion_4 = potion

                                                        if potion < 50:
                                                            v_.potion_count += 1
                                                            if v_.potion_count > 5:
                                                                v_.potion_count = 0
                                                                drag_maul_potion_(cla, dun_)
                                                                continue_juljun = True
                                                        else:
                                                            v_.potion_count = 0
                                                    else:
                                                        print("potion => 숫자 아님")


                            else:
                                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\potion\\out_potion_2.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(250, 960, 750, 1030, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    print("화면에 물약 존재한다", imgs_)
                                else:
                                    full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\potion\\out_potion_3.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(250, 960, 750, 1030, cla, img, 0.8)
                                    if imgs_ is not None and imgs_ != False:
                                        print("화면에 물약 존재한다", imgs_)
                                    else:
                                        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\dungeon\juljun_potion_2.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(250, 960, 750, 1030, cla, img, 0.7)
                                        if imgs_ is not None and imgs_ != False:
                                            print("small이라고 판단했지만,,, 사실 일딴 큰 물약 있다", imgs_)

                                        else:
                                            print("화면에 물약 존재하지 않는다", v_.potion_count)
                                            v_.potion_count += 1
                                            print("not have potoin?", v_.potion_count)
                                            if v_.potion_count > 3:

                                                # 마지막 점검
                                                last_potion = False
                                                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\dungeon\juljun_potion.PNG"
                                                img_array = np.fromfile(full_path, np.uint8)
                                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                                imgs_ = imgs_set_(250, 960, 750, 1030, cla, img, 0.7)
                                                if imgs_ is not None and imgs_ != False:
                                                    print("what_potion_ = 'small'")
                                                    full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\potion\juljun_not_small_potion.PNG"
                                                    img_array = np.fromfile(full_path, np.uint8)
                                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                                    imgs_ = imgs_set_(250, 960, 750, 1030, cla, img, 0.8)
                                                    if imgs_ is not None and imgs_ != False:
                                                        print("what_potion_ = 'not small'")
                                                        last_potion = True
                                                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\dungeon\juljun_potion_2.PNG"
                                                img_array = np.fromfile(full_path, np.uint8)
                                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                                imgs_ = imgs_set_(250, 960, 750, 1030, cla, img, 0.7)
                                                if imgs_ is not None and imgs_ != False:
                                                    print("what_potion_ = 'middle'")
                                                    full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\potion\juljun_not_middle_potion.PNG"
                                                    img_array = np.fromfile(full_path, np.uint8)
                                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                                    imgs_ = imgs_set_(250, 960, 750, 1030, cla, img, 0.8)
                                                    if imgs_ is not None and imgs_ != False:
                                                        print("what_potion_ = 'not middle'")
                                                        last_potion = True
                                                if last_potion == True:
                                                    v_.potion_count = 0

                                                    drag_pos(360, 550, 600, 550, cla)
                                                    time.sleep(1)

                                                    bag_open(cla)
                                                    time.sleep(0.2)

                                                    # 물약 찾기
                                                    potion_have = False
                                                    for i in range(10):
                                                        click_pos_2(935, 265, cla)
                                                        time.sleep(0.1)
                                                        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\potion\\potion_in_bag.PNG"
                                                        img_array = np.fromfile(full_path, np.uint8)
                                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                                        imgs_ = imgs_set_(670, 110, 900, 900, cla, img, 0.8)
                                                        if imgs_ is not None and imgs_ != False:
                                                            potion_have = True
                                                            print("가방에 물약 존재한다", imgs_)
                                                            #다시 절전 모드
                                                            click_pos_2(25, 970, cla)
                                                            for k in range(10):
                                                                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\dungeon\\juljun_mode.PNG"
                                                                img_array = np.fromfile(full_path, np.uint8)
                                                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                                                imgs_ = imgs_set_(400, 50, 600, 160, cla, img, 0.88)
                                                                if imgs_ is not None and imgs_ != False:
                                                                    break
                                                                time.sleep(0.3)

                                                            break
                                                        time.sleep(0.1)
                                                    if potion_have == False:
                                                        print("포션 구하러 ㄱㄱ")
                                                        drag_maul_potion_(cla, dun_)
                                                        continue_juljun = True
                            if potion_need == True:
                                print("포션 구하러 ㄱㄱ : potion_need")
                                drag_maul_potion_(cla, dun_)
                                continue_juljun = True
                        elif what_potion_ == 'middle':

                            potion_need = True

                            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\dungeon\juljun_potion_2.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(250, 960, 750, 1030, cla, img, 0.7)
                            if imgs_ is not None and imgs_ != False:

                                print("juljun_potion 일딴 물약 있다")
                                # 424 => - 5 + 15 // 996 => 1005, 1030
                                # 물약 파악
                                if cla == 'one':
                                    minus = 0
                                if cla == 'two':
                                    minus = 960
                                if cla == 'three':
                                    minus = 960 * 2
                                if cla == 'four':
                                    minus = 960 * 3
                                if cla == 'five':
                                    minus = 960 * 4
                                if cla == 'six':
                                    minus = 960 * 5
                                x_reg = imgs_.x
                                for i in range(10):
                                    full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\potion\juljun_number\\" + str(
                                        i) + ".PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_num(x_reg - minus, 1005, x_reg + 13 - minus, 1030, cla, img, 0.8)
                                    if imgs_ is not None and imgs_ != False:
                                        print("100자리 숫자는?'", i, imgs_)
                                        potion_need = False
                                        break





                            else:
                                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\dungeon\juljun_potion_22.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(250, 960, 750, 1030, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    print("화면에 물약 존재한다", imgs_)
                                else:
                                    full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\dungeon\juljun_potion.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(250, 960, 750, 1030, cla, img, 0.7)
                                    if imgs_ is not None and imgs_ != False:
                                        print("미들포션이라고 파악했지만,,, 사실 작은 물약이 있다...")
                                    else:
                                        print("화면에 물약 존재하지 않는다", v_.potion_count)
                                        v_.potion_count += 1
                                        print("not have potoin?", v_.potion_count)
                                        if v_.potion_count > 3:
                                            v_.potion_count = 0

                                            drag_pos(360, 550, 600, 550, cla)
                                            time.sleep(1)

                                            bag_open(cla)
                                            time.sleep(0.2)

                                            # 물약 찾기
                                            potion_have = False
                                            for i in range(10):
                                                click_pos_2(935, 265, cla)
                                                time.sleep(0.1)
                                                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\potion\\potion_in_bag.PNG"
                                                img_array = np.fromfile(full_path, np.uint8)
                                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                                imgs_ = imgs_set_(670, 110, 900, 900, cla, img, 0.8)
                                                if imgs_ is not None and imgs_ != False:
                                                    potion_have = True
                                                    print("가방에 물약 존재한다", imgs_)
                                                    break
                                                time.sleep(0.1)
                                            if potion_have == False:
                                                print("포션 구하러 ㄱㄱ")
                                                drag_maul_potion_(cla, dun_)
                                                continue_juljun = True
                            if potion_need == True:
                                print("포션 구하러 ㄱㄱ : potion_need")
                                drag_maul_potion_(cla, dun_)
                                continue_juljun = True
                    else:
                        nowtime_ = datetime.today().strftime("%Y년%m월%d일 %H시%M분%S초")
                        print("현재시간", nowtime_)

                        # line_to_me(cla, str(nowtime_) + "에 어떤 놈이 공격했다")

                        print("한대 맞은 듯...랜덤 이동 보이면 바로 이동하기!!", v_.dongool_dead_count)



                        # if int(nowstep) >= 3:
                        #
                        #     full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\check\\random_move_1.PNG"
                        #     img_array = np.fromfile(full_path, np.uint8)
                        #     img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        #     imgs_ = imgs_set_(250, 960, 420, 1030, cla, img, 0.8)
                        #     if imgs_ is not None and imgs_ != False:
                        #         print("동굴던전 스텝3 이상 : 랜덤이동 보여서 클릭", v_.dongool_dead_count)
                        #         click_pos_reg(imgs_.x, imgs_.y, cla)
                        # else:
                        #     full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\check\\maul_move_1.PNG"
                        #     img_array = np.fromfile(full_path, np.uint8)
                        #     img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        #     imgs_ = imgs_set_(250, 960, 420, 1030, cla, img, 0.8)
                        #     if imgs_ is not None and imgs_ != False:
                        #         print("동굴던전 스텝3 미만 : 마을이동 보여서 클릭", v_.dongool_dead_count)
                        #         v_.dongool_dead_count += 1
                        #         click_pos_reg(imgs_.x, imgs_.y, cla)

                        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\dead_die\\dead_die.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(700, 800, 960, 1030, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            continue_juljun = True
                            dead_die(cla)
                        # 동굴에서 3번 이상 죽으면 그날 마무리
                        if v_.dongool_dead_count > 3:
                            v_.dongool_dead_count = 0
                            continue_juljun = True
                            myQuest_play_add(cla, v_.now_ing_schedule)


                        else:

                            if int(nowstep) >= 5:
                                in_dungeon__ = False
                                in_dungeon__count = 0
                                while in_dungeon__ is False:
                                    in_dungeon__count += 1
                                    if in_dungeon__count > 10:
                                        in_dungeon__count = 0
                                        in_dungeon__ = True

                                    full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\dungeon\\juljun_mode.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(400, 50, 600, 160, cla, img, 0.88)
                                    if imgs_ is not None and imgs_ != False:
                                        print("juljun_potion_re", imgs_)
                                        in_dungeon__ = True
                                    else:

                                        fast_random_move_ = False
                                        fast_random_move_count = 0
                                        while fast_random_move_ is False:
                                            fast_random_move_count += 1
                                            if fast_random_move_count > 10:
                                                fast_random_move_ = True
                                            # dongool_move(cla, nowstep)
                                            # 이거 5층 미만 안되는 걸로 패치됨
                                            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\check\\random_move_1.PNG"
                                            img_array = np.fromfile(full_path, np.uint8)
                                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                            imgs_ = imgs_set_(250, 960, 420, 1030, cla, img, 0.7)
                                            if imgs_ is not None and imgs_ != False:
                                                print("동굴던전 : 랜덤이동 보여서 클릭")
                                                click_pos_reg(imgs_.x, imgs_.y, cla)
                                                fast_random_move_ = True



                                            else:
                                                print("동굴던전 : 랜덤이동 보이면 클릭")
                                            #이동 했으면 다시 사냥 시작 후 절전모드 하기
                                            time.sleep(0.2)
                                            if fast_random_move_ == True:
                                                juljun_ready = False
                                                juljun_ready_count = 0
                                                while juljun_ready is False:
                                                    juljun_ready_count += 1
                                                    if juljun_ready_count > 10:
                                                        juljun_ready = True

                                                    full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\dungeon\\" + dungeon_name + ".PNG"
                                                    img_array = np.fromfile(full_path, np.uint8)
                                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                                    imgs_ = imgs_set_(30, 75, 200, 110, cla, img, 0.75)
                                                    if imgs_ is not None and imgs_ != False:
                                                        print("동굴 절전모드에서 진행중")
                                                        print(dun_, imgs_)
                                                        # 공격하기

                                                        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\check\\hunting_1.PNG"
                                                        img_array = np.fromfile(full_path, np.uint8)
                                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                                        imgs_ = imgs_set_(300, 850, 600, 900, cla, img, 0.85)
                                                        if imgs_ is not None and imgs_ != False:
                                                            print("절전 hunting_1", imgs_)
                                                            juljun_ready = True
                                                        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\check\\hunting_2.PNG"
                                                        img_array = np.fromfile(full_path, np.uint8)
                                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                                        imgs_ = imgs_set_(300, 850, 600, 900, cla, img, 0.85)
                                                        if imgs_ is not None and imgs_ != False:
                                                            print("절전 hunting_2", imgs_)
                                                            juljun_ready = True
                                                        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\check\\hunting_3.PNG"
                                                        img_array = np.fromfile(full_path, np.uint8)
                                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                                        imgs_ = imgs_set_(300, 850, 600, 900, cla, img, 0.85)
                                                        if imgs_ is not None and imgs_ != False:
                                                            print("절전 hunting_3", imgs_)
                                                            juljun_ready = True

                                                        if juljun_ready == False:
                                                            # 가방 닫기
                                                            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\check\\pvp_1.PNG"
                                                            img_array = np.fromfile(full_path, np.uint8)
                                                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                                            imgs_ = imgs_set_(900, 275, 960, 365, cla, img, 0.8)
                                                            if imgs_ is not None and imgs_ != False:
                                                                print("menu_open 되어있음", imgs_)
                                                                click_pos_2(930, 60, cla)
                                                                time.sleep(0.1)
                                                            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\clean_screen\\gabang_title.PNG"
                                                            img_array = np.fromfile(full_path, np.uint8)
                                                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                                            imgs_ = imgs_set_(820, 80, 910, 120, cla, img, 0.83)
                                                            if imgs_ is not None and imgs_ != False:
                                                                click_pos_2(935, 100, cla)
                                                                time.sleep(0.1)
                                                            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\check\\pvp_1.PNG"
                                                            img_array = np.fromfile(full_path, np.uint8)
                                                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                                            imgs_ = imgs_set_(900, 275, 960, 365, cla, img, 0.8)
                                                            if imgs_ is not None and imgs_ != False:
                                                                print("menu_open 되어있음", imgs_)
                                                                click_pos_2(930, 60, cla)
                                                                time.sleep(0.1)


                                                            juljun_ready = True
                                                            print("동굴던전 : 공격하기 클릭후 절전모드 진입")
                                                            click_pos_2(930, 850, cla)
                                                            time.sleep(1)
                                                            # 절전모드로 다시 진입하기
                                                            click_pos_2(25, 970, cla)
                                                        else:
                                                            # 절전모드로 다시 진입하기
                                                            print("동굴던전 : 공격중이라 절전모드 바로 진입")
                                                            click_pos_2(25, 970, cla)
                                                    else:
                                                        # 마을인지 보기
                                                        print("마을인지 파악")

                                                        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\dungeon\\gujum.PNG"
                                                        img_array = np.fromfile(full_path, np.uint8)
                                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                                        imgs_ = imgs_set_(400, 880, 560, 960, cla, img, 0.9)
                                                        if imgs_ is not None and imgs_ != False:
                                                            print("거점이다. 동굴 끝난듯 하다.", imgs_)
                                                            drag_pos(360, 550, 600, 550, cla)

                                                            for i in range(5):
                                                                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\dungeon\\gujum.PNG"
                                                                img_array = np.fromfile(full_path, np.uint8)
                                                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                                                imgs_ = imgs_set_(400, 880, 560, 960, cla, img, 0.9)
                                                                if imgs_ is not None and imgs_ != False:
                                                                    print("드래그중...,,")
                                                                else:
                                                                    break
                                                                time.sleep(0.5)

                                                            time.sleep(0.5)
                                                            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\dungeon\\y_1.PNG"
                                                            img_array = np.fromfile(full_path, np.uint8)
                                                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                                            imgs_ = imgs_set_(300, 400, 800, 800, cla, img, 0.9)
                                                            if imgs_ is not None and imgs_ != False:
                                                                click_pos_reg(imgs_.x, imgs_.y, cla)
                                                                time.sleep(1)

                                                        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\character_start\\y_.PNG"
                                                        img_array = np.fromfile(full_path, np.uint8)
                                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                                        imgs_ = imgs_set_(0, 0, 960, 1030, cla, img, 0.8)
                                                        if imgs_ is not None and imgs_ != False:
                                                            click_pos_reg(imgs_.x, imgs_.y, cla)
                                                            time.sleep(0.3)

                                                        result_maul_in = in_maul_check(cla)
                                                        if result_maul_in == True:
                                                            juljun_ready = True
                                                            continue_juljun = True
                                                            in_dungeon__ = True
                                                last_juljun = False
                                                last_juljun_count = 0
                                                while last_juljun is False:
                                                    last_juljun_count += 1
                                                    if last_juljun_count > 10:
                                                        last_juljun = True
                                                        continue_juljun = True
                                                        # line_to_me(cla, "동굴던전 진입 오류")
                                                        clean_screen(cla)
                                                    full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\dungeon\\juljun_mode.PNG"
                                                    img_array = np.fromfile(full_path, np.uint8)
                                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                                    imgs_ = imgs_set_(400, 50, 600, 160, cla, img, 0.88)
                                                    if imgs_ is not None and imgs_ != False:
                                                        last_juljun = True
                                                    else:
                                                        print("절전 모드 진입중")
                                                        result_maul_in = in_maul_check(cla)
                                                        if result_maul_in == True:
                                                            continue_juljun = True
                                                            in_dungeon__ = True
                                                            last_juljun = True
                                                    time.sleep(0.2)
                            else:
                                for i in range(10):
                                    full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\check\\maul_move_1.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(250, 960, 420, 1030, cla, img, 0.)
                                    if imgs_ is not None and imgs_ != False:
                                        print("동굴던전 스텝 5 미만 : 마을이동 보여서 클릭", v_.dongool_dead_count, imgs_)
                                        continue_juljun = True
                                        # v_.dongool_dead_count += 1
                                        click_pos_reg(imgs_.x, imgs_.y, cla)
                                        time.sleep(1)
                                    else:
                                        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\potion\\janhwa_1.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(0, 90, 220, 350, cla, img, 0.9)
                                        if imgs_ is not None and imgs_ != False:
                                            break
                                    time.sleep(0.1)









    except Exception as e:
        print(e)

def drag_maul_potion_(cla, dun_):
    try:
        import cv2
        import numpy as np
        from function import text_check_get, int_put_, click_pos_2, click_pos_reg, imgs_set_, drag_pos
        from potion import maul_potion_only
        from action import in_maul_check, out_check, clean_screen

        print("drag_potion")

        if dun_ == "번영":
            dungeon_name = "bunyuong_1"
        elif dun_ == "수련":
            dungeon_name = "soolyun_1"
        elif dun_ == "신전":
            dungeon_name = "sinjun_1"
        elif dun_ == "유적":
            dungeon_name = "youjuk_1"
        elif dun_ == "동굴":
            dungeon_name = "dongool_1"


        go_maul_ = False
        go_maul_count = 0
        while go_maul_ is False:
            go_maul_count += 1
            if go_maul_count > 10:
                go_maul_ = True
            result_maul = in_maul_check(cla)
            if result_maul == True:
                go_maul_= True
                maul_potion_only(cla)


            else:
                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\dungeon\\juljun_mode.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(400, 50, 600, 160, cla, img, 0.88)
                if imgs_ is not None and imgs_ != False:
                    print("juljun_dungeon...", imgs_)
                    drag_pos(360, 550, 600, 550, cla)
                else:
                    full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\dungeon\\dongool_1.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(30, 75, 200, 110, cla, img, 0.75)
                    if imgs_ is not None and imgs_ != False:
                        go_maul_ = True
                        print("동굴 절전모드 포션 구하러 가는 길")
                        print(dun_, imgs_)
                        maul_potion_only(cla)

                    else:

                        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\dungeon\\dongool_3.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(30, 75, 200, 110, cla, img, 0.75)
                        if imgs_ is not None and imgs_ != False:
                            go_maul_ = True
                            print("동굴 절전모드 포션 구하러 가는 길")
                            print(dun_, imgs_)
                            maul_potion_only(cla)

                        else:
                            result_out = out_check(cla)
                            if result_out == True:
                                print("마을이동서 클릭")
                                click_pos_2(290, 990, cla)
                            else:
                                clean_screen(cla)


            time.sleep(1)

    except Exception as e:
        print(e)