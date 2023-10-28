import time

import requests
import json
# import os
import sys
sys.path.append('C:/my_games/nightcrow/data_nc/mymodule')

import variable as v_


def potion_check(cla):
    try:
        import cv2
        import numpy as np
        from function import text_check_get, int_put_, imgs_set_, click_pos_2, in_number_check, change_number, image_processing, get_region
        from action import dead_die_before, bag_open
        from realtime import soojib
        from schedule import myQuest_play_check
        import pyautogui
        import pytesseract

        if cla == "one":
            potion = v_.mypotion_1
        if cla == "two":
            potion = v_.mypotion_2
        if cla == "three":
            potion = v_.mypotion_3
        if cla == "four":
            potion = v_.mypotion_4

        is_potion = False


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
        if v_.potion_size == "none":
            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\potion\\quick3_potion_middle.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(370, 960, 420, 1020, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print(v_.potion_size, "존재한다.")
                is_potion = True

        if is_potion == True:
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

        else:

            potion_zero = False

            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\potion\\quick3_potion_small_zero.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(370, 990, 420, 1020, cla, img, 0.9)
            if imgs_ is not None and imgs_ != False:
                print(v_.potion_size, "zero 존재한다.")
                potion_zero = True
            else:
                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\potion\\quick3_potion_middle_zero.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(370, 990, 420, 1020, cla, img, 0.9)
                if imgs_ is not None and imgs_ != False:
                    print(v_.potion_size, "zero 존재한다.")
                    potion_zero = True

            if potion_zero == True:
                print("화면에 물약 존재하지 않는다", v_.potion_count)
                v_.potion_count += 1
                print("not have potoin?", v_.potion_count)
                if v_.potion_count > 2:
                    v_.potion_count = 0
                    maul_potion_only(cla)

                    # bag_open(cla)
                    # time.sleep(0.2)
                    #
                    # # 물약 찾기
                    # potion_have = False
                    # for i in range(10):
                    #     click_pos_2(935, 265, cla)
                    #     time.sleep(0.1)
                    #     full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\potion\\potion_in_bag.PNG"
                    #     img_array = np.fromfile(full_path, np.uint8)
                    #     img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    #     imgs_ = imgs_set_(670, 110, 900, 900, cla, img, 0.8)
                    #     if imgs_ is not None and imgs_ != False:
                    #         potion_have = True
                    #         print("가방에 물약 존재한다", imgs_)
                    #         break
                    #     full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\potion\\middle_potion_in_bag2.PNG"
                    #     img_array = np.fromfile(full_path, np.uint8)
                    #     img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    #     imgs_ = imgs_set_(670, 110, 900, 900, cla, img, 0.8)
                    #     if imgs_ is not None and imgs_ != False:
                    #         potion_have = True
                    #         print("가방에 물약 존재한다", imgs_)
                    #         break
                    #     time.sleep(0.1)
                    # if potion_have == False:
                    #     maul_potion(cla)
                    # else:
                    #     result_schedule = myQuest_play_check(v_.now_cla, "check")
                    #     print("물약 체크중 스케쥴 확인하기", result_schedule)
                    #     result_schedule_ = result_schedule[0][2]
                    #
                    #     dongool_check = "none"
                    #
                    #     if "_" in result_schedule_:
                    #         dungeon_ = result_schedule_.split("_")
                    #         if dungeon_[1] == "동굴":
                    #             dongool_check = "dongool"
                    #     if dongool_check == "dongool":
                    #         full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\check\\pvp_1.PNG"
                    #         img_array = np.fromfile(full_path, np.uint8)
                    #         img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    #         imgs_ = imgs_set_(900, 275, 960, 365, cla, img, 0.8)
                    #         if imgs_ is not None and imgs_ != False:
                    #             print("메뉴 닫자", imgs_)
                    #             click_pos_2(930, 60, cla)
                    #             time.sleep(0.1)
                    #         full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\clean_screen\\gabang_title.PNG"
                    #         img_array = np.fromfile(full_path, np.uint8)
                    #         img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    #         imgs_ = imgs_set_(820, 80, 910, 120, cla, img, 0.83)
                    #         if imgs_ is not None and imgs_ != False:
                    #             print("가방 닫자")
                    #             click_pos_2(935, 100, cla)
                    #             time.sleep(0.1)
                    #         full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\dungeon\juljun_mode.PNG"
                    #         img_array = np.fromfile(full_path, np.uint8)
                    #         img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    #         imgs_ = imgs_set_(400, 120, 600, 160, v_.now_cla, img, 0.8)
                    #         if imgs_ is None:
                    #             click_pos_2(25, 970, cla)
                    #             time.sleep(0.5)






        dead_die_before(cla)



        return potion
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
                                time.sleep(0.2)

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
                imgs_ = imgs_set_(0, 90, 80, 1030, cla, img, 0.83)
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





        # 랜덤이동서
        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\potion\\random_move.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(680, 110, 920, 1000, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            x_reg = imgs_.x
            if cla == "two":
                x_reg = x_reg - 960
            y_reg = imgs_.y

            img = pyautogui.screenshot(region=(get_region(x_reg - 2, y_reg + 13, x_reg + 28, y_reg + 33, cla)))
            white_img = image_processing(img, (148, 148, 148), (255, 255, 255))
            move_ = pytesseract.image_to_string(white_img, lang=None)
            print("how many random_move?", move_)

            move_bool = in_number_check(cla, move_)
            if move_bool == True:
                print("int_put_(random_move) 1?", int(int_put_(move_)))
                random_move = int(int_put_(move_))
                if random_move < 100:
                    jab_3 = False
                    click_count = 0
                    while jab_3 is False:
                        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\potion\\potion_buy.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(500, 700, 600, 770, cla, img, 0.83)
                        if imgs_ is not None and imgs_ != False:
                            print("potion_buy", imgs_)
                            for z in range(2):
                                click_pos_2(450, 580, cla)
                            jab_3 = True
                            time.sleep(0.5)
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                            time.sleep(0.2)
                            click_pos_2(410, 745, cla)
                            time.sleep(1.2)
                        else:
                            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\potion\\soongan.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(70, 100, 200, 700, cla, img, 0.83)
                            if imgs_ is not None and imgs_ != False:
                                click_count += 1
                                if click_count > 4:
                                    print("돈 없다. 강제노역이다~!")
                                    v_.force_sub_quest = True
                                    jab_3 = True
                                print("soongan????", imgs_)
                                click_pos_reg(imgs_.x, imgs_.y, cla)
            else:
                jab_3 = False
                click_count = 0
                while jab_3 is False:
                    full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\potion\\potion_buy.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(500, 700, 600, 770, cla, img, 0.83)
                    if imgs_ is not None and imgs_ != False:
                        print("potion_buy", imgs_)
                        #,click_pos_2(510, 580, cla)
                        for z in range(1):
                            click_pos_2(450, 580, cla)
                        jab_3 = True
                        time.sleep(0.5)
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        time.sleep(0.2)
                        click_pos_2(410, 745, cla)
                        time.sleep(1.2)
                    else:
                        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\potion\\soongan.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(70, 100, 200, 700, cla, img, 0.83)
                        if imgs_ is not None and imgs_ != False:
                            click_count += 1
                            if click_count > 4:
                                print("돈 없다. 강제노역이다~!")
                                v_.force_sub_quest = True
                                jab_3 = True
                            print("soongan????", imgs_)
                            click_pos_reg(imgs_.x, imgs_.y, cla)

        else:
            print("랜덤이동 안보여")
            jab_3 = False
            click_count = 0
            while jab_3 is False:
                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\potion\\potion_buy.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(500, 700, 600, 770, cla, img, 0.83)
                if imgs_ is not None and imgs_ != False:
                    print("potion_buy", imgs_)
                    # ,click_pos_2(510, 580, cla)
                    for z in range(1):
                        click_pos_2(450, 620, cla)
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
                    full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\potion\\soongan.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(70, 100, 200, 700, cla, img, 0.83)
                    if imgs_ is not None and imgs_ != False:
                        click_count += 1
                        if click_count > 4:
                            print("돈 없다. 강제노역이다~!")
                            v_.force_sub_quest = True
                            jab_3 = True
                        print("soongan????", imgs_)
                        click_pos_reg(imgs_.x, imgs_.y, cla)

        # 취소 있을 경우
        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\potion\\cancle.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(360, 720, 470, 770, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            click_pos_reg(imgs_.x, imgs_.y, cla)
            time.sleep(0.5)

        # 마을이동서
        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\potion\\maul_move_.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(680, 110, 920, 1000, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("already_in___2", imgs_)

            x_reg = imgs_.x
            if cla == "two":
                x_reg = x_reg - 960
            y_reg = imgs_.y

            img = pyautogui.screenshot(region=(get_region(x_reg - 2, y_reg + 13, x_reg + 28, y_reg + 33, cla)))
            white_img = image_processing(img, (148, 148, 148), (255, 255, 255))
            move_ = pytesseract.image_to_string(white_img, lang=None)
            print("how many maul_move_?", move_)

            move_bool = in_number_check(cla, move_)
            if move_bool == True:
                print("int_put_(maul_move_) 2?", int(int_put_(move_)))
                maul_move_ = int(int_put_(move_))
                if maul_move_ < 100:
                    jab_3 = False
                    click_count = 0
                    while jab_3 is False:
                        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\potion\\potion_buy.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(500, 700, 600, 770, cla, img, 0.83)
                        if imgs_ is not None and imgs_ != False:
                            print("potion_buy", imgs_)
                            for z in range(1):
                                click_pos_2(450, 580, cla)
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
                            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\potion\\gujum.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(70, 100, 200, 700, cla, img, 0.83)
                            if imgs_ is not None and imgs_ != False:
                                click_count += 1
                                if click_count > 4:
                                    print("돈 없다. 강제노역이당 흑흑")
                                    v_.force_sub_quest = True
                                    jab_3 = True
                                print("soongan", imgs_)
                                click_pos_reg(imgs_.x, imgs_.y, cla)
            else:
                jab_3 = False
                click_count = 0
                while jab_3 is False:
                    full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\potion\\potion_buy.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(500, 700, 600, 770, cla, img, 0.83)
                    if imgs_ is not None and imgs_ != False:
                        print("potion_buy", imgs_)
                        # click_pos_2(510, 580, cla)
                        for z in range(1):
                            click_pos_2(450, 580, cla)
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
                        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\potion\\gujum.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(70, 100, 200, 700, cla, img, 0.83)
                        if imgs_ is not None and imgs_ != False:
                            click_count += 1
                            if click_count > 4:
                                print("돈 없다. 강제노역이당 흑흑")
                                v_.force_sub_quest = True
                                jab_3 = True
                            print("soongan", imgs_)
                            click_pos_reg(imgs_.x, imgs_.y, cla)
        else:
            print("마을 이동 안보여")
            jab_3 = False
            click_count = 0
            while jab_3 is False:
                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\potion\\potion_buy.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(500, 700, 600, 770, cla, img, 0.83)
                if imgs_ is not None and imgs_ != False:
                    print("potion_buy", imgs_)
                    # click_pos_2(510, 580, cla)
                    for z in range(1):
                        click_pos_2(450, 620, cla)
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
                    full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\potion\\gujum.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(70, 100, 200, 700, cla, img, 0.83)
                    if imgs_ is not None and imgs_ != False:
                        click_count += 1
                        if click_count > 4:
                            print("돈 없다. 강제노역이당 흑흑")
                            v_.force_sub_quest = True
                            jab_3 = True
                        print("soongan", imgs_)
                        click_pos_reg(imgs_.x, imgs_.y, cla)

        # 취소 있을 경우
        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\potion\\cancle.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(360, 720, 470, 770, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            click_pos_reg(imgs_.x, imgs_.y, cla)
            time.sleep(0.5)

        # 돌격 포션
        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\potion\\dolgyuck_potion.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(680, 110, 920, 1000, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("dolgyuck_potion", imgs_)

            x_reg = imgs_.x
            if cla == "two":
                x_reg = x_reg - 960
            y_reg = imgs_.y

            img = pyautogui.screenshot(region=(get_region(x_reg - 1, y_reg + 13, x_reg + 29, y_reg + 33, cla)))
            white_img = image_processing(img, (148, 148, 148), (255, 255, 255))
            move_ = pytesseract.image_to_string(white_img, lang=None)
            print("how many dolgyuck_potion?", move_)

            move_bool = in_number_check(cla, move_)
            if move_bool == True:
                print("int_put_(dolgyuck_potion) 2?", int(int_put_(move_)))
                maul_move_ = int(int_put_(move_))
                if maul_move_ < 100:
                    jab_3 = False
                    click_count = 0
                    while jab_3 is False:
                        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\potion\\potion_buy.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(500, 700, 600, 770, cla, img, 0.83)
                        if imgs_ is not None and imgs_ != False:
                            print("potion_buy", imgs_)
                            for i in range(3):
                                click_pos_2(450, 620, cla)
                                time.sleep(0.1)

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
                            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\potion\\dolgyuck.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(70, 100, 200, 700, cla, img, 0.83)
                            if imgs_ is not None and imgs_ != False:
                                click_count += 1
                                if click_count > 4:
                                    print("돈 없다. 강제노역이당 흑흑")
                                    v_.force_sub_quest = True
                                    jab_3 = True
                                print("dolgyuck", imgs_)
                                click_pos_reg(imgs_.x, imgs_.y, cla)
            else:
                jab_3 = False
                click_count = 0
                while jab_3 is False:
                    full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\potion\\potion_buy.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(500, 700, 600, 770, cla, img, 0.83)
                    if imgs_ is not None and imgs_ != False:
                        print("potion_buy", imgs_)
                        # click_pos_2(510, 580, cla)
                        for i in range(2):
                            click_pos_2(450, 620, cla)
                            time.sleep(0.1)

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
                        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\potion\\dolgyuck.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(70, 100, 200, 700, cla, img, 0.83)
                        if imgs_ is not None and imgs_ != False:
                            click_count += 1
                            if click_count > 4:
                                print("돈 없다. 강제노역이당 흑흑")
                                v_.force_sub_quest = True
                                jab_3 = True
                            print("dolgyuck", imgs_)
                            click_pos_reg(imgs_.x, imgs_.y, cla)
        else:
            print("돌격포션 안 보여")
            jab_3 = False
            click_count = 0
            while jab_3 is False:
                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\potion\\potion_buy.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(500, 700, 600, 770, cla, img, 0.83)
                if imgs_ is not None and imgs_ != False:
                    print("potion_buy", imgs_)
                    # click_pos_2(510, 580, cla)
                    for i in range(7):
                        click_pos_2(450, 620, cla)
                        time.sleep(0.1)

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
                    full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\potion\\dolgyuck.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(70, 100, 200, 700, cla, img, 0.83)
                    if imgs_ is not None and imgs_ != False:
                        click_count += 1
                        if click_count > 4:
                            print("돈 없다. 강제노역이당 흑흑")
                            v_.force_sub_quest = True
                            jab_3 = True
                        print("dolgyuck", imgs_)
                        click_pos_reg(imgs_.x, imgs_.y, cla)

        # 취소 클릭
        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\potion\\cancle.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(360, 720, 470, 770, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            click_pos_reg(imgs_.x, imgs_.y, cla)
            time.sleep(0.5)

        # 필승 포션
        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\potion\\pilseong_potion.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(680, 110, 920, 1000, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("pilseong_potion", imgs_)

            x_reg = imgs_.x
            if cla == "two":
                x_reg = x_reg - 960
            y_reg = imgs_.y

            img = pyautogui.screenshot(region=(get_region(x_reg - 4, y_reg + 12, x_reg + 26, y_reg + 32, cla)))
            white_img = image_processing(img, (148, 148, 148), (255, 255, 255))
            move_ = pytesseract.image_to_string(white_img, lang=None)
            print("how many pilseong_potion?", move_)

            move_bool = in_number_check(cla, move_)
            if move_bool == True:
                print("int_put_(pilseong_potion) 2?", int(int_put_(move_)))
                maul_move_ = int(int_put_(move_))
                if maul_move_ < 100:
                    jab_3 = False
                    click_count = 0
                    while jab_3 is False:
                        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\potion\\potion_buy.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(500, 700, 600, 770, cla, img, 0.83)
                        if imgs_ is not None and imgs_ != False:
                            print("potion_buy", imgs_)
                            for i in range(3):
                                click_pos_2(450, 620, cla)
                                time.sleep(0.1)

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
                            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\potion\\pilseong.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(70, 100, 200, 700, cla, img, 0.83)
                            if imgs_ is not None and imgs_ != False:
                                click_count += 1
                                if click_count > 4:
                                    print("돈 없다. 강제노역이당 흑흑")
                                    v_.force_sub_quest = True
                                    jab_3 = True
                                print("pilseong", imgs_)
                                click_pos_reg(imgs_.x, imgs_.y, cla)
            else:
                jab_3 = False
                click_count = 0
                while jab_3 is False:
                    full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\potion\\potion_buy.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(500, 700, 600, 770, cla, img, 0.83)
                    if imgs_ is not None and imgs_ != False:
                        print("potion_buy", imgs_)
                        #click_pos_2(510, 580, cla)
                        for i in range(2):
                            click_pos_2(450, 620, cla)
                            time.sleep(0.1)

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
                        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\potion\\pilseong.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(70, 100, 200, 700, cla, img, 0.83)
                        if imgs_ is not None and imgs_ != False:
                            click_count += 1
                            if click_count > 4:
                                print("돈 없다. 강제노역이당 흑흑")
                                v_.force_sub_quest = True
                                jab_3 = True
                            print("pilseong", imgs_)
                            click_pos_reg(imgs_.x, imgs_.y, cla)
        else:
            print("필승포션 안보여")
            jab_3 = False
            click_count = 0
            while jab_3 is False:
                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\potion\\potion_buy.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(500, 700, 600, 770, cla, img, 0.83)
                if imgs_ is not None and imgs_ != False:
                    print("potion_buy", imgs_)
                    # click_pos_2(510, 580, cla)
                    for i in range(7):
                        click_pos_2(450, 620, cla)
                        time.sleep(0.1)

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
                    full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\potion\\pilseong.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(70, 100, 200, 700, cla, img, 0.83)
                    if imgs_ is not None and imgs_ != False:
                        click_count += 1
                        if click_count > 4:
                            print("돈 없다. 강제노역이당 흑흑")
                            v_.force_sub_quest = True
                            jab_3 = True
                        print("pilseong", imgs_)
                        click_pos_reg(imgs_.x, imgs_.y, cla)

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
                imgs_ = imgs_set_(0, 90, 80, 1030, cla, img, 0.83)
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


def maul_potion_only(cla):
    try:
        import cv2
        import os
        import numpy as np
        from function import text_check_get, int_put_, click_pos_2, imgs_set_, click_pos_reg, in_number_check, get_region, image_processing, drag_pos
        from action import out_check, clean_screen, bag_open, maul_check, dead_die_before
        from realtime import soojib, moogi_, jaelyo_, boonhae_
        from schedule import myQuest_play_add, myQuest_play_check
        from get_item import get_items
        import pyautogui
        import pytesseract

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

                # 여기에 나의 자동물약 확인하기
                v_.potion_size = available_potion(cla)
                time.sleep(0.2)

                #
                # get_items(cla)
                # soojib(cla)
                # moogi_(cla)
                # boonhae_(cla)
                #
                # jaelyo_(cla)
                # dead_die_before(cla)
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
                                time.sleep(0.2)
                                for i in range(10):
                                    full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\potion\\sangin.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(10, 75, 215, 330, cla, img, 0.8)
                                    if imgs_ is not None and imgs_ != False:
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
                # lv. 45 부터 사용 가능한 물약
                # full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\potion\\middle_potion.PNG"
                # img_array = np.fromfile(full_path, np.uint8)
                # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                # imgs_ = imgs_set_(0, 90, 80, 1030, cla, img, 0.83)
                # if imgs_ is not None and imgs_ != False:
                #     print("middle_potion", imgs_)
                #     jab_2 = True
                #     click_pos_reg(imgs_.x + 70, imgs_.y, cla)
                # else:
                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\potion\\small_potion.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(0, 90, 80, 1030, cla, img, 0.83)
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


        # # 캐리터 id 가져오기
        # result_schedule = myQuest_play_check(v_.now_cla, "check")
        # print("potion_result_schedule", result_schedule)
        # character_id = result_schedule[0][1]
        #
        # # 일일퀘스트 요구 레벨(나의 레벨)
        #
        # dir_path = "C:\\my_games\\nightcrow\\mysettings\\my_level"
        # if character_id == "1":
        #     id_file_path = dir_path + "\\one_character.txt"
        # if character_id == "2":
        #     id_file_path = dir_path + "\\two_character.txt"
        #
        # with open(id_file_path, "r", encoding='utf-8-sig') as file:
        #     read_level = file.read()
        #     read_level_ = int(read_level)
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
        print("물약팔기")
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

        print("포션 구매")
        jab_1_count = 0
        jab_3 = False
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
                click_pos_2(410, 745, cla)
                time.sleep(1.2)
            else:
                jab_1_count += 1
                print("jab_1_count", jab_1_count, v_.potion_size)
                if jab_1_count > 5:
                    jab_1_count = 0
                    jab_3 = True

                if v_.potion_size == "middle":
                    full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\potion\\middle_potion.PNG"
                elif v_.potion_size == "small":
                    full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\potion\\small_potion.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(0, 90, 80, 1030, cla, img, 0.83)
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
            imgs_ = imgs_set_(720, 760, 770, 810, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:

                # 체크 해제시 체크해주기

                for c in range(5):
                    full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\potion\\potion_checked.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(510, 800, 550, 840, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("potion_checked", imgs_)
                        break
                    else:
                        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\potion\\potion_not_checked.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(510, 800, 550, 840, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("potion_not_checked", imgs_)
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                    time.sleep(0.5)


                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\potion\\lv45.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(600, 900, 660, 930, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    v_.potion_size = "small"
                    click_pos_2(565, 900, cla)
                    break
                else:
                    full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\potion\\lv60.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(670, 900, 730, 930, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        v_.potion_size = "middle"
                        click_pos_2(635, 900, cla)
                    else:
                        v_.potion_size = "big"
                        click_pos_2(705, 900, cla)
                    break
            else:
                click_pos_2(735, 1000, cla)
            time.sleep(0.5)

        for i in range(5):
            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\potion\\exit.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(720, 760, 770, 810, cla, img, 0.8)
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



