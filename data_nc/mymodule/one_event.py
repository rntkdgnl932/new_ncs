import time

import requests
import json
# import os
import sys
sys.path.append('C:/my_games/nightcrow/data_nc/mymodule')

import variable as v_


def daily_one(cla):
    try:
        print("one_event_없음")

    except Exception as e:
        print(e)
        return 0

def daily_one_ex(cla):
    try:

        from function import click_pos_2, imgs_set, imgs_set_, random_int, drag_pos, text_check_get, click_pos_reg
        from action import out_check, clean_screen, bag_open, menu_open
        import numpy as np
        import cv2
        import os

        print("매일 한번 하기")
        print("일반 이벤트 성장 비약")
        # 일반 이벤트 성장 비약
        go_event = False
        go_event_count = 0
        while go_event is False:
            go_event_count += 1
            if go_event_count > 5:
                go_event = True

            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\item_1\\event\\sangjum_title.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(50, 40, 140, 75, cla, img, 0.83)
            if imgs_ is not None and imgs_ != False:
                # 이벤트 메뉴 있는지 확인 후 없다면 클릭
                event_menu_bool = False
                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\item_1\\event\\event_menu_1.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(10, 120, 80, 220, cla, img, 0.83)
                if imgs_ is not None and imgs_ != False:
                    event_menu_bool = True
                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\item_1\\event\\event_menu_2.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(10, 120, 80, 220, cla, img, 0.83)
                if imgs_ is not None and imgs_ != False:
                    event_menu_bool = True

                if event_menu_bool == False:
                    click_pos_2(215, 110, cla)
                    time.sleep(0.5)




                # 일반 이벤트 메뉴 클릭
                click_pos_2(100, 155, cla)
                time.sleep(0.5)

                # 품절이 아니라면

                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\item_1\\event\\poomjul.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(200, 200, 300, 300, cla, img, 0.83)
                if imgs_ is not None and imgs_ != False:
                    print("성장비약 품절", imgs_)
                    go_event = True
                else:
                    # 성장 비약 클릭
                    click_pos_2(270, 270, cla)
                    time.sleep(0.5)
                    full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\item_1\\event\\biyac_sungjang.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(400, 310, 540, 380, cla, img, 0.83)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_2(570, 710, cla)
            else:
                menu_open(cla)
                click_pos_2(750, 60, cla)
        print("일반 이벤트 재운의 비약")
        # 일반 이벤트 성장 비약
        go_event = False
        go_event_count = 0
        while go_event is False:
            go_event_count += 1
            if go_event_count > 5:
                go_event = True

            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\item_1\\event\\sangjum_title.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(50, 40, 140, 75, cla, img, 0.83)
            if imgs_ is not None and imgs_ != False:
                # 이벤트 메뉴 있는지 확인 후 없다면 클릭
                event_menu_bool = False
                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\item_1\\event\\event_menu_1.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(10, 120, 80, 220, cla, img, 0.83)
                if imgs_ is not None and imgs_ != False:
                    event_menu_bool = True
                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\item_1\\event\\event_menu_2.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(10, 120, 80, 220, cla, img, 0.83)
                if imgs_ is not None and imgs_ != False:
                    event_menu_bool = True

                if event_menu_bool == False:
                    click_pos_2(215, 110, cla)
                    time.sleep(0.5)

                # 일반 이벤트 메뉴 클릭
                click_pos_2(100, 155, cla)
                time.sleep(0.5)

                # 품절이 아니라면

                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\item_1\\event\\poomjul.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(200, 440, 300, 540, cla, img, 0.83)
                if imgs_ is not None and imgs_ != False:
                    print("성장비약 품절", imgs_)
                    go_event = True
                else:
                    # 재운의 비약 클릭
                    click_pos_2(270, 490, cla)
                    time.sleep(0.5)
                    full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\item_1\\event\\biyac_jaewoon.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(400, 310, 540, 380, cla, img, 0.83)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_2(570, 710, cla)
            else:
                menu_open(cla)
                click_pos_2(750, 60, cla)

        print("소환 이벤트 무기 외형 소환")
        # 소환 이벤트 무기 외형 소환
        go_event = False
        go_event_count = 0
        while go_event is False:
            go_event_count += 1
            if go_event_count > 5:
                go_event = True

            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\item_1\\event\\sangjum_title.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(40, 40, 140, 90, cla, img, 0.83)
            if imgs_ is not None and imgs_ != False:
                # 이벤트 메뉴 있는지 확인 후 없다면 클릭
                event_menu_bool = False
                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\item_1\\event\\event_menu_1.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(10, 120, 80, 220, cla, img, 0.83)
                if imgs_ is not None and imgs_ != False:
                    event_menu_bool = True
                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\item_1\\event\\event_menu_2.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(10, 120, 80, 220, cla, img, 0.83)
                if imgs_ is not None and imgs_ != False:
                    event_menu_bool = True

                if event_menu_bool == False:
                    click_pos_2(215, 110, cla)
                    time.sleep(0.5)

                # 소환 이벤트 메뉴 클릭
                click_pos_2(100, 185, cla)
                time.sleep(0.5)

                # 품절이 아니라면

                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\item_1\\event\\poomjul.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(240, 200, 300, 300, cla, img, 0.83)
                if imgs_ is not None and imgs_ != False:
                    print("무기외형 품절1", imgs_)
                else:
                    # 무기 소환 클릭
                    click_pos_2(270, 270, cla)
                    time.sleep(0.5)
                    full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\item_1\\event\\sohwan_1.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(400, 310, 540, 380, cla, img, 0.83)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_2(570, 710, cla)
                        time.sleep(0.5)
                        last_tal(cla)
                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\item_1\\event\\poomjul.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(440, 200, 500, 300, cla, img, 0.83)
                if imgs_ is not None and imgs_ != False:
                    print("무기외형 품절2", imgs_)
                else:
                    # 무기 소환 클릭
                    click_pos_2(470, 270, cla)
                    time.sleep(0.5)
                    full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\item_1\\event\\sohwan_1.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(400, 310, 540, 380, cla, img, 0.83)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_2(570, 710, cla)
                        time.sleep(0.5)
                        last_tal(cla)
                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\item_1\\event\\poomjul.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(640, 200, 700, 300, cla, img, 0.83)
                if imgs_ is not None and imgs_ != False:
                    print("무기외형 품절3", imgs_)
                    go_event = True
                else:
                    # 무기 소환 클릭
                    click_pos_2(670, 270, cla)
                    time.sleep(0.5)
                    full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\item_1\\event\\sohwan_1.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(400, 310, 540, 380, cla, img, 0.83)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_2(570, 710, cla)
                        time.sleep(0.5)
                        last_tal(cla)
                        go_event = True


            else:
                menu_open(cla)
                click_pos_2(750, 60, cla)
            time.sleep(1)
        print("소환 이벤트 탈것 소환")
        # 소환 이벤트 탈것것 소환
        go_event = False
        go_event_count = 0
        while go_event is False:
            go_event_count += 1
            if go_event_count > 5:
                go_event = True

            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\item_1\\event\\sangjum_title.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(50, 40, 140, 75, cla, img, 0.83)
            if imgs_ is not None and imgs_ != False:
                # 이벤트 메뉴 있는지 확인 후 없다면 클릭
                event_menu_bool = False
                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\item_1\\event\\event_menu_1.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(10, 120, 80, 220, cla, img, 0.83)
                if imgs_ is not None and imgs_ != False:
                    event_menu_bool = True
                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\item_1\\event\\event_menu_2.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(10, 120, 80, 220, cla, img, 0.83)
                if imgs_ is not None and imgs_ != False:
                    event_menu_bool = True

                if event_menu_bool == False:
                    click_pos_2(215, 110, cla)
                    time.sleep(0.5)

                # 소환 이벤트 메뉴 클릭
                click_pos_2(100, 185, cla)
                time.sleep(0.5)

                # 품절이 아니라면

                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\item_1\\event\\poomjul.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(240, 430, 300, 500, cla, img, 0.83)
                if imgs_ is not None and imgs_ != False:
                    print("탈것 품절1", imgs_)
                else:
                    # 탈것 클릭
                    click_pos_2(270, 470, cla)
                    time.sleep(0.5)
                    full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\item_1\\event\\sohwan_2.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(400, 310, 540, 380, cla, img, 0.83)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_2(570, 710, cla)
                        time.sleep(0.5)

                        last_tal(cla)

                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\item_1\\event\\poomjul.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(440, 430, 500, 500, cla, img, 0.83)
                if imgs_ is not None and imgs_ != False:
                    print("탈것 품절2", imgs_)
                else:
                    # 탈것 클릭
                    click_pos_2(470, 470, cla)
                    time.sleep(0.5)
                    full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\item_1\\event\\sohwan_2.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(400, 310, 540, 380, cla, img, 0.83)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_2(570, 710, cla)
                        time.sleep(0.5)
                        last_tal(cla)
                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\item_1\\event\\poomjul.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(640, 430, 700, 500, cla, img, 0.83)
                if imgs_ is not None and imgs_ != False:
                    print("탈것 품절3", imgs_)
                    go_event = True
                else:
                    # 탈것 클릭
                    click_pos_2(670, 470, cla)
                    time.sleep(0.5)
                    full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\item_1\\event\\sohwan_2.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(400, 310, 540, 380, cla, img, 0.83)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_2(570, 710, cla)
                        time.sleep(0.5)
                        last_tal(cla)
                        go_event = True


            else:
                menu_open(cla)
                click_pos_2(750, 60, cla)
        # 마무리
        time.sleep(0.5)
        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\clean_screen\\exit_1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(800, 0, 960, 120, cla, img, 0.83)
        if imgs_ is not None and imgs_ != False:
            print("exit_1", imgs_)
            click_pos_reg(imgs_.x, imgs_.y, cla)
            
    except Exception as e:
            print(e)


def last_tal(cla):
    import cv2
    import numpy as np
    from function import imgs_set_, click_pos_2, click_pos_reg
    try:
        print("소환 마무리")
        tal_1 = False
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
                while tal_last is False:
                    full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\item_1\\exit_1.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(400, 900, 570, 1030, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                    else:
                        tal_1 = True
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
    except Exception as e:
        print(e)
        return 0

