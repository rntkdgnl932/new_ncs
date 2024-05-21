import time

import requests
import json
# import os
import sys
sys.path.append('C:/my_games/nightcrow/data_nc/mymodule')

import variable as v_

die_count = 0
item_count = 0


def dead_die(cla):
    try:
        global die_count
        import cv2
        import numpy as np
        from function import text_check_get, int_put_, click_pos_2, click_pos_reg, imgs_set_
        from massenger import line_to_me
        from potion import maul_potion_only

        dead_ = False
        x_reg = 0
        y_reg = 0

        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\dead_die\\dead_die.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(700, 800, 960, 1030, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            dead_ = True
            x_reg = imgs_.x
            y_reg = imgs_.y
        else:
            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\dead_die\\dead_die2.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(700, 800, 960, 1030, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                dead_ = True
                x_reg = imgs_.x
                y_reg = imgs_.y



        if dead_ == True:

            die_count += 1
            print("dead_die", imgs_)
            if x_reg != 0:
                click_pos_reg(x_reg, y_reg, cla)

                for i in range(30):
                    result_out = out_check(cla)
                    if result_out == True:
                        break
                    else:
                        clean_screen(cla)
                    time.sleep(0.5)

            time.sleep(1)
            maul_potion_only(cla)
            if die_count > 4:
                line_to_me(cla, "나크 5번째 죽었다.")
                die_count = 0

                time.sleep(1)

                out_ = False
                out__count = 0
                while out_ is False:

                    out__count += 1
                    if out__count > 7:
                        out_ = True
                    out_ = out_check(cla)
                    if out_ == False:
                        print("dead_clean")
                        clean_screen(cla)
                        line_to_me(cla, "죽은것 같은데 원인 파악하러 빨리 구경와라!!")
                    else:
                        dead_die_before(cla)
                    time.sleep(0.5)
        else:
            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\dead_die\\dead_die_2.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(680, 0, 710, 82, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                dead_ = True
                dead_die_before(cla)


        return dead_
    except Exception as e:
        print(e)

# 죽음 죽어 전에
def dead_die_before(cla):
    try:
        global die_count
        import cv2
        import numpy as np
        from function import text_check_get, int_put_, click_pos_2, click_pos_reg, imgs_set_
        from massenger import line_to_me
        from schedule import myQuest_play_check
        from potion import maul_potion_only

        die_count = 0

        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\dead_die\\dead_die_2.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(680, 0, 710, 82, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("dead_die_2", imgs_)

            result_schedule = myQuest_play_check(cla, "check")
            print("dead_die : result_schedule", result_schedule)
            result_schedule_ = result_schedule[0][2]

            if "_" in result_schedule_:
                dungeon_ = result_schedule_.split("_")
                if dungeon_[1] == "동굴":
                    v_.dongool_dead_count += 1
                if dungeon_[0] == "격전지":
                    v_.gyucjunji_dead_count += 1

            if v_.force_sub_quest == False:

                # 골드 파악후 50만 미만이면 강제로 서브퀘스트 실행
                bag_open(cla)

                die_x = imgs_.x
                die_y = imgs_.y
                click_pos_reg(imgs_.x, imgs_.y, cla)
                dead_die_ = False
                while dead_die_ is False:
                    die_count += 1
                    if die_count > 5:
                        dead_die_ = True
                        die_count = 0
                    full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\dead_die\\exp_.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(50, 80, 150, 115, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\dead_die\\exp_1.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(55, 120, 120, 180, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:

                            for i in range(5):
                                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\dead_die\\dead_gold.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(50, 870, 270, 910, cla, img, 0.75)
                                if imgs_ is not None and imgs_ != False:
                                    click_pos_2(170, 940, cla)
                                    print("dead_gold 떳다.", imgs_)
                                    break
                                else:
                                    click_pos_2(95, 895, cla)
                                time.sleep(0.5)



                            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\dead_die\\not_enough_gold.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(400, 60, 600, 120, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                dead_die_ = True
                                v_.force_sub_quest = True
                            else:
                                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\dead_die\\not_enough_gold2.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(400, 60, 600, 120, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    dead_die_ = True
                                    v_.force_sub_quest = True
                        else:
                            dead_die_ = True
                            die_count = 0
                            click_pos_2(30, 205, cla)
                    else:
                        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\dead_die\\jangbi_.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(50, 80, 150, 115, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            dead_die_ = True
                        else:
                            click_pos_reg(die_x, die_y, cla)
                    time.sleep(0.5)
                dead_die_ = False
                while dead_die_ is False:
                    die_count += 1
                    if die_count > 5:
                        dead_die_ = True
                        die_count = 0
                    full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\dead_die\\jangbi_.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(50, 80, 150, 115, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\dead_die\\jangbi_1.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(55, 120, 120, 180, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:

                            for i in range(5):
                                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\dead_die\\dead_gold.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(50, 870, 270, 910, cla, img, 0.75)
                                if imgs_ is not None and imgs_ != False:
                                    click_pos_2(170, 940, cla)
                                    print("dead_gold 떳다.", imgs_)
                                    break
                                else:
                                    click_pos_2(95, 895, cla)
                                time.sleep(0.5)

                            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\dead_die\\not_enough_gold.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(400, 60, 600, 120, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                dead_die_ = True
                                v_.force_sub_quest = True
                            else:
                                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\dead_die\\not_enough_gold.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(400, 60, 600, 120, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    dead_die_ = True
                                    v_.force_sub_quest = True


                        else:
                            click_pos_2(25, 100, cla)
                            dead_die_ = True
                    else:
                        click_pos_2(30, 250, cla)
                    time.sleep(0.5)
                maul_potion_only(cla)
        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\clean_screen\\exit_3.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(0, 0, 100, 200, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            # clean_screen(cla)
            click_pos_reg(imgs_.x, imgs_.y, cla)

    except Exception as e:
        print(e)


def item_open(cla):
    try:
        global item_count
        from function import click_pos_2, imgs_set, imgs_set_, random_int, drag_pos, text_check_get, click_pos_reg
        from action import bag_open, clean_screen, menu_open
        from realtime import boonhae_

        import os
        import numpy as np
        import cv2

        result_bag = bag_open(cla)
        if result_bag == True:

            click_pos_2(935, 265, cla)
            time.sleep(0.2)

            # 이벤트 아이템

            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\item_1\\event\\event_fly.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(680, 90, 910, 880, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                click_pos_reg(imgs_.x, imgs_.y, cla)
                time.sleep(0.1)
                click_pos_reg(imgs_.x, imgs_.y, cla)
                time.sleep(1)

                tal_3 = False
                tal_3_count = 0
                while tal_3 is False:

                    tal_3_count += 1
                    if tal_3_count > 7:
                        tal_3 = True
                    full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\clean_screen\\glider.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(50, 40, 130, 75, cla, img, 0.83)
                    if imgs_ is not None and imgs_ != False:
                        talgut_ing_(cla)
                        tal_3 = True
                    else:
                        menu_open(cla)
                        click_pos_2(885, 260, cla)
                        time.sleep(1)
                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\check\\bag_check.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(850, 80, 910, 120, cla, img, 0.83)
                if imgs_ is None:
                    bag_open(cla)
                    time.sleep(0.2)
                    click_pos_2(935, 265, cla)
                time.sleep(0.2)

            # 스킬북
            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\item_1\\skillbook_1.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(680, 90, 910, 880, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                click_pos_reg(imgs_.x, imgs_.y, cla)
                time.sleep(0.1)
                click_pos_reg(imgs_.x, imgs_.y, cla)

            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\item_1\\skillbook_2.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(680, 90, 910, 880, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                click_pos_reg(imgs_.x, imgs_.y, cla)
                time.sleep(0.1)
                click_pos_reg(imgs_.x, imgs_.y, cla)

            # 상자

            dir_path = "C:\\my_games\\nightcrow\\data_nc"
            file_path = dir_path + "\\items\\item_open\\bag_item.txt"
            ###
            if os.path.isfile(file_path) == True:
                with open(file_path, "r", encoding='utf-8-sig') as file:
                    box_ = file.read().splitlines()
                    print("box_", box_)
            ###
            for i in range(len(box_)):
                x_reg = 0
                y_reg = 0
                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\item_1\\" + box_[i] + ".PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(680, 90, 910, 880, cla, img, 0.9)
                if imgs_ is not None and imgs_ != False:
                    print("상자 있", box_[i])
                    tal_1 = False
                    while tal_1 is False:
                        item_count += 1
                        print("item_count3", item_count)
                        if item_count > 5:
                            item_count = 0
                            tal_1 = True

                        time.sleep(0.3)
                        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\item_1\\get_clear.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(450, 450, 550, 550, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                            tal_1 = True
                            time.sleep(0.3)
                            for i in range(10):
                                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\item_1\\get_clear.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(450, 450, 550, 550, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                                    time.sleep(0.1)
                                else:
                                    break
                                time.sleep(0.2)

                        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\item_1\\ganghwa.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(30, 30, 140, 80, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("ganghwa.PNG 111111111111111111111111111111111111111111111111", box_[i])
                            tal_1 = True
                            bag_open(cla)
                            time.sleep(0.2)
                            click_pos_2(935, 265, cla)
                            time.sleep(0.2)

                        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\item_1\\max.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(500, 500, 700, 700, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("max.PNG")
                            x_max = imgs_.x
                            y_max = imgs_.y
                            time.sleep(0.2)


                            # 선택
                            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\item_1\\jangsigoo.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(300, 350, 630, 560, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                print("jangsigoo.PNG")
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                                time.sleep(0.1)
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                            else:
                                click_pos_2(585, 460, cla)
                                time.sleep(0.1)
                                click_pos_2(585, 460, cla)
                            time.sleep(0.1)

                            click_pos_reg(x_max, y_max, cla)
                            time.sleep(0.1)
                            click_pos_reg(x_max, y_max, cla)
                            time.sleep(0.3)
                            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\item_1\\confirm_1.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(480, 480, 630, 710, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                tal_1 = True
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                                time.sleep(0.2)
                                click_pos_2(935, 265, cla)
                        else:
                            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\item_1\\" + box_[i] + ".PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(680, 90, 910, 880, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                print("상자 있...", box_[i])
                                x_reg = imgs_.x
                                y_reg = imgs_.y

                                click_pos_reg(x_reg, y_reg, cla)
                                time.sleep(0.1)
                                click_pos_reg(x_reg, y_reg, cla)
                                time.sleep(0.3)

                                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\item_1\\umsik_2.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(330, 400, 630, 550, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                                    time.sleep(0.3)

                                # 여기 크로우 11회 선택하기 누르기
                                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\item_1\\crow_box_2.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(300, 400, 500, 500, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                                    time.sleep(0.3)

                                # full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\item_1\\confirm_1.PNG"
                                # img_array = np.fromfile(full_path, np.uint8)
                                # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                # imgs_ = imgs_set_(480, 480, 630, 710, cla, img, 0.8)
                                # if imgs_ is not None and imgs_ != False:
                                #     tal_1 = True
                                #     click_pos_reg(imgs_.x, imgs_.y, cla)
                                #     time.sleep(0.2)
                                #     click_pos_2(935, 265, cla)
                            else:
                                click_pos_2(935, 265, cla)
                                if x_reg != 0:
                                    # click_pos_reg(x_reg, y_reg, cla)
                                    time.sleep(0.3)
                                    full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\item_1\\confirm_1.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(480, 480, 630, 710, cla, img, 0.8)
                                    if imgs_ is not None and imgs_ != False:
                                        tal_1 = True
                                        click_pos_reg(imgs_.x, imgs_.y, cla)
                                        time.sleep(0.2)
                                        click_pos_2(935, 265, cla)

                        time.sleep(0.3)
                        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\item_1\\get_clear.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(450, 450, 550, 550, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                            tal_1 = True
                else:
                    print("상자 없")
                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\item_1\\exit_1.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(400, 980, 570, 1030, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\check\\bag_check.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(850, 80, 910, 120, cla, img, 0.83)
                if imgs_ is None:
                    bag_open(cla)
                    time.sleep(0.2)
            # 탈것_1
            dir_path = "C:\\my_games\\nightcrow\\data_nc"
            file_path = dir_path + "\\items\\item_open\\talgut.txt"
            ###
            if os.path.isfile(file_path) == True:
                with open(file_path, "r", encoding='utf-8-sig') as file:
                    box_ = file.read().splitlines()
                    print("box_", box_)
            ###

            ###
            print("탈것 시작")
            for i in range(len(box_)):
                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\item_1\\" + box_[i] + ".PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(680, 90, 910, 880, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("탈것 있", box_[i])
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                    time.sleep(0.1)
                    click_pos_reg(imgs_.x, imgs_.y, cla)

                    time.sleep(1)
                    full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\item_1\\max.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(500, 500, 700, 700, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("max.PNG")
                        time.sleep(0.2)
                        click_pos_2(585, 460, cla)
                        time.sleep(0.1)
                        click_pos_2(585, 460, cla)

                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        time.sleep(0.1)
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        time.sleep(0.3)

                    tal_1 = False
                    tal_1_2 = False
                    item_count = 0
                    while tal_1 is False:
                        item_count += 1
                        print("item_count", item_count)
                        if item_count > 20:
                            for i in range(2):
                                click_pos_2(480, 1010, cla)
                                time.sleep(0.1)
                            item_count = 0
                            tal_1 = True
                        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\item_1\\exit_1.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(400, 900, 570, 1030, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                            tal_last = False
                            tal_last_count = 0
                            while tal_last is False:

                                tal_last_count += 1
                                if tal_last_count > 7:
                                    tal_last = True
                                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\item_1\\exit_1.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(400, 900, 570, 1030, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                                else:
                                    tal_1 = True
                                    tal_1_2 = True
                                    tal_last = True
                        else:
                            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\item_1\\y_1.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(400, 400, 700, 1030, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                        time.sleep(0.3)
                        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\item_1\\get_clear.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(450, 450, 550, 550, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                    if tal_1_2 == True:

                        tal_3 = False
                        tal_3_count = 0
                        while tal_3 is False:

                            tal_3_count += 1
                            if tal_3_count > 7:
                                tal_3 = True
                            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\clean_screen\\talgut.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(50, 40, 140, 75, cla, img, 0.83)
                            if imgs_ is not None and imgs_ != False:
                                talgut_ing_(cla)
                                tal_3 = True
                            else:
                                menu_open(cla)
                                time.sleep(0.1)
                                click_pos_2(845, 260, cla)
                                time.sleep(1)
                    full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\check\\bag_check.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(850, 80, 910, 120, cla, img, 0.83)
                    if imgs_ is None:
                        bag_open(cla)
                        time.sleep(0.2)
                        click_pos_2(935, 265, cla)
                    time.sleep(0.2)
                else:
                    print("탈것 없 => ", box_[i])

            # 무기_2
            dir_path = "C:\\my_games\\nightcrow\\data_nc"
            file_path = dir_path + "\\items\\item_open\\moogi.txt"
            ###
            if os.path.isfile(file_path) == True:
                with open(file_path, "r", encoding='utf-8-sig') as file:
                    box_ = file.read().splitlines()
                    print("box_", box_)
            ###
            print("무기 시작")
            for i in range(len(box_)):
                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\item_1\\" + box_[i] + ".PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(680, 90, 910, 880, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("무기 있", box_[i])
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                    time.sleep(0.1)
                    click_pos_reg(imgs_.x, imgs_.y, cla)

                    time.sleep(0.5)
                    full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\item_1\\max.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(500, 500, 700, 700, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("max.PNG")
                        time.sleep(0.2)
                        click_pos_2(585, 460, cla)
                        time.sleep(0.1)
                        click_pos_2(585, 460, cla)

                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        time.sleep(0.1)
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        time.sleep(0.3)

                    tal_1 = False
                    tal_1_2 = False
                    item_count = 0
                    while tal_1 is False:
                        item_count += 1
                        print("item_count3", item_count)
                        if item_count > 20:
                            for i in range(2):
                                click_pos_2(480, 1010, cla)
                                time.sleep(0.1)
                            item_count = 0
                            tal_1 = True
                        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\item_1\\exit_1.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(400, 900, 570, 1030, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                            tal_last = False
                            tal_last_count = 0
                            while tal_last is False:

                                tal_last_count += 1
                                if tal_last_count > 7:
                                    tal_last = True
                                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\item_1\\exit_1.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(400, 900, 570, 1030, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                                else:
                                    tal_1 = True
                                    tal_1_2 = True
                                    tal_last = True
                        else:
                            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\item_1\\y_1.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(400, 400, 700, 1030, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                        time.sleep(0.3)
                        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\item_1\\get_clear.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(450, 450, 550, 550, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                    if tal_1_2 == True:
                        tal_3 = False
                        tal_3_count = 0
                        while tal_3 is False:

                            tal_3_count += 1
                            if tal_3_count > 7:
                                tal_3 = True
                            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\clean_screen\\moogioutlook.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(50, 40, 140, 75, cla, img, 0.83)
                            if imgs_ is not None and imgs_ != False:
                                talgut_ing_(cla)
                                tal_3 = True
                            else:
                                menu_open(cla)
                                click_pos_2(930, 260, cla)
                                time.sleep(1)
                    full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\check\\bag_check.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(850, 80, 910, 120, cla, img, 0.83)
                    if imgs_ is None:
                        bag_open(cla)
                        time.sleep(0.2)
                        click_pos_2(935, 265, cla)
                    time.sleep(0.2)
                else:
                    print("무기_ 없 => ", box_[i])
            # 음식
            x_reg = 0
            y_reg = 0
            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\item_1\\umsik_1.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(680, 90, 910, 880, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("음식 있")
                tal_1 = False
                while tal_1 is False:
                    item_count += 1
                    print("item_count3", item_count)
                    if item_count > 7:
                        item_count = 0
                        tal_1 = True
                    full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\item_1\\umsik_2.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(330, 400, 630, 550, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        time.sleep(0.3)
                        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\item_1\\max.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(500, 500, 700, 700, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                            time.sleep(0.1)
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                        time.sleep(0.3)
                        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\item_1\\confirm_1.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(480, 480, 630, 710, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            tal_1 = True
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                            time.sleep(0.2)
                            click_pos_2(935, 265, cla)
                    else:
                        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\item_1\\umsik_1.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(680, 90, 910, 880, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("음식 있")
                            x_reg = imgs_.x
                            y_reg = imgs_.y
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                            time.sleep(0.1)
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                        else:
                            if x_reg != 0:
                                tal_1 = True
                                click_pos_reg(x_reg, y_reg, cla)

                    time.sleep(0.3)
            else:
                print("음식 없")
            # 상자

            dir_path = "C:\\my_games\\nightcrow\\data_nc"
            file_path = dir_path + "\\items\\item_open\\bag_item.txt"
            ###
            if os.path.isfile(file_path) == True:
                with open(file_path, "r", encoding='utf-8-sig') as file:
                    box_ = file.read().splitlines()
                    print("box_", box_)
            ###
            for i in range(len(box_)):
                x_reg = 0
                y_reg = 0
                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\item_1\\" + box_[i] + ".PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(680, 90, 910, 880, cla, img, 0.9)
                if imgs_ is not None and imgs_ != False:
                    print("상자 있", box_[i])
                    tal_1 = False
                    while tal_1 is False:
                        item_count += 1
                        print("item_count3", item_count)
                        if item_count > 5:
                            item_count = 0
                            tal_1 = True

                        time.sleep(0.3)
                        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\item_1\\get_clear.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(450, 450, 550, 550, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                            tal_1 = True

                        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\item_1\\ganghwa.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(30, 30, 140, 80, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("ganghwa.PNG 111111111111111111111111111111111111111111111111", box_[i])
                            tal_1 = True
                            bag_open(cla)
                            time.sleep(0.2)
                            click_pos_2(935, 265, cla)
                            time.sleep(0.2)

                        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\item_1\\max.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(500, 500, 700, 700, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("max.PNG")
                            time.sleep(0.2)
                            click_pos_2(585, 460, cla)
                            time.sleep(0.1)
                            click_pos_2(585, 460, cla)

                            click_pos_reg(imgs_.x, imgs_.y, cla)
                            time.sleep(0.1)
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                            time.sleep(0.3)
                            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\item_1\\confirm_1.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(480, 480, 630, 710, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                tal_1 = True
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                                time.sleep(0.2)
                                click_pos_2(935, 265, cla)
                        else:
                            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\item_1\\" + box_[i] + ".PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(680, 90, 910, 880, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                print("상자 있...", box_[i])
                                x_reg = imgs_.x
                                y_reg = imgs_.y

                                click_pos_reg(x_reg, y_reg, cla)
                                time.sleep(0.1)
                                click_pos_reg(x_reg, y_reg, cla)
                                time.sleep(0.3)

                                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\item_1\\umsik_2.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(330, 400, 630, 550, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                                    time.sleep(0.3)


                                # 여기 크로우 11회 선택하기 누르기
                                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\item_1\\crow_box_2.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(300, 400, 500, 500, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                                    time.sleep(0.3)


                                # full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\item_1\\confirm_1.PNG"
                                # img_array = np.fromfile(full_path, np.uint8)
                                # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                # imgs_ = imgs_set_(480, 480, 630, 710, cla, img, 0.8)
                                # if imgs_ is not None and imgs_ != False:
                                #     tal_1 = True
                                #     click_pos_reg(imgs_.x, imgs_.y, cla)
                                #     time.sleep(0.2)
                                #     click_pos_2(935, 265, cla)
                            else:
                                click_pos_2(935, 265, cla)
                                if x_reg != 0:
                                    # click_pos_reg(x_reg, y_reg, cla)
                                    time.sleep(0.3)
                                    full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\item_1\\confirm_1.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(480, 480, 630, 710, cla, img, 0.8)
                                    if imgs_ is not None and imgs_ != False:
                                        tal_1 = True
                                        click_pos_reg(imgs_.x, imgs_.y, cla)
                                        time.sleep(0.2)
                                        click_pos_2(935, 265, cla)

                        time.sleep(0.3)
                        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\item_1\\get_clear.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(450, 450, 550, 550, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                            tal_1 = True
                    if box_[i] == "moolja_1":
                        boonhae_(cla)
                else:
                    print("상자 없")
                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\item_1\\exit_1.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(400, 980, 570, 1030, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    click_pos_reg(imgs_.x, imgs_.y, cla)

                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\check\\bag_check.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(850, 80, 910, 120, cla, img, 0.83)
                if imgs_ is None:
                    bag_open(cla)
                time.sleep(0.2)

            # 골드상자
            x_reg = 0
            y_reg = 0
            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\item_1\\gold_1.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(680, 90, 910, 880, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("골드 상자 있", imgs_)
                tal_1 = False
                while tal_1 is False:
                    item_count += 1
                    print("item_count3", item_count)
                    if item_count > 20:
                        item_count = 0
                        tal_1 = True
                    full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\item_1\\max.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(500, 500, 700, 700, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:

                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        time.sleep(0.1)
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        time.sleep(0.3)
                        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\item_1\\confirm_1.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(480, 480, 630, 710, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            tal_1 = True
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                            time.sleep(0.2)
                            click_pos_2(935, 265, cla)

                        time.sleep(0.3)
                    else:
                        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\item_1\\gold_1.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(680, 90, 910, 880, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("골드 상자 있", imgs_)
                            x_reg = imgs_.x
                            y_reg = imgs_.y
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                            time.sleep(0.1)
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                            time.sleep(0.1)
                        else:
                            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\item_1\\gold_1.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(680, 90, 910, 880, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                print("골드 상자 사용 있", imgs_)
                                time.sleep(0.1)
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                            else:
                                print("x_reg", x_reg)
                                if x_reg != 0:
                                    click_pos_reg(x_reg, y_reg, cla)

                    time.sleep(0.3)
                    full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\item_1\\exit_1.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(400, 980, 570, 1030, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_reg(imgs_.x, imgs_.y, cla)

            else:
                print("골드 상자 없")



        # 튜토육성 체크 후 클린스크린
        print("item_open_cleanscreen 1")
        clean_screen(cla)
        print("item_open clean end")
    except Exception as e:
        print(e)

def talgut_ing_(cla):
    try:

        from function import click_pos_2, imgs_set, imgs_set_, random_int, drag_pos, text_check_get, click_pos_reg
        import numpy as np
        import cv2

        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\get_item\\talgut_checked.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(600, 130, 700, 170, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("talgut_checked", imgs_)
            click_pos_2(930, 60, cla)
        else:

            # 탈것
            go_1 = False
            go_2 = False
            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\clean_screen\\talgut.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(50, 40, 90, 75, cla, img, 0.83)
            if imgs_ is not None and imgs_ != False:
                go_1 = True

            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\clean_screen\\glider.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(50, 40, 130, 75, cla, img, 0.83)
            if imgs_ is not None and imgs_ != False:
                go_1 = True

            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\clean_screen\\moogioutlook.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(50, 40, 130, 75, cla, img, 0.83)
            if imgs_ is not None and imgs_ != False:
                go_2 = True



            if go_1 == True:
                print("talgut_ing___", imgs_)
                click_pos_2(740, 200, cla)
                time.sleep(0.3)
                click_pos_2(870, 1010, cla)
                time.sleep(0.3)
                click_pos_2(870, 1010, cla)
                time.sleep(0.3)
                click_pos_2(930, 60, cla)
            if go_2 == True:
                click_pos_2(660, 200, cla)
                time.sleep(0.3)
                click_pos_2(870, 1010, cla)
                time.sleep(0.3)
                click_pos_2(870, 1010, cla)
                time.sleep(0.3)
                click_pos_2(930, 60, cla)


    except Exception as e:
        print(e)

def in_maul_check(cla):
    try:

        from function import click_pos_2, imgs_set, imgs_set_, random_int, drag_pos, text_check_get, click_pos_reg
        import numpy as np
        import cv2

        in_ = False

        maul_list = ["maul_", "maul_a", "maul_b", "maul_c", "maul_d"]
        for i in range(len(maul_list)):
            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\maul\\" + maul_list[i] + ".PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(50, 70, 160, 110, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print(maul_list[i], imgs_)
                in_ = True
        if in_ == True:
            click_pos_2(230, 90, cla)

        time.sleep(0.3)
        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\maul\\jabhwa_1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(0, 70, 220, 330, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("여긴 마을!!!!!!!!!!!!!")
            in_ = True


        return in_
    except Exception as e:
        print(e)


def bag_full_check(cla):
    try:
        import cv2
        import numpy as np
        import pyautogui
        from function import imgs_set_, click_pos_2
        from potion import maul_potion_only
        from realtime import boonhae_
        from massenger import line_to_me

        v_.bag_full_open_count += 1

        if v_.bag_full_open_count == 5:

            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\check\\bag_full_1.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(800, 45, 870, 70, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("point : bag_full_1", imgs_)
                bag_open(cla)
                pyautogui.moveTo(imgs_.x - 100, imgs_.y + 200, 0.1)
                time.sleep(1)
                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\check\\impossibletoattack.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(800, 60, 870, 100, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("point : impossibletoattack", imgs_)
                    line_to_me(cla, "가방 꽉 찼다 확인해줘라")
                    boonhae_(cla)
                    maul_potion_only(cla)

            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\check\\bag_check.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(850, 80, 910, 120, cla, img, 0.83)
            if imgs_ is not None and imgs_ != False:
                click_pos_2(935, 100, cla)
        if v_.bag_full_open_count > 99:
            v_.bag_full_open_count = 0


    except Exception as e:
        print(e)

def bag_open(cla):
    try:
        import cv2
        import numpy as np
        from function import text_check_get, int_put_, click_pos_2, imgs_set_, change_number
        from massenger import line_to_me

        go_ = False
        print("가방열기")

        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\check\\bag_check.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(850, 80, 910, 120, cla, img, 0.83)
        if imgs_ is not None and imgs_ != False:
            go_ = True
        else:
            go_count = 0
            is_go = False
            while is_go is False:
                go_count += 1
                if go_count > 5:
                    is_go = True

                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\check\\bag_check.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(850, 80, 910, 120, cla, img, 0.83)
                if imgs_ is not None and imgs_ != False:
                    print("가방이 열렸드아아아아아")
                    is_go = True
                    go_ = True
                else:
                    out_result = out_check(cla)
                    if out_result == True:



                        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\check\\pvp_1.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(900, 275, 960, 365, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("menu_open 되어있음", imgs_)
                            click_pos_2(930, 60, cla)
                            time.sleep(0.7)
                        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\check\\bag_check.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(850, 80, 910, 120, cla, img, 0.83)
                        if imgs_ is not None and imgs_ != False:
                            print("가방 열었다다")
                            is_go = True
                            go_ = True
                        else:
                            click_pos_2(840, 60, cla)
                            print("가방 열즈아아아아아아아아아")
                        time.sleep(0.5)

                    else:
                        print("bag open clean_screen")
                        clean_screen(cla)
                    time.sleep(0.2)

        if go_ == True:
            # 골드 파악 후 강제노역 시키기
            my_gold_bloon = False
            my_gold_count = 0
            while my_gold_bloon is False:
                my_gold_count += 1
                if my_gold_count > 3:
                    my_gold_bloon = True
                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\check\\gold_g.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(800, 870, 840, 920, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("gold_g", imgs_)

                    # 가방 골드
                    if cla == "one":
                        x_reg = imgs_.x + 10
                    if cla == "two":
                        x_reg = imgs_.x + 10 - 960
                    if cla == "three":
                        x_reg = imgs_.x + 10 - 960 - 960
                    if cla == "four":
                        x_reg = imgs_.x + 10 - 960 - 960 - 960

                    my_money = text_check_get(x_reg, 880, 892, 900, cla)
                    # my_money = text_check_get(830, 880, 892, 900, cla)

                    print("내 골드?", my_money)
                    my_money = change_number(my_money)
                    money_bool = my_money.isdigit()
                    if money_bool == True:
                        my_money = int(my_money)
                        if my_money > 0:
                            my_gold_bloon = True

                            onFG_ = int_put_(v_.onForceGold)
                            onFG = int(onFG_) * 10000
                            if my_money < onFG:

                                re_search_ = False
                                re_search_count = 0
                                while re_search_ is False:
                                    re_search_count += 1
                                    if re_search_count > 5:
                                        re_search_ = True
                                    full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\check\\check_my_gold.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(360, 380, 440, 460, cla, img, 0.8)
                                    if imgs_ is not None and imgs_ != False:
                                        my_money = text_check_get(400, 510, 470, 530, cla)

                                        print("내 골드????", my_money)
                                        my_money = change_number(my_money)
                                        money_bool = my_money.isdigit()
                                        if money_bool == True:
                                            my_money = int(my_money)
                                            if my_money > 0:
                                                re_search_ = True

                                                if my_money < onFG:
                                                    print("강제로 서브퀘스트 수행하기, 기준골드 : ", v_.onForceGold)
                                                    if v_.force_sub_quest != True:
                                                        v_.force_sub_quest = True
                                                        mg_ = str(my_money) + "골드 있다. 거지다. ㅠㅠ"
                                                        line_to_me(cla, mg_)
                                                else:
                                                    if my_money > onFG + 1000000:
                                                        print("기준골드보다 돈 100만원 더 많다 강제노역 해제하기, 기준골드 : ", v_.onForceGold)
                                                        v_.force_sub_quest = False
                                                click_pos_2(860, 895, cla)
                                    else:
                                        click_pos_2(860, 895, cla)
                                    time.sleep(1)
                            else:
                                print("기준골드보다 돈 많다 강제노역 해제하기, 기준골드 : ", v_.onForceGold)
                                v_.force_sub_quest = False
                    time.sleep(1)

        return go_
    except Exception as e:
        print(e)

def gyucjunji_check(cla):
    try:
        import cv2
        import numpy as np
        from function import text_check_get, int_put_, click_pos_2, imgs_set_

        go_ = False

        # 룩 서버는 투합의 방호
        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\gyucjunji\\toohab_1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(50, 70, 160, 110, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("toohab_1")
            go_ = True


        return go_
    except Exception as e:
        print(e)

def maul_check(cla):
    try:
        import cv2
        import numpy as np
        from function import text_check_get, int_put_, click_pos_2, imgs_set_

        go_ = False

        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\jadong\\maul_a.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(50, 70, 160, 110, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("maul_a")
            go_ = True
        else:
            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\jadong\\maul_b.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(50, 70, 160, 110, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("maul_b")
                go_ = True
            else:
                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\jadong\\maul_c.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(50, 70, 160, 110, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("maul_c")
                    go_ = True

        return go_
    except Exception as e:
        print(e)

def skip_click(cla):
    try:
        import cv2
        import numpy as np
        from function import click_pos_2, imgs_set_, click_pos_reg
        # skip
        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\grow\\grow_1\\skip_1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(800, 45, 960, 130, cla, img, 0.83)
        if imgs_ is not None and imgs_ != False:
            print("skip_1", imgs_)
            click_pos_reg(imgs_.x, imgs_.y, cla)
        else:
            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\grow\\grow_1\\skip_3.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(800, 45, 960, 130, cla, img, 0.83)
            if imgs_ is not None and imgs_ != False:
                print("skip_3", imgs_)
                click_pos_reg(imgs_.x, imgs_.y, cla)

        # skip
        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\grow\\grow_1\\skip_2.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(580, 880, 680, 920, cla, img, 0.83)
        if imgs_ is not None and imgs_ != False:
            print("skip_2", imgs_)
            click_pos_reg(imgs_.x, imgs_.y, cla)
    except Exception as e:
        print(e)

def quest_look(cla):
    try:
        import cv2
        import numpy as np
        from function import click_pos_2, imgs_set_

        lq_ = False

        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\check\\quest_check.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(895, 95, 925, 120, cla, img, 0.75)
        if imgs_ is not None and imgs_ != False:
            print("quest_check", imgs_)
            lq_ = True

        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\check\\quest_check_1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(895, 95, 925, 120, cla, img, 0.75)
        if imgs_ is not None and imgs_ != False:
            print("quest_check_1", imgs_)
            lq_ = True

        if lq_ == False:
            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\check\\quest_check2.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(895, 80, 960, 140, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("quest_check2", imgs_)
                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\check\\quest_check.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(895, 95, 925, 120, cla, img, 0.75)
                if imgs_ is not None and imgs_ != False:
                    print("quest_check", imgs_)
                else:
                    click_pos_2(930, 110, cla)
    except Exception as e:
        print(e)

def menu_open(cla):
    try:
        import cv2
        import numpy as np
        from function import text_check_get, int_put_, click_pos_2, imgs_set_
        from get_item import get_items
        from schedule import myQuest_play_check
        from massenger import line_to_me

        go_ = False

        menu_ready_ = False
        menu_ready_count = 0
        while menu_ready_ is False:
            menu_ready_count += 1
            if menu_ready_count > 10:
                menu_ready_ = True
                #line_to_me(cla, "씨팔, 메뉴 여는데 문제 있다.")

            print("menu_open의 out_check")
            out_result = out_check(cla)
            if out_result == True:

                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\check\\pvp_1.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(900, 275, 960, 365, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("pvp_1", imgs_)
                    menu_ready_ = True
                    go_ = True
                else:
                    click_pos_2(930, 60, cla)
                    for i in range(10):
                        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\check\\pvp_1.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(900, 275, 960, 365, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("메뉴 얄럈당")
                            break
                        time.sleep(0.5)




                time.sleep(0.5)
            else:
                print("menu open clean_screen")
                clean_screen(cla)

                print("캐릭터 화면인지 체크")

                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\character_start\\delete_character.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(20, 990, 150, 1040, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:

                    result_schedule = myQuest_play_check(cla, "check")
                    print("menu_open : result_schedule", result_schedule)
                    character_id = result_schedule[0][1]

                    character_change(cla, character_id)

            time.sleep(0.5)




        return go_
    except Exception as e:
        print(e)


def juljun_check(cla):
    import cv2
    import os
    import numpy as np
    from function import text_check_get, int_put_, click_pos_reg, imgs_set_, click_pos_2, drag_pos, imgs_set
    from schedule import myQuest_play_add, myQuest_play_check
    from massenger import line_to_me
    try:
        is_juljun = False
        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\dungeon\\juljun_mode.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(400, 50, 600, 160, cla, img, 0.88)
        if imgs_ is not None and imgs_ != False:
            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\dungeon\\juljun_mode2.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(0, 70, 60, 130, cla, img, 0.88)
            if imgs_ is not None and imgs_ != False:
                is_juljun = True

        return is_juljun

    except Exception as e:
        print(e)

def juljun_off(cla):
    import cv2
    import os
    import numpy as np
    from function import text_check_get, int_put_, click_pos_reg, imgs_set_, click_pos_2, drag_pos, imgs_set
    from schedule import myQuest_play_add, myQuest_play_check
    from massenger import line_to_me
    try:
        is_juljun = False
        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\dungeon\\juljun_mode.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(400, 50, 600, 160, cla, img, 0.88)
        if imgs_ is not None and imgs_ != False:
            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\dungeon\\juljun_mode2.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(0, 70, 60, 130, cla, img, 0.88)
            if imgs_ is not None and imgs_ != False:
                drag_pos(360, 550, 600, 550, cla)


    except Exception as e:
        print(e)

def jangsigan_check(cla):
    import cv2
    import os
    import numpy as np
    from function import text_check_get, int_put_, click_pos_reg, imgs_set_, click_pos_2, drag_pos, imgs_set
    from schedule import myQuest_play_add, myQuest_play_check
    from massenger import line_to_me
    try:
        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\monitor\\jangsigan_1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(300, 450, 700, 550, cla, img, 0.85)
        if imgs_ is not None and imgs_ != False:
            print("장시간이다!!!!!!!!!!!!!!!!")
            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\clean_screen\\confirm_1.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(0, 0, 960, 1030, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:
                print("확인버튼이다!!!!!!!!!!!!!!!!")
                click_pos_reg(imgs_.x, imgs_.y, cla)
                for i in range(20):
                    full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\clean_screen\\anymore_not_look.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(80, 680, 280, 780, cla, img, 0.83)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_2(110, 710, cla)
                        time.sleep(0.3)

                    full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\clean_screen\\nightcrow_i.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(300, 500, 330, 570, cla, img, 0.85)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        time.sleep(0.3)

                    full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\character_start\\game_start_1.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(810, 990, 950, 1040, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        time.sleep(0.2)
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        time.sleep(0.2)
                        for z in range(10):
                            result_out = out_check(cla)
                            if result_out == True:
                                break
                            time.sleep(0.5)
                        break


    except Exception as e:
        print(e)

def clean_screen(cla):
    import cv2
    import os
    import numpy as np
    from function import text_check_get, int_put_, click_pos_reg, imgs_set_, click_pos_2, drag_pos, imgs_set
    from schedule import myQuest_play_add, myQuest_play_check
    from massenger import line_to_me
    try:


        print("<< clean_screen >>")

        # 튕겼는지 확인
        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\check\\nightcrow_title.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(0, 0, 960, 1030, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:


            out_ = False

            # 메인퀘스트 및 서브퀘스트일 경우 스케쥴 추가
            if v_.now_ing_schedule != "none":
                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\dead_die\\dead_die.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(700, 800, 960, 1030, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("/////////////////////////////////////", v_.now_ing_schedule)

                    if v_.force_sub_quest == True:
                        v_.force_sub_quest = False

                    elif v_.now_ing_schedule == "메인퀘스트" or v_.now_ing_schedule == "서브퀘스트":
                        myQuest_play_add(cla, v_.now_ing_schedule)
                        v_.now_ing_schedule = "none"
                        time.sleep(2)
                    # click_pos_reg(imgs_.x, imgs_.y, cla)
                    dead_die(cla)
                    time.sleep(3)
                    full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\dead_die\\dead_die.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(700, 800, 960, 1030, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_reg(imgs_.x, imgs_.y, cla)

            else:
                print("none?", v_.now_ing_schedule)

            # 팝업창 끄기
            # _stop_please(cla)

            # 절전 해제

            result_juljun = juljun_check(cla)
            if result_juljun == True:
                print("juljun_mode : 절전일 경우 해제")
                drag_pos(360, 550, 600, 550, cla)

            else:
                # skip
                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\grow\\grow_1\\skip_1.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(800, 45, 960, 130, cla, img, 0.83)
                if imgs_ is not None and imgs_ != False:
                    print("skip_1", imgs_)
                    click_pos_reg(imgs_.x, imgs_.y, cla)

                # skip
                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\grow\\grow_1\\skip_2.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(580, 880, 680, 920, cla, img, 0.83)
                if imgs_ is not None and imgs_ != False:
                    print("skip_2", imgs_)
                    click_pos_reg(imgs_.x, imgs_.y, cla)

                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\clean_screen\\confirm_1.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(0, 0, 960, 1030, cla, img, 0.83)
                if imgs_ is not None and imgs_ != False:
                    print("confirm_1", imgs_)
                    click_pos_reg(imgs_.x, imgs_.y, cla)



                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\clean_screen\\exit_1.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(800, 0, 960, 120, cla, img, 0.83)
                if imgs_ is not None and imgs_ != False:
                    print("exit_1", imgs_)
                    click_pos_reg(imgs_.x, imgs_.y, cla)


                # dead_die_before 끄기
                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\dead_die\\exp_.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(50, 80, 150, 115, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\clean_screen\\exit_2.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(0, 0, 200, 600, cla, img, 0.83)
                    if imgs_ is not None and imgs_ != False:
                        print("exp_ exit_22", imgs_)
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        time.sleep(1)
                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\dead_die\\jangbi_.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(50, 80, 150, 115, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\clean_screen\\exit_2.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(0, 0, 200, 600, cla, img, 0.83)
                    if imgs_ is not None and imgs_ != False:
                        print("jangbi_ exit_22", imgs_)
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        time.sleep(1)


                # dun_ = ["bunyuong_1", "soolyun_1", "sinjun_1", "youjuk_1", "dongool_1"]
                #
                # for i in range(len(dun_)):
                #     full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\dungeon\\" + dun_[i] + ".PNG"
                #     img_array = np.fromfile(full_path, np.uint8)
                #     img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                #     imgs_ = imgs_set_(50, 75, 150, 110, cla, img, 0.75)
                #     if imgs_ is not None and imgs_ != False:
                #         print(dun_[i], imgs_)
                #         click_pos_2(230, 90, cla)
                #         time.sleep(0.5)
                #         full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\quest\\y_1.PNG"
                #         img_array = np.fromfile(full_path, np.uint8)
                #         img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                #         imgs_ = imgs_set_(50, 75, 800, 1030, cla, img, 0.75)
                #         if imgs_ is not None and imgs_ != False:
                #             print("y_", imgs_)
                #             click_pos_reg(imgs_.x, imgs_.y, cla)

                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\clean_screen\\exit_2.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(500, 0, 960, 600, cla, img, 0.83)
                if imgs_ is not None and imgs_ != False:
                    print("exit_2", imgs_)
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\clean_screen\\exit_3.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(500, 0, 960, 600, cla, img, 0.83)
                if imgs_ is not None and imgs_ != False:
                    print("exit_3", imgs_)
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\item_1\\exit_1.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(400, 900, 570, 1030, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\clean_screen\\setting_1.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(600, 800, 960, 1030, cla, img, 0.83)
                if imgs_ is not None and imgs_ != False:
                    print("setting_1", imgs_)
                    click_pos_2(930, 60, cla)

                clean_out_count = 0
                while out_ is False:
                    clean_out_count += 1
                    if clean_out_count > 5:
                        out_ = True

                    out_nc = False
                    full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\monitor\\out_nc.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set(430, 520, 560, 560, cla, img)
                    if imgs_ is not None and imgs_ != False:
                        out_nc = True
                    full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\monitor\\out_nc2.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set(430, 520, 560, 560, cla, img)
                    if imgs_ is not None and imgs_ != False:
                        out_nc = True

                    if out_nc == True:
                        ms_ = str("나크 ") + str("구글 로그인 화면이다. 꺼진것 같다")
                        line_to_me(cla, ms_)

                        dir_path = "C:\\my_games\\load\\nightcrow"
                        file_path = dir_path + "\\start.txt"
                        file_path2 = dir_path + "\\cla.txt"
                        with open(file_path, "w", encoding='utf-8-sig') as file:
                            data = 'no'
                            file.write(str(data))
                            time.sleep(0.2)
                        with open(file_path2, "w", encoding='utf-8-sig') as file:
                            data = cla
                            file.write(str(data))
                            time.sleep(0.2)

                        os.execl(sys.executable, sys.executable, *sys.argv)

                    else:

                        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\clean_screen\\nightcrow_i.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(300, 500, 330, 570, cla, img, 0.85)
                        if imgs_ is not None and imgs_ != False:
                            for i in range(10):
                                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\clean_screen\\nightcrow_i.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(300, 500, 330, 570, cla, img, 0.85)
                                if imgs_ is not None and imgs_ != False:
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                                else:
                                    break
                                time.sleep(0.2)

                        jangsigan_check(cla)

                        # 던전 끝났을때
                        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\dungeon\\y_1.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(300, 400, 800, 800, cla, img, 0.9)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                            time.sleep(0.1)

                        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\clean_screen\\setting_1.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(600, 800, 960, 1030, cla, img, 0.83)
                        if imgs_ is not None and imgs_ != False:
                            print("setting_1", imgs_)
                            click_pos_2(930, 60, cla)

                        re_1 = go_auto_ing_(cla)
                        re_2 = go_quest_ing_(cla)
                        if re_1 == True or re_2 == True:
                            out_ = True
                            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\check\\pvp_1.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(900, 275, 960, 365, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                print("pvp_1", imgs_)
                                click_pos_2(930, 60, cla)
                        else:
                            print("클린 스크린 바깥 화면이 아니다.")
                            # 더 이상 보지 않음
                            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\clean_screen\\anymore_not_look.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(80, 680, 280, 780, cla, img, 0.83)
                            if imgs_ is not None and imgs_ != False:
                                print("anymore_not_look", imgs_)
                                click_pos_2(110, 710, cla)
                                time.sleep(0.3)
                                click_pos_2(110, 710, cla)

                            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\clean_screen\\logout.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(40, 980, 160, 1030, cla, img, 0.83)
                            if imgs_ is not None and imgs_ != False:
                                print("logout 보여", imgs_)
                                click_pos_2(110, 710, cla)
                                time.sleep(0.3)
                                click_pos_2(110, 710, cla)

                            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\character_start\\delete_character.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(20, 990, 150, 1040, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                result_schedule = myQuest_play_check(cla, "check")
                                print("clean_screen : 캐릭터 선택화면이 보여 result_schedule", result_schedule)
                                character_id = result_schedule[0][1]

                                character_change(cla, character_id)

                            # skip
                            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\grow\\grow_1\\skip_1.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(800, 45, 960, 130, cla, img, 0.83)
                            if imgs_ is not None and imgs_ != False:
                                print("skip_1", imgs_)
                                click_pos_reg(imgs_.x, imgs_.y, cla)

                            # skip
                            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\grow\\grow_1\\skip_2.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(580, 880, 680, 920, cla, img, 0.83)
                            if imgs_ is not None and imgs_ != False:
                                print("skip_2", imgs_)
                                click_pos_reg(imgs_.x, imgs_.y, cla)

                            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\clean_screen\\gabang_title.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(820, 80, 910, 120, cla, img, 0.83)
                            if imgs_ is not None and imgs_ != False:
                                print("clean screen 가방 닫자")
                                click_pos_2(935, 100, cla)

                            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\clean_screen\\confirm_1.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(0, 0, 960, 1030, cla, img, 0.83)
                            if imgs_ is not None and imgs_ != False:
                                print("confirm_1", imgs_)
                                click_pos_reg(imgs_.x, imgs_.y, cla)

                            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\quest\\y_1.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(0, 0, 960, 1030, cla, img, 0.83)
                            if imgs_ is not None and imgs_ != False:
                                print("y_", imgs_)
                                click_pos_reg(imgs_.x, imgs_.y, cla)

                            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\clean_screen\\setting_1.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(600, 800, 960, 1030, cla, img, 0.83)
                            if imgs_ is not None and imgs_ != False:
                                print("setting_1", imgs_)
                                click_pos_2(930, 60, cla)

                            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\clean_screen\\exit_1.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(800, 0, 960, 120, cla, img, 0.83)
                            if imgs_ is not None and imgs_ != False:
                                print("exit_1", imgs_)
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\clean_screen\\exit_2.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(500, 0, 960, 600, cla, img, 0.83)
                            if imgs_ is not None and imgs_ != False:
                                print("exit_2", imgs_)
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\clean_screen\\exit_3.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(500, 0, 960, 600, cla, img, 0.83)
                            if imgs_ is not None and imgs_ != False:
                                print("exit_3", imgs_)
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\check\\bag_check.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(850, 80, 910, 120, cla, img, 0.83)
                            if imgs_ is not None and imgs_ != False:
                                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\clean_screen\\exit_3.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(900, 70, 960, 200, cla, img, 0.83)
                                if imgs_ is not None and imgs_ != False:
                                    click_pos_reg(imgs_.x, imgs_.y, cla)

                            # 물약 닫기
                            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\potion\\cancle.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(360, 720, 470, 770, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_reg(imgs_.x, imgs_.y, cla)
            return out_
        else:

            print("나이트크로우 꺼진것 같은데...10초동안 지켜본다.")

            look_nightcrows = False
            for i in range(10):
                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\check\\nightcrow_title.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(0, 0, 960, 1030, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    look_nightcrows = True
                    break
                time.sleep(1)
            if look_nightcrows == False:
                why = "나이트 크로우 꺼진 것 같다.."
                print(why)
                line_to_me(cla, why)

                dir_path = "C:\\my_games\\load\\nightcrow"
                file_path = dir_path + "\\start.txt"
                file_path2 = dir_path + "\\cla.txt"
                with open(file_path, "w", encoding='utf-8-sig') as file:
                    data = 'no'
                    file.write(str(data))
                    time.sleep(0.2)
                with open(file_path2, "w", encoding='utf-8-sig') as file:
                    data = cla
                    file.write(str(data))
                    time.sleep(0.2)
                os.execl(sys.executable, sys.executable, *sys.argv)


    except Exception as e:
        print(e)

def in_number_check(cla, data):
    try:
        import cv2
        import numpy as np
        from function import text_check_get, int_put_

        isNumber = False
        print("들어온 데이타?", data)
        print("len potion", len(data))
        if len(data) > 0:
            print("길이가 0 보다 크다", len(data))
            for i in range(len(data)):
                result_num_bool = data[i].isdigit()
                if result_num_bool == True:
                    isNumber = True
        else:
            print("데이터가 길이가 없고 비어있다")

        return isNumber
    except Exception as e:
        print(e)

def game_loading(cla):
    import cv2
    import numpy as np
    from function import imgs_set_
    try:

        print('game loading')
        loaded = False
        loaded_count = 0
        load_out = 0
        while loaded is False:
            loaded_count += 1
            if loaded_count > 150:
                loaded = True
            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\action\\loading.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(150, 850, 750, 1050, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print('loding...', loaded_count)
            else:
                load_out += 1
                if load_out > 2:
                    loaded = True

            time.sleep(1)
    except Exception as e:
        print(e)

def out_check(cla):
    try:
        import cv2
        import numpy as np
        from function import text_check_get, int_put_
        from schedule import myQuest_play_check

        out_ = False

        re_1 = go_auto_ing_(cla)
        re_2 = go_quest_ing_(cla)
        # re_3 = out_checking(cla)
        if re_1 == True or re_2 == True:
            out_ = True


        return out_
    except Exception as e:
        print(e)

def out_checking(cla):
    try:

        from function import click_pos_2, imgs_set, imgs_set_, random_int, drag_pos, text_check_get, click_pos_reg
        import numpy as np
        import cv2

        go_ = False

        #퀘스트 진행중인지 여부
        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\action\\out_check_attack.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(810, 870, 910, 980, cla, img, 0.9)
        if imgs_ is not None and imgs_ != False:
            print("out_check_attack", imgs_)
            go_ = True

        return go_

    except Exception as e:
        print(e)

def go_quest_ing_(cla):
    try:

        from function import click_pos_2, imgs_set, imgs_set_, random_int, drag_pos, text_check_get, click_pos_reg
        import numpy as np
        import cv2

        go_ = False

        #퀘스트 진행중인지 여부
        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\grow\\grow_1\\quest_ing_1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(900, 820, 945, 860, cla, img, 0.9)
        if imgs_ is not None and imgs_ != False:
            print("quest_ing_1", imgs_)
            go_ = True

        return go_

    except Exception as e:
        print(e)

def go_auto_ing_(cla):
    try:

        from function import click_pos_2, imgs_set, imgs_set_, random_int, drag_pos, text_check_get, click_pos_reg
        import numpy as np
        import cv2

        go_ = False

        # 자동사냥 진행중인지 여부
        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\grow\\grow_1\\auto_1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(900, 820, 945, 860, cla, img, 0.9)
        if imgs_ is not None and imgs_ != False:
            print("auto_1", imgs_)
            go_ = True
        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\grow\\grow_1\\auto_2.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(900, 820, 945, 860, cla, img, 0.9)
        if imgs_ is not None and imgs_ != False:
            print("auto_2", imgs_)
            go_ = True
        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\grow\\grow_1\\auto_3.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(900, 820, 945, 860, cla, img, 0.9)
        if imgs_ is not None and imgs_ != False:
            print("auto_3", imgs_)
            go_ = True
        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\grow\\grow_1\\auto_3.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(900, 820, 945, 860, cla, img, 0.9)
        if imgs_ is not None and imgs_ != False:
            print("auto_4", imgs_)
            go_ = True

        return go_

    except Exception as e:
        print(e)

def skill_check_(cla):
    try:
        import numpy as np
        import cv2
        from function import imgs_set_, click_pos_reg, click_pos_2
        from action import menu_open
        # 기술서 적용 체크
        in_skill_all = False
        in_skill_all_count = 0
        in_skill_1 = False
        in_skill_2 = False
        in_skill_3 = False
        in_skill_4 = False
        while in_skill_all is False:
            in_skill_all_count += 1
            if in_skill_all_count > 10:
                in_skill_all = True
            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\dungeon\\refresh_1.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(50, 980, 130, 1030, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\dungeon\\in_skill_1.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(25, 115, 80, 180, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("스킬이 등록되어 있다", imgs_)
                    full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\dungeon\\skill_5.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(0, 920, 50, 960, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        in_skill_1 = True
                        print("반복사용 체크 완료")
                    else:
                        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\dungeon\\skill_2.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(0, 920, 50, 960, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("반복사용 체크 중")
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                        else:
                            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\dungeon\\skill_22.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(0, 920, 50, 960, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                print("반복사용 체크 중2")
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                    time.sleep(0.2)
                    full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\dungeon\\skill_5.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(125, 920, 160, 960, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        in_skill_2 = True
                        print("pvp 시 사용 체크 완료")
                    else:
                        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\dungeon\\skill_2.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(125, 920, 160, 960, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("pvp 시 사용 체크 중")
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                        else:
                            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\dungeon\\skill_22.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(125, 920, 160, 960, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                print("pvp 시 사용 체크 중2")
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                    time.sleep(0.2)
                    full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\dungeon\\skill_5.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(0, 955, 50, 980, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        in_skill_3 = True
                        print("사용 불가 건너뛰기 체크 완료")
                    else:
                        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\dungeon\\skill_2.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(0, 955, 50, 980, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("사용 불가 건너뛰기 체크 중")
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                        else:
                            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\dungeon\\skill_22.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(0, 955, 50, 980, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                print("사용 불가 건너뛰기 체크 중2")
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                    time.sleep(0.2)
                    full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\dungeon\\skill_4.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(60, 900, 140, 940, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        in_skill_4 = True
                        print("자동사용 켬 완료")
                    else:
                        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\dungeon\\skill_3.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(60, 900, 140, 940, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("자동사용 켜는 중")
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                    if in_skill_1 == True and in_skill_2 == True and in_skill_3 == True and in_skill_4 == True:
                        in_skill_all = True

                        in_skill_last_count = 0
                        in_skill_last = False
                        while in_skill_last is False:
                            in_skill_last_count += 1
                            if in_skill_last_count > 10:
                                in_skill_last = True
                            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\dungeon\\skill_1.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(700, 900, 760, 960, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                in_skill_last2 = False
                                in_skill_last2_count = 0
                                while in_skill_last2 is False:
                                    in_skill_last2_count += 1
                                    if in_skill_last2_count > 10:
                                        in_skill_last2 = True
                                    full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\dungeon\\skill_7.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(900, 50, 960, 150, cla, img, 0.8)
                                    if imgs_ is not None and imgs_ != False:
                                        click_pos_reg(imgs_.x, imgs_.y, cla)
                                    else:
                                        print("스킬 세팅 완료")
                                        in_skill_last = True
                                        in_skill_last2 = True
                                        v_.skill_checked_ = True

                                    time.sleep(0.2)
                            else:
                                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\dungeon\\skill_6.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(700, 900, 760, 960, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                else:
                    print("스킬이 등록 되지 않았다.")
                    y_gob = 40
                    for i in range(4):
                        click_pos_2(55, 155 + (y_gob * i), cla)
                        time.sleep(0.1)
                        click_pos_2(55, 155 + (y_gob * i), cla)
                        time.sleep(0.1)
                    y_gob = 60
                    for i in range(4):
                        click_pos_2(715, 160 + (y_gob * i), cla)
                        time.sleep(0.1)
                        click_pos_2(715, 160 + (y_gob * i), cla)
                        time.sleep(0.1)
                    for i in range(5):
                        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\dungeon\\in_skill_1.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(25, 115, 80, 180, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            break
                        time.sleep(0.4)


            else:
                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\dungeon\\skill_1.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(700, 900, 760, 960, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    for i in range(4):
                        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\dungeon\\skill_3.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(830, 610, 910, 800, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("자동사용 켜는 중")
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                            time.sleep(0.3)

                    full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\dungeon\\skill_1.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(700, 900, 760, 960, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                else:
                    menu_open(cla)
                    click_pos_2(885, 60, cla)
            time.sleep(0.3)

    except Exception as e:
        print(e)

def mine_check(cla):
    import numpy as np
    import cv2
    from function import imgs_set_, click_pos_reg, click_pos_2, text_check_get, in_number_check, int_put_, imgs_set_num
    from schedule import myQuest_play_add

    try:
        print("mine_check")

        if cla == 'one':
            plus = 0
        if cla == 'two':
            plus = 960
        if cla == 'three':
            plus = 960 + 960
        if cla == 'four':
            plus = 960 + 960 + 960

        gold_ = 0
        dia_ = 0

        auction_in = False
        auction_in_count = 0
        while auction_in is False:
            auction_in_count += 1
            if auction_in_count > 7:
                auction_in = True
            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\auction\\auction_title.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(5, 30, 150, 80, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                auction_in = True

                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\property\\gold.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_num(360, 30, 600, 70, cla, img, 0.85)
                if imgs_ is not None and imgs_ != False:
                    print("gold", imgs_)
                    # 491
                    x_reg_1 = imgs_.x - plus

                    for i in range(4):
                        read_gold = text_check_get(x_reg_1 + 14 + i, 35, x_reg_1 + 90, 65, cla)
                        if read_gold == "":
                            print("골드 못 읽음")
                        else:
                            print("read_gold", read_gold)
                            break

                    digit_ready = in_number_check(cla, read_gold)
                    print("digit_ready", digit_ready)
                    if digit_ready == True:
                        read_data_int = int(int_put_(read_gold))
                        print("read_data_int", read_data_int)
                        gold_ = read_data_int

                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\property\\dia.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_num(360, 30, 600, 70, cla, img, 0.85)
                if imgs_ is not None and imgs_ != False:
                    print("dia", imgs_)
                    # 410
                    x_reg_2 = imgs_.x - plus

                    for i in range(4):
                        read_dia = text_check_get(x_reg_2 + 15 + i, 35, x_reg_2 + 60, 65, cla)
                        if read_dia == "":
                            print("다이아 못 읽음")
                        else:
                            print("read_dia", read_dia)
                            break

                    digit_ready = in_number_check(cla, read_dia)
                    print("digit_ready", digit_ready)
                    if digit_ready == True:
                        read_data_int = int(int_put_(read_dia))
                        print("read_data_int", read_data_int)
                        dia_ = read_data_int


            else:
                menu_open(cla)
                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\auction\\menu_auction.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(720, 100, 960, 450, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                    for i in range(10):
                        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\auction\\auction_title.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(10, 10, 130, 80, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            break
                        else:
                            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\auction\\menu_auction.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(720, 100, 960, 450, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                                if i > 7:
                                    auction_in = True
                        time.sleep(0.5)


        return gold_, dia_

    except Exception as e:
        print(e)
        return 0


def character_change(cla, character_id):
    from function import click_pos_2, imgs_set, imgs_set_, random_int, drag_pos, text_check_get, click_pos_reg
    from massenger import line_to_me
    from potion import maul_potion
    import numpy as np
    import cv2
    import os
    try:



        print("캐릭터 체인지")

        # 현재 진입되었던 캐릭터 번호(id)

        dir_path = "C:\\my_games\\nightcrow"
        if cla == 'one':
            file_path = dir_path + "\\mysettings\\myschedule\\one_now_id.txt"
        if cla == 'two':
            file_path = dir_path + "\\mysettings\\myschedule\\two_now_id.txt"
        if cla == 'three':
            file_path = dir_path + "\\mysettings\\myschedule\\three_now_id.txt"
        if cla == 'four':
            file_path = dir_path + "\\mysettings\\myschedule\\four_now_id.txt"

        cha_select = False
        cha_select_count = 0
        while cha_select is False:
            cha_select_count += 1
            if cha_select_count > 10:
                cha_select = True
                line_to_me(cla, "처음 스타트 화면에 문제가 있다.")


            # 절전모드 해제 juljun
            result_juljun = juljun_check(cla)
            if result_juljun == True:
                drag_pos(360, 550, 600, 550, cla)


            # 캐릭터 선택 화면
            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\character_start\\delete_character.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(20, 990, 150, 1040, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\character_start\\game_start_1.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(810, 990, 950, 1040, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    # 좌표
                    x_reg = imgs_.x
                    y_reg = imgs_.y

                    last_change = False
                    last_change_count = 0
                    while last_change is False:
                        last_change_count += 1
                        if last_change_count > 10:
                            last_change = True
                        print("진입")
                        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\character_start\\delete_character.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(20, 990, 150, 1040, cla, img, 0.8)
                        if imgs_ is None:
                            # 진입여부 파악
                            in_game = False
                            in_game_count = 0
                            while in_game is False:
                                in_game_count += 1
                                if in_game_count > 40:
                                    in_game = True
                                    line_to_me(cla, "게임화면 진입에 문제가 있다.")
                                result_out = out_check(cla)
                                if result_out == True:
                                    last_change = True
                                    cha_select = True
                                    in_game = True

                                    # 포션 구매
                                    maul_potion(cla)

                                    # read_id = '0'

                                    is_out = False
                                    is_out_count = 0
                                    while is_out is False:
                                        is_out_count += 1
                                        if is_out_count > 15:
                                            is_out = True
                                        if os.path.isfile(file_path) == True:
                                            with open(file_path, "r", encoding='utf-8-sig') as file:
                                                read_id = file.read()
                                                if str(character_id) == str(read_id):
                                                    is_out = True
                                                else:
                                                    with open(file_path, "w", encoding='utf-8-sig') as file:
                                                        file.write(str(character_id))
                                                time.sleep(0.3)
                                        else:
                                            with open(file_path, "w", encoding='utf-8-sig') as file:
                                                file.write(str(character_id))
                                        time.sleep(0.3)


                                else:
                                    print("진입중")
                                time.sleep(0.5)
                        else:
                            if int(character_id) == 1:
                                for i in range(10):
                                    full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\character_start\\character_select_1.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(0, 110, 120, 250, cla, img, 0.8)
                                    if imgs_ is not None and imgs_ != False:
                                        time.sleep(0.2)
                                        click_pos_reg(x_reg, y_reg, cla)
                                        break
                                    else:
                                        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\character_start\\character_select_2.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(0, 110, 120, 250, cla, img, 0.8)
                                        if imgs_ is not None and imgs_ != False:
                                            time.sleep(0.2)
                                            click_pos_reg(x_reg, y_reg, cla)
                                            break
                                        else:
                                            click_pos_2(130, 180, cla)
                                    time.sleep(0.5)
                            if int(character_id) == 2:
                                for i in range(10):
                                    full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\character_start\\character_select_1.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(0, 200, 120, 350, cla, img, 0.8)
                                    if imgs_ is not None and imgs_ != False:
                                        time.sleep(0.2)
                                        click_pos_reg(x_reg, y_reg, cla)
                                        break
                                    else:
                                        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\character_start\\character_select_2.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(0, 200, 120, 350, cla, img, 0.8)
                                        if imgs_ is not None and imgs_ != False:
                                            time.sleep(0.2)
                                            click_pos_reg(x_reg, y_reg, cla)
                                            break
                                        else:
                                            click_pos_2(130, 280, cla)
                                    time.sleep(0.5)

                            time.sleep(0.2)
                            click_pos_reg(x_reg, y_reg, cla)
                        time.sleep(0.5)



            else:
                # 추후 대기중 화면 설정하기
                # 대기중 화면이 아닐때



                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\character_start\\y_.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(480, 580, 630, 630, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:

                    click_pos_reg(imgs_.x, imgs_.y, cla)
                    is_select = False
                    is_select_count = 0
                    while is_select is False:
                        is_select_count += 1
                        if is_select_count > 30:
                            is_select = True
                            line_to_me(cla, "캐릭 선택화면으로 가는 것에 문제가 있다.")
                        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\character_start\\game_start_1.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(810, 990, 950, 1040, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            is_select = True
                        else:
                            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\character_start\\y_.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(480, 580, 630, 630, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                            else:
                                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\action\\loading.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(150, 850, 750, 1050, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    game_loading(cla)
                        time.sleep(0.5)
                else:


                    # 마을이 아니라면...
                    for i in range(20):
                        result_maul_check = in_maul_check(cla)
                        if result_maul_check == True:
                            break
                        else:
                            clean_screen(cla)

                            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\check\\maul_move_1.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(250, 960, 420, 1030, cla, img, 0.7)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_reg(imgs_.x, imgs_.y, cla)

                            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\action\\loading.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(150, 850, 750, 1050, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                game_loading(cla)
                        time.sleep(1)

                    menu_open(cla)
                    time.sleep(0.1)
                    click_pos_2(930, 1000, cla)
                    wait_y = False
                    wait_y_count = 0
                    while wait_y is False:
                        wait_y_count += 1
                        if wait_y_count > 20:
                            wait_y = True
                        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\character_start\\y_.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(480, 580, 630, 630, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            wait_y = True
                        time.sleep(0.3)
                time.sleep(0.5)

    except Exception as e:
        print(e)

def my_gold_check(cla):
    try:

        from function import click_pos_2, imgs_set, imgs_set_, random_int, drag_pos, text_check_get, click_pos_reg
        import numpy as np
        import cv2

        result_out = out_check(cla)
        if result_out == True:
            # 가방 열어 골드 파악하는거 서브퀘스트일때 and 300초마다
            v_.bag_open_count += 1
            if v_.bag_open_count == 5:
                time.sleep(0.5)
                bag_open(cla)
                time.sleep(0.2)
                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\clean_screen\\gabang_title.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(820, 80, 910, 120, cla, img, 0.83)
                if imgs_ is not None and imgs_ != False:
                    click_pos_2(935, 100, cla)
            if v_.bag_open_count > 99:
                v_.bag_open_count = 0




    except Exception as e:
        print(e)

def juljun_fullbag_check(cla):
    from function import click_pos_2, imgs_set, imgs_set_, imgs_set_num
    from realtime import boonhae_
    import numpy as np
    import cv2
    try:

        is_full = False

        result_juljun = juljun_check(cla)
        if result_juljun == True:

            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\check\\juljun_full_bag_1.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(40, 200, 100, 240, cla, img, 0.75)
            if imgs_ is not None and imgs_ != False:
                print("juljun_full_bag_1", imgs_)
                is_full = True

            for i in range(5):
                num = i + 6
                add_x = 0
                if num == 10:
                    add_x = 10
                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\check\\juljun_full_bag_num\\" + str(num) + ".PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_num(50, 200, 65 + add_x, 230, cla, img, 0.75)
                if imgs_ is not None and imgs_ != False:
                    print("juljun_full_bag : ", num)
                    if num == 9 or num == 10:
                        is_full = True
                    break

        if is_full == True:
            print("분해")
            boonhae_(cla)

    except Exception as e:
        print("에러", e)
        return e

def fullbag_check(cla):
    from function import click_pos_2, imgs_set, imgs_set_
    from realtime import boonhae_
    import numpy as np
    import cv2
    try:

        is_full = False

        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\check\\full_bag_2.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(817, 45, 845, 70, cla, img, 0.75)
        if imgs_ is not None and imgs_ != False:
            print("full_bag_2", imgs_)
            is_full = True

        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\check\\full_bag_3.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(817, 45, 845, 70, cla, img, 0.75)
        if imgs_ is not None and imgs_ != False:
            print("full_bag_3", imgs_)
            is_full = True

        if is_full == True:
            print("분해")
            boonhae_(cla)

    except Exception as e:
        print("에러", e)
        return e

def move_check(cla):
    try:

        from function import click_pos_2, imgs_set, imgs_set_, random_int, drag_pos, text_check_get, click_pos_reg, mouse_move_cpp
        from potion import maul_potion_move_buy
        from schedule import myQuest_play_check
        import numpy as np
        import cv2

        not_have = False

        # 마을 이동 체크
        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\check\\maul_move_1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(250, 960, 420, 1030, cla, img, 0.7)
        if imgs_ is not None and imgs_ != False:
            print("마을 이동서 있다.")
        else:
            bag_open(cla)
            time.sleep(0.1)
            click_pos_2(935, 265, cla)
            time.sleep(0.2)
            click_pos_2(885, 935, cla)
            time.sleep(1)
            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\bag\\bag_maul_move.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(680, 110, 900, 880, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                click_pos_reg(imgs_.x, imgs_.y, cla)
                time.sleep(0.3)
                for i in range(10):
                    full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\bag\\bag_checked.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(680, 910, 730, 960, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_2(290, 1000, cla)
                        break
                    else:
                        click_pos_2(710, 935, cla)
                        time.sleep(0.2)
                        mouse_move_cpp(700, 500, cla)
                        time.sleep(0.3)
                    time.sleep(0.1)
            else:
                print("마을 이동서 없다.")
                not_have = True



        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\check\\random_move_1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(250, 960, 420, 1030, cla, img, 0.7)
        if imgs_ is not None and imgs_ != False:
            print("랜덤 이동서 있다.")
        else:
            bag_open(cla)
            time.sleep(0.1)
            click_pos_2(935, 265, cla)
            time.sleep(0.2)
            click_pos_2(885, 935, cla)
            time.sleep(1)
            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\bag\\bag_random_move.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(680, 110, 900, 880, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                click_pos_reg(imgs_.x, imgs_.y, cla)
                time.sleep(0.3)
                for i in range(10):
                    full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\bag\\bag_checked.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(680, 910, 730, 960, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_2(345, 1000, cla)
                        break
                    else:
                        click_pos_2(710, 935, cla)
                        time.sleep(0.2)
                        mouse_move_cpp(700, 500, cla)
                        time.sleep(0.3)
                    time.sleep(0.1)
            else:
                print("랜덤 이동서 없다.")
                not_have = True





        for i in range(10):
            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\bag\\bag_checked.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(680, 910, 730, 960, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                click_pos_2(940, 100, cla)
                time.sleep(0.2)

        if not_have == True:

            clean_screen(cla)

            result_schedule = myQuest_play_check(cla, "check")
            print("result_schedule", result_schedule)
            character_id = result_schedule[0][1]
            result_schedule_ = result_schedule[0][2]

            maul_in_ = False
            maul_in_count = 0
            while maul_in_ is False:
                maul_in_count += 1
                if maul_in_count > 7:
                    maul_in_ = True

                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\potion\\janhwa_1.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(0, 90, 220, 350, cla, img, 0.9)
                if imgs_ is not None and imgs_ != False:
                    print("janhwa_1", imgs_)
                    maul_in_ = True
                    maul_potion_move_buy(cla)
                else:
                    if "사냥" in result_schedule_:
                        click_pos_2(110, 160, cla)

                        for i in range(10):
                            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\jadong\\world_1.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(450, 990, 510, 1030, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                break
                            time.sleep(0.5)
                        for i in range(10):
                            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\bag\\worldmap_maul.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(710, 165, 780, 225, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\jadong\\confirm_1.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(480, 580, 630, 630, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                                    break
                                else:
                                    click_pos_2(925, 200, cla)
                            else:
                                drag_pos(800, 250, 800, 900, cla)
                            time.sleep(0.5)
                        for i in range(10):
                            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\potion\\janhwa_1.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(0, 90, 220, 350, cla, img, 0.9)
                            if imgs_ is not None and imgs_ != False:
                                print("janhwa_1", imgs_)
                                break
                            time.sleep(1)
                    elif "던전" in result_schedule_:

                        dungeon_ = result_schedule_.split("_")

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

                        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\dungeon\\" + dungeon_name + ".PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(30, 75, 200, 110, cla, img, 0.75)
                        if imgs_ is not None and imgs_ != False:

                            for i in range(10):
                                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\jadong\\confirm_1.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(480, 580, 630, 630, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    click_pos_reg(imgs_.x, imgs_.y, cla)

                                    for k in range(20):
                                        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\action\\loading.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(150, 850, 750, 1050, cla, img, 0.8)
                                        if imgs_ is not None and imgs_ != False:
                                            game_loading(cla)
                                            break
                                        time.sleep(0.3)

                                    break
                                else:
                                    click_pos_2(230, 95, cla)
                                time.sleep(1)
                        else:
                            click_pos_2(110, 160, cla)

                            for i in range(10):
                                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\jadong\\world_1.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(450, 990, 510, 1030, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    break
                                time.sleep(0.5)
                            for i in range(10):
                                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\bag\\worldmap_maul.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(710, 165, 780, 225, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\jadong\\confirm_1.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(480, 580, 630, 630, cla, img, 0.8)
                                    if imgs_ is not None and imgs_ != False:
                                        click_pos_reg(imgs_.x, imgs_.y, cla)
                                        break
                                    else:
                                        click_pos_2(925, 200, cla)
                                else:
                                    drag_pos(800, 250, 800, 900, cla)
                                time.sleep(0.5)
                            for i in range(10):
                                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\potion\\janhwa_1.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(0, 90, 220, 350, cla, img, 0.9)
                                if imgs_ is not None and imgs_ != False:
                                    print("janhwa_1", imgs_)
                                    break
                                time.sleep(1)
                time.sleep(1)



    except Exception as e:
        print(e)
