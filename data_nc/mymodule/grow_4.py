import sys
import time

import pyautogui

sys.path.append('C:/my_games/nightcrow/data_nc/mymodule')

import variable as v_

daily_quest = False

def select_daily_quest_grow(cla, character_id, step):
    try:
        global daily_quest

        from function import click_pos_2, imgs_set, imgs_set_, random_int, drag_pos, text_check_get, click_pos_reg
        from massenger import line_to_me
        from schedule import myQuest_play_add
        from potion import potion_check, maul_potion
        from action import go_quest_ing_, go_auto_ing_, clean_screen, dead_die, in_maul_check

        import pyautogui
        import random
        import numpy as np
        import cv2

        print("nightcrow daily quest")
        print("v_.sub_quest_count(10이면 일일퀘스트 끝) =>", v_.sub_quest_count)

        result_dead = dead_die(cla)
        print("죽었당!!!!!!!!!!!!!!!!!!!!?????????????", result_dead)
        if result_dead == True:
            add_data = "일일퀘스트_" + str(step)
            myQuest_play_add(cla, add_data)

        # result_check = talgut_board_check
        # if result_check == True:
        # dfasdfasfasf
        if daily_quest == False:

            quest_get(cla, character_id, step)
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
                quest_check(cla, step, "start")
            else:
                clean_screen(cla)

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
            quest_check(cla, step, "ing")

    except Exception as e:
        print(e)

def quest_get(cla, character_id, step):
    global daily_quest
    import numpy as np
    import cv2
    from action import menu_open
    from function import click_pos_2, click_pos_reg, imgs_set_, text_check_get, int_put_, mouse_move_cpp
    try:

        print("일일퀘스트 받기")
        daily_quest = True

        # clear_sub_quest = False


        if cla == 'one':
            plus = 0
        if cla == 'two':
            plus = 960
        if cla == 'three':
            plus = 960 + 960
        if cla == 'four':
            plus = 960 + 960 + 960

        step = int(step)


        # 요구레벨 불러오기
        dir_path = "C:\\my_games\\nightcrow\\mysettings\\my_level"

        if character_id == "1":
            file_path = dir_path + "\\one_character.txt"
        if character_id == "2":
            file_path = dir_path + "\\two_character.txt"


        with open(file_path, "r", encoding='utf-8-sig') as file:
            read_level = file.read()

        in_quest_1 = False
        in_quest_1_count = 0
        while in_quest_1 is False:
            in_quest_1_count += 1
            if in_quest_1_count > 10:
                in_quest_1 = True
            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\grow\\grow_3\\quest_.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(30, 30, 120, 80, cla, img, 0.83)
            if imgs_ is not None and imgs_ != False:
                print("quest_", imgs_)

                daily_click = False
                daily_click_count = 0
                while daily_click is False:
                    daily_click_count += 1
                    if daily_click_count > 10:
                        daily_click = True
                        in_quest_1 = True
                    full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\quest\\daily_check_1.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(160, 990, 220, 1015, cla, img, 0.83)
                    if imgs_ is not None and imgs_ != False:
                        print("daily_check_1", imgs_)

                        for i in range(10):
                            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\quest\\continue_on.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(525, 980, 600, 1020, cla, img, 0.83)
                            if imgs_ is not None and imgs_ != False:
                                print("continue_on", imgs_)
                                break
                            else:
                                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\quest\\continue_off.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(525, 980, 600, 1020, cla, img, 0.83)
                                if imgs_ is not None and imgs_ != False:
                                    print("continue_off", imgs_)
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                                    time.sleep(0.1)
                                    mouse_move_cpp(390, 520, cla)
                            time.sleep(0.5)




                            # 바스티움
                        for i in range(10):
                            if step == 1:
                                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\quest\\daily_step_1_click.PNG"
                            if step == 2:
                                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\quest\\daily_step_2_click.PNG"
                            if step == 3:
                                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\quest\\daily_step_3_click.PNG"
                            if step == 4:
                                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\quest\\daily_step_4_click.PNG"

                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(230, 170, 305, 200, cla, img, 0.83)
                            if imgs_ is not None and imgs_ != False:
                                break
                            else:
                                if step == 1:
                                    click_pos_2(60, 190, cla)
                                if step == 2:
                                    click_pos_2(60, 225, cla)
                                if step == 3:
                                    click_pos_2(60, 260, cla)
                                if step == 4:
                                    click_pos_2(60, 295, cla)
                            time.sleep(0.5)

                        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\quest\\daily_check_2.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        for i in pyautogui.locateAllOnScreen(img, region=(160 + plus, 230, 60, 750), confidence=0.8):
                            last_x = i.left
                            if cla == "two":
                                last_x = last_x - 960
                            if cla == "three":
                                last_x = last_x - 960 - 960
                            if cla == "four":
                                last_x = last_x - 960 - 960 - 960
                            last_y = i.top

                            print("check point!!!!!!!!!!!!!", last_x, last_y)



                            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\quest\\daily_check_2.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(last_x - 7, last_y - 7, last_x + 43, last_y + 18, cla, img, 0.83)
                            if imgs_ is not None and imgs_ != False:
                                level_check = text_check_get(last_x - 7, last_y - 7, last_x + 43, last_y + 18, cla)
                                result_lev = int_put_(level_check)
                                num_bool = result_lev.isdigit()
                                if num_bool == True:
                                    if int(result_lev) < int(read_level) and int(result_lev) != 4 and int(result_lev) != 5 and int(result_lev) != 6 and int(result_lev) != 7:
                                        print("result_lev", result_lev)

                                        click_pos_2(last_x + 200, last_y, cla)
                                        time.sleep(0.1)

                                        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\quest\\soolock.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(640, 970, 770, 1020, cla, img, 0.83)
                                        if imgs_ is not None and imgs_ != False:
                                            click_pos_reg(imgs_.x, imgs_.y, cla)
                                    else:
                                        print("give_up_2 : result_lev", result_lev)
                                        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\quest\\give_up_2.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(850, 120, 950, 200, cla, img, 0.8)
                                        if imgs_ is not None and imgs_ != False:
                                            click_pos_2(last_x + 200, last_y, cla)
                                            time.sleep(0.1)

                                        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\quest\\give_up_2.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(850, 120, 950, 200, cla, img, 0.8)
                                        if imgs_ is not None and imgs_ != False:
                                            click_pos_reg(imgs_.x, imgs_.y, cla)
                                            time.sleep(0.3)
                                            for z in range(3):
                                                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\quest\\y_1.PNG"
                                                img_array = np.fromfile(full_path, np.uint8)
                                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                                imgs_ = imgs_set_(480, 580, 630, 630, cla, img, 0.8)
                                                if imgs_ is not None and imgs_ != False:
                                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                                                    break
                                                time.sleep(0.3)
                                    time.sleep(0.2)
                                else:
                                    print("요구레벨이 숫자 아니라고 읽음", result_lev)


                        # 일일퀘스트 받기 끝
                        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\quest\\y_1.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(480, 580, 630, 630, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_reg(imgs_.x, imgs_.y, cla)

                        in_quest_2 = False
                        in_quest_2_count = 0
                        while in_quest_2 is False:
                            in_quest_2_count += 1
                            if in_quest_2_count > 10:
                                in_quest_2 = True
                                daily_click = True
                            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\grow\\grow_3\\quest_.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(30, 30, 120, 80, cla, img, 0.83)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_2(930, 60, cla)
                            else:
                                in_quest_1 = True
                                in_quest_2 = True
                                daily_click = True
                            time.sleep(0.5)
                    else:
                        click_pos_2(480, 110, cla)

                        for i in range(10):
                            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\quest\\daily_check_1.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(160, 990, 220, 1015, cla, img, 0.83)
                            if imgs_ is not None and imgs_ != False:
                                break
                            time.sleep(0.2)

                    time.sleep(0.5)

            else:
                menu_open(cla)
                click_pos_2(745, 195, cla)

                for i in range(10):
                    full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\grow\\grow_3\\quest_.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(30, 30, 120, 80, cla, img, 0.83)
                    if imgs_ is not None and imgs_ != False:
                        break
                    time.sleep(0.2)

            time.sleep(0.3)


    except Exception as e:
        print(e)

def quest_check(cla, step, now):
    from function import click_pos_2, imgs_set_, click_pos_reg, mouse_move_cpp
    from action import dead_die, menu_open, go_quest_ing_
    from schedule import myQuest_play_add
    import numpy as np
    import cv2
    try:

        step = int(step)

        in_quest_1 = False
        in_quest_1_count = 0
        while in_quest_1 is False:
            in_quest_1_count += 1
            if in_quest_1_count > 10:
                in_quest_1 = True
            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\grow\\grow_3\\quest_.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(30, 30, 120, 80, cla, img, 0.83)
            if imgs_ is not None and imgs_ != False:
                print("quest_", imgs_)

                in_quest_1 = True

                daily_click = False
                daily_click_count = 0
                while daily_click is False:
                    daily_click_count += 1
                    if daily_click_count > 10:
                        daily_click = True

                    full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\quest\\daily_check_1.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(140, 970, 250, 1040, cla, img, 0.83)
                    if imgs_ is not None and imgs_ != False:
                        print("daily_check_1", imgs_)

                        for i in range(10):
                            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\quest\\continue_on.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(525, 980, 600, 1020, cla, img, 0.83)
                            if imgs_ is not None and imgs_ != False:
                                print("continue_on", imgs_)
                                break
                            else:
                                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\quest\\continue_off.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(525, 980, 600, 1020, cla, img, 0.83)
                                if imgs_ is not None and imgs_ != False:
                                    print("continue_off", imgs_)
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                                    time.sleep(0.1)
                                    mouse_move_cpp(390, 520, cla)
                            time.sleep(0.5)



                        if step == 1:
                            # 바스티움
                            for i in range(10):
                                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\quest\\daily_step_1_click.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(230, 170, 305, 200, cla, img, 0.83)
                                if imgs_ is not None and imgs_ != False:
                                    break
                                else:
                                    click_pos_2(60, 185, cla)
                                time.sleep(0.5)



                        if step == 2:
                            # 첼라노
                            for i in range(10):
                                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\quest\\daily_step_2_click.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(230, 170, 305, 200, cla, img, 0.83)
                                if imgs_ is not None and imgs_ != False:
                                    break
                                else:
                                    click_pos_2(60, 225, cla)
                                time.sleep(0.5)


                        if step == 3:
                            # 아빌리우스
                            for i in range(10):
                                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\quest\\daily_step_3_click.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(230, 170, 305, 200, cla, img, 0.83)
                                if imgs_ is not None and imgs_ != False:
                                    break
                                else:
                                    click_pos_2(60, 260, cla)
                                time.sleep(0.5)


                        if step == 4:
                            # 트로네텔
                            for i in range(10):
                                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\quest\\daily_step_4_click.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(230, 170, 305, 200, cla, img, 0.83)
                                if imgs_ is not None and imgs_ != False:
                                    break
                                else:
                                    click_pos_2(60, 295, cla)
                                time.sleep(0.5)

                        daily_click = True

                        daily_quest_start = True
                        while daily_quest_start is True:
                            result_dead = dead_die(cla)
                            if result_dead == True:
                                add_data = "일일퀘스트_" + str(step)
                                myQuest_play_add(cla, add_data)
                                daily_quest_start = False
                            else:
                                result_ = go_quest_ing_(cla)
                                if result_ == False:

                                    full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\grow\\grow_3\\quest_.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(30, 30, 120, 80, cla, img, 0.83)
                                    if imgs_ is not None and imgs_ != False:
                                        print("quest_...", imgs_)





                                        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\quest\\quest_ing.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(540, 220, 630, 960, cla, img, 0.8)
                                        if imgs_ is not None and imgs_ != False:
                                            if now == "start":
                                                click_pos_reg(imgs_.x, imgs_.y, cla)
                                                time.sleep(0.3)
                                                click_pos_2(860, 1000, cla)
                                                for z in range(3):
                                                    full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\quest\\y_1.PNG"
                                                    img_array = np.fromfile(full_path, np.uint8)
                                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                                    imgs_ = imgs_set_(480, 580, 630, 660, cla, img, 0.8)
                                                    if imgs_ is not None and imgs_ != False:
                                                        click_pos_reg(imgs_.x, imgs_.y, cla)
                                                        break
                                                    time.sleep(0.3)
                                            else:


                                                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\quest\\tobul.PNG"
                                                img_array = np.fromfile(full_path, np.uint8)
                                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                                imgs_ = imgs_set_(650, 300, 840, 330, cla, img, 0.8)
                                                if imgs_ is not None and imgs_ != False:
                                                    print("퀘스트 진행중...20초")
                                                else:
                                                    full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\quest\\quest_ing.PNG"
                                                    img_array = np.fromfile(full_path, np.uint8)
                                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                                    imgs_ = imgs_set_(540, 220, 630, 960, cla, img, 0.8)
                                                    if imgs_ is not None and imgs_ != False:
                                                        click_pos_reg(imgs_.x - 200, imgs_.y, cla)
                                                for i in range(20):
                                                    result_ = go_quest_ing_(cla)
                                                    if result_ == True:
                                                        break
                                                    time.sleep(1)
                                        else:
                                            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\quest\\quest_complete.PNG"
                                            img_array = np.fromfile(full_path, np.uint8)
                                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                            imgs_ = imgs_set_(540, 220, 630, 960, cla, img, 0.8)
                                            if imgs_ is not None and imgs_ != False:
                                                click_pos_reg(imgs_.x, imgs_.y, cla)
                                                time.sleep(0.2)

                                                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\quest\\already_complete.PNG"
                                                img_array = np.fromfile(full_path, np.uint8)
                                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                                imgs_ = imgs_set_(700, 970, 750, 1030, cla, img, 0.8)
                                                if imgs_ is not None and imgs_ != False:
                                                    add_data = "일일퀘스트_" + str(step)
                                                    myQuest_play_add(cla, add_data)
                                                    daily_quest_start = False
                                                    time.sleep(0.2)
                                                else:
                                                    full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\quest\\bosang_1.PNG"
                                                    img_array = np.fromfile(full_path, np.uint8)
                                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                                    imgs_ = imgs_set_(730, 970, 830, 1030, cla, img, 0.8)
                                                    if imgs_ is not None and imgs_ != False:
                                                        click_pos_reg(imgs_.x, imgs_.y, cla)
                                                        time.sleep(0.2)
                                                        for i in range(10):
                                                            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\quest\\quest_ing.PNG"
                                                            img_array = np.fromfile(full_path, np.uint8)
                                                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                                            imgs_ = imgs_set_(540, 220, 630, 960, cla, img, 0.8)
                                                            if imgs_ is not None and imgs_ != False:
                                                                break
                                                            time.sleep(0.2)
                                            else:
                                                add_data = "일일퀘스트_" + str(step)
                                                myQuest_play_add(cla, add_data)
                                                daily_quest_start = False
                                                time.sleep(0.2)
                                else:
                                    daily_quest_start = False
                                    time.sleep(0.2)
                            time.sleep(0.3)
                    else:
                        click_pos_2(480, 110, cla)

                        for i in range(10):
                            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\quest\\daily_check_1.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(160, 990, 220, 1015, cla, img, 0.83)
                            if imgs_ is not None and imgs_ != False:
                                break
                            time.sleep(0.2)

                    time.sleep(0.5)

            else:
                menu_open(cla)
                click_pos_2(745, 195, cla)

                for i in range(10):
                    full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\grow\\grow_3\\quest_.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(30, 30, 120, 80, cla, img, 0.83)
                    if imgs_ is not None and imgs_ != False:
                        break
                    time.sleep(0.2)

            time.sleep(0.3)




    except Exception as e:
        print(e)

