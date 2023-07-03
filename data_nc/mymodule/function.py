# import random
# import pyautogui
# import pytesseract
# import numpy as np
# import numpy
# from PIL import Image
# import re
# import cv2
import time
import sys
sys.path.append('C:/my_games/nightcrow/data_nc/mymodule')

import variable as v_

def go_test(cla):
    print('hi test!', cla)

def get_region(start_x, start_y, end_x, end_y, cla):
    coordinate = 0
    if cla == 'one':
        coordinate = 0
    if cla == 'two':
        coordinate = 960
    if cla == 'three':
        coordinate = 960 + 960


    # pyautogui.moveTo(pos_1 + random_int() + coordinate, pos_2 + random_int(), abc)

    value = (start_x + coordinate, start_y, end_x - start_x, end_y - start_y)
    return value

# 이미지 특정 색상 제외함
def image_processing(src, min_color, max_color):
    import cv2
    import numpy
    img_ = cv2.cvtColor(numpy.array(src), cv2.COLOR_RGB2BGR)
    exception_img = cv2.inRange(img_, min_color, max_color)
    return exception_img

def random_int():
    try:
        import random
        result = random.randint(1, 4)
        return result
    except Exception as e:
        print(e)

def random_int_2():
    try:
        import random
        result = random.randint(100, 200)
        return result
    except Exception as e:
        print(e)

def isNumber_(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


def change_number(many_potion):
    try:

        potion_ = many_potion

        if " " in potion_:
            potion_ = potion_.replace(' ', '')
            print("!!!!!! ['   '] !!!!!!!", potion_)
        if "고" in potion_:
            potion_ = potion_.replace('고', '2')
            print("!!!!!! [' 고 => 2 '] !!!!!!!", potion_)
        if "ㄷ" in potion_:
            potion_ = potion_.replace('ㄷ', '5')
            print("!!!!!! [' ㄷ => 5 '] !!!!!!!", potion_)
        if "요" in potion_:
            potion_ = potion_.replace('요', '8')
            print("!!!!!! [' 요 => 8 '] !!!!!!!", potion_)
        if "°" in potion_:
            potion_ = potion_.replace('°', '0')
            print("!!!!!! [   ° => 0   ] !!!!!!!", potion_)
        if ")" in potion_:
            potion_ = potion_.replace(')', '1')
            print("!!!!!! [   ) => 1   ] !!!!!!!", potion_)
        if "‘" in potion_:
            potion_ = potion_.replace('‘', '1')
            print("!!!!!! [   ‘ => 1   ] !!!!!!!", potion_)
        if "?" in potion_:
            potion_ = potion_.replace('?', '2')
            print("!!!!!! [   ? => 2  ] !!!!!!!", potion_)
        if "L" in potion_:
            potion_ = potion_.replace('L', '1')
            print("!!!!!! [   L => 1  ] !!!!!!!", potion_)
        if "|" in potion_:
            potion_ = potion_.replace('|', '1')
            print("!!!!!!![   | => 1  ]!!!!!!!!!!!", potion_)
        if "A" in potion_:
            potion_ = potion_.replace('A', '4')
            print("!!!!!!!!![  A => 4 ]!!!!!!!!!!!!!", potion_)
        if "D" in potion_:
            potion_ = potion_.replace('D', '2')
            print("!!!!!!!!![  D => 2 ]!!!!!!!!!!!!!", potion_)
        if "G" in potion_:
            potion_ = potion_.replace('G', '6')
            print("!!!!!!!!![  G => 6 ]!!!!!!!!!!!!!", potion_)
        if "B" in potion_:
            potion_ = potion_.replace('B', '8')
            print("!!!!!!!!![  B => 8  ]!!!!!!!!!!!!!", potion_)
        if "T" in potion_:
            potion_ = potion_.replace('T', '7')
            print("!!!!!!!!![  T => 7  ]!!!!!!!!!!!!!", potion_)
        if "S" in potion_:
            potion_ = potion_.replace('S', '5')
            print("!!!!!!!!![  S => 5  ]!!!!!!!!!!!!!", potion_)
        if "Q" in potion_:
            potion_ = potion_.replace('Q', '9')
            print("!!!!!!!!![  Q => 9  ]!!!!!!!!!!!!!", potion_)
        if "R" in potion_:
            potion_ = potion_.replace('R', '8')
            print("!!!!!!!!![  R => 8  ]!!!!!!!!!!!!!", potion_)

        potion_ = int_put_(potion_)

        if potion_[0] == "0":
            potion_ = "1" + potion_
            print("potion_ = '1' + potion_", potion_)

        return potion_
    except Exception as e:
        print(e)


def int_put_(data):
    try:
        import re
        data_ = data.replace(',', '').strip()
        data_2 = data_.replace('.', '').strip()
        data_3 = data_2.replace(' ', '').strip()
        data_4 = data_3.replace('/', '').strip()

        # data_2 = data_.strip().replace('.', '')
        # data_3 = data_2.strip().replace(' ', '')
        # data_4 = data_3.strip().replace('/', '')
        result = re.sub(r'[^0-9]', '', data_4)
        return result
    except ValueError:
        return False

def in_number_check(cla, data):
    try:
        import cv2
        import numpy as np
        from function import text_check_get, int_put_

        isNumber = False
        print("들어온 데이타?", data)
        print("len potion", len(data))
        if len(data) > 0:
            print("길이가 0 보다 크다", len(data))
            for i in range(len(data)):
                result_num_bool = data[i].isdigit()
                if result_num_bool == True:
                    isNumber = True
        else:
            print("데이터가 길이가 없고 비어있다")

        return isNumber
    except Exception as e:
        print(e)

def imgs_set(a, b, c, d, cla, img):
    try:
        import pyautogui
        if cla == 'one':
            plus = 0
        if cla == 'two':
            plus = 960
        if cla == 'three':
            plus = 960 + 960
        result = pyautogui.locateCenterOnScreen(img, region=(a + plus, b, c - a + 10 , d - b + 10),
                                               confidence=0.7)
        return result
    except ValueError:
        return False

def imgs_set_(a, b, c, d, cla, img, data):
    try:
        import pyautogui
        if cla == 'one':
            plus = 0
        if cla == 'two':
            plus = 960
        if cla == 'three':
            plus = 960 + 960
        result = pyautogui.locateCenterOnScreen(img, region=(a + plus, b, c - a + 10 , d - b + 10),
                                               confidence=data)
        return result
    except ValueError:
        return False


def click_with_image(image_path):
    try:
        import pyautogui
        isClick = False
        while isClick is False:
            location = pyautogui.locateOnScreen(image_path)
            if location is not None:
                pyautogui.click(location)
                isClick = True
    except Exception as e:
        print(e)


def click_pos(pos):
    try:
        import pyautogui
        pyautogui.moveTo(pos[0] + random_int(), pos[1] + random_int())
        time.sleep(random_int())
        pyautogui.click()
    except Exception as e:
        print(e)


def click_pos_2(pos_1, pos_2, cla):
    try:
        import pyautogui
        coordinate = 0
        if cla == 'one':
            coordinate = 0
        if cla == 'two':
            coordinate = 960
        if cla == 'three':
            coordinate = 960 + 960

        xy_ = pyautogui.position()

        k_ = random_int()
        if k_ == 1 or k_ ==2:
            x_ = xy_[0] + random_int_2()
        if k_ == 3 or k_ == 4:
            x_ = -xy_[0] - random_int_2()
            if x_ < 0:
                x_ = 0
        k_ = random_int()
        if k_ == 1 or k_ ==2:
            abc = 0.3
            y_ = xy_[1] + random_int_2()
        if k_ == 3 or k_ == 4:
            abc = 0.4
            y_ = -xy_[1] - random_int_2()
            if y_ < 0:
                y_ = 0

        pyautogui.moveTo(pos_1 + random_int() + coordinate, pos_2 + random_int())
        # time.sleep(0.2)
        # pyautogui.click()
        pyautogui.click(pos_1 + random_int() + coordinate, pos_2 + random_int())
        time.sleep(0.5)
    except Exception as e:
        print(e)

def click_pos_reg(pos_1, pos_2, cla):
    try:
        import pyautogui
        coordinate = 0
        if cla == 'one':
            coordinate = 0
        if cla == 'two':
            coordinate = 0
        if cla == 'three':
            coordinate = 0

        xy_ = pyautogui.position()

        k_ = random_int()
        if k_ == 1 or k_ ==2:
            x_ = xy_[0] + random_int_2()
        if k_ == 3 or k_ == 4:
            x_ = -xy_[0] - random_int_2()
            if x_ < 0:
                x_ = 0
        k_ = random_int()
        if k_ == 1 or k_ ==2:
            abc = 0.3
            y_ = xy_[1] + random_int_2()
        if k_ == 3 or k_ == 4:
            abc = 0.4
            y_ = -xy_[1] - random_int_2()
            if y_ < 0:
                y_ = 0

        pyautogui.moveTo(pos_1 + random_int() + coordinate, pos_2 + random_int())

        pyautogui.click(pos_1 + random_int() + coordinate, pos_2 + random_int())
        time.sleep(0.5)
        # pyautogui.click()
    except Exception as e:
        print(e)


def drag_pos(pos_1, pos_2, pos_3, pos_4, cla):
    try:
        import pyautogui
        coordinate = 0
        if cla == 'one':
            coordinate = 0
        if cla == 'two':
            coordinate = 960
        if cla == 'three':
            coordinate = 960 + 960
        pyautogui.moveTo(pos_1 + random_int() + coordinate, pos_2 + random_int(), 0.5)
        pyautogui.dragTo(pos_3 + random_int() + coordinate, pos_4 + random_int(), 1)
        time.sleep(0.3)
    except Exception as e:
        print(e)

def drag_pos_reg(pos_1, pos_2, pos_3, pos_4, cla):
    try:
        import pyautogui
        coordinate = 0
        if cla == 'one':
            coordinate = 0
        if cla == 'two':
            coordinate = 0
        if cla == 'three':
            coordinate = 0
        pyautogui.moveTo(pos_1 + random_int() + coordinate, pos_2 + random_int(), 0.5)
        pyautogui.dragTo(pos_3 + random_int() + coordinate, pos_4 + random_int(), 1)
        time.sleep(0.3)
    except Exception as e:
        print(e)


# def text_check(posX1, posY1, posX2, posY2, text, method, method_pos):
#     try:
#         isClick = False
#         pos = (posX1, posY1, posX2 - posX1, posY2 - posY1)
#         while isClick is False:
#             pic = pyautogui.screenshot("asd.png", region=pos)
#             pic_ = numpy.array(pic)
#             # result = reader.readtext(pic_)
#             for txt in result:
#                 if txt is not None:
#                     print(txt[1])
#                     for text_ in text:
#                         if txt[1] == text_:
#                             print("aaa!!")
#                             method(method_pos)
#                             isClick = True
#     except Exception as e:
#         print(e)

def text_check_get(posX1, posY1, posX2, posY2, cla):
    try:
        import cv2
        import pytesseract
        import numpy
        import pyautogui
        coordinate = 0
        if cla == 'one':
            coordinate = 0
        if cla == 'two':
            coordinate = 960
        if cla == 'three':
            coordinate = 960 + 960
        pos = (posX1 + coordinate, posY1, posX2 - posX1, posY2 - posY1)
        pyautogui.screenshot("asd.png", region=pos)
        pic = cv2.imread("asd.png", cv2.IMREAD_COLOR)  # 사진을 컬러로 읽어오기
        cv2.imwrite("asd.png", pic)
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
        pic_ = numpy.array(pic)
        result = pytesseract.image_to_string(pic_, lang='kor+eng')

        ##
        return result
    except Exception as e:
        print(e)
        return 0

def text_check_get_2(posX1, posY1, posX2, posY2, cla):
    try:
        import cv2
        import pytesseract
        import numpy
        import pyautogui
        coordinate = 0
        if cla == 'one':
            coordinate = 0
        if cla == 'two':
            coordinate = 960
        if cla == 'three':
            coordinate = 960 + 960
        isClick = False
        pos = (posX1 + coordinate, posY1, posX2 - posX1, posY2 - posY1)
        pyautogui.screenshot("asd.png", region=pos)
        pic = cv2.imread("asd.png", cv2.IMREAD_COLOR)  # 사진을 컬러로 읽어오기
        cv2.imwrite("asd.png", pic)
        ##
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
        # path = Image.open(r'asd.png')
        pic_ = numpy.array(pic)
        rgb_image = cv2.cvtColor(pic_, cv2.COLOR_BGR2RGB)
        result = pytesseract.image_to_string(rgb_image, lang='kor+eng')

        ##
        return result
    except Exception as e:
        print(e)
        return 0

def text_check_get_3(posX1, posY1, posX2, posY2, color, cla):
    try:
        import cv2
        import pytesseract
        import numpy
        from PIL import Image
        import pyautogui
        # color change
        coordinate = 0
        if cla == 'one':
            coordinate = 0
        if cla == 'two':
            coordinate = 960
        if cla == 'three':
            coordinate = 960 + 960
        pos = (posX1 + coordinate, posY1, posX2 - posX1, posY2 - posY1)
        pyautogui.screenshot("asd.png", region=pos)
        pic = cv2.imread("asd.png", cv2.IMREAD_COLOR)  # 사진을 컬러로 읽어오기
        cv2.imwrite("asd.png", pic)
        ##
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
        path = Image.open(r'asd.png')
        pic_ = numpy.array(pic)
        if color == 0:
            rgb_image = cv2.cvtColor(pic_, cv2.COLOR_BGR2RGB)
        if color == 1:
            rgb_image = cv2.cvtColor(pic_, cv2.COLOR_BGR2GRAY)
        if color == 2:
            rgb_image = cv2.cvtColor(pic_, cv2.COLOR_BGR2HSV)
        if color == 3:
            rgb_image = cv2.cvtColor(pic_, cv2.COLOR_BGR2YUV)
        if color == 4:
            rgb_image = cv2.cvtColor(pic_, cv2.COLOR_BGR2RGB)
        if color == 5:
            rgb_image = cv2.cvtColor(pic_, cv2.COLOR_BGR2RGB)
        if color == 6:
            rgb_image = cv2.cvtColor(pic_, cv2.COLOR_BGR2RGB)
        result = pytesseract.image_to_string(rgb_image, lang='kor+eng')

        ##
        return result
    except Exception as e:
        print(e)
        return 0

def text_check_get_4(posX1, posY1, posX2, posY2, color, cla):
    try:
        import numpy as np
        import cv2
        import pytesseract
        import numpy
        import pyautogui
        # color change
        coordinate = 0
        if cla == 'one':
            coordinate = 0
        if cla == 'two':
            coordinate = 960
        if cla == 'three':
            coordinate = 960 + 960
        pos = (posX1 + coordinate, posY1, posX2 - posX1, posY2 - posY1)
        pyautogui.screenshot("asd.png", region=pos)
        pic = cv2.imread("asd.png")
        cv2.imwrite("asd.png", pic)
        ##
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
        # path = Image.open(r'asd.png')
        pic_ = numpy.array(pic)

        rgb_image_ = cv2.cvtColor(pic_, cv2.COLOR_BGR2HSV)

        lower_yellow = np.array([60, 100, 100])
        upper_yellow = np.array([90, 255, 255])

        lower_green = np.array([50, 100, 100])
        upper_green = np.array([70, 255, 255])

        lower_red = np.array([-10, 100, 100])
        upper_red = np.array([10, 255, 255])

        if color == 0:
            rgb_image_ready = cv2.inRange(rgb_image_, lower_yellow, upper_yellow)
            rgb_image = cv2.bitwise_and(pic, pic, mask = rgb_image_ready)
        if color == 1:
            rgb_image_ready = cv2.inRange(rgb_image_, lower_green, upper_green)
            rgb_image = cv2.bitwise_and(pic, pic, mask=rgb_image_ready)
        if color == 2:
            rgb_image_ready = cv2.inRange(rgb_image_, lower_red, upper_red)
            rgb_image = cv2.bitwise_and(pic, pic, mask=rgb_image_ready)
        result = pytesseract.image_to_string(rgb_image, lang='kor+eng')

        cv2.imshow('img_color', pic)

        ##
        return result
    except Exception as e:
        print(e)
        return 0





