import time

import requests
import json
# import os
import sys
sys.path.append('C:/my_games/nightcrow/data_nc/mymodule')

import variable as v_


def gyucjunji_play(cla, lv):
    try:
        import cv2
        import numpy as np
        from function import text_check_get, int_put_, imgs_set_, click_pos_2, click_pos_reg, drag_pos
        from action import menu_open, clean_screen, dead_die_before
        from massenger import line_to_me
        from potion import maul_potion
        from schedule import myQuest_play_add

        print("gyucjunji_play")

        complete_ = False

        if v_.gyucjunji_dead_count > 3:
            data = "격전지_" + str(lv)
            myQuest_play_add(cla, data)
            time.sleep(0.1)
        else:

            print("격전지 시작 : ", v_.gyucjunji_dead_count)

            in_dungeon__ = False

            in_dungeon__count = 0
            while in_dungeon__ is False:
                in_dungeon__count += 1
                if in_dungeon__count > 3:
                    in_dungeon__count = 0
                    in_dungeon__ = True

                print("격전지 체크")

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


                # 죽었을때
                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\dead_die\\dead_die_2.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(680, 0, 710, 82, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    dead_die_before(cla)
                    time.sleep(0.5)

                # 격전지 체크

                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\gyucjunji\\toohab_1.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(30, 75, 200, 110, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("toohab_1", imgs_)

                    in_dungeon__ = True

                    if v_.gyucjunji_setting == False:
                        scan_jungye_setting(cla)
                        v_.gyucjunji_setting = True
                    else:
                        now_playing(cla, lv)
                else:
                    full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\gyucjunji\\gyuc_jabhwa.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(10, 145, 110, 180, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("gyuc_jabhwa", imgs_)

                        in_dungeon__ = True

                        now_playing(cla, lv)
                    else:

                        # 던전 진입하기
                        print("격전지 진입하기")
                        gyucjunji_in(cla, lv)



        return complete_
    except Exception as e:
        print(e)

def gyucjunji_in(cla, lv):
    import numpy as np
    import cv2
    from function import click_pos_reg, imgs_set_, click_pos_2
    from action import menu_open, dead_die_before
    try:
        in_gyuc_ = False
        in_gyuc_count = 0
        while in_gyuc_ is False:
            in_gyuc_count += 1
            if in_gyuc_count > 10:
                in_gyuc_ = True
            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\gyucjunji\\menu_gyucjunji.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(720, 105, 955, 500, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                # 죽었을때
                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\dead_die\\dead_die_2.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(680, 0, 710, 82, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    dead_die_before(cla)
                    time.sleep(0.5)

                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\gyucjunji\\menu_gyucjunji.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(720, 105, 955, 500, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("menu_gyucjunji", imgs_)
                    click_pos_reg(imgs_.x, imgs_.y, cla)

                cancle_ = False
                for i in range(10):
                    full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\character_start\\y_.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(0, 0, 960, 1030, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_reg(imgs_.x, imgs_.y, cla)

                        time.sleep(1)

                        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\gyucjunji\\already_gyucjunji.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(400, 70, 500, 120, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("already gyucjunji")
                            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\gyucjunji\\cancle.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(0, 0, 960, 1030, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                                time.sleep(0.5)
                                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\gyucjunji\\toohab_1.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(40, 60, 120, 120, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    print("continue")
                                else:
                                    my_lv_go(cla, lv)

                        cancle_ = True
                        break
                    time.sleep(0.3)


                is_walking = False


                if cancle_ == True:
                    is_walking_count = 0
                    while is_walking is False:
                        is_walking_count += 1
                        if is_walking_count > 15:
                            is_walking = True
                        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\jadong\\in_spot_walking_2.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(480, 880, 500, 900, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            is_walking_count = 0
                            print("in_spot_walking_2 보여", is_walking_count)
                        else:
                            print("in_spot_walking_2 안 보여", is_walking_count)
                            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\gyucjunji\\arrive_killdebat.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(430, 380, 530, 430, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_2(480, 730, cla)
                                time.sleep(1)
                        time.sleep(0.2)


                    #full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\gyucjunji\\cancle.PNG"
                    #img_array = np.fromfile(full_path, np.uint8)
                    #img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    #imgs_ = imgs_set_(370, 600, 460, 660, cla, img, 0.8)
                    #if imgs_ is not None and imgs_ != False:
                    #    click_pos_reg(imgs_.x, imgs_.y, cla)
                    #    in_gyuc_ = True


                    if is_walking == True:

                        arrive = False
                        arrive_count = 0
                        while arrive is False:
                            arrive_count += 1
                            if arrive_count > 10:
                                arrive = True
                                in_gyuc_ = True

                            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\character_start\\y_.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(0, 0, 960, 1030, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                                time.sleep(1)
                                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\gyucjunji\\already_gyucjunji.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(400, 70, 500, 120, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    print("already gyucjunji")
                                    full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\gyucjunji\\cancle.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(0, 0, 960, 1030, cla, img, 0.8)
                                    if imgs_ is not None and imgs_ != False:
                                        click_pos_reg(imgs_.x, imgs_.y, cla)
                                        time.sleep(0.5)
                                        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\gyucjunji\\toohab_1.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(40, 60, 120, 120, cla, img, 0.8)
                                        if imgs_ is not None and imgs_ != False:
                                            print("continue")
                                        else:
                                            my_lv_go(cla, lv)
                                else:
                                    print("인원초과")
                                    full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\gyucjunji\\people_over.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(360, 70, 560, 120, cla, img, 0.8)
                                    if imgs_ is not None and imgs_ != False:
                                        print("people over")
                                        for i in range(60):
                                            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\gyucjunji\\arrive_killdebat.PNG"
                                            img_array = np.fromfile(full_path, np.uint8)
                                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                            imgs_ = imgs_set_(430, 380, 530, 430, cla, img, 0.8)
                                            if imgs_ is not None and imgs_ != False:
                                                click_pos_2(480, 730, cla)
                                                time.sleep(1)
                                            else:
                                                break
                                            time.sleep(3)



                            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\gyucjunji\\toohab_1.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(40, 60, 120, 120, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                arrive = True
                                in_gyuc_ = True
                                # click_pos_2(230, 90, cla)
                                time.sleep(0.2)
                            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\gyucjunji\\gyuc_jabhwa2.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(5, 70, 60, 190, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_2(230, 90, cla)
                                time.sleep(0.2)
                            time.sleep(1)

            else:

                # 죽었을때
                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\dead_die\\dead_die_2.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(680, 0, 710, 82, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    dead_die_before(cla)
                    time.sleep(0.5)

                menu_open(cla)

            time.sleep(0.5)
    except Exception as e:
        print(e)

def now_playing(cla, lv):
    import cv2
    import numpy as np
    from function import click_pos_2, click_pos_reg, imgs_set_, drag_pos, mouse_move_cpp
    from action import clean_screen, skill_check_
    from get_item import guild_jilyung
    from schedule import myQuest_play_add
    from potion import potion_check

    try:
        print("now_격전지_playing")

        play_ = False

        if v_.gyucjunji_dead_count > 3:
            data = "격전지_" + str(lv)
            myQuest_play_add(cla, data)
            time.sleep(0.1)
        else:
            print("격전지에서 죽은 횟수 : ", v_.gyucjunji_dead_count)
            in_ = False
            in__count = 0
            while in_ is False:

                in__count += 1
                if in__count > 7:
                    in_ = True

                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\dungeon\\different.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(520, 410, 620, 450, cla, img, 0.83)
                if imgs_ is not None and imgs_ != False:
                    print("던전 중 실수로 다른 퀘스트 클릭한 경우", imgs_)
                    click_pos_2(410, 640, cla)



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
                    clean_screen(cla)
                    go_ice_1 = False
                    go_ice_count = 0
                    while go_ice_1 is False:
                        print("go_gyuc_count_1", go_ice_count)
                        go_ice_count += 1
                        if go_ice_count > 10:
                            go_ice_1 = True

                        # 격전지 상인 등 격전지인지 파악 하기기

                        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\gyucjunji\\toohab_1.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(50, 75, 150, 110, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("toohab_1", imgs_)
                            go_ice_1 = True
                            go_ice_2 = False
                            go_ice_count = 0
                            while go_ice_2 is False:
                                print("go_gyuc_count_2", go_ice_count)
                                go_ice_count += 1
                                if go_ice_count > 10:
                                    go_ice_2 = True

                                # 킬ㄷ데바트인지 파악
                                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\gyucjunji\\kiidebat.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(777, 77, 865, 115, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:

                                    # 투항의 집결지 옆으로...
                                    full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\dungeon\\dungeon_move_1.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(260, 80, 680, 700, cla, img, 0.8)
                                    if imgs_ is not None and imgs_ != False:
                                        print("자동이동")
                                        click_pos_reg(imgs_.x, imgs_.y, cla)
                                        time.sleep(1)
                                        go_ice_2 = True
                                        go_ice_3 = False
                                        go_ice_count = 0
                                        while go_ice_3 is False:
                                            print("go_gyuc_count_3", go_ice_count)
                                            go_ice_count += 1
                                            if go_ice_count > 10:
                                                go_ice_3 = True
                                            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\dungeon\\dungeon_move_1.PNG"
                                            img_array = np.fromfile(full_path, np.uint8)
                                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                            imgs_ = imgs_set_(260, 80, 680, 700, cla, img, 0.8)
                                            if imgs_ is not None and imgs_ != False:
                                                click_pos_reg(imgs_.x, imgs_.y, cla)
                                                time.sleep(1)
                                            else:
                                                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\gyucjunji\\kiidebat.PNG"
                                                img_array = np.fromfile(full_path, np.uint8)
                                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                                imgs_ = imgs_set_(777, 77, 865, 115, cla, img, 0.8)
                                                if imgs_ is not None and imgs_ != False:
                                                    click_pos_2(930, 60, cla)
                                                else:
                                                    go_ice_3 = True

                                                    is_walking = False

                                                    is_walking_count = 0
                                                    while is_walking is False:
                                                        is_walking_count += 1
                                                        if is_walking_count > 15:
                                                            is_walking = True

                                                        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\gyucjunji\\toohab_1.PNG"
                                                        img_array = np.fromfile(full_path, np.uint8)
                                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                                        imgs_ = imgs_set_(50, 75, 150, 110, cla, img, 0.8)
                                                        if imgs_ is not None and imgs_ != False:
                                                            print("toohab_1 : move", imgs_)
                                                            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\jadong\\in_spot_walking_2.PNG"
                                                            img_array = np.fromfile(full_path, np.uint8)
                                                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                                            imgs_ = imgs_set_(480, 880, 500, 900, cla, img, 0.8)
                                                            if imgs_ is not None and imgs_ != False:
                                                                is_walking_count = 0
                                                                print("사냥터 이동...in_spot_walking_2 보여", is_walking_count)
                                                            else:
                                                                print("사냥터 이동...in_spot_walking_2 안 보여",
                                                                      is_walking_count)
                                                                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\gyucjunji\\arrive_killdebat.PNG"
                                                                img_array = np.fromfile(full_path, np.uint8)
                                                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                                                imgs_ = imgs_set_(430, 380, 530, 430, cla, img, 0.8)
                                                                if imgs_ is not None and imgs_ != False:
                                                                    click_pos_2(480, 730, cla)
                                                                    time.sleep(1)
                                                            time.sleep(0.2)
                                                        else:
                                                            now_playing(cla, lv)
                                                            is_walking = True



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

                                                    if is_walking == True:
                                                        if v_.skill_checked_ == False:
                                                            skill_check_(cla)
                                                            time.sleep(0.2)
                                                            click_pos_2(925, 850, cla)
                                                            time.sleep(0.2)
                                                        else:
                                                            click_pos_2(925, 850, cla)
                                                            time.sleep(0.2)


                                    else:
                                        for i in range(2):
                                            drag_pos(820, 260, 820, 820, cla)
                                            time.sleep(0.2)
                                            click_pos_2(820, 260, cla)
                                            time.sleep(0.2)
                                        time.sleep(0.5)
                                        if int(lv) == 40:
                                            click_pos_2(400, 550, cla)
                                            time.sleep(0.1)
                                        elif int(lv) == 45:
                                            click_pos_2(400, 350, cla)
                                            time.sleep(0.1)
                                        elif int(lv) == 50:
                                            click_pos_2(550, 750, cla)
                                            time.sleep(0.1)
                                    time.sleep(0.2)
                                else:
                                    click_pos_2(110, 160, cla)
                                    time.sleep(0.1)
                                    for i in range(10):
                                        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\gyucjunji\\kiidebat.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(777, 77, 865, 115, cla, img, 0.8)
                                        if imgs_ is not None and imgs_ != False:
                                            print("격전지 지도임")
                                            break
                                        time.sleep(0.5)
                                time.sleep(0.2)
                        else:
                            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\gyucjunji\\gyuc_jabhwa.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(10, 145, 110, 180, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_2(230, 90, cla)
                            else:
                                # in_ = True
                                go_ice_1 = True


                        time.sleep(0.3)







                else:


                    # m 이 없어질때 절전어택 시작 : nowplaying
                    if int(lv) == 40:
                        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\gyucjunji\\lv40.PNG"
                        #full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\gyucjunji\\toohab_1.PNG"
                    if int(lv) == 45:
                        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\gyucjunji\\lv45.PNG"
                    if int(lv) == 50:
                        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\gyucjunji\\lv50.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(50, 75, 200, 110, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("렙40~50 격전지 공격중???", lv)

                        v_.skill_checked_ = True

                        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\character_start\\y_.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(0, 0, 960, 1030, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                            time.sleep(1)
                            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\gyucjunji\\already_gyucjunji.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(400, 70, 500, 120, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                print("already gyucjunji")
                                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\gyucjunji\\cancle.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(0, 0, 960, 1030, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                                    time.sleep(0.5)
                                    #마을이동버튼
                                    full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\gyucjunji\\toohab_1.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(40, 60, 120, 120, cla, img, 0.8)
                                    if imgs_ is not None and imgs_ != False:
                                        print("continue")
                                    else:
                                        my_lv_go(cla, lv)

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

                        # 창 닫혔으면 다시 열기
                        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\gyucjunji\\scan_setting.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(860, 225, 910, 280, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("탐색창 열림")
                        else:
                            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\gyucjunji\\gyucjunji_trash.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(500, 225, 910, 280, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                print("gyucjunji_trash")
                            else:
                                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\gyucjunji\\gyucjunji_scaning.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(500, 225, 910, 280, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    print("gyucjunji_scaning")
                                else:
                                    scan_jungye_setting(cla)
                                    time.sleep(0.5)

                        # 정예몹 찾아서 공격하기기
                        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\gyucjunji\\devulllll.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(600, 80, 910, 240, cla, img, 0.75)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                            time.sleep(0.2)

                        else:
                            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\gyucjunji\\boss.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(600, 80, 910, 240, cla, img, 0.75)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                                time.sleep(0.2)
                        mouse_move_cpp(480, 480, cla)
                        time.sleep(0.1)

                        # 포션 체크하기
                        potion_check(cla)

                        # 정예몹 찾아서 공격하기기
                        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\gyucjunji\\devulllll.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(600, 80, 910, 240, cla, img, 0.75)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                            time.sleep(0.2)
                        else:
                            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\gyucjunji\\boss.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(600, 80, 910, 240, cla, img, 0.75)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                                time.sleep(0.2)
                        mouse_move_cpp(480, 480, cla)
                        time.sleep(0.1)

                        play_ = True
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
                                    guild_jilyung(cla, "gyucjunji")
                                    jilyung_is_ = True
                                else:
                                    full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\guild\\guild_jilyung.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(660, 90, 730, 300, cla, img, 0.8)
                                    if imgs_ is not None and imgs_ != False:
                                        click_pos_reg(imgs_.x, imgs_.y, cla)

                                time.sleep(0.4)
                    else:
                        click_pos_2(925, 850, cla)
                        time.sleep(0.2)

        return play_
    except Exception as e:
        print(e)

def scan_jungye_setting(cla):
    import cv2
    import numpy as np
    from function import imgs_set_, click_pos_2, click_pos_reg
    from action import clean_screen
    try:

        scan_ = False
        scan_count = 0

        while scan_ is False:
            scan_count += 1
            if scan_count > 7:
                scan_ = True

            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\gyucjunji\\scan_setting.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(860, 225, 910, 280, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                click_pos_reg(imgs_.x, imgs_.y, cla)
                time.sleep(0.2)

                for i in range(10):
                    full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\gyucjunji\\setting_title.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(780, 80, 830, 130, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        scan_ = True
                        break
                    else:
                        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\gyucjunji\\scan_setting.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(860, 225, 910, 280, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                            time.sleep(0.2)
                    time.sleep(0.3)

                # 주변 대상 탐색
                for i in range(10):
                    full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\gyucjunji\\look_daesang.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(660, 190, 720, 230, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        break
                    else:
                        click_pos_2(720, 135, cla)
                        time.sleep(0.2)
                    time.sleep(0.5)

                # 갱신시간
                for i in range(2):
                    click_pos_2(757, 187, cla)
                    time.sleep(0.2)
                    click_pos_2(751, 231, cla)
                    time.sleep(0.2)
                    full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\gyucjunji\\on.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(815, 255, 895, 300, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        time.sleep(0.2)
                    full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\gyucjunji\\off.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(815, 285, 895, 335, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        time.sleep(0.2)
                    full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\gyucjunji\\on.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(815, 320, 895, 370, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        time.sleep(0.2)

                # 대상필터
                for i in range(10):
                    full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\gyucjunji\\monster.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(660, 265, 730, 300, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        break
                    else:
                        click_pos_2(840, 135, cla)
                        time.sleep(0.2)
                    time.sleep(0.5)

                # 캐릭터
                for i in range(2):
                    full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\gyucjunji\\clicked.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(665, 165, 705, 210, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        time.sleep(0.2)
                    full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\gyucjunji\\clicked.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(735, 165, 775, 210, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        time.sleep(0.2)
                    full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\gyucjunji\\clicked.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(805, 165, 850, 210, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        time.sleep(0.2)
                    full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\gyucjunji\\clicked.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(665, 190, 705, 240, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        time.sleep(0.2)
                    full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\gyucjunji\\clicked.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(735, 190, 775, 240, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        time.sleep(0.2)
                    full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\gyucjunji\\not_clicked.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(805, 190, 850, 240, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        time.sleep(0.2)
                    full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\gyucjunji\\clicked.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(665, 220, 705, 265, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        time.sleep(0.2)

                    # 주요 몬스터
                    full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\gyucjunji\\not_clicked.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(665, 280, 705, 325, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        time.sleep(0.2)
                    full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\gyucjunji\\not_clicked.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(735, 280, 775, 325, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        time.sleep(0.2)
                    full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\gyucjunji\\not_clicked.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(805, 280, 850, 325, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        time.sleep(0.2)
                    full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\gyucjunji\\clicked.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(665, 310, 705, 360, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        time.sleep(0.2)
                    full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\gyucjunji\\clicked.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(735, 310, 775, 360, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        time.sleep(0.2)
                    full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\gyucjunji\\clicked.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(805, 310, 850, 360, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        time.sleep(0.2)

            else:
                clean_screen(cla)
                time.sleep(0.2)

                click_pos_2(930, 215, cla)
                time.sleep(0.2)

                for i in range(10):
                    full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\gyucjunji\\scan_setting.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(860, 225, 910, 280, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        break
                    time.sleep(0.2)



        for i in range(5):
            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\gyucjunji\\setting_title.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(780, 80, 830, 130, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                click_pos_2(890, 105, cla)
                time.sleep(0.2)
            else:
                break
            time.sleep(0.3)

    except Exception as e:
        print(e)

def my_lv_go(cla, lv):
    import cv2
    import numpy as np
    from function import click_pos_2, click_pos_reg, imgs_set_, drag_pos
    from action import clean_screen, skill_check_
    from potion import maul_potion_only
    try:
        clean_screen(cla)
        go_ice_2 = False
        go_ice_count = 0
        while go_ice_2 is False:
            print("my_lv_2", go_ice_count)
            go_ice_count += 1
            if go_ice_count > 10:
                go_ice_2 = True
                maul_potion_only(cla)

            # 킬ㄷ데바트인지 파악
            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\gyucjunji\\kiidebat.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(777, 77, 865, 115, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:

                # 투항의 집결지 옆으로...
                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\dungeon\\dungeon_move_1.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(260, 80, 680, 700, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("자동이동")
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                    time.sleep(1)
                    go_ice_2 = True
                    go_ice_3 = False
                    go_ice_count = 0
                    while go_ice_3 is False:
                        print("my_lv_3", go_ice_count)
                        go_ice_count += 1
                        if go_ice_count > 10:
                            go_ice_3 = True
                        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\dungeon\\dungeon_move_1.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(260, 80, 680, 700, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                            time.sleep(1)
                        else:
                            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\gyucjunji\\kiidebat.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(777, 77, 865, 115, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_2(930, 60, cla)
                            else:
                                go_ice_3 = True

                                is_walking = False

                                is_walking_count = 0
                                not_walking_count = 0
                                while is_walking is False:
                                    is_walking_count += 1
                                    if is_walking_count > 100:
                                        is_walking = True

                                    full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\gyucjunji\\toohab_1.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(50, 75, 150, 110, cla, img, 0.8)
                                    if imgs_ is not None and imgs_ != False:
                                        print("toohab_1 : move", imgs_)
                                        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\jadong\\in_spot_walking_2.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(480, 880, 500, 900, cla, img, 0.8)
                                        if imgs_ is not None and imgs_ != False:
                                            # is_walking_count = 0
                                            print("사냥터 이동...in_spot_walking_2 보여(is_walking_count) : 100", is_walking_count)
                                        else:
                                            print("사냥터 이동...in_spot_walking_2 안 보여(not_walking_count) : 7",
                                                  not_walking_count)
                                            not_walking_count += 1

                                            if not_walking_count > 7:
                                                is_walking = True

                                            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\gyucjunji\\arrive_killdebat.PNG"
                                            img_array = np.fromfile(full_path, np.uint8)
                                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                            imgs_ = imgs_set_(430, 380, 530, 430, cla, img, 0.8)
                                            if imgs_ is not None and imgs_ != False:
                                                click_pos_2(480, 730, cla)
                                                time.sleep(1)
                                        time.sleep(0.2)
                                    else:
                                        my_lv_go(cla, lv)
                                        is_walking = True

                                    time.sleep(1)

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

                                if is_walking == True:

                                    attack = False

                                    full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\check\\hunting_1.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(400, 850, 600, 900, cla, img, 0.8)
                                    if imgs_ is not None and imgs_ != False:
                                        print("lv_hunting_1", imgs_)
                                        attack = True
                                    full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\check\\hunting_2.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(400, 850, 600, 900, cla, img, 0.8)
                                    if imgs_ is not None and imgs_ != False:
                                        print("lv_hunting_2", imgs_)
                                        attack = True
                                    full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\check\\hunting_3.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(400, 850, 600, 900, cla, img, 0.8)
                                    if imgs_ is not None and imgs_ != False:
                                        print("lv_hunting_3", imgs_)
                                        attack = True


                                    if v_.skill_checked_ == False:
                                        skill_check_(cla)
                                        time.sleep(0.2)


                                    if attack == False:
                                        click_pos_2(925, 850, cla)
                                        time.sleep(0.2)
                                    else:
                                        click_pos_2(925, 850, cla)
                                        time.sleep(0.1)
                                        click_pos_2(925, 850, cla)
                                        time.sleep(0.2)



                else:
                    for i in range(2):
                        drag_pos(820, 260, 820, 820, cla)
                        time.sleep(0.2)
                        click_pos_2(820, 260, cla)
                        time.sleep(0.2)
                    time.sleep(0.5)
                    if int(lv) == 40:
                        click_pos_2(400, 550, cla)
                        time.sleep(0.1)
                    elif int(lv) == 45:
                        click_pos_2(400, 350, cla)
                        time.sleep(0.1)
                    elif int(lv) == 50:
                        click_pos_2(550, 750, cla)
                        time.sleep(0.1)
                time.sleep(0.2)
            else:
                click_pos_2(110, 160, cla)
                time.sleep(0.1)
                for i in range(10):
                    full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\gyucjunji\\kiidebat.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(777, 77, 865, 115, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("격전지 지도임")
                        break
                    time.sleep(0.5)
            time.sleep(0.2)
    except Exception as e:
        print(e)