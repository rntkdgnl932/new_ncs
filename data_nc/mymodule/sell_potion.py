import time

import requests
import json
# import os
import sys
sys.path.append('C:/my_games/nightcrow/data_nc/mymodule')

import variable as v_


def sell_potion_start(cla):
    try:

        from function import click_pos_2, imgs_set, imgs_set_, random_int, drag_pos, text_check_get, click_pos_reg
        from action import out_check, clean_screen, bag_open
        import numpy as np
        import cv2
        import os

        print("창고 포션 팔기")
        # 창고 가기

        in_chango_1 = False
        in_chango_1_count = 0
        while in_chango_1 is False:
            in_chango_1_count += 1
            if in_chango_1_count > 100:
                in_chango_1 = True

            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\check\\touching.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(0, 0, 960, 1030, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("touching", imgs_)
            else:
                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\chango\\maul_chango_1.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(0, 70, 220, 330, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:

                    in_chango_2 = False
                    in_chango_2_count = 0
                    while in_chango_2 is False:
                        in_chango_2_count += 1
                        if in_chango_2_count > 100:
                            in_chango_2_count = 0
                            in_chango_2 = True

                        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\check\\touching.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(0, 0, 960, 1030, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("touching", imgs_)
                        else:

                            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\chango\\maul_chango_2.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(50, 80, 110, 110, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:

                                in_chango_3 = False
                                in_chango_3_count = 0
                                while in_chango_3 is False:
                                    in_chango_3_count += 1
                                    if in_chango_3_count > 100:
                                        in_chango_3 = True

                                    full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\check\\touching.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(0, 0, 960, 1030, cla, img, 0.8)
                                    if imgs_ is not None and imgs_ != False:
                                        print("touching", imgs_)
                                    else:
                                        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\chango\\sell_potion_1.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(0, 0, 300, 1000, cla, img, 0.8)
                                        if imgs_ is not None and imgs_ != False:
                                            in_chango_3 = True
                                            in_chango_1_count = 0
                                            in_chango_2_count = 0
                                            in_chango_3_count = 0

                                            click_pos_reg(imgs_.x, imgs_.y, cla)
                                            time.sleep(0.1)
                                            click_pos_reg(imgs_.x, imgs_.y, cla)
                                            time.sleep(0.1)
                                            click_pos_2(930, 55, cla)

                                            #반복문
                                            issangin_ = False
                                            while issangin_ is False:

                                                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\check\\touching.PNG"
                                                img_array = np.fromfile(full_path, np.uint8)
                                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                                imgs_ = imgs_set_(0, 0, 960, 1030, cla, img, 0.8)
                                                if imgs_ is not None and imgs_ != False:
                                                    print("touching", imgs_)
                                                else:
                                                    full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\chango\\sangin_gabang.PNG"
                                                    img_array = np.fromfile(full_path, np.uint8)
                                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                                    imgs_ = imgs_set_(850, 70, 910, 120, cla, img, 0.8)
                                                    if imgs_ is not None and imgs_ != False:
                                                        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\chango\\sell_potion_1.PNG"
                                                        img_array = np.fromfile(full_path, np.uint8)
                                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                                        imgs_ = imgs_set_(680, 110, 920, 920, cla, img, 0.8)
                                                        if imgs_ is not None and imgs_ != False:
                                                            click_pos_reg(imgs_.x, imgs_.y, cla)

                                                        #반복문
                                                        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\chango\\max.PNG"
                                                        img_array = np.fromfile(full_path, np.uint8)
                                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                                        imgs_ = imgs_set_(520, 560, 610, 610, cla, img, 0.8)
                                                        if imgs_ is not None and imgs_ != False:
                                                            click_pos_reg(imgs_.x, imgs_.y, cla)
                                                            time.sleep(0.1)
                                                            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\chango\\sell_y.PNG"
                                                            img_array = np.fromfile(full_path, np.uint8)
                                                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                                            imgs_ = imgs_set_(480, 710, 610, 770, cla, img, 0.8)
                                                            if imgs_ is not None and imgs_ != False:
                                                                click_pos_reg(imgs_.x, imgs_.y, cla)
                                                                time.sleep(0.1)
                                                                click_pos_2(930, 55, cla)
                                                                issangin_ = True

                                                    else:
                                                        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\jadong\\in_spot_walking_2.PNG"
                                                        img_array = np.fromfile(full_path, np.uint8)
                                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                                        imgs_ = imgs_set_(480, 880, 500, 900, cla, img, 0.8)
                                                        if imgs_ is not None and imgs_ != False:
                                                            print("가는 중")
                                                        else:
                                                            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\chango\\chobo_skill_sangin.PNG"
                                                            img_array = np.fromfile(full_path, np.uint8)
                                                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                                            imgs_ = imgs_set_(0, 70, 220, 330, cla, img, 0.8)
                                                            if imgs_ is not None and imgs_ != False:
                                                                click_pos_reg(imgs_.x, imgs_.y, cla)
                                                    time.sleep(0.3)


                                        else:
                                            in_chango_1 = True
                                            in_chango_2 = True
                                            in_chango_3 = True
                                            print("찾고 팔기 끝")



                            else:
                                if in_chango_2_count == 1:
                                    full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\chango\\maul_chango_1.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(0, 70, 220, 330, cla, img, 0.8)
                                    if imgs_ is not None and imgs_ != False:
                                        click_pos_reg(imgs_.x, imgs_.y, cla)
                                else:
                                    time.sleep(2)


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




