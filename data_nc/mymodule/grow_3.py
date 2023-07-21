import sys
import time

import pyautogui

sys.path.append('C:/my_games/nightcrow/data_nc/mymodule')

import variable as v_

fly_ = 0
sub_quest = False

def sub_quest_grow(cla):
    try:
        global camera_, media_, talchool_, prison_, boonji_, force_quest, fly_, sub_quest

        from function import click_pos_2, imgs_set, imgs_set_, random_int, drag_pos, text_check_get, click_pos_reg
        from massenger import line_to_me
        from schedule import myQuest_play_add
        from potion import potion_check, maul_potion
        from action import go_quest_ing_, go_auto_ing_, clean_screen, dead_die, in_maul_check

        import pyautogui
        import random
        import numpy as np
        import cv2

        print("nightcrow sub quest")

        result_dead = dead_die(cla)
        print("죽었당!!!!!!!!!!!!!!!!!!!!?????????????", result_dead)
        if result_dead == True:
            myQuest_play_add(cla, "서브퀘스트")

        if sub_quest == False:

            quest_get(cla)
            clean_screen(cla)

        result_potion = potion_check(cla)
        print("내 물약 갯수? ", result_potion)

        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\clean_screen\\gabang_title.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(820, 80, 910, 120, cla, img, 0.83)
        if imgs_ is not None and imgs_ != False:
            click_pos_2(935, 100, cla)

        result_ = go_quest_ing_(cla)
        if result_ == False:

            result_auto = go_auto_ing_(cla)
            if result_auto == True:
                talgut_board_(cla)

            talgut_ing_(cla)

            result_maul = in_maul_check(cla)
            if result_maul == True:
                maul_potion(cla)

            quest_check(cla)

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




            # 아이템 장착
            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\grow\\grow_1\\fit_1.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(660, 760, 750, 830, cla, img, 0.7)
            if imgs_ is not None and imgs_ != False:
                print("fit_1", imgs_)
                click_pos_reg(imgs_.x - 50, imgs_.y + 10, cla)
                time.sleep(0.5)
                item_open(cla)

            # 확인 버튼
            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\clean_screen\\confirm_1.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(490, 620, 620, 660, cla, img, 0.83)
            if imgs_ is not None and imgs_ != False:
                print("confirm_1", imgs_)
                click_pos_reg(imgs_.x, imgs_.y, cla)




        else:
            print("진행중")
            quest_check(cla)

    except Exception as e:
        print(e)

def quest_get(cla):
    try:
        global sub_quest
        import numpy as np
        import cv2
        from action import menu_open, clean_screen
        from function import click_pos_2, click_pos_reg, imgs_set_
        from schedule import myQuest_play_add
        from jadong_crow import go_to_spot
        print("서브퀘스트 받기")
        sub_quest = True

        clear_sub_quest = False

        sub_count_1 = 0

        in_quest_1 = False
        in_quest_1_count = 0
        while in_quest_1 is False:

            in_quest_1_count += 1
            if in_quest_1_count > 7:
                in_quest_1 = True
            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\grow\\grow_3\\quest_.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(30, 30, 120, 80, cla, img, 0.83)
            if imgs_ is not None and imgs_ != False:
                print("quest_", imgs_)
                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\grow\\grow_3\\sub_ing_1.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(110, 970, 260, 1030, cla, img, 0.83)
                if imgs_ is not None and imgs_ != False:
                    time.sleep(0.5)

                    full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\quest\\sub_not_checked.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(510, 990, 540, 1020, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        time.sleep(0.5)


                    full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\check\\point.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(550, 140, 620, 970, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_reg(imgs_.x - 20, imgs_.y + 5, cla)
                        time.sleep(0.5)

                    full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\quest\\bosang_1.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(600, 900, 960, 1030, cla, img, 0.83)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        time.sleep(0.5)

                    full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\grow\\grow_3\\soolock_1.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(710, 970, 850, 1030, cla, img, 0.83)
                    if imgs_ is not None and imgs_ != False:
                        in_quest_1 = True
                        in_quest_2 = False
                        # 처음부터 없을 경우 생각하기
                        in_quest_2_count = 0
                        while in_quest_2 is False:
                            in_quest_2_count += 1
                            if in_quest_2_count > 20:
                                in_quest_2 = True

                            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\check\\point.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(550, 140, 620, 970, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_reg(imgs_.x - 20, imgs_.y + 5, cla)
                                time.sleep(0.5)

                            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\grow\\grow_3\\soolock_1.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(710, 970, 850, 1030, cla, img, 0.83)
                            if imgs_ is not None and imgs_ != False:
                                print("soolock_1", imgs_)
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                            else:
                                sub_count_1 += 1
                                if sub_count_1 > 10:
                                    in_quest_2 = True
                                    sub_count_1 = 0
                            time.sleep(0.3)
                        # 서브퀘가 있었을 경우
                        in_quest_3 = False
                        in_quest_3_count = 0
                        while in_quest_3 is False:

                            in_quest_3_count += 1
                            if in_quest_3_count > 7:
                                in_quest_3 = True
                            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\grow\\grow_3\\move_.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(780, 970, 910, 1030, cla, img, 0.83)
                            if imgs_ is not None and imgs_ != False:
                                print("move_", imgs_)
                                in_quest_3 = True
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                            else:
                                sub_count_1 += 1
                                if sub_count_1 > 10:
                                    in_quest_3 = True
                                    sub_count_1 = 0
                            time.sleep(0.3)
                        # 서브퀘가 있었을 경우
                        in_quest_4 = False
                        in_quest_4_count = 0
                        while in_quest_4 is False:

                            in_quest_4_count += 1
                            if in_quest_4_count > 7:
                                in_quest_4 = True
                            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\grow\\grow_3\\confirm_1.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(480, 620, 620, 660, cla, img, 0.83)
                            if imgs_ is not None and imgs_ != False:
                                print("confirm_1", imgs_)
                                in_quest_4 = True
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                            else:
                                sub_count_1 += 1
                                if sub_count_1 > 10:
                                    in_quest_4 = True
                                    sub_count_1 = 0
                            time.sleep(0.3)
                    else:
                        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\grow\\grow_3\\move_.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(780, 970, 910, 1030, cla, img, 0.83)
                        if imgs_ is not None and imgs_ != False:
                            print("move_", imgs_)

                            # 서브퀘가 있었을 경우
                            in_quest_3 = False
                            in_quest_3_count = 0
                            while in_quest_3 is False:

                                in_quest_3_count += 1
                                if in_quest_3_count > 7:
                                    in_quest_3 = True
                                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\grow\\grow_3\\move_.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(780, 970, 910, 1030, cla, img, 0.83)
                                if imgs_ is not None and imgs_ != False:
                                    print("move_", imgs_)
                                    in_quest_3 = True
                                    in_quest_1 = True
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                                else:
                                    sub_count_1 += 1
                                    if sub_count_1 > 10:
                                        in_quest_3 = True
                                        sub_count_1 = 0
                                time.sleep(0.3)
                            # 서브퀘가 있었을 경우
                            in_quest_4 = False
                            in_quest_4_count = 0
                            while in_quest_4 is False:

                                in_quest_4_count += 1
                                if in_quest_4_count > 7:
                                    in_quest_4 = True
                                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\grow\\grow_3\\confirm_1.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(480, 620, 620, 660, cla, img, 0.83)
                                if imgs_ is not None and imgs_ != False:
                                    print("confirm_1", imgs_)

                                    in_quest_4 = True
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                                else:
                                    sub_count_1 += 1
                                    if sub_count_1 > 10:
                                        in_quest_4 = True
                                        sub_count_1 = 0
                                time.sleep(0.3)
                        else:
                            #
                            in_quest_1 = True
                            sub_quest = False
                            print("서브퀘스트 끝")
                            clear_sub_quest = True
                            #
                    # 퀘스트 끝 체크
                    full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\quest\\sub_clear_1.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(250, 450, 350, 580, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        clear_sub_quest = True
                        in_quest_1 = True

                    full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\quest\\sub_clear_2.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(300, 580, 400, 620, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        clear_sub_quest = True
                        in_quest_1 = True

                else:
                    click_pos_2(220, 110, cla)
            else:
                menu_open(cla)
                click_pos_2(745, 195, cla)

            time.sleep(0.3)

        if clear_sub_quest == True:
            myQuest_play_add(cla, "서브퀘스트")
            clean_screen(cla)
        else:
            go_to_spot(cla, "sub")

        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\clean_screen\\quest_title.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(80, 40, 160, 80, cla, img, 0.83)
        if imgs_ is not None and imgs_ != False:
            print("quest_title", imgs_)
            click_pos_2(930, 60, cla)

    except Exception as e:
        print(e)

def quest_check(cla):
    try:

        from function import click_pos_2, imgs_set, imgs_set_, random_int, drag_pos, text_check_get, click_pos_reg
        from action import go_quest_ing_
        from get_item import guild_jilyung
        import numpy as np
        import cv2

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
                    guild_jilyung(cla, "jadong")
                    jilyung_is_ = True
                else:
                    full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\guild\\guild_jilyung.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(660, 90, 730, 300, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\dungeon\\chogwa.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(390, 70, 470, 120, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("초과가 보여")
                            jilyung_is_ = True
                            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\quest\\quest_click.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(680, 170, 720, 220, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                v_.sub_quest_count = 0
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                time.sleep(0.4)

        # 퀘스트 수락
        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\grow\\grow_1\\quest_soolock_2.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(800, 90, 960, 900, cla, img, 0.83)
        if imgs_ is not None and imgs_ != False:
            print("quest_soolock_2", imgs_)
            click_pos_reg(imgs_.x, imgs_.y, cla)
            result_ = go_quest_ing_(cla)
            if result_ == False:
                talgut_board_(cla)



        # 퀘스트 완료
        is_daily = False
        is_daily_count = 0
        while is_daily is False:
            is_daily_count += 1
            if is_daily_count > 5:
                is_daily = True
            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\grow\\grow_1\\quest_complete_2.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(800, 90, 960, 900, cla, img, 0.83)
            if imgs_ is not None and imgs_ != False:
                print("quest_complete_2", imgs_)
                click_pos_reg(imgs_.x, imgs_.y, cla)

            else:
                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\grow\\grow_1\\quest_complete_1.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(800, 90, 960, 900, cla, img, 0.83)
                if imgs_ is not None and imgs_ != False:
                    print("quest_complete_1", imgs_)
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                else:
                    is_daily = True
                    result_ = go_quest_ing_(cla)
                    if result_ == False:
                        talgut_board_(cla)

        # 붕붕 날아다니자
        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\jadong\\flying_.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(820, 880, 910, 970, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:

            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\grow\\grow_3\\gyunway_bawigil.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(40, 75, 160, 110, cla, img, 0.75)
            if imgs_ is not None and imgs_ != False:
                time.sleep(0.1)
                pyautogui.keyDown('a')
                time.sleep(0.1)
                pyautogui.keyUp('a')
                time.sleep(0.1)
                print("pyautogui.press('a')")

            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\jadong\\fly_.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(770, 970, 960, 1030, cla, img, 0.7)
            if imgs_ is not None and imgs_ != False:
                click_pos_reg(imgs_.x, imgs_.y, cla)
                print("플라잉 부스터!!!")




    except Exception as e:
        print(e)


def talgut_ing_(cla):
    try:

        from function import click_pos_2, imgs_set, imgs_set_, random_int, drag_pos, text_check_get, click_pos_reg
        import numpy as np
        import cv2

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
            print("talgut_ing_", imgs_)
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

def talgut_board_(cla):
    try:
        from function import click_pos_2, imgs_set, imgs_set_, random_int, drag_pos, text_check_get, click_pos_reg
        from action import menu_open, clean_screen, go_quest_ing_, go_auto_ing_
        from jadong_crow import go_to_spot
        from schedule import myQuest_play_add
        from get_item import guild_jilyung
        import numpy as np
        import cv2
        import pyautogui

        # 탈것
        go_ = False
        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\quest\\quest_click.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(680, 130, 720, 220, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            go_ = True
            v_.sub_quest_count = 0
            click_pos_reg(imgs_.x, imgs_.y, cla)
        else:
            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\grow\\grow_1\\talgut_1.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(680, 130, 720, 170, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                go_ = True
                v_.sub_quest_count = 0
                click_pos_reg(imgs_.x, imgs_.y, cla)
            else:
                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\grow\\grow_1\\talgut_2.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(680, 130, 720, 170, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    go_ = True
                    v_.sub_quest_count = 0
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                else:
                    full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\grow\\grow_1\\talgut_3.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(680, 130, 720, 170, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        go_ = True
                        v_.sub_quest_count = 0
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                    else:
                        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\quest\\talgut_4.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(680, 130, 720, 170, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            go_ = True
                            v_.sub_quest_count = 0
                            click_pos_reg(imgs_.x, imgs_.y, cla)
        sojin_ = False
        jilyung = False
        for i in range(10):
            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\quest\\sub_sojin_1.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(400, 70, 550, 120, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("sub_sojin_1", imgs_)
                sojin_ = True
                break
            else:
                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\quest\\sub_sojin_1.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(400, 70, 550, 120, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("sub_sojin_1", imgs_)
                    sojin_ = True
                    break
            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\quest\\guild_jilyung_1.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(350, 70, 550, 120, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("guild_jilyung_1", imgs_)
                jilyung = True
                break
            else:
                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\quest\\guild_jilyung_2.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(350, 70, 550, 120, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("guild_jilyung_2", imgs_)
                    jilyung = True
                    break
        if jilyung == True:
            print("지령 관련 퀘스트 여긴 서브퀘스트")
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
                        guild_jilyung(cla, "jadong")
                        jilyung_is_ = True
                    else:
                        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\guild\\guild_jilyung.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(660, 90, 730, 300, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\dungeon\\chogwa.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(390, 70, 470, 120, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                print("초과가 보여")
                                jilyung_is_ = True
                                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\quest\\quest_click.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(680, 170, 720, 220, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    v_.sub_quest_count = 0
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                    time.sleep(0.4)
            # myQuest_play_add(cla, "서브퀘스트")
        if sojin_ == True:
            in_quest_title = False
            in_quest_title_count = 0
            while in_quest_title is False:
                in_quest_title_count += 1
                if in_quest_title_count > 5:
                    in_quest_title = True
                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\quest\\quest_title.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(30, 30, 120, 80, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\quest\\in_quest_dungeon.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(0, 130, 160, 900, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        give_up_ready = False
                        give_up_ready_count = 0
                        while give_up_ready is False:
                            give_up_ready_count += 1
                            if give_up_ready_count > 10:
                                give_up_ready = True

                            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\quest\\in_quest_dungeon.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(0, 130, 160, 900, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                print("in_quest_dungeon", imgs_)
                                click_pos_reg(imgs_.x, imgs_.y + 30, cla)

                                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\quest\\give_up_1.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(560, 150, 630, 330, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                                    full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\quest\\give_up_2.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(850, 120, 950, 200, cla, img, 0.8)
                                    if imgs_ is not None and imgs_ != False:
                                        click_pos_reg(imgs_.x, imgs_.y, cla)
                                else:
                                    give_up_ready = True
                                    in_quest_title = True
                            time.sleep(1)
                            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\quest\\y_1.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(500, 580, 600, 630, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                    else:
                        click_pos_2(345, 105, cla)
                else:
                    menu_open(cla)
                    click_pos_2(745, 190, cla)
            time.sleep(0.5)
            clean_screen(cla)
            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\quest\\quest_title.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(30, 30, 120, 80, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                click_pos_2(930, 60, cla)


        # 추후 고렙때 가능

        # if cla == 'one':
        #     plus = 0
        # if cla == 'two':
        #     plus = 960
        #
        #
        # for z in range(3):
        #     last_x = 0
        #     last_y = 0
        #     if z != 0:
        #         pic_ = "talgut_" + str(z)
        #         full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\grow\\grow_1\\" + pic_ + ".PNG"
        #         img_array = np.fromfile(full_path, np.uint8)
        #         img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        #         for i in pyautogui.locateAllOnScreen(img, region=(680 + plus, 90, 40, 170), confidence=0.7):
        #             last_x = i.left
        #             last_y = i.top
        #             print("last_x", last_x)
        #             print("last_y", last_y)
        #         if last_x != 0:
        #             go_ = True
        #             click_pos_reg(last_x, last_y, cla)
        #             break

        #

        if go_ == False:

            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\check\\quest_check.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(895, 95, 925, 120, cla, img, 0.75)
            if imgs_ is not None and imgs_ != False:
                print("quest_check", imgs_)
                click_pos_2(700, 110, cla)
            else:
                click_pos_2(930, 110, cla)
                time.sleep(0.2)
                click_pos_2(700, 110, cla)

            print("v_.sub_quest_count", v_.sub_quest_count)
            v_.sub_quest_count += 1
            if v_.sub_quest_count > 1:
                result_ = go_quest_ing_(cla)
                if result_ == False:

                    result_auto = go_auto_ing_(cla)
                    if result_auto == True:
                        v_.sub_quest_count = 0
                        quest_get(cla)
            else:
                click_pos_2(700, 155, cla)
        # 확인 버튼
        time.sleep(1)
        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\clean_screen\\confirm_1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(490, 620, 620, 660, cla, img, 0.83)
        if imgs_ is not None and imgs_ != False:
            print("confirm_1", imgs_)
            click_pos_reg(imgs_.x, imgs_.y, cla)

        time.sleep(0.5)

        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\grow\\grow_1\\no_talgut_1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(365, 85, 450, 115, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("no_talgut_1", imgs_)
            click_pos_2(880, 110, cla)

        #비행장?
        go_to_spot(cla, "sub")

        return go_
    except Exception as e:
        print(e)

def talgut_board_check(cla):
    try:
        from function import click_pos_2, imgs_set, imgs_set_, random_int, drag_pos, text_check_get, click_pos_reg
        from action import menu_open, clean_screen, go_quest_ing_, go_auto_ing_
        from get_item import guild_jilyung
        import numpy as np
        import cv2
        import pyautogui

        go_ = False

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
                    guild_jilyung(cla, "jadong")
                    jilyung_is_ = True
                else:
                    full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\guild\\guild_jilyung.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(660, 90, 730, 300, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\dungeon\\chogwa.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(390, 70, 470, 120, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("초과가 보여")
                            jilyung_is_ = True
                            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\quest\\quest_click.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(680, 170, 720, 220, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                v_.sub_quest_count = 0
                                go_ = True
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                time.sleep(0.4)

        # 탈것
        if go_ == False:
            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\quest\\quest_click.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(680, 120, 720, 220, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                go_ = True
                v_.sub_quest_count = 0
                click_pos_reg(imgs_.x, imgs_.y, cla)
            # else:
            #     full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\grow\\grow_1\\talgut_1.PNG"
            #     img_array = np.fromfile(full_path, np.uint8)
            #     img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            #     imgs_ = imgs_set_(680, 120, 720, 170, cla, img, 0.8)
            #     if imgs_ is not None and imgs_ != False:
            #         go_ = True
            #         v_.sub_quest_count = 0
            #         click_pos_reg(imgs_.x, imgs_.y, cla)
            #     else:
            #         full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\grow\\grow_1\\talgut_2.PNG"
            #         img_array = np.fromfile(full_path, np.uint8)
            #         img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            #         imgs_ = imgs_set_(680, 120, 720, 170, cla, img, 0.8)
            #         if imgs_ is not None and imgs_ != False:
            #             go_ = True
            #             v_.sub_quest_count = 0
            #             click_pos_reg(imgs_.x, imgs_.y, cla)
            #         else:
            #             full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\grow\\grow_1\\talgut_3.PNG"
            #             img_array = np.fromfile(full_path, np.uint8)
            #             img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            #             imgs_ = imgs_set_(680, 120, 720, 170, cla, img, 0.8)
            #             if imgs_ is not None and imgs_ != False:
            #                 go_ = True
            #                 v_.sub_quest_count = 0
            #                 click_pos_reg(imgs_.x, imgs_.y, cla)
            #             else:
            #                 full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\quest\\talgut_4.PNG"
            #                 img_array = np.fromfile(full_path, np.uint8)
            #                 img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            #                 imgs_ = imgs_set_(680, 120, 720, 170, cla, img, 0.8)
            #                 if imgs_ is not None and imgs_ != False:
            #                     go_ = True
            #                     v_.sub_quest_count = 0
            #                     click_pos_reg(imgs_.x, imgs_.y, cla)


        return go_
    except Exception as e:
        print(e)

def item_open(cla):
    try:

        from function import click_pos_2, imgs_set, imgs_set_, random_int, drag_pos, text_check_get, click_pos_reg
        from action import bag_open, clean_screen, menu_open

        import numpy as np
        import cv2

        result_bag = bag_open(cla)
        if result_bag == True:

            # 스킬북
            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\item_1\\skillbook_1.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(680, 90, 910, 900, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                click_pos_reg(imgs_.x, imgs_.y, cla)
                time.sleep(0.1)
                click_pos_reg(imgs_.x, imgs_.y, cla)

            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\item_1\\skillbook_2.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(680, 90, 910, 900, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                click_pos_reg(imgs_.x, imgs_.y, cla)
                time.sleep(0.1)
                click_pos_reg(imgs_.x, imgs_.y, cla)

            # 탈것
            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\item_1\\talgut_1.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(680, 90, 720, 140, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                click_pos_reg(imgs_.x, imgs_.y, cla)
                time.sleep(0.1)
                click_pos_reg(imgs_.x, imgs_.y, cla)

                tal_1 = False
                tal_1_count = 0
                while tal_1 is False:

                    tal_1_count += 1
                    if tal_1_count > 7:
                        tal_1 = True
                    full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\item_1\\exit_1.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(400, 980, 570, 1030, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        tal_1 = True
                    else:
                        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\item_1\\open_1.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(400, 980, 570, 1030, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                    time.sleep(0.3)
                tal_2_count = 0
                while tal_2 is False:

                    tal_2_count += 1
                    if tal_2_count > 7:
                        tal_2 = True
                    menu_result = menu_open(cla)
                    if menu_result == True:
                        click_pos_2(795, 260, cla)
                        tal_2 = True
                        time.sleep(1)
                tal_3 = False
                tal_3_count = 0
                while tal_3 is False:

                    tal_3_count += 1
                    if tal_3_count > 7:
                        tal_3 = True
                    full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\clean_screen\\talgut.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(50, 40, 90, 75, cla, img, 0.83)
                    if imgs_ is not None and imgs_ != False:
                        talgut_ing_(cla)
                        tal_3 = True

        #튜토육성 체크 후 클린스크린
        clean_screen(cla)

    except Exception as e:
        print(e)
