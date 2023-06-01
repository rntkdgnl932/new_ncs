import sys
import time

sys.path.append('C:/my_games/nightcrow/data_nc/mymodule')

fly_ = 0

def main_quest_grow(cla):
    try:
        global camera_, media_, talchool_, prison_, boonji_, force_quest, fly_

        from function import click_pos_2, imgs_set, imgs_set_, random_int, drag_pos, text_check_get, click_pos_reg
        from massenger import line_to_me
        from schedule import myQuest_play_add
        from potion import potion_check
        from action import go_quest_ing_, go_auto_ing_, clean_screen, dead_die, item_open, talgut_ing_

        import pyautogui
        import random
        import numpy as np
        import cv2

        print("nightcrow main quest")

        result_dead = dead_die(cla)
        if result_dead == True:
            myQuest_play_add(cla, "메인퀘스트")
        else:
            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\dungeon\\youjuk_1.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(30, 75, 200, 110, cla, img, 0.75)
            if imgs_ is not None and imgs_ != False:
                print("youjuk_1 => 유적까지 퀘스트 완료", imgs_)
                line_to_me(cla, "유적이다. 준비끝...")
                myQuest_play_add(cla, "메인퀘스트")
            else:

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


def quest_check(cla):
    try:

        from function import click_pos_2, imgs_set, imgs_set_, random_int, drag_pos, text_check_get, click_pos_reg
        import numpy as np
        import cv2

        # 퀘스트 수락
        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\grow\\grow_1\\quest_soolock_1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(800, 90, 960, 300, cla, img, 0.83)
        if imgs_ is not None and imgs_ != False:
            print("quest_soolock_1", imgs_)
            click_pos_reg(imgs_.x, imgs_.y, cla)
            talgut_board_(cla)
        else:
            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\jadong\\in_spot_walking_2.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(480, 880, 500, 900, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("메인퀘하러 가는 중")
            else:
                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\grow\\grow_1\\quest_soolock_2.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(800, 90, 960, 300, cla, img, 0.83)
                if imgs_ is not None and imgs_ != False:
                    print("quest_soolock_2", imgs_)
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                    talgut_board_(cla)
        # 붕붕 날아다니자
        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\jadong\\fly_.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(770, 970, 960, 1030, cla, img, 0.7)
        if imgs_ is not None and imgs_ != False:
            click_pos_reg(imgs_.x, imgs_.y, cla)
        # 퀘스트 완료
        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\grow\\grow_1\\quest_complete_1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(800, 90, 960, 900, cla, img, 0.83)
        if imgs_ is not None and imgs_ != False:
            print("quest_complete_1", imgs_)
            click_pos_reg(imgs_.x, imgs_.y, cla)
            talgut_board_(cla)
        else:
            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\grow\\grow_1\\quest_complete_2.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(800, 90, 960, 900, cla, img, 0.83)
            if imgs_ is not None and imgs_ != False:
                print("quest_complete_2", imgs_)
                click_pos_reg(imgs_.x, imgs_.y, cla)
                talgut_board_(cla)




    except Exception as e:
        print(e)




def talgut_board_(cla):
    try:

        from function import click_pos_2, imgs_set, imgs_set_, random_int, drag_pos, text_check_get, click_pos_reg
        from action import menu_open, clean_screen
        from get_item import guild_jilyung
        import numpy as np
        import cv2
        import pyautogui

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
                    guild_jilyung(cla)
                    jilyung_is_ = True
                else:
                    full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\guild\\guild_jilyung.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(660, 90, 730, 300, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                time.sleep(0.4)

        # 탈것
        go_ = False
        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\grow\\grow_1\\talgut_1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(680, 90, 720, 140, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            go_ = True
            click_pos_reg(imgs_.x, imgs_.y, cla)
        else:
            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\grow\\grow_1\\talgut_2.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(680, 90, 720, 140, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                go_ = True
                click_pos_reg(imgs_.x, imgs_.y, cla)
            else:
                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\grow\\grow_1\\talgut_3.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(680, 90, 720, 140, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    go_ = True
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                else:
                    full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\quest\\talgut_4.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(680, 90, 720, 140, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        go_ = True
                        click_pos_reg(imgs_.x, imgs_.y, cla)

        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\quest\\sub_sojin_1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(400, 70, 550, 120, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("sub_sojin_1", imgs_)
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
        return go_
    except Exception as e:
        print(e)


