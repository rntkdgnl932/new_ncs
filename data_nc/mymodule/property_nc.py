import sys

sys.path.append('C:/my_games/nightcrow/data_nc/mymodule')

import variable as v_
import requests
from ftplib import FTP
import os

# 이건 엑셀로 변환시 필요한 것...
# import pandas

ftp_username = 'gamer'
ftp_password = 'coobccocco'
data_list = []  # data_list 변수를 전역 변수로 초기화



def my_property_upload(cla):
    import cv2
    import time
    import os
    import numpy as np
    from action import out_check, clean_screen, mine_check
    from function import imgs_set_, click_pos_2

    try:


        # 1. coob, ccocco 파악

        dir_path = "C:\\my_games"
        file_path = dir_path + "\\line\\line.txt"

        with open(file_path, "r", encoding='utf-8-sig') as file:
            line = file.read()
            line_ = line.split(":")
            print('line', line)
            # line_[0] => coob, ccocco
            # line_[1] => 컴퓨터번호

        # 2. game 파악

        game_name = v_.this_game

        # 3. 게임 서버 파악

        file_path3 = dir_path + "\\nightcrow\\mysettings\\game_server\\game_server.txt"

        isstart1 = False
        while isstart1 is False:
            if os.path.isfile(file_path) == True:
                with open(file_path3, "r", encoding='utf-8-sig') as file:
                    isstart1 = True
                    game_server = file.read()
                    print('나크 game server', game_server)
                    # line3 => 게임서버
            else:
                with open(file_path3, "w", encoding='utf-8-sig') as file:
                    data = 'none'
                    file.write(str(data))




        # 4. 다이야, 골드 파악

        result_mine = mine_check(cla)
        print("result_mine", result_mine)
        # result_mine[0] => 골드
        # result_mine[1] => 다이아

        # # 파악한 곳 나가기
        # for i in range(10):
        #     full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\auction\\menu_auction.PNG"
        #     img_array = np.fromfile(full_path, np.uint8)
        #     img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        #     imgs_ = imgs_set_(5, 30, 150, 80, cla, img, 0.8)
        #     if imgs_ is not None and imgs_ != False:
        #         click_pos_2(935, 55, cla)
        #     else:
        #         result_out = out_check(cla)
        #         if result_out == True:
        #             break
        #         else:
        #             clean_screen(cla)
        #     time.sleep(0.5)

        # 다이야 0이면 업로드 안하기

        if int(result_mine[1]) != 0:

            # 5. 내 서버 ip 불러오기

            ftp_server = ftp_ip_get()



            # 업로드 처리 과정

            # 6. 로컬 파일 경로 (절대 경로 사용)
            local_file_path = 'C:/my_games/nightcrow/mysettings/my_property/my_property.txt'

            dir_path = "C:\\my_games\\nightcrow\\mysettings\\my_property"
            file_path = dir_path + "\\my_property.txt"

            isstart1 = False
            while isstart1 is False:
                if os.path.isdir(dir_path) == True:
                    isstart1 = True
                    with open(file_path, "w", encoding='utf-8-sig') as file:
                        # data = 사용자:게임이름:게임서버:다이아:골드
                        data = str(line_[0]) + ':' + str(game_name) + ':' + str(game_server) + ':' + str(result_mine[1]) + ':' + str(
                            result_mine[0])
                        file.write(str(data))

                else:
                    os.makedirs(dir_path)




            # 7. 원격 파일 경로 (FTP 서버 내)
            remote_directory = '/nightcrow/' + str(line_[0])  # 원격 디렉토리 경로
            remote_file_path = '/nightcrow/' + str(line_[0]) + '/' + str(line_[1]) + '.txt'
            print("7", remote_file_path)

            # # 미리 삭제해버리자?
            # if os.path.isdir(remote_directory) == False:
            #     os.makedirs(remote_directory)
            #
            # if os.path.isfile(remote_file_path) == True:
            #     os.remove(file_path)
            #     print('기존 파일이 삭제되었습니다.')

            # FTP 연결 및 파일 업로드
            try:
                print("aaa")
                with FTP(ftp_server) as ftp:
                    ftp.login(ftp_username, ftp_password)

                    # # 원격 디렉토리가 이미 존재하지 않는 경우에만 생성
                    # if remote_directory not in ftp.nlst():
                    #     ftp.mkd(remote_directory)
                    #     print("remote_directory")
                    # if remote_file_path in ftp.nlst():
                    #     ftp.delete(remote_file_path)
                    #     print("delete")
                    # else:
                    #     print(" not delete")

                    with open(local_file_path, 'rb') as file:
                        # 파일 업로드시 UTF-8 인코딩 사용
                        ftp.storbinary('STOR ' + remote_file_path, file, 8192)
                    print(f'로컬 파일 {local_file_path}을 FTP 서버의 {remote_file_path}로 업로드했습니다.')
            except Exception as e:
                print(f'파일 업로드 실패: {e}')

    except Exception as e:
        print(e)
        return 0

def ftp_ip_get():
    try:
        url = "https://raw.githubusercontent.com/rntkdgnl932/server/master/server_ip.txt"

        response = requests.get(url, headers={'Cache-Control': 'no-cache'})
        # response = requests.get(url, headers={'Cache-Control': 'no-cache'})
        data = response.text

        print("ftp_ip_get", data)
        return data
    except Exception as e:
        print(e)
        return 0