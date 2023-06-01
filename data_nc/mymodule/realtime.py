import time

import requests
import json
# import os
import sys
sys.path.append('C:/my_games/nightcrow/data_nc/mymodule')

import variable as v_


def mystatus_check():
    try:
        from function import imgs_set_, click_pos_reg, imgs_set, text_check_get, int_put_, text_check_get_3, click_pos_2
        from action import menu_open, dead_die_before
        from get_item import get_items, get_upjuk
        from jadong_crow import jadong_play

        import numpy as np
        import pyautogui
        import cv2

        cla = "one"

        if cla == 'one':
            plus = 0
        if cla == 'two':
            plus = 960



        dead_die_before(cla)

        get_upjuk(cla)


    except Exception as e:
        print(e)


def moogi_(cla):
    try:
        from function import imgs_set_, click_pos_reg, imgs_set, text_check_get, int_put_, text_check_get_3, click_pos_2, drag_pos
        from action import menu_open, dead_die_before
        from get_item import get_items, get_upjuk
        from jadong_crow import jadong_play

        import numpy as np
        import pyautogui
        import cv2

        moo_1 = False
        moo_count = 0
        while moo_1 is False:
            moo_count += 1
            if moo_count > 3:
                moo_1 = True
            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\check\\moogi_sooglyun_1.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(30, 30, 140, 80, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("moogi_title", imgs_)
                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\check\\point.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(20, 410, 250, 1030, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    moo_1 = True
                    print("point : moo_1", imgs_)
                    click_pos_reg(imgs_.x - 20, imgs_.y + 20, cla)

                    moo_2 = False
                    while moo_2 is False:
                        moo_count += 1
                        if moo_count > 4:
                            moo_2 = True
                        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\check\\moogi_sooglyun_2.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(450, 330, 560, 380, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\check\\none_1.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(640, 700, 715, 735, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                print("none")

                                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\check\\point.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(110, 400, 200, 690, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    print("point : moo_2", imgs_)
                                    click_pos_reg(imgs_.x + 100, imgs_.y + 20, cla)


                            else:
                                print("무언가 있다.")
                                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\check\\moogi_sooglyun_4.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(490, 590, 615, 625, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    moo_2 = True
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\check\\moogi_sooglyun_3.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(750, 695, 850, 735, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                            time.sleep(0.5)


                        else:
                            print("진행중")
                        time.sleep(0.3)
                    click_pos_2(930, 60, cla)
                    time.sleep(0.3)
                    click_pos_2(930, 60, cla)

                else:
                    drag_pos(130, 900, 130, 500, cla)
            else:
                menu_open(cla)

                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\check\\point.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(790, 110, 820, 150, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("무기숙련 있다?", imgs_)
                    click_pos_2(790, 140, cla)
                else:
                    print("무기숙련 없다?")
                    moo_1 = True
                    click_pos_2(930, 60, cla)
            time.sleep(0.5)
        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\check\\moogi_sooglyun_1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(30, 30, 140, 80, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            click_pos_2(930, 60, cla)
    except Exception as e:
        print(e)

def soojib(cla):
    try:
        from function import imgs_set_, click_pos_reg, imgs_set, text_check_get, int_put_, text_check_get_3, click_pos_2, drag_pos
        from action import menu_open, dead_die_before
        from get_item import get_items, get_upjuk
        from jadong_crow import jadong_play

        import numpy as np
        import pyautogui
        import cv2

        print("수집")

        if v_.onCollection == True:
            print("수집 on")
            col_1 = False
            collect_count = 0
            while col_1 is False:
                collect_count += 1
                if collect_count > 15:
                    col_1 = True
                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\check\\collection_1.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(30, 30, 140, 80, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("collection_1", imgs_)

                    col_1 = True

                    full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\check\\confirm_1.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(490, 580, 630, 630, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("confirm_1 : collection", imgs_)
                        click_pos_reg(imgs_.x, imgs_.y, cla)

                    print("몬스터")
                    collect_1 = False
                    collect_count2 = 0
                    while collect_1 is False:
                        collect_count2 += 1
                        if collect_count2 > 15:
                            collect_1 = True
                        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\check\\point.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(90, 70, 150, 130, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("point : col_1", imgs_)
                            click_pos_reg(imgs_.x - 20, imgs_.y + 10, cla)
                            time.sleep(0.3)
                            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\check\\point.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(220, 130, 620, 990, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                print("point : collection", imgs_)
                                click_pos_reg(imgs_.x - 20, imgs_.y + 20, cla)
                                time.sleep(0.5)
                                click_pos_2(830, 950, cla)
                                time.sleep(0.5)
                            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\check\\confirm_1.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(490, 580, 630, 630, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                print("confirm_1 : collection", imgs_)
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                                time.sleep(0.5)
                            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\check\\confirm_1.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(490, 580, 630, 630, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                print("confirm_1 : collection", imgs_)
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                        else:
                            collect_1 = True

                    print("골동품")
                    collect_1 = False
                    collect_count2 = 0
                    while collect_1 is False:
                        collect_count2 += 1
                        if collect_count2 > 15:
                            collect_1 = True
                        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\check\\point.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(415, 70, 470, 130, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("point : col_1", imgs_)
                            click_pos_reg(imgs_.x - 20, imgs_.y + 10, cla)
                            time.sleep(0.3)
                            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\check\\point.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(220, 130, 620, 990, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                print("point : collection", imgs_)
                                click_pos_reg(imgs_.x - 20, imgs_.y + 20, cla)
                                time.sleep(0.5)
                                click_pos_2(830, 950, cla)
                                time.sleep(0.5)
                            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\check\\confirm_1.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(490, 580, 630, 630, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                print("confirm_1 : collection", imgs_)
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                                time.sleep(0.5)
                            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\check\\confirm_1.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(490, 580, 630, 630, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                print("confirm_1 : collection", imgs_)
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                        else:
                            collect_1 = True



                else:
                    menu_open(cla)

                    time.sleep(1)

                    full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\check\\point.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(925, 110, 950, 150, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("point : soojib", imgs_)
                        click_pos_2(930, 140, cla)
                    else:
                        col_1 = True
                time.sleep(0.5)

        print("몬스터 장비 골동품 수집 안함, 수집 off")
        col_1 = False
        collect_count = 0
        while col_1 is False:
            collect_count += 1
            if collect_count > 15:
                col_1 = True
            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\check\\collection_1.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(30, 30, 140, 80, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("collection_1", imgs_)

                col_1 = True

                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\check\\confirm_1.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(490, 580, 630, 630, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("confirm_1 : collection", imgs_)
                    click_pos_reg(imgs_.x, imgs_.y, cla)

                print("업적")
                collect_1 = False
                collect_count2 = 0
                while collect_1 is False:
                    collect_count2 += 1
                    if collect_count2 > 15:
                        collect_1 = True
                    full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\check\\point.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(180, 70, 270, 130, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("point : col_1", imgs_)
                        click_pos_reg(imgs_.x - 20, imgs_.y + 10, cla)
                        time.sleep(0.3)
                        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\check\\point.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(220, 130, 620, 990, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("point : collection", imgs_)
                            click_pos_reg(imgs_.x - 20, imgs_.y + 20, cla)
                            time.sleep(0.5)
                            click_pos_2(830, 950, cla)
                            time.sleep(0.5)
                        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\check\\confirm_1.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(490, 580, 630, 630, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("confirm_1 : collection", imgs_)
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                            time.sleep(0.5)
                        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\check\\confirm_1.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(490, 580, 630, 630, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("confirm_1 : collection", imgs_)
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                    else:
                        collect_1 = True

                print("이벤트")
                collect_1 = False
                collect_count2 = 0
                while collect_1 is False:
                    collect_count2 += 1
                    if collect_count2 > 15:
                        collect_1 = True
                    full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\check\\point.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(530, 70, 610, 130, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("point : col_1", imgs_)
                        click_pos_reg(imgs_.x - 20, imgs_.y + 10, cla)
                        time.sleep(0.3)
                        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\check\\point.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(220, 130, 620, 990, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("point : collection", imgs_)
                            click_pos_reg(imgs_.x - 20, imgs_.y + 20, cla)
                            time.sleep(0.5)
                            click_pos_2(830, 950, cla)
                            time.sleep(0.5)
                        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\check\\confirm_1.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(490, 580, 630, 630, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("confirm_1 : collection", imgs_)
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                            time.sleep(0.5)
                        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\check\\confirm_1.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(490, 580, 630, 630, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("confirm_1 : collection", imgs_)
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                    else:
                        collect_1 = True


            else:
                menu_open(cla)

                time.sleep(1)

                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\check\\point.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(925, 110, 950, 150, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("point : soojib", imgs_)

                    click_pos_2(930, 140, cla)
                else:
                    col_1 = True

                # click_pos_2(930, 140, cla)
                # in_soojib_ = False
                # in_soojib_count = 0
                # while in_soojib_ is False:
                #     in_soojib_count += 1
                #     if in_soojib_count > 5:
                #         in_soojib_ = True
                #     full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\check\\collection_1.PNG"
                #     img_array = np.fromfile(full_path, np.uint8)
                #     img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                #     imgs_ = imgs_set_(30, 30, 140, 80, cla, img, 0.8)
                #     if imgs_ is not None and imgs_ != False:
                #         print("collection_1", imgs_)
                #         in_soojib_ = True
                #     time.sleep(0.2)

            time.sleep(0.5)
        col_last = False
        collect_count = 0
        while col_last is False:
            collect_count += 1
            if collect_count > 15:
                col_last = True
            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\check\\collection_1.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(30, 30, 140, 80, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("collection_1", imgs_)
                click_pos_2(930, 60, cla)
            else:
                col_last = True

    except Exception as e:
        print(e)

def soojib_exam(cla):
    try:
        from function import imgs_set_, click_pos_reg, imgs_set, text_check_get, int_put_, text_check_get_3, click_pos_2, drag_pos
        from action import menu_open, dead_die_before
        from get_item import get_items, get_upjuk
        from jadong_crow import jadong_play

        import numpy as np
        import pyautogui
        import cv2

        if v_.onCollection == True:
            col_1 = False
            collect_count = 0
            while col_1 is False:
                collect_count += 1
                if collect_count > 15:
                    col_1 = True
                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\check\\collection_1.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(30, 30, 140, 80, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("collection_1", imgs_)

                    full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\check\\confirm_1.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(490, 580, 630, 630, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("confirm_1 : collection", imgs_)
                        click_pos_reg(imgs_.x, imgs_.y, cla)

                    full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\check\\point.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(20, 70, 480, 130, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("point : col_1", imgs_)
                        click_pos_reg(imgs_.x - 20, imgs_.y + 10, cla)
                        time.sleep(0.3)
                        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\check\\point.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(220, 130, 620, 990, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("point : collection", imgs_)
                            click_pos_reg(imgs_.x - 20, imgs_.y + 20, cla)
                            time.sleep(0.5)
                            click_pos_2(830, 950, cla)
                            time.sleep(0.5)
                        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\check\\confirm_1.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(490, 580, 630, 630, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("confirm_1 : collection", imgs_)
                            click_pos_reg(imgs_.x, imgs_.y, cla)


                    else:
                        col_2 = False
                        collect_count = 0
                        while col_2 is False:
                            collect_count += 1
                            if collect_count > 15:
                                col_2 = True
                            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\check\\collection_1.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(30, 30, 140, 80, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                print("collection_1", imgs_)
                                click_pos_2(930, 60, cla)
                            else:
                                col_1 = True
                                col_2 = True
                else:
                    menu_open(cla)
                    click_pos_2(930, 140, cla)
                time.sleep(0.5)
        else:
            print("수집 안함")
            col_1 = False
            collect_count = 0
            while col_1 is False:
                collect_count += 1
                if collect_count > 15:
                    col_1 = True
                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\check\\collection_1.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(30, 30, 140, 80, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("collection_1", imgs_)

                    col_1 = True

                    full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\check\\confirm_1.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(490, 580, 630, 630, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("confirm_1 : collection", imgs_)
                        click_pos_reg(imgs_.x, imgs_.y, cla)

                    collect_1 = False
                    collect_count2 = 0
                    while collect_1 is False:
                        collect_count2 += 1
                        if collect_count2 > 15:
                            collect_1 = True
                        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\check\\point.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(180, 70, 270, 130, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("point : col_1", imgs_)
                            click_pos_reg(imgs_.x - 20, imgs_.y + 10, cla)
                            time.sleep(0.3)
                            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\check\\point.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(220, 130, 620, 990, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                print("point : collection", imgs_)
                                click_pos_reg(imgs_.x - 20, imgs_.y + 20, cla)
                                time.sleep(0.5)
                                click_pos_2(830, 950, cla)
                                time.sleep(0.5)
                            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\check\\confirm_1.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(490, 580, 630, 630, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                print("confirm_1 : collection", imgs_)
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                                time.sleep(0.5)
                            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\check\\confirm_1.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(490, 580, 630, 630, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                print("confirm_1 : collection", imgs_)
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                        else:
                            collect_1 = True
                    collect_1 = False
                    collect_count2 = 0
                    while collect_1 is False:
                        collect_count2 += 1
                        if collect_count2 > 15:
                            collect_1 = True
                        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\check\\point.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(530, 70, 610, 130, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("point : col_1", imgs_)
                            click_pos_reg(imgs_.x - 20, imgs_.y + 10, cla)
                            time.sleep(0.3)
                            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\check\\point.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(220, 130, 620, 990, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                print("point : collection", imgs_)
                                click_pos_reg(imgs_.x - 20, imgs_.y + 20, cla)
                                time.sleep(0.5)
                                click_pos_2(830, 950, cla)
                                time.sleep(0.5)
                            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\check\\confirm_1.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(490, 580, 630, 630, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                print("confirm_1 : collection", imgs_)
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                                time.sleep(0.5)
                            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\check\\confirm_1.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(490, 580, 630, 630, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                print("confirm_1 : collection", imgs_)
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                        else:
                            collect_1 = True


                else:
                    menu_open(cla)
                    click_pos_2(930, 140, cla)
                time.sleep(0.5)


    except Exception as e:
        print(e)

def jaelyo_(cla):
    try:

        from function import click_pos_2, imgs_set, imgs_set_, random_int, drag_pos, text_check_get, click_pos_reg
        from action import out_check, clean_screen, bag_open
        from sell_potion import sell_potion_start
        import numpy as np
        import cv2
        import os

        print("재료 창고에 넣기")
        # 창고 가기

        in_chango_1 = False
        in_chango_1_count = 0
        while in_chango_1 is False:
            in_chango_1_count += 1
            if in_chango_1_count > 5:
                in_chango_1 = True
            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\chango\\maul_chango_1.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(0, 70, 220, 330, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:

                in_chango_2 = False
                in_chango_2_count = 0
                while in_chango_2 is False:
                    in_chango_2_count += 1
                    if in_chango_2_count > 5:
                        in_chango_2_count = 0
                        in_chango_2 = True
                    full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\chango\\maul_chango_2.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(50, 80, 110, 110, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:

                        # 물약 있을 경우 전부다 팔아버리기
                        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\chango\\sell_potion_1.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(0, 0, 300, 1000, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            sell_potion_start(cla)
                            time.sleep(1)


                        in_chango_3 = False
                        in_chango_3_count = 0
                        while in_chango_3 is False:
                            in_chango_3_count += 1
                            if in_chango_3_count > 5:
                                in_chango_3 = True
                            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\chango\\maul_chango_3.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(50, 80, 110, 110, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_2(930, 265, cla)
                                time.sleep(0.5)
                                click_pos_2(170, 1010, cla)

                                dir_path = "C:\\my_games\\nightcrow\\data_nc"
                                file_path = dir_path + "\\items\\chango\\jaelyo.txt"
                                ###
                                if os.path.isfile(file_path) == True:
                                    with open(file_path, "r", encoding='utf-8-sig') as file:
                                        jaelyo_ready = file.read().splitlines()
                                        print("jaelyos", jaelyo_ready)
                                ###
                                for i in range(len(jaelyo_ready)):
                                    full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\chango\\" + jaelyo_ready[i] + ".PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(680, 90, 910, 880, cla, img, 0.8)
                                    if imgs_ is not None and imgs_ != False:
                                        print("재료 있")
                                        click_pos_reg(imgs_.x, imgs_.y, cla)
                                        time.sleep(0.1)
                                        click_pos_reg(imgs_.x, imgs_.y, cla)
                                        time.sleep(0.1)
                                        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\chango\\bogwan.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(500, 400, 600, 500, cla, img, 0.8)
                                        if imgs_ is not None and imgs_ != False:
                                            click_pos_reg(imgs_.x, imgs_.y, cla)
                                sj_ = False
                                sj_count = 0
                                while sj_ is False:
                                    sj_count += 1
                                    if sj_count > 5:
                                        sj_ = True
                                    full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\chango\\soojib_item.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(680, 90, 910, 880, cla, img, 0.8)
                                    if imgs_ is not None and imgs_ != False:
                                        print("수집재료 있")
                                        click_pos_reg(imgs_.x + 15, imgs_.y + 15, cla)
                                        time.sleep(0.1)
                                        click_pos_reg(imgs_.x + 15, imgs_.y + 15, cla)
                                        time.sleep(0.1)
                                        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\chango\\bogwan.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(500, 400, 600, 500, cla, img, 0.8)
                                        if imgs_ is not None and imgs_ != False:
                                            click_pos_reg(imgs_.x, imgs_.y, cla)

                                    else:
                                        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\chango\\maul_chango_3.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(50, 80, 110, 110, cla, img, 0.8)
                                        if imgs_ is not None and imgs_ != False:
                                            click_pos_2(930, 60, cla)
                                        else:
                                            in_chango_1 = True
                                            in_chango_2 = True
                                            in_chango_3 = True
                                            sj_ = True
                                            print("창고 정리 끝")

                            else:
                                click_pos_2(20, 200, cla)

                        in_chango_3 = False
                        in_chango_3_count = 0
                        while in_chango_3 is False:
                            in_chango_3_count += 1
                            if in_chango_3_count > 5:
                                in_chango_3 = True
                            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\chango\\maul_chango_4.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(50, 80, 110, 110, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_2(930, 145, cla)
                                time.sleep(0.5)
                                # click_pos_2(170, 1010, cla)

                                dir_path = "C:\\my_games\\nightcrow\\data_nc"
                                file_path = dir_path + "\\items\\chango\\jaelyo.txt"
                                ###
                                if os.path.isfile(file_path) == True:
                                    with open(file_path, "r", encoding='utf-8-sig') as file:
                                        jaelyo_ready = file.read().splitlines()
                                        print("jaelyos", jaelyo_ready)
                                ###
                                for i in range(len(jaelyo_ready)):
                                    full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\chango\\" + jaelyo_ready[i] + ".PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(680, 90, 910, 880, cla, img, 0.8)
                                    if imgs_ is not None and imgs_ != False:
                                        print("재료 있")
                                        click_pos_reg(imgs_.x, imgs_.y, cla)
                                        time.sleep(0.1)
                                        click_pos_reg(imgs_.x, imgs_.y, cla)
                                        time.sleep(0.1)
                                        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\chango\\bogwan.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(500, 400, 600, 500, cla, img, 0.8)
                                        if imgs_ is not None and imgs_ != False:
                                            click_pos_reg(imgs_.x, imgs_.y, cla)
                                sj_ = False
                                sj_count = 0
                                while sj_ is False:
                                    sj_count += 1
                                    if sj_count > 5:
                                        sj_ = True
                                    full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\chango\\soojib_item.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(680, 90, 910, 880, cla, img, 0.8)
                                    if imgs_ is not None and imgs_ != False:
                                        print("수집재료 있")
                                        click_pos_reg(imgs_.x + 15, imgs_.y + 15, cla)
                                        time.sleep(0.1)
                                        click_pos_reg(imgs_.x + 15, imgs_.y + 15, cla)
                                        time.sleep(0.1)
                                        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\chango\\bogwan.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(500, 400, 600, 500, cla, img, 0.8)
                                        if imgs_ is not None and imgs_ != False:
                                            click_pos_reg(imgs_.x, imgs_.y, cla)

                                    else:
                                        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\chango\\maul_chango_4.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(50, 80, 110, 110, cla, img, 0.8)
                                        if imgs_ is not None and imgs_ != False:
                                            click_pos_2(930, 60, cla)
                                        else:
                                            in_chango_1 = True
                                            in_chango_2 = True
                                            in_chango_3 = True
                                            sj_ = True
                                            print("창고 정리 끝")

                            else:
                                click_pos_2(20, 150, cla)

                    else:
                        if in_chango_2_count == 1:
                            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\chango\\maul_chango_1.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(0, 70, 220, 330, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                        else:
                            time.sleep(3)


            else:
                result_out = out_check(cla)
                if result_out == False:
                    clean_screen(cla)
                else:
                    full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\chango\\chanel.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(160, 80, 220, 120, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_2(230, 90, cla)








    except Exception as e:
        print(e)

def boonhae_(cla):
    try:
        import cv2
        import numpy as np
        from function import text_check_get, int_put_, click_pos_2, imgs_set_, click_pos_reg
        from action import bag_open


        bag_open(cla)

        boonhae_ready = False
        boonhae_ready_count = 0
        while boonhae_ready is False:
            boonhae_ready_count += 1
            if boonhae_ready_count > 5:
                boonhae_ready = True

            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\chango\\boonhae_title.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(480, 80, 540, 160, cla, img, 0.83)
            if imgs_ is not None and imgs_ != False:
                print("분해화면")
                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\chango\\boonhae_not_check.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(415, 345, 450, 380, cla, img, 0.83)
                if imgs_ is not None and imgs_ != False:
                    print("분해체크하기")
                    click_pos_2(435, 365, cla)
                    time.sleep(0.1)
                    #click_pos_2(510, 365, cla)
                else:
                    click_pos_2(580, 450, cla)
                    time.sleep(0.2)
                    click_pos_2(475, 425, cla)
                    boonhae_ready = True
            else:
                click_pos_2(770, 930, cla)
            time.sleep(0.3)

        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\chango\\boonhae_after.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(420, 450, 500, 500, cla, img, 0.83)
        if imgs_ is not None and imgs_ != False:
            click_pos_reg(imgs_.x, imgs_.y, cla)
        print("분해하기 끝")

    except Exception as e:
        print(e)