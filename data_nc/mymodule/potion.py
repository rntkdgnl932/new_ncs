import time

import requests
import json
# import os
import sys
sys.path.append('C:/my_games/nightcrow/data_nc/mymodule')

import variable as v_


def potion_check(cla):
    import cv2
    import numpy as np
    from function import imgs_set_num, imgs_set_
    from action import dead_die_before, juljun_check, out_check, juljun_off

    try:

        if cla == "one":
            potion = v_.mypotion_1
        if cla == "two":
            potion = v_.mypotion_2
        if cla == "three":
            potion = v_.mypotion_3
        if cla == "four":
            potion = v_.mypotion_4

        # 기준
        potion_zero = True

        result_juljun = juljun_check(cla)

        if result_juljun == False:

            result_out = out_check(cla)

            if result_out == True:

                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\potion\\quick3_potion_middle_zero.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_num(370, 990, 430, 1030, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("quick3_potion_middle_zero", imgs_)
                    potion_zero = True
                else:
                    print("물약 0개 이상 있다.")
                    potion_zero = False

                # for i in range(10):
                #     full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\potion\\out_number\\" + str(i) + ".PNG"
                #     img_array = np.fromfile(full_path, np.uint8)
                #     img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                #     imgs_ = imgs_set_num(240, 1004, 254, 1016, cla, img, 0.83)
                #     if imgs_ is not None and imgs_ != False:
                #         print("숫자는? ", i, imgs_)
                #         potion_zero = False
                #         v_.potion_count = 0
                #         break

            else:
                print("바깥 화면 아니라서 물약 파악 불가능...")
                potion_zero = False

            if potion_zero == True:

                v_.potion_count += 1
                print("물약 100개 이하로 파악된 횟수 => ", v_.potion_count)
                if v_.potion_count > 3:
                    v_.potion_count = 0

                    result = juljun_check(cla)
                    if result == True:
                        juljun_off(cla)

                    maul_potion_only(cla)
            else:
                print("물약 100개 이하로 파악된 횟수 => ", v_.potion_count)

        else:
            # potion_zero = juljun_potion_check(cla)

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

            potion_need = True

            what_potion_ = "none"
            x_reg = 0

            # 물약 파악
            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\dungeon\juljun_potion.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(100, 960, 750, 1030, cla, img, 0.7)
            if imgs_ is not None and imgs_ != False:
                what_potion_ = 'small'
                x_reg = imgs_.x
                print("what_potion_ = 'small'")
            else:
                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\dungeon\juljun_potion_2.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(100, 960, 750, 1030, cla, img, 0.7)
                if imgs_ is not None and imgs_ != False:
                    what_potion_ = 'middle'
                    x_reg = imgs_.x

                    print("what_potion_ = 'middle'")
            if what_potion_ == 'small' or what_potion_ == 'middle':
                for b in range(10):

                    for i in range(10):
                        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\potion\juljun_number\\" + str(
                            i) + ".PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_num(x_reg - minus, 1005, x_reg + 13 - minus, 1030, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("100자리 숫자는?'", i, imgs_)
                            potion_need = False
                            v_.potion_count = 0

                            break
                    if potion_need == False:
                        break
                    else:
                        time.sleep(0.1)
            else:
                potion_need = False
                print("절전 물약 파악 안되어서 보류...")



            if potion_need == True:

                v_.potion_count += 1
                print("물약 100개 이하로 파악된 횟수 => ", v_.potion_count)
                if v_.potion_count > 3:
                    v_.potion_count = 0

                    result = juljun_check(cla)
                    if result == True:
                        juljun_off(cla)

                    maul_potion_only(cla)
            else:
                print("물약 100개 이하로 파악된 횟수 => ", v_.potion_count)

        dead_die_before(cla)



        return potion_zero
    except Exception as e:
        print(e)




def juljun_potion_check(cla):
    import cv2
    import numpy as np
    from function import text_check_get, imgs_set_num, imgs_set_, click_pos_2

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

    try:

        print("juljun potion check")

        potion_need = True

        what_potion_ = "none"
        x_reg = 0

        # 물약 파악
        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\dungeon\juljun_potion.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(250, 960, 750, 1030, cla, img, 0.7)
        if imgs_ is not None and imgs_ != False:
            what_potion_ = 'small'
            x_reg = imgs_.x
            print("what_potion_ = 'small'")
        else:
            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\dungeon\juljun_potion_2.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(250, 960, 750, 1030, cla, img, 0.7)
            if imgs_ is not None and imgs_ != False:
                what_potion_ = 'middle'
                x_reg = imgs_.x

                print("what_potion_ = 'middle'")
        if what_potion_ == 'small' or what_potion_ == 'middle':
            for b in range(10):

                for i in range(10):
                    full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\potion\juljun_number\\" + str(
                        i) + ".PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_num(x_reg - minus, 1005, x_reg + 13 - minus, 1030, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("100자리 숫자는?'", i, imgs_)
                        potion_need = False
                        v_.potion_count = 0

                        break
                if potion_need == False:
                    break
                else:
                    time.sleep(0.1)
        else:
            potion_need = False
            print("절전 물약 파악 안되어서 보류...")


        return potion_need
    except Exception as e:
        print(e)

def maul_potion(cla):
    import cv2
    import numpy as np
    from function import int_put_, click_pos_2, imgs_set_, click_pos_reg, in_number_check, get_region, \
        image_processing, drag_pos
    from action import out_check, clean_screen, bag_open, maul_check, dead_die_before
    from realtime import soojib, moogi_, jaelyo_, boonhae_
    from get_item import get_items
    import pyautogui
    import pytesseract
    try:

        v_.potion_count = 0
        v_.potion_size = "none"


        jab_ready = False
        jab_ready_count = 0
        while jab_ready is False:
            jab_ready_count += 1
            if jab_ready_count > 3:
                jab_ready = True
            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\check\\maul_move_1.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(250, 960, 420, 1030, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("maul_move_1", imgs_)
                jab_ready = True
                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\potion\\janhwa_1.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(0, 90, 220, 350, cla, img, 0.9)
                if imgs_ is not None and imgs_ != False:
                    print("janhwa_1", imgs_)
                else:
                    result_maul = maul_check(cla)
                    if result_maul == True:
                        click_pos_2(230, 90, cla)
                    else:
                        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\check\\maul_move_1.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(250, 960, 420, 1030, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                            for i in range(10):
                                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\action\\not_have_item.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(370, 80, 480, 120, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:

                                    break
                                time.sleep(0.3)

            else:
                bag_open(cla)
                time.sleep(1)
                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\check\\maul_move_1.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(680, 100, 920, 900, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    click_pos_2(710, 935, cla)
                    time.sleep(0.5)
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                    time.sleep(0.5)
                    click_pos_2(290, 1000, cla)
                    time.sleep(0.5)
                    clean_screen(cla)

                time.sleep(1)
                click_pos_2(290, 1000, cla)


        time.sleep(2)
        jab_1_count = 0
        jab_1 = False
        while jab_1 is False:
            time.sleep(1)
            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\potion\\janhwa_1.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(0, 90, 220, 350, cla, img, 0.9)
            if imgs_ is not None and imgs_ != False:



                print("janhwa_1^_^", imgs_)
                jab_1 = True
                v_.potion_size = available_potion(cla)
                time.sleep(0.2)

                #
                get_items(cla)
                soojib(cla)
                moogi_(cla)
                boonhae_(cla)

                jaelyo_(cla)
                dead_die_before(cla)
                #
                time.sleep(0.2)

                click_pos_reg(imgs_.x, imgs_.y, cla)
            else:
                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\potion\\sangin.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(10, 75, 215, 330, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    drag_pos(110, 110, 110, 300, cla)
                    time.sleep(0.2)
                else:
                    full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\potion\\dunjun_out_.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(400, 510, 560, 560, cla, img, 0.83)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_2(555, 610, cla)
                        time.sleep(2)
                        click_pos_2(295, 1000, cla)
                        time.sleep(2)
                    else:
                        jab_1_count += 1
                        clean_screen(cla)

                        if jab_1_count > 5:
                            jab_1_count = 0

                            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\clean_screen\\exit_2.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(0, 0, 200, 600, cla, img, 0.83)
                            if imgs_ is not None and imgs_ != False:
                                print("maul potion exit_22", imgs_)
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                                time.sleep(1)

                            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\check\\maul_move_1.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(250, 960, 420, 1030, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                print("maul_move__1", imgs_)
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                                for i in range(10):
                                    full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\action\\not_have_item.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(370, 80, 480, 120, cla, img, 0.8)
                                    if imgs_ is not None and imgs_ != False:

                                        break
                                    time.sleep(0.3)

                                for i in range(10):
                                    full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\potion\\sangin.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(10, 75, 215, 330, cla, img, 0.8)
                                    if imgs_ is not None and imgs_ != False:
                                        print("sangin", imgs_)
                                        break
                                    time.sleep(0.5)

                            time.sleep(1)
                            # click_pos_2(230, 90, cla)
            time.sleep(1)


        # 잡화 상인 진입
        jab_2 = False
        jab_2_count = 0
        while jab_2 is False:
            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\potion\\janhwa_2.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(40, 900, 175, 1030, cla, img, 0.83)
            if imgs_ is not None and imgs_ != False:
                print("janhwa_2", imgs_)
                jab_1_count = 0
                time.sleep(0.2)
                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\potion\\small_potion.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(0, 90, 80, 1030, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("small_potion", imgs_)
                    jab_2 = True
                    # click_pos_reg(imgs_.x + 70, imgs_.y, cla)
            else:
                jab_1_count += 1
                jab_2_count += 1
                time.sleep(2)
                if jab_1_count > 5:
                    jab_1_count = 0
                    full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\potion\\janhwa_1.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(0, 90, 220, 350, cla, img, 0.9)
                    if imgs_ is not None and imgs_ != False:
                        print("janhwa_11", imgs_)
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                    else:
                        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\clean_screen\\exit_2.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(0, 0, 200, 600, cla, img, 0.83)
                        if imgs_ is not None and imgs_ != False:
                            print("maul potion exit_22222", imgs_)
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        time.sleep(1)
                if jab_2_count > 10:
                    jab_2_count = 0
                    full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\clean_screen\\exit_2.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(0, 0, 200, 600, cla, img, 0.83)
                    if imgs_ is not None and imgs_ != False:
                        print("maul potion exit_22", imgs_)
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        time.sleep(1)
                    click_pos_2(295, 995, cla)



        # 자동 구매하기
        ilgwal_count = 0
        ilgwal = True
        while ilgwal is True:
            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\potion\\ilgwal_title.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(400, 290, 550, 350, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:

                ilgwal = False

                for i in range(10):
                    full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\potion\\ilgwal_title.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(400, 290, 550, 350, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\potion\\potion_buy.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(500, 700, 600, 770, cla, img, 0.83)
                        if imgs_ is not None and imgs_ != False:
                            print("potion_buy", imgs_)
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                    else:
                        break
                    time.sleep(0.5)


            else:

                for i in range(10):
                    full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\potion\\ilgwal_title.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(400, 290, 550, 350, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        break
                    else:
                        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\potion\\not_ilgwal_msg.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(480, 70, 600, 120, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            ilgwal = False
                            break
                        else:
                            click_pos_2(245, 1015, cla)
                        time.sleep(0.5)


        # 취소 클릭
        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\potion\\cancle.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(360, 720, 470, 770, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            click_pos_reg(imgs_.x, imgs_.y, cla)
            time.sleep(0.5)

        # 해당되지 않는 물약 팔아버리기
        sell_ = False
        if v_.potion_size == "middle":
            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\potion\\small_potion_sell.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(680, 120, 910, 910, cla, img, 0.83)
            if imgs_ is not None and imgs_ != False:
                print("small_potion : ", imgs_)
                sell_ = True
        elif v_.potion_size == "small":
            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\potion\\middle_potion_sell.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(680, 120, 910, 910, cla, img, 0.83)
            if imgs_ is not None and imgs_ != False:
                print("middle_potion : ", imgs_)
                sell_ = True
        # 물약 팔기
        sell_count = 0
        while sell_ is True:
            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\potion\\potion_sell.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(490, 630, 600, 770, cla, img, 0.83)
            if imgs_ is not None and imgs_ != False:
                print("potion_buy", imgs_)

                sell_x = imgs_.x
                sell_y = imgs_.y

                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\potion\\max.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(520, 550, 610, 610, cla, img, 0.83)
                if imgs_ is not None and imgs_ != False:
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                    time.sleep(0.1)
                sell_ = False
                time.sleep(0.5)
                click_pos_reg(sell_x, sell_y, cla)
                time.sleep(0.2)
                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\potion\\max.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(340, 630, 480, 780, cla, img, 0.83)
                if imgs_ is not None and imgs_ != False:
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                    time.sleep(0.1)
                time.sleep(1.2)
            else:
                sell_count += 1
                if sell_count > 5:
                    sell_count = 0
                    sell_ = False

                if v_.potion_size == "middle":
                    full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\potion\\small_potion_sell.PNG"
                elif v_.potion_size == "small":
                    full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\potion\\middle_potion_sell.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(680, 120, 910, 910, cla, img, 0.83)
                if imgs_ is not None and imgs_ != False:
                    print("potion sell", imgs_)
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                else:
                    sell_ = False
            time.sleep(0.5)

        # 취소
        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\potion\\cancle.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(360, 720, 470, 770, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            click_pos_reg(imgs_.x, imgs_.y, cla)
            time.sleep(0.5)


        # 물약 사기
        jab_3 = False
        jab_1_count = 0
        while jab_3 is False:
            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\potion\\potion_buy.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(500, 700, 600, 770, cla, img, 0.83)
            if imgs_ is not None and imgs_ != False:
                print("potion_buy", imgs_)
                click_pos_2(560, 550, cla)
                jab_3 = True
                time.sleep(0.5)
                click_pos_reg(imgs_.x, imgs_.y, cla)
                time.sleep(0.2)
                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\potion\\cancle.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(360, 720, 470, 770, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                    time.sleep(0.5)
                time.sleep(0.5)
            else:
                jab_1_count += 1
                if jab_1_count > 5:
                    jab_1_count = 0
                    jab_3 = True

                if v_.potion_size == "middle":
                    full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\potion\\middle_potion.PNG"
                elif v_.potion_size == "small":
                    full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\potion\\small_potion.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(0, 90, 80, 1030, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("potion : ", v_.potion_size, imgs_)
                    click_pos_reg(imgs_.x + 70, imgs_.y, cla)
            time.sleep(0.5)


        jab_3 = False
        print("potion_jab_3")
        jab_3_count = 0
        while jab_3 is False:
            jab_3_count += 1
            if jab_3_count > 7:
                jab_3 = True
            out_result = out_check(cla)
            if out_result == True:
                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\check\\pvp_1.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(900, 275, 960, 365, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    click_pos_2(930, 60, cla)
                    time.sleep(0.1)
                jab_3 = True
            else:
                clean_screen(cla)

        time.sleep(0.5)
        quick3_potion(cla)

        # get_items(cla)
        # soojib(cla)
        # moogi_(cla)
        # boonhae_(cla)
        #
        # jaelyo_(cla)
        # dead_die_before(cla)

    except Exception as e:
        print(e)


def maul_potion_move_buy(cla):
    try:
        maul_potion(cla)

    except Exception as e:
        print(e)



def maul_potion_only(cla):
    try:
        maul_potion(cla)
    except Exception as e:
        print(e)


def juljun_maul_potion(cla):
    import cv2
    import numpy as np
    from function import click_pos_2, click_pos_reg, imgs_set_, drag_pos
    from potion import maul_potion_only
    from action import in_maul_check, out_check, clean_screen, juljun_check

    print("juljun_maul_potion")
    try:



        go_maul_ = False
        go_maul_count = 0
        while go_maul_ is False:
            go_maul_count += 1
            if go_maul_count > 10:
                go_maul_ = True
            result_maul = in_maul_check(cla)
            if result_maul == True:
                go_maul_ = True
                maul_potion_only(cla)


            else:
                result_juljun = juljun_check(cla)
                if result_juljun == True:
                    print("juljun_dungeon...")
                    drag_pos(360, 550, 600, 550, cla)
                else:
                    full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\check\\maul_move_1.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(250, 960, 420, 1030, cla, img, 0.7)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        for i in range(10):
                            result_maul = in_maul_check(cla)
                            if result_maul == True:
                                break
                            time.sleep(1)



            time.sleep(1)

    except Exception as e:
        print(e)

def available_potion(cla):
    import numpy as np
    import cv2
    from function import imgs_set_, click_pos_reg, click_pos_2
    from action import clean_screen, bag_open
    try:

        v_.potion_size = "none"

        clean_screen(cla)
        time.sleep(1)

        for i in range(10):
            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\potion\\exit.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(480, 760, 530, 810, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:

                # 체크 해제시 체크해주기

                for c in range(5):
                    full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\potion\\potion_checked.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(275, 800, 315, 840, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("potion_checked", imgs_)
                        break
                    else:
                        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\potion\\potion_not_checked.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(275, 800, 315, 840, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("potion_not_checked", imgs_)
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                    time.sleep(0.5)


                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\potion\\lv45.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(340, 900, 660, 930, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("lv45 x :small", imgs_)
                    v_.potion_size = "small"
                    click_pos_2(320, 900, cla)
                    break
                else:
                    full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\potion\\lv60.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(340, 900, 660, 930, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("lv60 x : middle", imgs_)
                        v_.potion_size = "middle"
                        click_pos_2(320, 900, cla)
                    else:
                        print("lv60 o : big", imgs_)
                        v_.potion_size = "big"
                        click_pos_2(370, 900, cla)
                    break
            else:
                click_pos_2(240, 1000, cla)
            time.sleep(0.5)

        for i in range(5):
            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\potion\\exit.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(480, 760, 530, 810, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                click_pos_reg(imgs_.x, imgs_.y, cla)
            else:
                break
            time.sleep(0.5)

        print("available_potion", v_.potion_size)

        quick3_potion(cla)

        return v_.potion_size
    except Exception as e:
        print(e)

def quick3_potion(cla):
    import numpy as np
    import cv2
    from function import imgs_set_, click_pos_reg, click_pos_2
    from action import clean_screen, bag_open
    try:

        print("quick3_potion", v_.potion_size)

        if v_.potion_size == "middle":
            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\potion\\quick3_potion_middle.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(370, 960, 420, 1020, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print(v_.potion_size, "존재한다.")
            else:
                print(v_.potion_size, "존재하지 않는다.")
                bag_open(cla)
                click_pos_2(935, 265, cla)
                time.sleep(0.5)
                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\potion\\middle_potion_in_bag2.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(670, 110, 900, 900, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                    time.sleep(0.2)
                    click_pos_2(710, 935, cla)
                    time.sleep(0.2)
                    click_pos_2(400, 1000, cla)
                    time.sleep(0.2)
                    click_pos_2(710, 935, cla)
                    time.sleep(0.2)
                    click_pos_2(935, 100, cla)
                    time.sleep(0.2)
                else:
                    click_pos_2(935, 100, cla)
                    time.sleep(0.2)


        elif v_.potion_size == "small":
            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\potion\\quick3_potion_small.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(370, 960, 420, 1020, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print(v_.potion_size, "존재한다.")
            else:
                print(v_.potion_size, "존재하지 않는다.")
                bag_open(cla)
                click_pos_2(935, 265, cla)
                time.sleep(0.5)
                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\potion\\potion_in_bag.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(670, 110, 900, 900, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                    time.sleep(0.2)
                    click_pos_2(710, 935, cla)
                    time.sleep(0.2)
                    click_pos_2(400, 1000, cla)
                    time.sleep(0.2)
                    click_pos_2(710, 935, cla)
                    time.sleep(0.2)
                    click_pos_2(935, 100, cla)
                    time.sleep(0.2)
                else:
                    click_pos_2(935, 100, cla)
                    time.sleep(0.2)

    except Exception as e:
        print(e)



###################################
def potion_check_ex(cla):
    import cv2
    import numpy as np
    from function import text_check_get, int_put_, imgs_set_, click_pos_2, in_number_check, change_number, \
        image_processing, get_region
    from action import dead_die_before, bag_open
    from realtime import soojib
    from schedule import myQuest_play_check
    import pyautogui
    import pytesseract

    try:

        if cla == "one":
            potion = v_.mypotion_1
        if cla == "two":
            potion = v_.mypotion_2
        if cla == "three":
            potion = v_.mypotion_3
        if cla == "four":
            potion = v_.mypotion_4

        is_potion = False

        potion_zero = False

        if v_.potion_size == "none":
            available_potion(cla)
            time.sleep(0.5)
        if v_.potion_size == "small":
            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\potion\\quick3_potion_small.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(370, 960, 420, 1020, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print(v_.potion_size, "존재한다.")
                is_potion = True

                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\potion\\quick3_potion_small_zero.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(370, 990, 420, 1020, cla, img, 0.88)
                if imgs_ is not None and imgs_ != False:
                    print(v_.potion_size, "zero 존재한다.")
                    potion_zero = True

        if v_.potion_size == "middle":
            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\potion\\quick3_potion_middle.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(370, 960, 420, 1020, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print(v_.potion_size, "존재한다.")
                is_potion = True

                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\potion\\quick3_potion_middle_zero.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(370, 990, 420, 1020, cla, img, 0.88)
                if imgs_ is not None and imgs_ != False:
                    print(v_.potion_size, "zero 존재한다.")
                    potion_zero = True
            for i in range(10):

                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\potion\\out_number\\" + str(i) + ".PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(390, 1004, 406, 1016, cla, img, 0.83)
                if imgs_ is not None and imgs_ != False:
                    print("숫자는? ", i)
                    break
                else:
                    full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\potion\\out_number\\out_middle_100.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(380, 985, 426, 1020, cla, img, 0.83)
                    if imgs_ is not None and imgs_ != False:
                        print("물량 100개 이하")
                        potion_zero = True
                        break
                    else:
                        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\potion\\out_number\\out_middle_100_2.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(380, 985, 426, 1020, cla, img, 0.83)
                        if imgs_ is not None and imgs_ != False:
                            print("물량 100개 이하...")
                            potion_zero = True
                            break

        if is_potion == True and potion_zero == False:
            # img = pyautogui.screenshot(region=(get_region(730, 1004, 759, 1016, cla)))
            # white_img = image_processing(img, (148, 148, 148), (255, 255, 255))
            # potion_ready = pytesseract.image_to_string(white_img, lang=None)
            potion_ready = text_check_get(730, 1004, 759, 1018, cla)
            print("전체4자리 potion_?", potion_ready)
            result_num_in = in_number_check(cla, potion_ready)
            if result_num_in == True:
                potion = change_number(potion_ready)
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
                        if v_.potion_count > 3:
                            v_.potion_count = 0
                            maul_potion_only(cla)
                    else:
                        v_.potion_count = 0
                else:
                    print("potion => 숫자 아님")
            else:
                # img = pyautogui.screenshot(region=(get_region(733, 1004, 758, 1016, cla)))
                # white_img = image_processing(img, (148, 148, 148), (255, 255, 255))
                # potion_ready = pytesseract.image_to_string(white_img, lang=None)
                potion_ready = text_check_get(733, 1004, 758, 1018, cla)
                print("전체4자리 potion_2?", potion_ready)
                result_num_in = in_number_check(cla, potion_ready)
                if result_num_in == True:
                    potion = change_number(potion_ready)
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
                                maul_potion_only(cla)
                        else:
                            v_.potion_count = 0
                    else:
                        print("potion => 숫자 아님")
                else:
                    # img = pyautogui.screenshot(region=(get_region(730, 1004, 752, 1016, cla)))
                    # white_img = image_processing(img, (148, 148, 148), (255, 255, 255))
                    # potion_ready = pytesseract.image_to_string(white_img, lang=None)
                    potion_ready = text_check_get(730, 1004, 752, 1018, cla)
                    print("앞3자리 potion_?", potion_ready)
                    result_num_in = in_number_check(cla, potion_ready)
                    if result_num_in == True:
                        potion = change_number(potion_ready)
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
                                if v_.potion_count > 3:
                                    v_.potion_count = 0
                                    maul_potion_only(cla)
                            else:
                                v_.potion_count = 0
                        else:
                            print("potion => 숫자 아님")
                    else:
                        # img = pyautogui.screenshot(region=(get_region(738, 1004, 759, 1016, cla)))
                        # white_img = image_processing(img, (148, 148, 148), (255, 255, 255))
                        # potion_ready = pytesseract.image_to_string(white_img, lang=None)
                        potion_ready = text_check_get(738, 1004, 759, 1018, cla)
                        print("뒷3자리 potion_??", potion_ready)
                        result_num_in = in_number_check(cla, potion_ready)
                        if result_num_in == True:
                            potion = change_number(potion_ready)
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

                                if potion < 100:
                                    v_.potion_count += 1
                                    if v_.potion_count > 3:
                                        v_.potion_count = 0
                                        maul_potion_only(cla)
                                else:
                                    v_.potion_count = 0

                            else:
                                print("potion => 숫자 아님")

        elif potion_zero == True:

            print("화면에 물약 존재하지 않는다", v_.potion_count)
            v_.potion_count += 1
            print("not have potoin?", v_.potion_count)
            if v_.potion_count > 2:
                v_.potion_count = 0
                maul_potion_only(cla)

        dead_die_before(cla)



        return potion
    except Exception as e:
        print(e)
############################################