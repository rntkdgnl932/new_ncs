import time

import requests
import json
# import os
import sys
sys.path.append('C:/my_games/nightcrow/data_nc/mymodule')

import variable as v_


def fuckyou_popup(cla):
    from function import click_pos_reg, imgs_set, imgs_set_
    import numpy as np
    import cv2


    print("욕 나오는 팝업창")
    # x 같은 팝업창
    full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\18_popup\\exit_18.PNG"
    img_array = np.fromfile(full_path, np.uint8)
    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    imgs_ = imgs_set(700, 200, 900, 600, cla, img)
    if imgs_ is not None:
        click_pos_reg(imgs_.x, imgs_.y, cla)

    # 보스 퇴치 성공
    full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\boss\\boss_success.PNG"
    img_array = np.fromfile(full_path, np.uint8)
    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    imgs_ = imgs_set_(300, 400, 700, 800, cla, img, 0.8)
    if imgs_ is not None and imgs_ != False:
        full_path = "c:\\my_games\\nightcrow\\data_nc\\imgs\\character_start\\y_.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(300, 400, 700, 800, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            click_pos_reg(imgs_.x, imgs_.y, cla)

