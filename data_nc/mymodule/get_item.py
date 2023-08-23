import time

import requests
import json
# import os
import sys
sys.path.append('C:/my_games/nightcrow/data_nc/mymodule')

import variable as v_

season_count = 0

def get_items(cla):
    try:
        import cv2
        import numpy as np
        from function import text_check_get, int_put_, click_pos_reg, imgs_set_, click_pos_2, drag_pos
        from action import clean_screen, item_open
        from schedule import myQuest_play_add

        if cla == "one":
            potion = v_.mypotion_1
        if cla == "two":
            potion = v_.mypotion_2
        if cla == "three":
            potion = v_.mypotion_3
        if cla == "four":
            potion = v_.mypotion_4



        print("<< 아이템 받기 시작 >>")
        clean_screen(cla)
        # 시즌패스 받기
        print("시즌패스 받기")
        get_season_pass(cla)
        # 이벤트 받기
        print("이벤트 받기")
        get_event(cla)
        # 업적 받기
        print("업적 받기")
        get_upjuk(cla)
        # 신념전승
        print("신념전승")
        sinnyum_junseong(cla)
        # 길드 체크
        print("길드 체크")
        guild_check(cla)
        # 우편 받기
        print("우편 받기")
        get_post(cla)
        # 가방 아이템 정리
        print("가방 아이템 정리")
        item_open(cla)

        result_schedule = myQuest_play_check(v_.now_cla, "check")
        print("result_schedule", result_schedule)
        character_id = result_schedule[0][1]
        result_schedule_ = result_schedule[0][2]

        if result_schedule_ == "각종템받기":
            myQuest_play_add(cla, result_schedule_)

        clean_screen(cla)
        print("오케잇!!!!!!!!")



    except Exception as e:
        print(e)


def get_item_checking(cla):
    try:
        import cv2
        import numpy as np
        from function import text_check_get, int_put_, click_pos_reg, imgs_set_, click_pos_2, drag_pos
        from action import clean_screen, menu_open

        go_ = False

        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\check\\point.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(150, 0, 220, 100, cla, img, 0.85)
        if imgs_ is not None and imgs_ != False:
            print("시즌패스 체크", imgs_)
            go_ = True

        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\check\\point.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(770, 0, 830, 100, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("이벤트 체크", imgs_)
            go_ = True

        if go_ == True:

            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\character_start\\y_.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(0, 0, 960, 1030, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                click_pos_reg(imgs_.x, imgs_.y, cla)
                time.sleep(0.3)

            get_items(cla)

    except Exception as e:
        print(e)


def get_post(cla):
    try:
        import cv2
        import numpy as np
        from function import text_check_get, int_put_, click_pos_reg, imgs_set_, click_pos_2, drag_pos
        from action import clean_screen, menu_open

        in_post_ = False
        in_post_count = 0
        while in_post_ is False:
            in_post_count += 1
            if in_post_count > 5:
                in_post_ = True
            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\get_item\\post_1.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(40, 40, 120, 80, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("우편함", imgs_)

                point_search = False
                point_search_count = 0
                while point_search is False:
                    point_search_count += 1
                    if point_search_count > 10:
                        point_search = True
                    full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\check\\point.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(0, 0, 960, 1030, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        point_search = True
                        print("point search compleate", imgs_)
                    time.sleep(0.2)

                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\check\\point.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(360, 75, 420, 110, cla, img, 0.7)
                if imgs_ is not None and imgs_ != False:
                    print("point1", imgs_)

                    click_pos_2(350, 105, cla)
                    time.sleep(1)
                    system_post = False
                    system_post_count = 0
                    while system_post is False:

                        system_post_count += 1
                        if system_post_count > 7:
                            system_post = True
                        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\get_item\\post_2.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(810, 140, 960, 210, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_2(910, 180, cla)

                            time.sleep(0.3)
                            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\get_item\\confirm_1.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(470, 570, 640, 640, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\get_item\\confirm_1.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(470, 680, 640, 740, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_reg(imgs_.x, imgs_.y, cla)

                        else:
                            system_post = True

                            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\check\\point.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(110, 75, 155, 110, cla, img, 0.7)
                            if imgs_ is not None and imgs_ != False:
                                print("point2", imgs_)
                                click_pos_2(80, 105, cla)
                            else:
                                in_post_ = True
                        time.sleep(0.3)
                time.sleep(0.7)
                get_post_sever_ = False
                get_post_sever__count = 0
                while get_post_sever_ is False:

                    get_post_sever__count += 1
                    if get_post_sever__count > 7:
                        get_post_sever_ = True
                    full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\check\\point.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(110, 75, 155, 110, cla, img, 0.7)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_2(80, 105, cla)
                        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\check\\point.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(900, 120, 960, 330, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:
                            print("point2", imgs_)
                            in_post_ = True
                            click_pos_2(880, 1010, cla)
                            time.sleep(0.5)
                            click_pos_2(880, 1010, cla)
                            clean_screen(cla)
                    else:
                        in_post_ = True
                        get_post_sever_ = True
                        click_pos_2(930, 60, cla)
                        # click_pos_2(80, 105, cla)
                    time.sleep(0.3)




            else:
                menu_open(cla)

                time.sleep(0.5)

                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\check\\point.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(720, 970, 780, 1030, cla, img, 0.75)
                if imgs_ is not None and imgs_ != False:
                    click_pos_2(750, 1000, cla)
                else:
                    full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\check\\point_2.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(720, 970, 780, 1030, cla, img, 0.75)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_2(750, 1000, cla)
                    else:
                        print("우편에 빨강점이 안보여!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                        in_post_ = True
            time.sleep(0.5)

    except Exception as e:
        print(e)

def get_season_pass(cla):
    try:
        global season_count
        import cv2
        import numpy as np
        from function import text_check_get, int_put_, click_pos_reg, imgs_set_, click_pos_2, drag_pos, drag_pos_reg
        from action import clean_screen
        import random

        clean_screen(cla)
        time.sleep(1)
        complete_ = False
        while complete_ is False:
            season_count += 1
            if season_count > 20:
                complete_ = True
                season_count = 0

            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\check\\point.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(150, 0, 220, 100, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:
                print("시즌패스", imgs_)
                click_pos_reg(imgs_.x - 15, imgs_.y + 15, cla)

                a = 0
                b = 420
                get_season = False
                while get_season is False:
                    season_count += 1
                    if season_count > 20:
                        get_season = True
                        season_count = 0
                    full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\get_item\\pass_1.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(300, 500, 800, 800, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        get_season = True

                        get_season_start = False
                        while get_season_start is False:
                            season_count += 1
                            if season_count > 20:
                                get_season_start = True
                                season_count = 0
                            a = b
                            b = a + 50
                            if b < 750:

                                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\check\\point.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(240, a, 275, b, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    click_pos_reg(imgs_.x - 50, imgs_.y + 15, cla)
                                    time.sleep(0.4)
                                    click_pos_2(830, 695, cla)
                                    time.sleep(0.1)
                                    click_pos_2(830, 695, cla)
                                    time.sleep(0.3)


                                    # get_season_last = False
                                    # while get_season_last is False:
                                    #     season_count += 1
                                    #     if season_count > 20:
                                    #         get_season_last = True
                                    #         season_count = 0
                                    #     full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\check\\point.PNG"
                                    #     img_array = np.fromfile(full_path, np.uint8)
                                    #     img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    #     imgs_ = imgs_set_(240, a, 275, b, cla, img, 0.8)
                                    #     if imgs_ is not None and imgs_ != False:
                                    #
                                    #         full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\check\\point.PNG"
                                    #         img_array = np.fromfile(full_path, np.uint8)
                                    #         img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    #         imgs_ = imgs_set_(280, 495, 880, 525, cla, img, 0.85)
                                    #         if imgs_ is not None and imgs_ != False:
                                    #             click_pos_reg(imgs_.x - 20, imgs_.y + 45, cla)
                                    #             time.sleep(0.2)
                                    #             click_pos_2(860, 410, cla)
                                    #             time.sleep(0.3)
                                    #         else:
                                    #             print("1")
                                    #
                                    #             result_int = random.randint(150, 200)
                                    #
                                    #             full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\get_item\\checked.PNG"
                                    #             img_array = np.fromfile(full_path, np.uint8)
                                    #             img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    #             imgs_ = imgs_set_(280, 495, 880, 525, cla, img, 0.8)
                                    #             if imgs_ is not None and imgs_ != False:
                                    #                 drag_pos_reg(imgs_.x, imgs_.y, imgs_.x + result_int, imgs_.y, cla)
                                    #
                                    #             full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\get_item\\num_2.PNG"
                                    #             img_array = np.fromfile(full_path, np.uint8)
                                    #             img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    #             imgs_ = imgs_set_(350, 600, 450, 680, cla, img, 0.88)
                                    #             if imgs_ is not None and imgs_ != False:
                                    #                 get_season_last = True
                                    #
                                    #                 full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\check\\point.PNG"
                                    #                 img_array = np.fromfile(full_path, np.uint8)
                                    #                 img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    #                 imgs_ = imgs_set_(280, 495, 880, 525, cla, img, 0.85)
                                    #                 if imgs_ is not None and imgs_ != False:
                                    #                     print("?>???", imgs_)
                                    #                     click_pos_reg(imgs_.x - 20, imgs_.y + 45, cla)
                                    #                     time.sleep(0.2)
                                    #                     click_pos_2(860, 410, cla)
                                    #                     time.sleep(0.3)
                                    #                 else:
                                    #                     get_season_last = True
                                    #         time.sleep(1)
                                    #     else:
                                    #         get_season_last = True


                            else:
                                print("3")
                                get_season_start = True
                                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\get_item\\pass_1.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(300, 500, 800, 800, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    click_pos_2(860, 370, cla)
                                else:
                                    clean_screen(cla)
                            time.sleep(1)
                    else:
                        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\check\\point.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(150, 0, 220, 100, cla, img, 0.85)
                        if imgs_ is not None and imgs_ != False:
                            print("시즌패스", imgs_)
                            click_pos_reg(imgs_.x - 15, imgs_.y + 15, cla)
                    time.sleep(2)
            else:
                complete_ = True

            time.sleep(2)
        clean_screen(cla)

    except Exception as e:
        print(e)



def get_event(cla):
    try:
        import cv2
        import numpy as np
        from function import text_check_get, int_put_, click_pos_reg, imgs_set_, click_pos_2, drag_pos
        from action import clean_screen

        clean_screen(cla)
        time.sleep(1)
        complete_ = False
        complete_count = 0
        while complete_ is False:
            complete_count += 1
            if complete_count > 5:
                complete_ = True
            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\check\\point.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(770, 0, 830, 100, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("이벤트", imgs_)
                click_pos_reg(imgs_.x - 15, imgs_.y + 15, cla)

                a = 0
                b = 340
                get_season = False
                get_season_count = 0
                while get_season is False:
                    get_season_count += 0
                    if get_season_count > 5:
                        get_season = True
                    full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\get_item\\event_1.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(400, 300, 550, 350, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        get_season = True

                        get_season_start = False
                        get_season_start_count = 0
                        while get_season_start is False:
                            get_season_start_count += 1
                            if get_season_start_count > 10:
                                get_season_start = True


                            if b < 750:

                                a = b
                                b = a + 55

                                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\check\\point.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(200, a, 250, b, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    click_pos_reg(imgs_.x - 50, imgs_.y + 15, cla)
                                    time.sleep(0.4)

                                    get_season_last = False
                                    get_season_last_count = 0
                                    while get_season_last is False:
                                        get_season_last_count += 1
                                        if get_season_last_count > 5:
                                            get_season_last = True

                                        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\check\\point.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(200, a, 250, b, cla, img, 0.8)
                                        if imgs_ is not None and imgs_ != False:
                                            time.sleep(0.4)

                                            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\check\\point.PNG"
                                            img_array = np.fromfile(full_path, np.uint8)
                                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                            imgs_ = imgs_set_(280, 460, 880, 720, cla, img, 0.9)
                                            if imgs_ is not None and imgs_ != False:
                                                click_pos_reg(imgs_.x - 20, imgs_.y + 15, cla)
                                                time.sleep(0.2)
                                                click_pos_2(860, 410, cla)
                                                time.sleep(0.3)
                                            else:
                                                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\check\\point.PNG"
                                                img_array = np.fromfile(full_path, np.uint8)
                                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                                imgs_ = imgs_set_(760, 400, 870, 500, cla, img, 0.9)
                                                if imgs_ is not None and imgs_ != False:
                                                    click_pos_reg(imgs_.x - 20, imgs_.y + 15, cla)
                                                    time.sleep(0.2)
                                                    click_pos_2(860, 410, cla)
                                                    time.sleep(0.3)
                                                else:
                                                    if get_season_last_count > 3:
                                                        drag_pos(500, 600, 500, 300, cla)
                                                    if get_season_last_count > 5:
                                                        get_season_last = True
                                                    print("1")
                                        time.sleep(0.3)
                            else:
                                drag_pos(140, 660, 140, 430, cla)
                                time.sleep(0.5)

                                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\check\\point.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(200, 340, 250, 760, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    click_pos_reg(imgs_.x - 50, imgs_.y + 15, cla)
                                    time.sleep(0.4)

                                    get_season_last = False
                                    get_season_last_count = 0
                                    while get_season_last is False:
                                        get_season_last_count += 1
                                        if get_season_last_count > 5:
                                            get_season_last = True

                                        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\check\\point.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(280, 460, 880, 720, cla, img, 0.9)
                                        if imgs_ is not None and imgs_ != False:
                                            click_pos_reg(imgs_.x - 20, imgs_.y + 15, cla)
                                            time.sleep(0.2)
                                            click_pos_2(860, 410, cla)
                                            time.sleep(0.3)
                                        else:
                                            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\check\\point.PNG"
                                            img_array = np.fromfile(full_path, np.uint8)
                                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                            imgs_ = imgs_set_(760, 400, 870, 500, cla, img, 0.9)
                                            if imgs_ is not None and imgs_ != False:
                                                click_pos_reg(imgs_.x - 20, imgs_.y + 15, cla)
                                                time.sleep(0.2)
                                                click_pos_2(860, 410, cla)
                                                time.sleep(0.3)
                                            else:
                                                if get_season_last_count > 3:
                                                    drag_pos(500, 600, 500, 300, cla)
                                                if get_season_last_count > 5:
                                                    get_season_last = True
                                                print("11")
                                        time.sleep(0.3)

                                else:

                                    print("3")
                                    get_season_start = True
                                    full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\get_item\\event_1.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(400, 300, 550, 350, cla, img, 0.8)
                                    if imgs_ is not None and imgs_ != False:
                                        click_pos_2(870, 335, cla)
                                    else:
                                        clean_screen(cla)
                            time.sleep(1)
                    else:
                        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\check\\point.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(770, 0, 830, 100, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("이벤트", imgs_)
                            click_pos_reg(imgs_.x - 15, imgs_.y + 15, cla)
                    time.sleep(2)
            else:
                complete_ = True

            time.sleep(2)
        clean_screen(cla)

    except Exception as e:
        print(e)

def get_upjuk(cla):
    try:
        import cv2
        import numpy as np
        from function import text_check_get, int_put_, click_pos_reg, imgs_set_, click_pos_2, drag_pos
        from action import clean_screen, menu_open

        get_upjuk_ = False
        get_upjuk_count = 0
        while get_upjuk_ is False:
            get_upjuk_count += 1
            if get_upjuk_count > 5:
                get_upjuk_ = True
            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\get_item\\upjuk_1.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(400, 400, 535, 480, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                get_upjuk_ = True
                print("업적", imgs_)
                point_search = False
                point_search_count = 0
                while point_search is False:
                    point_search_count += 1
                    if point_search_count > 10:
                        point_search = True
                    full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\check\\point.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(0, 0, 960, 1030, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        point_search = True
                        print("point search compleate", imgs_)
                    time.sleep(0.2)
                # 성장
                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\check\\point.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(220, 470, 280, 520, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("성장", imgs_)
                    click_pos_reg(imgs_.x - 40, imgs_.y + 10, cla)

                    sungjang = False
                    sungjang_count = 0
                    while sungjang is False:
                        sungjang_count += 1
                        if sungjang_count > 5:
                            sungjang = True
                        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\get_item\\upjuk_sungjang.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(160, 90, 240, 140, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_2(850, 130, cla)
                            time.sleep(0.2)
                            sungjang = True
                            back_ = False
                            back_count = 0
                            while back_ is False:
                                back_count += 1
                                if back_count > 10:
                                    back_ = True
                                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\get_item\\upjuk_1.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(400, 400, 535, 480, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    sungjang = True
                                    back_ = True
                                else:
                                    click_pos_2(30, 55, cla)
                                time.sleep(0.2)
                # 협동
                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\check\\point.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(790, 470, 840, 520, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("협동", imgs_)
                    click_pos_reg(imgs_.x - 40, imgs_.y + 10, cla)
                    sungjang = False
                    sungjang_count = 0
                    while sungjang is False:
                        sungjang_count += 1
                        if sungjang_count > 5:
                            sungjang = True
                        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\get_item\\upjuk_hyubdong.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(160, 90, 240, 140, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_2(850, 130, cla)
                            time.sleep(0.2)
                            sungjang = True
                            back_ = False
                            back_count = 0
                            while back_ is False:
                                back_count += 1
                                if back_count > 10:
                                    back_ = True
                                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\get_item\\upjuk_1.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(400, 400, 535, 480, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    sungjang = True
                                    back_ = True
                                else:
                                    click_pos_2(30, 55, cla)
                                time.sleep(0.2)
                # 장비
                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\check\\point.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(220, 700, 280, 740, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("장비", imgs_)
                    click_pos_reg(imgs_.x - 40, imgs_.y + 10, cla)
                    sungjang = False
                    sungjang_count = 0
                    while sungjang is False:
                        sungjang_count += 1
                        if sungjang_count > 5:
                            sungjang = True
                        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\get_item\\upjuk_jangbi.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(160, 90, 240, 140, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_2(850, 130, cla)
                            time.sleep(0.2)
                            sungjang = True
                            back_ = False
                            back_count = 0
                            while back_ is False:
                                back_count += 1
                                if back_count > 10:
                                    back_ = True
                                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\get_item\\upjuk_1.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(400, 400, 535, 480, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    sungjang = True
                                    back_ = True
                                else:
                                    click_pos_2(30, 55, cla)
                                time.sleep(0.2)
                # 모험
                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\check\\point.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(790, 700, 840, 740, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("모험", imgs_)
                    click_pos_reg(imgs_.x - 40, imgs_.y + 10, cla)
                    sungjang = False
                    sungjang_count = 0
                    while sungjang is False:
                        sungjang_count += 1
                        if sungjang_count > 5:
                            sungjang = True
                        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\get_item\\upjuk_mohum.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(160, 90, 240, 140, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_2(850, 130, cla)
                            time.sleep(0.2)
                            sungjang = True
                            back_ = False
                            back_count = 0
                            while back_ is False:
                                back_count += 1
                                if back_count > 10:
                                    back_ = True
                                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\get_item\\upjuk_1.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(400, 400, 535, 480, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    sungjang = True
                                    back_ = True
                                else:
                                    click_pos_2(30, 55, cla)
                                time.sleep(0.2)
                # 주요 업적
                last_upjuk_ = False
                last_upjuk_count = 0
                while last_upjuk_ is False:
                    last_upjuk_count += 1
                    if last_upjuk_count > 10:
                        last_upjuk_ = True
                    full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\check\\point.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(400, 600, 560, 660, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("주요업적", imgs_)
                        click_pos_reg(imgs_.x - 40, imgs_.y + 10, cla)
                        time.sleep(0.5)
                        click_pos_2(480, 730, cla)
                    else:
                        last_upjuk_ = True
                        clean_screen(cla)
                    time.sleep(0.2)


            else:
                menu_open(cla)

                time.sleep(0.5)

                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\check\\point.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(780, 160, 825, 195, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    click_pos_2(790, 190, cla)
                else:
                    get_upjuk_ = True
                time.sleep(0.5)


    except Exception as e:
        print(e)

def sinnyum_junseong(cla):
    try:
        import cv2
        import numpy as np
        from function import text_check_get, int_put_, click_pos_reg, imgs_set_, click_pos_2, drag_pos
        from action import clean_screen, menu_open

        get_trust = False
        get_trust_count = 0
        while get_trust is False:
            get_trust_count += 1
            if get_trust_count > 5:
                get_trust = True
            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\get_item\\sinnyum_title.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(500, 340, 550, 380, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\get_item\\sinnyum_zero.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(460, 380, 495, 415, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    get_trust = True
                else:
                    right_ = False
                    right_count = 0
                    while right_ is False:
                        right_count += 1
                        if right_count > 10:
                            right_ = True
                        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\get_item\\sinnyum_right.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(380, 530, 430, 590, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("sinnyum_right", imgs_)
                            right_ = True

                            last_sinnyum = False
                            last_sinnyum_count = 0
                            while last_sinnyum is False:
                                last_sinnyum_count += 1
                                if last_sinnyum_count > 10:
                                    last_sinnyum = True
                                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\get_item\\sinnyum_zero.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(460, 380, 495, 415, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    click_pos_2(520, 725, cla)
                                    time.sleep(0.1)
                                    click_pos_2(520, 725, cla)
                                    full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\get_item\\sinnyum_title.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(500, 340, 550, 380, cla, img, 0.8)
                                    if imgs_ is not None and imgs_ != False:
                                        click_pos_2(930, 60, cla)
                                    else:
                                        last_sinnyum = True

                                else:
                                    full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\get_item\\sinnyum_right.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(380, 530, 430, 590, cla, img, 0.8)
                                    if imgs_ is not None and imgs_ != False:
                                        click_pos_reg(imgs_.x, imgs_.y, cla)

                        else:
                            # 활쟁이
                            click_pos_2(365, 565, cla)
                            time.sleep(0.5)





            else:
                menu_open(cla)

                time.sleep(0.5)

                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\check\\point.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(875, 160, 910, 195, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    click_pos_2(885, 190, cla)
                    time.sleep(1.5)
                else:
                    get_trust = True



    except Exception as e:
        print(e)


def guild_check(cla):
    try:
        import cv2
        import numpy as np
        from function import text_check_get, int_put_, click_pos_reg, imgs_set_, click_pos_2, drag_pos
        from action import clean_screen, menu_open

        #clean_screen(cla)

        get_guild = False
        get_guild_count = 0
        while get_guild is False:
            get_guild_count += 1
            if get_guild_count > 7:
                get_guild = True
            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\guild\\guild_title.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(20, 30, 100, 80, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:

                time.sleep(0.2)

                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\guild\\guild_giboo_out.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(400, 900, 700, 1030, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:


                    full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\check\\point.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(110, 80, 150, 115, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_reg(imgs_.x - 70, imgs_.y + 10, cla)
                        time.sleep(0.5)

                        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\guild\\guild_information.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(400, 900, 600, 1030, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            time.sleep(0.3)
                            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\check\\point.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(840, 940, 890, 990, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                print("guild_point", imgs_)
                                click_pos_reg(imgs_.x - 70, imgs_.y + 10, cla)
                                time.sleep(0.1)
                                click_pos_reg(imgs_.x - 70, imgs_.y + 10, cla)
                                time.sleep(0.1)
                                click_pos_reg(imgs_.x - 70, imgs_.y + 10, cla)
                                time.sleep(0.1)

                            click_pos_2(430, 950, cla)
                            time.sleep(0.1)
                            click_pos_2(430, 950, cla)
                            time.sleep(0.1)
                            click_pos_2(430, 950, cla)
                            time.sleep(0.1)

                            giboo_ = False
                            giboo_count = 0
                            while giboo_ is False:
                                giboo_count += 1
                                if giboo_count > 7:
                                    giboo_ = True

                                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\guild\\guild_giboo.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(440, 300, 510, 380, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    giboo_ = True
                                    for i in range(5):
                                        click_pos_2(230, 670, cla)
                                    time.sleep(0.1)
                                    for i in range(2):
                                        click_pos_2(930, 60, cla)
                                        get_guild = True
                                    clean_screen(cla)

                                else:
                                    click_pos_2(555, 950, cla)
                                time.sleep(0.5)
                        else:
                            time.sleep(0.2)
                            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\check\\point.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(840, 940, 890, 990, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                print("guild_point", imgs_)
                                click_pos_reg(imgs_.x - 70, imgs_.y + 10, cla)
                                time.sleep(0.1)
                                click_pos_reg(imgs_.x - 70, imgs_.y + 10, cla)
                                time.sleep(0.1)
                                click_pos_reg(imgs_.x - 70, imgs_.y + 10, cla)
                                time.sleep(0.1)

                            click_pos_2(430, 990, cla)
                            time.sleep(0.1)
                            click_pos_2(430, 990, cla)
                            time.sleep(0.1)

                            giboo_ = False
                            giboo_count = 0
                            while giboo_ is False:
                                giboo_count += 1
                                if giboo_count > 7:
                                    giboo_ = True
                                # 위치 바뀜
                                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\guild\\guild_giboo.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(440, 300, 510, 380, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    giboo_ = True
                                    for i in range(3):
                                        click_pos_2(230, 670, cla)
                                    time.sleep(0.1)
                                    for i in range(2):
                                        click_pos_2(930, 60, cla)
                                        get_guild = True
                                    clean_screen(cla)

                                else:
                                    click_pos_2(555, 990, cla)
                                time.sleep(0.5)

                    full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\check\\point.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(350, 80, 420, 115, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_reg(imgs_.x - 70, imgs_.y + 10, cla)
                        guild_jilyung(cla, "dungeon")
                else:
                    get_guild = True
            else:
                menu_open(cla)

                time.sleep(0.5)

                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\check\\point.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(740, 235, 770, 270, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    click_pos_2(745, 260, cla)
                    time.sleep(1.5)
                else:
                    get_guild = True



    except Exception as e:
        print(e)

def guild_jilyung(cla, data):
    import cv2
    import numpy as np
    from function import click_pos_reg, imgs_set_, click_pos_2
    try:
        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\guild\\guild_title.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(20, 30, 100, 80, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:

            # 길드지령 보상 모두 받기
            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\check\\point.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(130, 745, 210, 780, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                click_pos_reg(imgs_.x - 50, imgs_.y + 10, cla)


            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\guild\\jilyung_refresh_3.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(800, 990, 900, 1030, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                click_pos_reg(imgs_.x, imgs_.y, cla)
                time.sleep(1)


            # 여기서부터 진짜 지령 수락...

            # 일반 지령(jadong)
            if data == "jadong":
                # 다른 곳 지령 중이면 포기부터...
                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\guild\\giveup.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(510, 680, 930, 730, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    click_pos_reg(imgs_.x, imgs_.y, cla)

                    j_c = False
                    j_c_count = 0
                    while j_c is False:
                        j_c_count += 1
                        if j_c_count > 10:
                            j_c = True

                        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\character_start\\y_.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(0, 0, 960, 1030, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                            j_c = True
                            time.sleep(0.3)

                            for z in range(10):
                                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\guild\\soolock.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(510, 680, 930, 730, cla, img, 0.9)
                                if imgs_ is not None and imgs_ != False:
                                    break
                                else:
                                    full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\character_start\\y_.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(0, 0, 960, 1030, cla, img, 0.8)
                                    if imgs_ is not None and imgs_ != False:
                                        click_pos_reg(imgs_.x, imgs_.y, cla)
                                time.sleep(0.3)

                        time.sleep(0.3)

                # 아래는 지령 수락 과정...
                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\guild\\soolock.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(300, 680, 470, 730, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    is_soolock = False
                    is_soolock_count = 0
                    while is_soolock is False:
                        is_soolock_count += 1
                        if is_soolock_count > 5:
                            is_soolock = True

                        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\guild\\jinhang.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(330, 480, 410, 560, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("진행 보여", imgs_)
                            click_pos_2(930, 60, cla)

                        else:
                            print("진행 안 보여")
                            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\guild\\soolock.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(300, 680, 470, 730, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                            # full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\guild\\soolock.PNG"
                            # img_array = np.fromfile(full_path, np.uint8)
                            # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            # imgs_ = imgs_set_(300, 680, 470, 730, cla, img, 0.8)
                            # if imgs_ is not None and imgs_ != False:
                            #
                            #     click_gilyung = False
                            #
                            #     full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\guild\\800.PNG"
                            #     img_array = np.fromfile(full_path, np.uint8)
                            #     img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            #     imgs_ = imgs_set_(300, 570, 430, 610, cla, img, 0.9)
                            #     if imgs_ is not None and imgs_ != False:
                            #         click_gilyung = True
                            #
                            #     full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\guild\\800_2.PNG"
                            #     img_array = np.fromfile(full_path, np.uint8)
                            #     img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            #     imgs_ = imgs_set_(300, 570, 430, 610, cla, img, 0.9)
                            #     if imgs_ is not None and imgs_ != False:
                            #         click_gilyung = True
                            #
                            #     full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\guild\\400.PNG"
                            #     img_array = np.fromfile(full_path, np.uint8)
                            #     img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            #     imgs_ = imgs_set_(300, 570, 430, 610, cla, img, 0.9)
                            #     if imgs_ is not None and imgs_ != False:
                            #         click_gilyung = True
                            #
                            #     full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\guild\\400_2.PNG"
                            #     img_array = np.fromfile(full_path, np.uint8)
                            #     img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            #     imgs_ = imgs_set_(300, 570, 430, 610, cla, img, 0.9)
                            #     if imgs_ is not None and imgs_ != False:
                            #         click_gilyung = True
                            #
                            #     if click_gilyung == True:
                            #         full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\guild\\soolock.PNG"
                            #         img_array = np.fromfile(full_path, np.uint8)
                            #         img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            #         imgs_ = imgs_set_(300, 680, 470, 730, cla, img, 0.8)
                            #         if imgs_ is not None and imgs_ != False:
                            #             click_pos_reg(imgs_.x, imgs_.y, cla)
                            #     else:
                            #         click_pos_2(845, 1015, cla)

                        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\guild\\guild_title.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(20, 30, 100, 80, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("길드지령 체크중")
                        else:
                            is_soolock = True
                        time.sleep(0.3)

            if data == "gyucjunji":
                # 다른 곳 지령 중이면 포기부터...1
                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\guild\\giveup.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(300, 680, 470, 730, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    click_pos_reg(imgs_.x, imgs_.y, cla)

                    j_c = False
                    j_c_count = 0
                    while j_c is False:
                        j_c_count += 1
                        if j_c_count > 10:
                            j_c = True

                        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\character_start\\y_.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(0, 0, 960, 1030, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                            j_c = True
                            time.sleep(0.3)
                            for z in range(10):
                                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\guild\\soolock.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(300, 680, 470, 730, cla, img, 0.9)
                                if imgs_ is not None and imgs_ != False:
                                    break
                                else:
                                    full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\character_start\\y_.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(0, 0, 960, 1030, cla, img, 0.8)
                                    if imgs_ is not None and imgs_ != False:
                                        click_pos_reg(imgs_.x, imgs_.y, cla)
                                time.sleep(0.3)

                        time.sleep(0.3)

                # 다른 곳 지령 중이면 포기부터...2
                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\guild\\giveup.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(740, 680, 930, 730, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    click_pos_reg(imgs_.x, imgs_.y, cla)

                    j_c = False
                    j_c_count = 0
                    while j_c is False:
                        j_c_count += 1
                        if j_c_count > 10:
                            j_c = True

                        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\character_start\\y_.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(0, 0, 960, 1030, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                            j_c = True
                            time.sleep(0.3)
                            for z in range(10):

                                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\guild\\soolock.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(740, 680, 930, 730, cla, img, 0.9)
                                if imgs_ is not None and imgs_ != False:
                                    break
                                else:
                                    full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\character_start\\y_.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(0, 0, 960, 1030, cla, img, 0.8)
                                    if imgs_ is not None and imgs_ != False:
                                        click_pos_reg(imgs_.x, imgs_.y, cla)
                                time.sleep(0.3)

                        time.sleep(0.3)

                # 아래는 지령 수락 과정...
                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\guild\\soolock.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(300, 680, 470, 730, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    is_soolock = False
                    is_soolock_count = 0
                    while is_soolock is False:
                        is_soolock_count += 1
                        if is_soolock_count > 5:
                            is_soolock = True
                        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\guild\\jinhang.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(560, 480, 625, 545, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("진행 보여", imgs_)
                            click_pos_2(930, 60, cla)
                        # full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\guild\\giveup.PNG"
                        # img_array = np.fromfile(full_path, np.uint8)
                        # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        # imgs_ = imgs_set_(300, 680, 470, 730, cla, img, 0.8)
                        # if imgs_ is not None and imgs_ != False:
                        #     print("진행 보여", imgs_)
                        #     click_pos_2(930, 60, cla)

                        else:
                            print("진행 안 보여")
                            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\guild\\soolock.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(560, 680, 660, 740, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_reg(imgs_.x, imgs_.y, cla)

                        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\guild\\guild_title.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(20, 30, 100, 80, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("길드지령 체크중")
                        else:
                            is_soolock = True
                        time.sleep(0.3)

            if data == "dungeon":
                # 다른 곳 지령 중이면 포기부터...
                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\guild\\giveup.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(290, 680, 720, 730, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    click_pos_reg(imgs_.x, imgs_.y, cla)

                    j_c = False
                    j_c_count = 0
                    while j_c is False:
                        j_c_count += 1
                        if j_c_count > 10:
                            j_c = True

                        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\character_start\\y_.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(0, 0, 960, 1030, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                            j_c = True
                            time.sleep(0.3)
                            for z in range(10):
                                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\guild\\soolock.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(290, 680, 720, 730, cla, img, 0.9)
                                if imgs_ is not None and imgs_ != False:
                                    break
                                else:
                                    full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\character_start\\y_.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(0, 0, 960, 1030, cla, img, 0.8)
                                    if imgs_ is not None and imgs_ != False:
                                        click_pos_reg(imgs_.x, imgs_.y, cla)
                                time.sleep(0.3)

                        time.sleep(0.3)

                # 아래는 지령 수락 과정...

                is_soolock_ready = False
                is_soolock_ready_count = 0
                while is_soolock_ready is False:
                    is_soolock_ready_count += 1
                    if is_soolock_ready_count > 4:
                        is_soolock_ready = True

                    full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\guild\\jinhang.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(780, 490, 850, 540, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("진행 보여")
                        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\guild\\special.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(760, 395, 920, 430, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("특수 보여", imgs_)
                            click_pos_2(835, 705, cla)
                            time.sleep(0.3)
                            for i in range(10):
                                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\character_start\\y_.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(0, 0, 960, 1030, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                                    break
                                time.sleep(0.2)
                        else:
                            is_soolock_ready = True
                            click_pos_2(930, 60, cla)




                    else:
                        print("진행 안 보여")
                        is_soolock = False
                        is_soolock_count = 0
                        while is_soolock is False:
                            is_soolock_count += 1
                            if is_soolock_count > 5:
                                is_soolock = True
                            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\guild\\special.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(760, 395, 810, 430, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                print("특수 보여용", imgs_)
                                click_pos_2(845, 1015, cla)
                            else:
                                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\guild\\soolock.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(740, 680, 920, 730, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    print("수락하즈아")
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                                    is_soolock = True

                            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\character_start\\y_.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(0, 0, 960, 1030, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_reg(imgs_.x, imgs_.y, cla)

                            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\guild\\guild_title.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(20, 30, 100, 80, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                print("길드지령 체크중")

                            time.sleep(0.5)
                    time.sleep(1)
                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\guild\\guild_title.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(20, 30, 100, 80, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    click_pos_2(930, 60, cla)

    except Exception as e:
        print(e)

def guild_jilyung_get(cla, data):
    import cv2
    import numpy as np
    from function import text_check_get, int_put_, click_pos_reg, imgs_set_, click_pos_2, drag_pos
    from action import clean_screen, menu_open
    try:
        # 추후 길드 가입 여부 부터 체크 후...
        # 아니면 화면에 길드 지령 있는지 확인 후...
        print("guild_jilyung_get")

        guild_in_ = False
        guild_in_count = 0
        while guild_in_ is False:
            guild_in_count += 1
            if guild_in_count > 5:
                guild_in_ = True

            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\guild\\guild_title.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(20, 30, 100, 80, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\guild\\guild_jilyung_click.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(280, 70, 400, 130, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                    guild_in_ = True
                    guild_jilyung(cla, data)
                else:
                    guild_in_ = True
                    click_pos_2(930, 60, cla)

            else:
                menu_open(cla)
                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\guild\\menu_guild.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(720, 100, 960, 450, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                    time.sleep(1)
            time.sleep(0.5)



    except Exception as e:
        print(e)