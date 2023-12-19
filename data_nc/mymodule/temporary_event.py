import time

import requests
import json
# import os
import sys

sys.path.append('C:/my_games/nightcrow/data_nc/mymodule')

import variable as v_


def dungeon_play_event(cla, result_schedule_):
    try:
        import cv2
        import numpy as np
        from function import text_check_get, int_put_, imgs_set_, click_pos_2, click_pos_reg, drag_pos
        from action import menu_open, clean_screen, in_maul_check
        from massenger import line_to_me
        from potion import maul_potion_only
        from get_item import guild_jilyung_get

        print("dungeon")

        complete_ = False

        dungeon_ = result_schedule_.split("_")

        print("이벤트 던전 시작")

        if dungeon_[1] == "이벤트":
            dungeon_name = "event_1"

        dungeon_clear = False

        in_dungeon__ = False

        in_dungeon__count = 0
        while in_dungeon__ is False:
            in_dungeon__count += 1
            if in_dungeon__count > 3:
                in_dungeon__count = 0
                in_dungeon__ = True

            print("던전체크", in_dungeon__count)

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
            imgs_ = imgs_set_(400, 50, 600, 160, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("juljun_dungeon", imgs_)
                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\dungeon\dongool_2.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(40, 40, 200, 80, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("dongool_2", imgs_)
                    full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\dungeon\\dongool_hunting.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(450, 640, 540, 710, cla, img, 0.9)
                    if imgs_ is not None and imgs_ != False:
                        print("동굴 사냥중인듯 하다")
                        # 동굴 진입해서 사냥중
                        #juljun_attack(cla, dungeon_[1], dungeon_[2])
                    else:
                        drag_pos(360, 550, 600, 550, cla)
                else:
                    drag_pos(360, 550, 600, 550, cla)

            else:
                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\dungeon\\event\\" + dungeon_name + ".PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(30, 75, 200, 110, cla, img, 0.75)
                if imgs_ is not None and imgs_ != False:
                    print(dungeon_[1], imgs_)

                    in_dungeon__ = True

                    complete_ = now_playing(cla, dungeon_[1], dungeon_[2])
                else:
                    # 던전 끝났을때
                    full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\dungeon\\y_1.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(300, 400, 800, 800, cla, img, 0.9)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        time.sleep(0.1)

                    # 던전 진입하기
                    in_dungeon_title = False
                    in_dungeon_title_count = 0
                    while in_dungeon_title is False:
                        in_dungeon_title_count += 1
                        if in_dungeon_title_count > 10:
                            in_dungeon_title = True
                        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\dungeon\\dungeon_title.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(40, 40, 100, 80, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            in_dungeon_title = True

                            # 던전 진입 전 골드
                            my_money = text_check_get(495, 40, 570, 60, cla)

                            print("내 골드?", my_money)
                            my_money = int_put_(my_money)
                            money_bool = my_money.isdigit()
                            if money_bool == True:
                                my_money = int(my_money)
                                if my_money > 0:

                                    onFG_ = int_put_(v_.onForceGold)
                                    onFG = int(onFG_) * 10000
                                    if my_money < onFG:
                                        in_dungeon__ = True
                                        print("강제로 서브퀘스트 수행하기, 기준골드 : ", v_.onForceGold)
                                        if v_.force_sub_quest != True:
                                            v_.force_sub_quest = True
                                            mg_ = str(my_money) + "골드 있다. 거지다. ㅠㅠ"
                                            line_to_me(cla, mg_)
                                    else:
                                        print("기준골드보다 돈 많다 강제노역 해제하기, 기준골드 : ", v_.onForceGold)
                                        v_.force_sub_quest = False

                            if v_.force_sub_quest == False:
                                if dungeon_[1] == "이벤트":

                                    for i in range(10):
                                        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\dungeon\\event\\event_dun_ready.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(720, 240, 820, 290, cla, img, 0.8)
                                        if imgs_ is not None and imgs_ != False:
                                            break
                                        else:
                                            click_pos_2(610, 110, cla)
                                        time.sleep(0.5)

                                    full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\dungeon\\event\\manlyo.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(390, 180, 540, 240, cla, img, 0.8)
                                    if imgs_ is not None and imgs_ != False:
                                        dungeon_clear = True

                                    if dungeon_clear == False:

                                        click_pos_2(200, 200, cla)

                                time.sleep(0.2)

                        else:

                            menu_open(cla)
                            click_pos_2(840, 200, cla)
                            for i in range(10):
                                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\dungeon\\dungeon_title.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(40, 40, 100, 80, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    break
                                else:
                                    print("진입중")
                                time.sleep(0.5)
                            time.sleep(1)

                        # 들어가기 클릭한 상태임.

                        time.sleep(0.2)
                        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\dungeon\\y_1.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(300, 400, 800, 900, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                        time.sleep(2)

                    if v_.force_sub_quest == False:
                        if dungeon_clear == False:
                            step_ready = int(dungeon_[2])
                            if dungeon_[1] == "이벤트":
                                if step_ready == 7 or step_ready == 6:
                                    step_ready = 5
                            print("step_ready", step_ready)
                            step = 115 + (step_ready * 50)
                            click_pos_2(800, step, cla)
                            time.sleep(1)

                            for i in range(20):

                                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\clean_screen\\confirm_1.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(480, 600, 620, 640, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    print("confirm_1", imgs_)
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                                    break
                                else:
                                    click_pos_2(880, 1010, cla)
                                    time.sleep(0.5)

                                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\dungeon\\chogwa_.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(200, 80, 700, 120, cla, img, 0.85)
                                if imgs_ is not None and imgs_ != False:
                                    print("chogwa_!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!", imgs_)
                                    in_dungeon__ = True
                                    dungeon_clear = True
                                    complete_ = True
                                    break
                                else:
                                    full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\dungeon\\already_in.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(420, 80, 500, 120, cla, img, 0.8)
                                    if imgs_ is not None and imgs_ != False:
                                        print("already_in!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!", imgs_)
                                        click_pos_2(930, 60, cla)
                                        break
                                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\dead_die\\not_enough_gold.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(400, 60, 600, 120, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    v_.force_sub_quest = True
                                    in_dungeon__ = True
                                    click_pos_2(930, 60, cla)
                                    print("not_enough_gold")
                                    break
                                else:
                                    full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\dead_die\\not_enough_gold.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(400, 60, 600, 120, cla, img, 0.8)
                                    if imgs_ is not None and imgs_ != False:
                                        v_.force_sub_quest = True
                                        in_dungeon__ = True
                                        click_pos_2(930, 60, cla)
                                        print("not_enough_gold2")
                                        break
                                time.sleep(0.3)

                            loop_y = False
                            loop_y_count = 0
                            while loop_y is False:
                                loop_y_count += 1
                                if loop_y_count > 10:
                                    loop_y = True
                                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\dungeon\\y_1.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(300, 400, 700, 800, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    print("y_1", imgs_)
                                    loop_y = True
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\clean_screen\\confirm_1.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(300, 400, 700, 800, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    print("confirm_1", imgs_)
                                    loop_y = True
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                                time.sleep(0.3)
                            time.sleep(0.4)

                            for i in range(10):
                                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\dungeon\\dungeon_title.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(40, 40, 100, 80, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    print("진입중")
                                else:
                                    full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\dungeon\\event\\" + dungeon_name + ".PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(30, 75, 200, 110, cla, img, 0.75)
                                    if imgs_ is not None and imgs_ != False:
                                        print("진입완료")
                                        break
                                time.sleep(1)

                            time.sleep(1)
                            # 진입할때까지 있어보자 3초?
                            three_second = False
                            three_second_count = 0
                            while three_second is False:
                                three_second_count += 1
                                if three_second_count > 10:
                                    three_second = True
                                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\dungeon\\event\\" + dungeon_name + ".PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(30, 75, 200, 110, cla, img, 0.75)
                                if imgs_ is not None and imgs_ != False:
                                    three_second = True
                                    print("던전 진입 완료", dungeon_name)
                                    # if dungeon_[1] != "동굴":
                                    #     guild_jilyung_get(cla, "dungeon")
                                time.sleep(0.5)

                        else:
                            in_dungeon__ = True
                            complete_ = True
                            print("던전클리어", result_schedule_)
                            time.sleep(0.2)
            time.sleep(1)
        return complete_
    except Exception as e:
        print(e)


def dungeon_1(cla):
    try:
        import cv2
        import numpy as np
        from function import text_check_get, int_put_
        from potion import potion_check

        print("hi")


    except Exception as e:
        print(e)


def now_playing(cla, dun_, nowstep):
    try:
        import cv2
        import numpy as np
        import random
        from function import text_check_get, int_put_, click_pos_2, click_pos_reg, imgs_set_, drag_pos
        from potion import potion_check, maul_potion_only, maul_potion
        from action import clean_screen, out_check, bag_open, skill_check_, in_maul_check, dead_die
        from get_item import guild_jilyung
        from schedule import myQuest_play_add

        print("now_dungeon_playing")

        complete_ = False

        if dun_ == "이벤트":
            dungeon_name = "event_1"

        # play_ = False

        in_ = False
        in__count = 0
        while in_ is False:

            in__count += 1
            if in__count > 7:
                in_ = True

            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\dungeon\\event\\" + dungeon_name + ".PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(30, 75, 200, 110, cla, img, 0.75)
            if imgs_ is not None and imgs_ != False:

                # 서브퀘스트
                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\grow\\grow_1\\quest_soolock_2.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(800, 90, 960, 800, cla, img, 0.83)
                if imgs_ is not None and imgs_ != False:
                    print("던전 서브 수락", imgs_)
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\grow\\grow_1\\quest_complete_2.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(800, 90, 960, 800, cla, img, 0.83)
                if imgs_ is not None and imgs_ != False:
                    print("던전 서브 완료", imgs_)
                    click_pos_reg(imgs_.x, imgs_.y, cla)

                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\dungeon\\different.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(520, 410, 620, 450, cla, img, 0.83)
                if imgs_ is not None and imgs_ != False:
                    print("던전 중 실수로 다른 퀘스트 클릭한 경우", imgs_)
                    click_pos_2(410, 640, cla)

                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\check\\pvp_1.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(900, 275, 960, 365, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("메뉴 닫자", imgs_)
                    click_pos_2(930, 60, cla)
                    time.sleep(0.1)

                if dun_ != "동굴":
                    full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\clean_screen\\gabang_title.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(820, 80, 910, 120, cla, img, 0.83)
                    if imgs_ is not None and imgs_ != False:
                        print("10초 뒤 가방 닫자")
                        time.sleep(10)
                        click_pos_2(935, 100, cla)

                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\check\\hunting_1.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(400, 850, 600, 900, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("던전이름 : ", dungeon_name, "hunting_1", imgs_)
                    in_ = True
                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\check\\hunting_2.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(400, 850, 600, 900, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("던전이름 : ", dungeon_name, "hunting_2", imgs_)
                    in_ = True
                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\check\\hunting_3.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(400, 850, 600, 900, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("던전이름 : ", dungeon_name, "hunting_3", imgs_)
                    in_ = True

                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\dungeon\juljun_mode.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(400, 50, 600, 160, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\dungeon\dongool_2.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(40, 40, 200, 80, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("now_playing...", imgs_)
                        in_ = True

                if in_ == False:
                    clean_screen(cla)

                    if v_.skill_checked_ == False:
                        skill_check_(cla)

                    # drag_pos(480, 250, 480, 600, cla)
                    # time.sleep(1)
                    # click_pos_2(480, 280, cla)
                    # time.sleep(3)
                    if dun_ == "동굴":
                        print("동굴 진입 하즈아!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                        #dongool_move(cla, nowstep)
                    # 위까지 동굴 끝

                    # 아래에는 공통 랜덤 이동동

                    else:
                        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\check\\random_move_1.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(250, 960, 420, 1030, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("random_move_1", imgs_)
                            in_ = True
                            click_pos_2(345, 995, cla)

                            in_dungeon__ = False

                            in_dungeon__count = 0
                            while in_dungeon__ is False:
                                in_dungeon__count += 1
                                if in_dungeon__count > 10:
                                    in_dungeon__count = 0
                                    in_dungeon__ = True

                                print("랜덤 이동 후 던전 진입 여부 체크")

                                for i in range(10):
                                    full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\dungeon\\event\\" + dungeon_name + ".PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(30, 75, 200, 110, cla, img, 0.75)
                                    if imgs_ is not None and imgs_ != False:
                                        print(dun_, imgs_)
                                        in_dungeon__ = True
                                    time.sleep(1)

                            click_pos_2(930, 850, cla)
                            time.sleep(1)
                        else:
                            bag_open(cla)
                            time.sleep(1)
                            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\check\\random_move_1.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(680, 100, 920, 900, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                in_ = True
                                click_pos_2(710, 935, cla)
                                time.sleep(0.5)
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                                time.sleep(0.5)
                                click_pos_2(345, 1000, cla)
                                time.sleep(0.5)
                                clean_screen(cla)

                                in_dungeon__ = False

                                in_dungeon__count = 0
                                while in_dungeon__ is False:
                                    in_dungeon__count += 1
                                    if in_dungeon__count > 10:
                                        in_dungeon__count = 0
                                        in_dungeon__ = True

                                    print("랜덤 이동 후 던전 진입 여부 체크2")
                                    time.sleep(1)

                                    full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\dungeon\\event\\" + dungeon_name + ".PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(30, 75, 200, 110, cla, img, 0.75)
                                    if imgs_ is not None and imgs_ != False:
                                        print(dun_, imgs_)

                                        in_dungeon__ = True

                                click_pos_2(930, 850, cla)
                                time.sleep(1)
                            else:
                                print("랜덤이동서가 없다. 마을 포션 구매하러 가자")

                                maul_che_ = False
                                maul_che_count = 0
                                while maul_che_ is False:
                                    maul_che_count += 1
                                    if maul_che_count > 8:
                                        maul_che_ = True
                                    result_in_maul = in_maul_check(cla)
                                    if result_in_maul == True:
                                        maul_che_ = True
                                        in_ = True
                                        maul_potion(cla)
                                    else:
                                        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\check\\maul_move_1.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(250, 960, 420, 1030, cla, img, 0.8)
                                        if imgs_ is not None and imgs_ != False:
                                            click_pos_reg(imgs_.x, imgs_.y, cla)
                                    time.sleep(1)



                else:
                    v_.skill_checked_ = True

                    full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\dungeon\\dongool_1.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(50, 75, 150, 110, cla, img, 0.75)
                    if imgs_ is not None and imgs_ != False:
                        print("동굴 공격중")
                        click_pos_2(25, 970, cla)
                        time.sleep(0.1)
                        # if v_.who_attack_ == False:
                        #     click_pos_2(25, 970, cla)
                        #     v_.who_attack_ = True
                        # else:
                        #     juljun_attack(cla, dun_, nowstep)
                        #     v_.who_attack_ = False
                    else:
                        # 던전중일때만
                        print("동굴 말고 다른 던전 공격중...던전이름 : ", dungeon_name)
                        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\dungeon\\event\\" + dungeon_name + ".PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(30, 75, 200, 110, cla, img, 0.75)
                        if imgs_ is not None and imgs_ != False:

                            print("정상적으로 사냥중...총 10초 딜레이중")
                            potion_check(cla)
                            time.sleep(10)
                            # play_ = True
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
                                        guild_jilyung(cla, "dungeon")
                                        jilyung_is_ = True
                                    else:
                                        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\guild\\guild_jilyung.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(660, 90, 730, 300, cla, img, 0.8)
                                        if imgs_ is not None and imgs_ != False:
                                            click_pos_reg(imgs_.x, imgs_.y, cla)

                                    time.sleep(0.4)
                        else:
                            print("던전 안이 아니당.")
                            in_ = True
            else:
                print("던전 안이 아니다.")
                in_ = True
        return complete_
    except Exception as e:
        print(e)

