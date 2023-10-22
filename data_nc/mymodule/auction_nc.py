import time

from screeninfo import get_monitors
# import os
import sys
sys.path.append('C:/my_games/nightcrow/data_nc/mymodule')

import variable as v_

def auction_ready(cla):
    from function import imgs_set_, click_pos_2
    import numpy as np
    import cv2
    from schedule import myQuest_play_add
    from realtime import boonhae_
    try:
        print("auction_ready")
        # 창고에서 물건 가져오고
        jaelyo_out(cla)

        # 거래소 열어서
        auction_open(cla)
        # 모두 받기하고

        # 일괄회수 누르고

        # 등록하고

        # 나간다.
        for i in range(5):
            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\auction\\auction_title.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(10, 10, 130, 80, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                click_pos_2(935, 60, cla)
            else:
                break
            time.sleep(0.5)
        # 그리고 다시 창고에 넣는다
        jaelyo_in(cla)
        # 다 넣고 마무리는 스케쥴 완료
        myQuest_play_add(cla, "거래소등록")

        # 분해까지 마무리
        boonhae_(cla)
    except Exception as e:
        print(e)
        return 0




def jaelyo_out(cla):
    from function import click_pos_2, imgs_set_, click_pos_reg, mouse_move_cpp
    from action import out_check, clean_screen
    import numpy as np
    import cv2
    import os
    try:
        print("거래물품 창고에서 가져오기")
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

                in_chango_1 = True

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

                        in_chango_2 = True


                        # 모리온 빼버리기
                        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\auction\\list\\morion.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(55, 115, 270, 930, cla, img, 0.85)
                        if imgs_ is not None and imgs_ != False:
                            print("morion 거래물건 있다", imgs_)
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                            time.sleep(0.1)
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                            time.sleep(0.1)
                        else:
                            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\auction\\list\\morion2.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(55, 115, 270, 930, cla, img, 0.85)
                            if imgs_ is not None and imgs_ != False:
                                print("morion2 거래물건 있다", imgs_)
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                                time.sleep(0.1)
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                                time.sleep(0.1)




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

                                in_chango_3 = True

                                dir_path = "C:\\my_games\\nightcrow\\data_nc"
                                file_path = dir_path + "\\items\\chango\\jaelyo_out.txt"
                                ###
                                if os.path.isfile(file_path) == True:
                                    with open(file_path, "r", encoding='utf-8-sig') as file:
                                        jaelyo_ready = file.read().splitlines()
                                        print("jaelyos", jaelyo_ready)
                                ###

                                for i in range(len(jaelyo_ready)):
                                    for z in range(4):
                                        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\chango\\maul_chango_3.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(50, 80, 110, 110, cla, img, 0.8)
                                        if imgs_ is not None and imgs_ != False:
                                            break
                                        else:
                                            click_pos_2(20, 200, cla)
                                        time.sleep(0.5)




                                    print("1. 거래물건 있나???", jaelyo_ready[i])
                                    full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\auction\\list\\" + jaelyo_ready[i] + ".PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(55, 115, 270, 930, cla, img, 0.85)
                                    if imgs_ is not None and imgs_ != False:
                                        print("2. 거래물건 있다", jaelyo_ready[i])
                                        click_pos_reg(imgs_.x, imgs_.y, cla)
                                        time.sleep(0.1)
                                        click_pos_reg(imgs_.x, imgs_.y, cla)
                                        time.sleep(0.1)
                                        mouse_move_cpp(450, 350, cla)
                                        time.sleep(0.2)
                                    time.sleep(0.5)


                            else:
                                for i in range(10):
                                    full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\chango\\maul_chango_3.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(50, 80, 110, 110, cla, img, 0.8)
                                    if imgs_ is not None and imgs_ != False:
                                        break
                                    else:
                                        click_pos_2(20, 200, cla)
                                    time.sleep(0.5)
                            time.sleep(0.5)



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

                        maul_in = False

                        for i in range(10):
                            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\chango\\maul_chango_1.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(0, 70, 220, 330, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                maul_in = True
                                break
                            time.sleep(0.2)

                        if maul_in == False:
                            click_pos_2(295, 995, cla)

                            for i in range(10):
                                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\chango\\maul_chango_1.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(0, 70, 220, 330, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    break
                                time.sleep(0.5)



                time.sleep(0.5)
    except Exception as e:
        print(e)

def jaelyo_in(cla):
    from function import click_pos_2, imgs_set_, click_pos_reg, mouse_move_cpp
    from action import out_check, clean_screen
    import numpy as np
    import cv2
    import os
    try:
        print("거래물품 창고에 다시 넣기")
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

                in_chango_1 = True

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

                        in_chango_2 = True


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

                                click_pos_2(165, 1015, cla)
                                time.sleep(0.5)

                                in_chango_3 = True

                                dir_path = "C:\\my_games\\nightcrow\\data_nc"
                                file_path = dir_path + "\\items\\chango\\jaelyo_out.txt"
                                ###
                                if os.path.isfile(file_path) == True:
                                    with open(file_path, "r", encoding='utf-8-sig') as file:
                                        jaelyo_ready = file.read().splitlines()
                                        print("jaelyos", jaelyo_ready)
                                ###
                                for i in range(len(jaelyo_ready)):

                                    for z in range(4):
                                        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\chango\\maul_chango_3.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(50, 80, 110, 110, cla, img, 0.8)
                                        if imgs_ is not None and imgs_ != False:
                                            break
                                        else:
                                            click_pos_2(20, 200, cla)
                                        time.sleep(0.5)
                                    if jaelyo_ready[i] != "morion":
                                        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\auction\\list\\" + jaelyo_ready[i] + ".PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(680, 110, 910, 990, cla, img, 0.85)
                                        if imgs_ is not None and imgs_ != False:
                                            print("거래물건 있", jaelyo_ready[i])
                                            click_pos_reg(imgs_.x, imgs_.y, cla)
                                            time.sleep(0.1)
                                            click_pos_reg(imgs_.x, imgs_.y, cla)
                                            time.sleep(0.1)
                                            mouse_move_cpp(450, 350, cla)
                                            time.sleep(0.5)

                                for i in range(5):
                                    full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\chango\\maul_chango_3.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(50, 80, 110, 110, cla, img, 0.8)
                                    if imgs_ is not None and imgs_ != False:
                                        click_pos_2(935, 60, cla)
                                    else:
                                        break
                                    time.sleep(0.5)

                            else:

                                for i in range(10):
                                    full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\chango\\maul_chango_3.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(50, 80, 110, 110, cla, img, 0.8)
                                    if imgs_ is not None and imgs_ != False:
                                        break
                                    else:
                                        click_pos_2(20, 200, cla)
                                    time.sleep(0.5)
                            time.sleep(0.5)



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

                        maul_in = False

                        for i in range(10):
                            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\chango\\maul_chango_1.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(0, 70, 220, 330, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                maul_in = True
                                break
                            time.sleep(0.2)

                        if maul_in == False:
                            click_pos_2(295, 995, cla)

                            for i in range(10):
                                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\chango\\maul_chango_1.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(0, 70, 220, 330, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    break
                                time.sleep(0.5)



                time.sleep(0.5)
    except Exception as e:
        print(e)

def auction_open(cla):
    from function import imgs_set_, click_pos_reg, click_pos_2, mouse_move_cpp
    from action import menu_open
    from property_nc import my_property_upload
    import numpy as np
    import cv2
    import os
    try:
        print("auction_open")

        in_chango_1 = False
        in_chango_1_count = 0
        while in_chango_1 is False:
            in_chango_1_count += 1
            if in_chango_1_count > 5:
                in_chango_1 = True
            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\auction\\auction_title.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(10, 10, 130, 80, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:




                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\auction\\auction_bag.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(850, 90, 910, 140, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("시작")
                    in_chango_1 = True

                    full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\auction\\2020.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(65, 995, 120, 1030, cla, img, 0.9)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_2(935, 60, cla)

                    else:

                        # 일괄회수
                        click_pos_2(845, 1015, cla)
                        time.sleep(0.5)


                        # 다이아 모두 받기
                        click_pos_2(680, 1015, cla)
                        time.sleep(0.5)

                        for i in range(10):
                            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\auction\\y.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(545, 575, 610, 630, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                            time.sleep(0.2)

                        # 다이야 파악 후 업로드
                        my_property_upload(cla)
                        time.sleep(0.2)

                        dir_path = "C:\\my_games\\nightcrow\\data_nc"
                        file_path = dir_path + "\\items\\chango\\jaelyo_out.txt"
                        ###
                        if os.path.isfile(file_path) == True:
                            with open(file_path, "r", encoding='utf-8-sig') as file:
                                jaelyo_ready = file.read().splitlines()
                                print("jaelyos", jaelyo_ready)
                        ###
                        for i in range(len(jaelyo_ready)):

                            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\auction\\2020.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(65, 995, 120, 1030, cla, img, 0.9)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_2(935, 60, cla)
                                break
                            else:

                                data = "<<<<<<<<<<<<<<<<<<<<" + str(i) + ">>>>>>>>>>>>>>>>>>>>"
                                print(data)
                                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\auction\\list\\" + jaelyo_ready[i] + ".PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(670, 125, 930, 930, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    print("auction : 재료 있", jaelyo_ready[i])

                                    click_pos_reg(imgs_.x, imgs_.y, cla)

                                    for z in range(5):
                                        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\auction\\sell_title.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(430, 330, 530, 380, cla, img, 0.8)
                                        if imgs_ is not None and imgs_ != False:
                                            break
                                        time.sleep(0.5)

                                    # 거래단가 구하기
                                    full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\auction\\sell_title.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(430, 330, 530, 380, cla, img, 0.8)
                                    if imgs_ is not None and imgs_ != False:
                                        result_auction_price = auction_start(cla)
                                        if float(result_auction_price[0]) > float(result_auction_price[1]):
                                            price_ = float(result_auction_price[0])
                                        else:
                                            price_ = float(result_auction_price[1])

                                        # 높은 가격 구했음.
                                        print("price_", price_)
                                        mouse_move_cpp(450, 350, cla)
                                        time.sleep(0.2)

                                        # 수량 구하기기
                                        click_pos_2(680, 400, cla)
                                        time.sleep(0.1)
                                        click_pos_2(680, 400, cla)
                                        time.sleep(0.5)
                                        # 숫자 1로 바뀌면 맥스 버튼 누르기기

                                        result_1_equal = auction_start2(cla)

                                        if result_1_equal == "1":
                                            # 맥스 버튼
                                            click_pos_2(707, 607, cla)
                                            time.sleep(0.1)
                                            click_pos_2(707, 607, cla)
                                            time.sleep(0.5)

                                            result_auction_many = auction_start2(cla)
                                            result_last_price = price_ * float(result_auction_many)

                                        else:
                                            result_last_price = price_

                                        print("result_last_price", result_last_price)

                                        result_click_num_ready = str(int(float(result_last_price)))

                                        print("result_click_num_ready", result_click_num_ready)

                                        if int(float(result_last_price)) >= 10:
                                            # 구한 값 순서대로 마우스 클릭하고 클릭 다 한후에 다시 금액 비교하기기

                                            click_pos_2(690, 430, cla)
                                            time.sleep(0.1)
                                            click_pos_2(690, 430, cla)
                                            time.sleep(0.1)

                                            for y in range(len(result_click_num_ready)):
                                                print(y, result_click_num_ready[y])
                                                if result_click_num_ready[y] == "0":
                                                    click_pos_2(530, 645, cla)
                                                elif result_click_num_ready[y] == "1":
                                                    click_pos_2(530, 610, cla)
                                                elif result_click_num_ready[y] == "2":
                                                    click_pos_2(590, 610, cla)
                                                elif result_click_num_ready[y] == "3":
                                                    click_pos_2(650, 610, cla)
                                                elif result_click_num_ready[y] == "4":
                                                    click_pos_2(530, 575, cla)
                                                elif result_click_num_ready[y] == "5":
                                                    click_pos_2(590, 575, cla)
                                                elif result_click_num_ready[y] == "6":
                                                    click_pos_2(650, 575, cla)
                                                elif result_click_num_ready[y] == "7":
                                                    click_pos_2(530, 540, cla)
                                                elif result_click_num_ready[y] == "8":
                                                    click_pos_2(590, 540, cla)
                                                elif result_click_num_ready[y] == "9":
                                                    click_pos_2(650, 540, cla)
                                                time.sleep(0.2)

                                            result_equal = auction_start2(cla)
                                            print("result_click_num_ready", result_click_num_ready)
                                            print("result_equal", result_equal)



                                            if result_click_num_ready == result_equal:
                                                for u in range(10):
                                                    full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\auction\\sell_title.PNG"
                                                    img_array = np.fromfile(full_path, np.uint8)
                                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                                    imgs_ = imgs_set_(430, 330, 530, 380, cla, img, 0.75)
                                                    if imgs_ is not None and imgs_ != False:

                                                        if int(float(result_equal)) >= 10:
                                                            for t in range(10):
                                                                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\auction\\y.PNG"
                                                                img_array = np.fromfile(full_path, np.uint8)
                                                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                                                imgs_ = imgs_set_(480, 630, 700, 750, cla, img, 0.8)
                                                                if imgs_ is not None and imgs_ != False:
                                                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                                                                    time.sleep(0.2)
                                                                else:
                                                                    break
                                                                time.sleep(0.7)

                                                        else:
                                                            # 그냥 나가기
                                                            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\auction\\sell_exit.PNG"
                                                            img_array = np.fromfile(full_path, np.uint8)
                                                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                                            imgs_ = imgs_set_(720, 320, 780, 380, cla, img, 0.8)
                                                            if imgs_ is not None and imgs_ != False:
                                                                click_pos_reg(imgs_.x, imgs_.y, cla)
                                                                time.sleep(0.2)

                                                    else:
                                                        break
                                                    time.sleep(0.2)

                                            else:
                                                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\auction\\sell_exit.PNG"
                                                img_array = np.fromfile(full_path, np.uint8)
                                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                                imgs_ = imgs_set_(720, 320, 780, 380, cla, img, 0.8)
                                                if imgs_ is not None and imgs_ != False:
                                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                                                    time.sleep(0.2)

                                            for e in range(10):
                                                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\auction\\sell_title.PNG"
                                                img_array = np.fromfile(full_path, np.uint8)
                                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                                imgs_ = imgs_set_(430, 330, 530, 380, cla, img, 0.8)
                                                if imgs_ is not None and imgs_ != False:
                                                    full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\auction\\sell_exit.PNG"
                                                    img_array = np.fromfile(full_path, np.uint8)
                                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                                    imgs_ = imgs_set_(720, 320, 780, 380, cla, img, 0.8)
                                                    if imgs_ is not None and imgs_ != False:
                                                        click_pos_reg(imgs_.x, imgs_.y, cla)
                                                        time.sleep(0.2)
                                                else:
                                                    break
                                                time.sleep(0.3)
                                            time.sleep(0.5)
                                        else:
                                            print("10원 미만이다 -> ", price_)
                                    for z in range(5):
                                        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\auction\\sell_title.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(430, 330, 530, 380, cla, img, 0.8)
                                        if imgs_ is not None and imgs_ != False:
                                            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\auction\\sell_exit.PNG"
                                            img_array = np.fromfile(full_path, np.uint8)
                                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                            imgs_ = imgs_set_(720, 320, 780, 380, cla, img, 0.8)
                                            if imgs_ is not None and imgs_ != False:
                                                click_pos_reg(imgs_.x, imgs_.y, cla)
                                        else:
                                            break
                                        time.sleep(0.5)
                else:
                    full_path ="c:\\my_games\\nightcrow\\data_nc\\imgs\\auction\\sell_click.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(150, 70, 350, 140, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_reg(imgs_.x, imgs_.y, cla)

                        for i in range(10):
                            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\auction\\2020.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(65, 995, 120, 1030, cla, img, 0.9)
                            if imgs_ is not None and imgs_ != False:
                                break
                            time.sleep(0.2)

                    time.sleep(0.2)

            else:

                full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\auction\\menu_auction.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(720, 100, 960, 450, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                    for i in range(10):
                        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\auction\\auction_bag.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(850, 90, 910, 140, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            break
                        time.sleep(0.5)

                else:
                    menu_open(cla)
                time.sleep(0.5)

    except Exception as e:
        print(e)

def auction_start(cla):
    from function import imgs_set_num
    import numpy as np
    import cv2
    try:

        if cla == "one":
            x_plus = 0
        elif cla == "two":
            x_plus = 960
        elif cla == "three":
            x_plus = 960 * 2
        elif cla == "four":
            x_plus = 960 * 3

        # 결과값
        sell_ready_now_low = ""
        sell_ready_last = ""
        x1_reg_point = 0
        x1_reg_1000 = 0
        x2_reg_point = 0
        x2_reg_1000 = 0


        x1_plus = False

        x2_plus = False

        # 첫번째 소수점 및 쉼표 파악
        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\auction\\num\\point.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_num(377, 580, 410, 600, cla, img, 0.99)
        if imgs_ is not None and imgs_ != False:
            print("현재 최저 금액 : point", imgs_)
            # 첫번째 소수점 x = 379, 378
            # 두번째 소수점 x = 387, 386
            # 세번째 소수점 x = 395
            x1_plus = True
            x1_reg_point = imgs_.x
        else:
            print("현재 최저 금액 : not point")

        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\auction\\num\\1000.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_num(377, 580, 410, 600, cla, img, 0.99)
        if imgs_ is not None and imgs_ != False:
            print("현재 최저 금액 : , ", imgs_)
            x1_plus = True
            x1_reg_1000 = imgs_.x
        else:
            print("현재 최저 금액 : not 1000")

        # 두번째 소수점 및 쉼표 파악
        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\auction\\num\\point.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_num(377, 650, 410, 670, cla, img, 0.99)
        if imgs_ is not None and imgs_ != False:
            print("마지막 거래 금액 : point", imgs_)
            x2_plus = True
            x2_reg_point = imgs_.x
        else:
            print("마지막 거래 금액 : not point")

        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\auction\\num\\1000.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_num(377, 650, 410, 670, cla, img, 0.99)
        if imgs_ is not None and imgs_ != False:
            print("마지막 거래 금액 : , ", imgs_)
            x2_plus = True
            x2_reg_1000 = imgs_.x
        else:
            print("마지막 거래 금액 : not 1000")


        # 값 구하기
        for k in range(4):
            if k == 0:
                # 첫째자리
                x_1 = 369
                x_2 = 378
                x_3 = 369
                x_4 = 378
            if k == 1:
                # 둘째자리
                x_1 = 377
                x_2 = 386
                x_3 = 377
                x_4 = 386
            if k == 2:
                # 셋째자리
                x_1 = 385
                x_2 = 394
                x_3 = 385
                x_4 = 394
            if k == 3:
                # 넷째자리
                x_1 = 393
                x_2 = 402
                x_3 = 393
                x_4 = 402

            y_1 = 570
            y_2 = 588
            y_3 = 648
            y_4 = 664

            # sell_ready_now_low

            if x1_plus == True:
                if k != 0:
                    if x1_reg_point != 0 or x1_reg_1000 != 0:
                        if 375 + x_plus < x1_reg_point < 380 + x_plus or 375 + x_plus < x1_reg_1000 < 380 + x_plus:
                            if k > 0:
                                x_1 = x_1 + 3
                                x_2 = x_2 + 3
                        if 384 + x_plus < x1_reg_point < 390 + x_plus or 384 + x_plus < x1_reg_1000 < 390 + x_plus:
                            if k > 1:
                                x_1 = x_1 + 3
                                x_2 = x_2 + 3
                        if 390 + x_plus < x1_reg_point < 400 + x_plus or 390 + x_plus < x1_reg_1000 < 400 + x_plus:
                            if k > 2:
                                x_1 = x_1 + 3
                                x_2 = x_2 + 3

            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\auction\\num\\vacant.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_num(x_1, y_1, x_2, y_2, cla, img, 0.99)
            if imgs_ is not None and imgs_ != False:
                print("숫자 없다")

            else:


                # sell_ready_now_low = text_check_get(x_1, y_1, x_2, y_2, cla)

                for i in range(10):
                    full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\auction\\num\\" + str(i) + ".PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_num(x_1, y_1, x_2, y_2, cla, img, 0.99)
                    if imgs_ is not None and imgs_ != False:
                        # data = "현재 최저 금액 : 숫자 " + str(i) + " 보여"
                        # print(data, imgs_)


                        if k != 0:
                            # 첫번째 소수점 x = 379, 378
                            # 두번째 소수점 x = 387, 386
                            # 세번째 소수점 x = 395, 394
                            if k == 1:
                                if x1_reg_point != 0 and (375 + x_plus < x1_reg_point < 380 + x_plus):
                                    sell_ready_now_low += "."
                            if k == 2:
                                if x1_reg_point != 0 and (384 + x_plus < x1_reg_point < 390 + x_plus):
                                    sell_ready_now_low += "."
                            if k == 3:
                                if x1_reg_point != 0 and (390 + x_plus < x1_reg_point < 400 + x_plus):
                                    sell_ready_now_low += "."
                            sell_ready_now_low += str(i)
                        else:
                            sell_ready_now_low += str(i)

                        break

            # sell_ready_last

            if x2_plus == True:
                if k != 0:
                    if x2_reg_point != 0 or x2_reg_1000 != 0:
                        if 375 + x_plus < x2_reg_point < 380 + x_plus or 375 + x_plus < x2_reg_1000 < 380 + x_plus:
                            if k > 0:
                                x_3 = x_3 + 3
                                x_4 = x_4 + 3
                        if 384 + x_plus < x2_reg_point < 390 + x_plus or 384 + x_plus < x2_reg_1000 < 390 + x_plus:
                            if k > 1:
                                x_3 = x_3 + 3
                                x_4 = x_4 + 3
                        if 390 + x_plus < x2_reg_point < 400 + x_plus or 390 + x_plus < x2_reg_1000 < 400 + x_plus:
                            if k > 2:
                                x_3 = x_3 + 3
                                x_4 = x_4 + 3


            full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\auction\\num\\vacant.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_num(x_3, y_3, x_4, y_4, cla, img, 0.99)
            if imgs_ is not None and imgs_ != False:
                print("숫자 없다")

            else:


                # sell_ready_last = text_check_get(x_3, y_3, x_4, y_4, cla)
                for i in range(10):
                    full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\auction\\num\\" + str(i) + ".PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_num(x_3, y_3, x_4, y_4, cla, img, 0.99)
                    if imgs_ is not None and imgs_ != False:
                        # data = "마지막 거래 금액 : 숫자 " + str(i) + " 보여"
                        # print(data, imgs_)

                        if k != 0:
                            # 첫번째 소수점 x = 379, 378
                            # 두번째 소수점 x = 387, 386
                            # 세번째 소수점 x = 395, 394
                            if k == 1:
                                if x2_reg_point != 0 and (375 + x_plus < x2_reg_point < 380 + x_plus):
                                    sell_ready_last += "."
                            if k == 2:
                                if x2_reg_point != 0 and (384 + x_plus < x2_reg_point < 390 + x_plus):
                                    sell_ready_last += "."
                            if k == 3:
                                if x2_reg_point != 0 and (390 + x_plus < x2_reg_point < 400 + x_plus):
                                    sell_ready_last += "."
                            sell_ready_last += str(i)
                        else:
                            sell_ready_last += str(i)

                        break

            print("3 되면 끝 : ", k)



        return sell_ready_now_low, sell_ready_last
    except Exception as e:
        print(e)
        return 0

def auction_start2(cla):
    from function import imgs_set_num, text_check_get
    import numpy as np
    import cv2
    try:

        # 결과값
        sell_ready = ""
        # 쉼표 여부부터 파악

        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\auction\\many\\1000.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_num(590, 500, 620, 520, cla, img, 0.99)
        if imgs_ is not None and imgs_ != False:
            print("1000", imgs_)
            for k in range(4):
                if k == 0:
                    # 첫째자리
                    x_1 = 590
                    x_2 = 607
                if k == 1:
                    # 둘째자리
                    x_1 = 607
                    x_2 = 625
                if k == 2:
                    # 셋째자리
                    x_1 = 617
                    x_2 = 634
                if k == 3:
                    # 셋째자리
                    x_1 = 630
                    x_2 = 645

                y_1 = 492
                y_2 = 515

                print("k", k)
                text_check_get(617, 493, 634, 520, cla)
                for i in range(10):
                    full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\auction\\many\\" + str(i) + ".PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_num(x_1, y_1, x_2, y_2, cla, img, 0.99)
                    if imgs_ is not None and imgs_ != False:
                        data = "현재 네자리 : 숫자 " + str(i) + " 보여"
                        print(data, imgs_)

                        sell_ready += str(i)

                        break

        else:
            print("1000 안보여")
            sell_ready_last = text_check_get(600, 493, 615, 513, cla)

            # 값 구하기
            for k in range(3):
                if k == 0:
                    # 첫째자리
                    x_1 = 600
                    x_2 = 615
                    # x_2 = 620
                if k == 1:
                    # 둘째자리
                    x_1 = 613
                    x_2 = 625
                    # x_2 = 630
                if k == 2:
                    # 셋째자리
                    x_1 = 623
                    x_2 = 635

                y_1 = 492
                y_2 = 515



                for i in range(10):
                    full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\auction\\many\\" + str(i) + ".PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_num(x_1, y_1, x_2, y_2, cla, img, 0.99)
                    if imgs_ is not None and imgs_ != False:
                        data = "현재 세자리 : 숫자 " + str(i) + " 보여"
                        print(data, imgs_)




                        sell_ready += str(i)


                        break
            if sell_ready == "" or len(sell_ready) != 3:
                sell_ready = ""
                # 값 구하기
                for k in range(2):
                    if k == 0:
                        # 첫째자리
                        x_1 = 605
                        x_2 = 618
                    if k == 1:
                        # 둘째자리
                        x_1 = 618
                        x_2 = 632

                    y_1 = 492
                    y_2 = 515

                    for i in range(10):
                        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\auction\\many\\" + str(i) + ".PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_num(x_1, y_1, x_2, y_2, cla, img, 0.99)
                        if imgs_ is not None and imgs_ != False:
                            data = "현재 두자리 : 숫자 " + str(i) + " 보여"
                            print(data, imgs_)

                            sell_ready += str(i)

                            break
            if sell_ready == "" or (len(sell_ready) != 3 and len(sell_ready) != 2):
                sell_ready = ""
                # 값 구하기
                x_1 = 610
                x_2 = 625
                y_1 = 492
                y_2 = 515

                for i in range(10):
                    full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\auction\\many\\" + str(i) + ".PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_num(x_1, y_1, x_2, y_2, cla, img, 0.99)
                    if imgs_ is not None and imgs_ != False:
                        data = "현재 한자리 : 숫자 " + str(i) + " 보여"
                        print(data, imgs_)

                        sell_ready += str(i)

                        break


        return sell_ready
    except Exception as e:
        print(e)
        return 0

