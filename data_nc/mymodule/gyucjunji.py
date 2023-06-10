import time

import requests
import json
# import os
import sys
sys.path.append('C:/my_games/nightcrow/data_nc/mymodule')

import variable as v_


def gyucjunji_play(cla):
    try:
        import cv2
        import numpy as np
        from function import text_check_get, int_put_, imgs_set_, click_pos_2, click_pos_reg, drag_pos
        from action import menu_open, clean_screen
        from massenger import line_to_me
        from potion import maul_potion

        print("gyucjunji_play")



        complete_ = False

        print("격전지 시작")

        dungeon_clear = False

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

            time.sleep(1)

            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\dungeon\juljun_mode.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(400, 120, 600, 160, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("juljun_dungeon", imgs_)
                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\gyucjunji\\toohab_2.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(40, 40, 200, 80, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("toohab_2", imgs_)
                    full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\dungeon\\dongool_hunting.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(450, 640, 540, 710, cla, img, 0.9)
                    if imgs_ is not None and imgs_ != False:
                        in_dungeon__ = True
                        print("격전지 사냥중인듯 하다")
                        # 동굴 진입해서 사냥중
                        juljun_attack(cla)
                    else:
                        drag_pos(360, 550, 600, 550, cla)
                else:
                    drag_pos(360, 550, 600, 550, cla)

            else:
                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\gyucjunji\\toohab_1.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(30, 75, 200, 110, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("toohab_1", imgs_)

                    in_dungeon__ = True

                    now_playing(cla)
                else:
                    full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\gyucjunji\\gyuc_jabhwa.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(10, 145, 110, 180, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("gyuc_jabhwa", imgs_)

                        in_dungeon__ = True

                        now_playing(cla)
                    else:

                        # 던전 진입하기
                        print("격전지 진입하기")
                        gyucjunji_in(cla)



        return complete_
    except Exception as e:
        print(e)

def gyucjunji_in(cla):
    import numpy as np
    import cv2
    from function import click_pos_reg, imgs_set_, click_pos_2
    from action import menu_open
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
                        cancle_ = True
                        break
                    time.sleep(0.3)
                is_walking = False
                if cancle_ == True:
                    full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\gyucjunji\\cancle.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(0, 0, 960, 1030, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        in_gyuc_ = True
                    else:
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
                            time.sleep(0.2)

                    if is_walking == True:

                        arrive = False
                        arrive_count = 0
                        while arrive is False:
                            arrive_count += 1
                            if arrive_count > 10:
                                arrive = True
                                in_gyuc_ = True

                            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\gyucjunji\\arrive_killdebat.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(430, 380, 530, 430, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_2(480, 730, cla)
                                time.sleep(1)

                            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\gyucjunji\\toohab_1.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(0, 0, 960, 1030, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                arrive = True
                                in_gyuc_ = True
                                click_pos_2(230, 90, cla)
                                time.sleep(0.2)
                            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\gyucjunji\\gyuc_jabhwa.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(10, 145, 110, 180, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_2(230, 90, cla)

            else:
                menu_open(cla)
    except Exception as e:
        print(e)

def now_playing(cla):
    try:
        import cv2
        import numpy as np
        from function import text_check_get, int_put_, click_pos_2, click_pos_reg, imgs_set_, drag_pos
        from potion import potion_check, maul_potion
        from action import clean_screen, out_check, bag_open, skill_check_, in_maul_check
        from get_item import guild_jilyung


        print("now_격전지_playing")

        play_ = False

        in_ = False
        while in_ is False:

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

            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\dungeon\juljun_mode.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(400, 120, 600, 160, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\gyucjunji\\toohab_2.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(40, 40, 200, 80, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("toohab_2 now_playing...", imgs_)
                    in_ = True


            if in_ == False:
                clean_screen(cla)
                go_ice_1 = False
                go_ice_count = 0
                while go_ice_1 is False:
                    print("go_ice_count_1", go_ice_count)
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
                            print("go_ice_count_2", go_ice_count)
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
                                                    full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\jadong\\in_spot_walking_2.PNG"
                                                    img_array = np.fromfile(full_path, np.uint8)
                                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                                    imgs_ = imgs_set_(480, 880, 500, 900, cla, img, 0.8)
                                                    if imgs_ is not None and imgs_ != False:
                                                        is_walking_count = 0
                                                        print("사냥터 이동...in_spot_walking_2 보여", is_walking_count)
                                                    else:
                                                        print("사냥터 이동...in_spot_walking_2 안 보여", is_walking_count)
                                                    time.sleep(0.2)

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
                                    full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\gyucjunji\\toohab_3.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(100, 100, 670, 870, cla, img, 0.8)
                                    if imgs_ is not None and imgs_ != False:
                                        click_pos_reg(imgs_.x - 70, imgs_.y, cla)
                                time.sleep(0.2)
                            else:
                                click_pos_2(110, 160, cla)
                            time.sleep(0.2)
                    else:
                        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\gyucjunji\\gyuc_jabhwa.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(10, 145, 110, 180, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_2(230, 90, cla)
                    time.sleep(0.3)







            else:
                v_.skill_checked_ = True

                # m 이 없어질때 절전어택 시작작
                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\gyucjunji\\toohab_1.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(50, 75, 150, 110, cla, img, 0.75)
                if imgs_ is not None and imgs_ != False:
                    if v_.who_attack_ == False:
                        click_pos_2(25, 970, cla)
                        v_.who_attack_ = True
                    else:
                        juljun_attack(cla)
                        v_.who_attack_ = False
                else:
                    print("정상적으로 사냥중...총 10초 딜레이중")
                    potion_check(cla)
                    time.sleep(10)
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

        return play_
    except Exception as e:
        print(e)


def juljun_attack(cla):
    try:
        import cv2
        import numpy as np
        from datetime import date, timedelta, datetime
        from function import text_check_get, int_put_, click_pos_2, click_pos_reg, imgs_set_, drag_pos, change_number
        from massenger import line_to_me
        from action import in_number_check, bag_open, maul_check, in_maul_check, clean_screen, gyucjunji_check


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
                print("격전지 대기중인 비행장일 경우 절전 전투모드 잠시 해제")
                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\gyucjunji\\gyuc_jabhwa.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(10, 145, 110, 180, cla, img, 0.9)
                if imgs_ is not None and imgs_ != False:
                    print("격전지 대기중인 비행장이면 스케쥴 진행 ㄱㄱ", imgs_)
                    in_maul_ = True
                else:
                    # 격전지 비행장인지 체크
                    result_maul = gyucjunji_check(v_.now_cla)
                    if result_maul == True:
                        click_pos_2(230, 90, v_.now_cla)
                        in_maul_ = True
                    else:
                        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\dungeon\\gujum.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(450, 640, 490, 670, cla, img, 0.9)
                        if imgs_ is not None and imgs_ != False:
                            in_maul_ = True
                            print("거점이다. 격전지 대기중인 비행장인듯 하다.", imgs_)
                            drag_pos(360, 550, 600, 550, cla)
                            time.sleep(1)
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
                            imgs_ = imgs_set_(450, 640, 540, 710, cla, img, 0.9)
                            if imgs_ is not None and imgs_ != False:
                                print("격전지 사냥중인듯 하다")
                            else:
                                in_maul_ = True
                                print("격전지 사냥중이지 않다. 다시 체크해보자", imgs_)
                                drag_pos(360, 550, 600, 550, cla)
                                time.sleep(1)
                                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\dungeon\\y_1.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(300, 400, 800, 800, cla, img, 0.9)
                                if imgs_ is not None and imgs_ != False:
                                    click_pos_reg(imgs_.x, imgs_.y, cla)

                if in_maul_ == True:
                    print("절전모드 잠시 중지...")
                    continue_juljun = True
                else:
                    print("절전모드 피격시 옮기기 모드")
                    full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\dungeon\juljun_mode.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(400, 120, 600, 160, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("gyuc_juljun_mode", imgs_)

                        # 물약 파악
                        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\dungeon\juljun_potion.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(250, 960, 750, 1030, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("gyuc_juljun_mode juljun_potion 일딴 물약 있다", imgs_)
                            x_reg = imgs_.x
                            y_reg = imgs_.y
                            if cla == "two":
                                x_reg = x_reg - 960

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
                                    else:
                                        v_.mypotion_2 = potion

                                    if potion < 50:
                                        v_.potion_count += 1
                                        if v_.potion_count > 3:
                                            v_.potion_count = 0
                                            # maul_potion(cla)
                                            drag_maul_potion_(cla)
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
                                        else:
                                            v_.mypotion_2 = potion

                                        if potion < 10:
                                            v_.potion_count += 1
                                            if v_.potion_count > 5:
                                                v_.potion_count = 0
                                                # maul_potion(cla)
                                                drag_maul_potion_(cla)
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
                                            else:
                                                v_.mypotion_2 = potion

                                            if potion < 50:
                                                v_.potion_count += 1
                                                if v_.potion_count > 5:
                                                    v_.potion_count = 0
                                                    # maul_potion(cla)
                                                    drag_maul_potion_(cla)
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
                                            # maul_potion(cla)
                                            drag_maul_potion_(cla)
                                            continue_juljun = True

                    else:
                        nowtime_ = datetime.today().strftime("%Y년%m월%d일 %H시%M분%S초")
                        # print("현재시간", nowtime_)
                        print("한대 맞은 듯...랜덤 이동 보이면 바로 이동하기!!")
                        line_to_me(cla, str(nowtime_) + "에 어떤 놈이 공격했다")

                        in_dungeon__ = False
                        in_dungeon__count = 0
                        while in_dungeon__ is False:
                            in_dungeon__count += 1
                            if in_dungeon__count > 10:
                                in_dungeon__count = 0
                                in_dungeon__ = True

                            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\dungeon\juljun_mode.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(400, 120, 600, 160, cla, img, 0.8)
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
                                    full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\check\\random_move_1.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(250, 960, 420, 1030, cla, img, 0.8)
                                    if imgs_ is not None and imgs_ != False:
                                        print("격전지 : 랜덤이동 보여서 클릭")
                                        click_pos_reg(imgs_.x, imgs_.y, cla)
                                        fast_random_move_ = True
                                    else:
                                        print("격전지 : 랜덤이동 보여서 클릭 후 다시 절전모드 클릭")
                                        click_pos_2(345, 995, cla)
                                        # 이동 했으면 다시 사냥 시작 후 절전모드 하기
                                    time.sleep(0.1)

                                    juljun_ready = False
                                    juljun_ready_count = 0
                                    while juljun_ready is False:
                                        juljun_ready_count += 1
                                        if juljun_ready_count > 10:
                                            juljun_ready = True

                                        # 격전지인지 파악
                                        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\gyucjunji\\toohab_1.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(30, 75, 200, 110, cla, img, 0.75)
                                        if imgs_ is not None and imgs_ != False:
                                            print("격전지 절전모드에서 진행중")
                                            # 공격하기

                                            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\check\\hunting_1.PNG"
                                            img_array = np.fromfile(full_path, np.uint8)
                                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                            imgs_ = imgs_set_(400, 850, 600, 900, cla, img, 0.8)
                                            if imgs_ is not None and imgs_ != False:
                                                print("hunting_1", imgs_)
                                                juljun_ready = True
                                            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\check\\hunting_2.PNG"
                                            img_array = np.fromfile(full_path, np.uint8)
                                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                            imgs_ = imgs_set_(400, 850, 600, 900, cla, img, 0.8)
                                            if imgs_ is not None and imgs_ != False:
                                                print("hunting_2", imgs_)
                                                juljun_ready = True
                                            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\check\\hunting_3.PNG"
                                            img_array = np.fromfile(full_path, np.uint8)
                                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                            imgs_ = imgs_set_(400, 850, 600, 900, cla, img, 0.8)
                                            if imgs_ is not None and imgs_ != False:
                                                print("hunting_3", imgs_)
                                                juljun_ready = True

                                            if juljun_ready == False:
                                                # 가방 닫기
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
                                                print("격전지 : 공격하기 클릭후 절전모드 진입")
                                                click_pos_2(930, 850, cla)
                                                time.sleep(1)
                                                # 절전모드로 다시 진입하기
                                                click_pos_2(25, 970, cla)
                                            else:
                                                # 절전모드로 다시 진입하기
                                                print("격전지 : 공격중이라 절전모드 바로 진입")
                                                click_pos_2(25, 970, cla)
                                        else:
                                            # 마을인지 보기
                                            print("격전지 비행지인지 파악")

                                            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\character_start\\y_.PNG"
                                            img_array = np.fromfile(full_path, np.uint8)
                                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                            imgs_ = imgs_set_(0, 0, 960, 1030, cla, img, 0.8)
                                            if imgs_ is not None and imgs_ != False:
                                                click_pos_reg(imgs_.x, imgs_.y, cla)
                                                time.sleep(0.3)

                                            #격전지 비행지인지 파악
                                            result_maul_in = gyucjunji_check(cla)
                                            if result_maul_in == True:
                                                juljun_ready = True
                                                continue_juljun = True
                                                fast_random_move_ = True
                                                in_dungeon__ = True
                                    last_juljun = False
                                    last_juljun_count = 0
                                    while last_juljun is False:
                                        last_juljun_count += 1
                                        if last_juljun_count > 10:
                                            last_juljun = True
                                            continue_juljun = True
                                            line_to_me(cla, "격전지 진입 오류")
                                            clean_screen(cla)
                                        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\dungeon\juljun_mode.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(400, 120, 600, 160, cla, img, 0.8)
                                        if imgs_ is not None and imgs_ != False:
                                            last_juljun = True
                                        else:
                                            print("격전지 절전 모드 진입중")
                                            result_maul_in = gyucjunji_check(cla)
                                            if result_maul_in == True:
                                                continue_juljun = True
                                                fast_random_move_ = True
                                                in_dungeon__ = True
                                        time.sleep(0.2)







        # potion_ = text_check_get(515, 1007, 542, 1022, cla)
        # print("전체4자리 potion_2 =>", potion_)
        #
        # potion_ = text_check_get(515, 1007, 536, 1022, cla)
        # print("앞3자리 potion_ =>", potion_)
        #
        # potion_ = text_check_get(520, 1007, 542, 1022, cla)
        # print("뒷3자리 potion_ =>", potion_)




    except Exception as e:
        print(e)

def drag_maul_potion_(cla):
    try:
        import cv2
        import numpy as np
        from function import text_check_get, int_put_, click_pos_2, click_pos_reg, imgs_set_, drag_pos
        from potion import maul_potion
        from action import in_maul_check, out_check, clean_screen

        print("drag_potion")



        go_maul_ = False
        go_maul_count = 0
        while go_maul_ is False:
            go_maul_count += 1
            if go_maul_count > 10:
                go_maul_ = True
            result_maul = in_maul_check(cla)
            if result_maul == True:
                go_maul_= True
                maul_potion(cla)


            else:
                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\dungeon\juljun_mode.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(400, 120, 600, 160, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("juljun_dungeon...", imgs_)
                    drag_pos(360, 550, 600, 550, cla)
                else:
                    # 절전모드 아닐 경우
                    full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\dungeon\\dongool_1.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(30, 75, 200, 110, cla, img, 0.75)
                    if imgs_ is not None and imgs_ != False:
                        go_maul_ = True
                        print("동굴 절전모드 포션 구하러 가는 길")
                        print(imgs_)
                        maul_potion(cla)
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